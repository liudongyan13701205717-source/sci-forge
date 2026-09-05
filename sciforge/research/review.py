"""模拟同行评审（peer_review）：对已有论文产出结构化审稿意见。

读取 projects/{paper_id}/doc.md（或 sections/），给出
  - 四个维度评分（novelty/rigor/clarity/soundness，1-10）
  - 总体推荐（Accept/Minor/Major/Reject）
  - 优点（strengths）
  - 缺点（weaknesses / concerns）
  - 具体修改建议（modifications）
落盘 projects/{paper_id}/research/peer_review.json + md。
无 LLM 时基于文本结构做确定性评分（字数/关键章节覆盖/是否有图与表）。
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from sciforge.core import Layout
from sciforge.core import model as llm
from sciforge.write.doc import DocStore

_SECTIONS = ["摘要", "引言", "研究问题", "建模", "求解", "结果", "结论", "参考文献",
             "abstract", "introduction", "method", "results", "conclusion", "references"]


@dataclass
class PeerReview:
    ok: bool
    paper_id: str = ""
    scores: dict = field(default_factory=dict)
    recommendation: str = ""
    strengths: list = field(default_factory=list)
    weaknesses: list = field(default_factory=list)
    modifications: list = field(default_factory=list)
    stats: dict = field(default_factory=dict)
    notes: list = field(default_factory=list)
    error: str = ""
    llm_used: bool = False

    def to_dict(self) -> dict:
        return {k: getattr(self, k) for k in (
            "ok", "paper_id", "scores", "recommendation", "strengths",
            "weaknesses", "modifications", "stats", "notes", "error", "llm_used",
        )}

    def to_markdown(self) -> str:
        def bullet(xs):
            return "\n".join(f"- {x}" for x in xs) if xs else "- （待补充）"

        sc = "\n".join(f"- {k}: {v}/10" for k, v in self.scores.items()) or "- （待评）"
        return "\n\n".join([
            f"# 同行评审意见（{self.paper_id}）",
            f"**推荐：** {self.recommendation}",
            f"## 评分\n{sc}",
            f"**统计：** 正文 {self.stats.get('chars',0)} 字，覆盖章节 "
            f"{'、'.join(self.stats.get('sections_found',[])) or '—'}，图表 "
            f"{self.stats.get('tables',0)} 表 / {self.stats.get('figures',0)} 图",
            f"## 优点\n{bullet(self.strengths)}",
            f"## 缺点 / 关注点\n{bullet(self.weaknesses)}",
            f"## 修改建议\n{bullet(self.modifications)}",
        ])


def _read_doc(layout: Layout, paper_id: str) -> str:
    doc = DocStore(layout, paper_id)
    parts = []
    if doc.doc_md.exists():
        parts.append(doc.doc_md.read_text(encoding="utf-8"))
    else:
        for f in sorted(doc.sections_dir.glob("*.md")):
            parts.append(f.read_text(encoding="utf-8"))
    return "\n".join(parts)


def peer_review(
    *,
    paper_id: str,
    layout: Layout,
) -> PeerReview:
    r = PeerReview(ok=False, paper_id=paper_id)
    notes: list = []
    text = _read_doc(layout, paper_id)
    if not text.strip():
        r.error = f"项目 {paper_id} 尚无正文，请先用 write_section / agent 写入内容。"
        r.ok = False
        return r

    stats, found = _stats(text)

    scoring = _template_scoring(text, stats, found)
    r.scores = scoring["scores"]
    r.recommendation = scoring["recommendation"]
    r.strengths = scoring["strengths"]
    r.weaknesses = scoring["weaknesses"]
    r.modifications = scoring["modifications"]
    r.stats = stats

    if llm.configured():
        try:
            _llm_review(r, text, notes)
            r.llm_used = True
        except RuntimeError as e:
            notes.append(f"LLM 评审不可用，保留模板评分：{e}")

    r.notes = notes
    r.ok = True
    _persist(layout, paper_id, r)
    return r


def _stats(text: str) -> tuple[dict, list]:
    text_nl = re.sub(r"\s+", " ", text)
    chars = len(text_nl.replace(" ", ""))
    tables = text.count("|") // 10 if text.count("|") > 3 else 0
    figures = len(re.findall(r"!\[|\\includegraphics|\\begin\{figure\}", text))
    found = [s for s in _SECTIONS if re.search(rf"(?i)(#+\s*{s}|##\s*.*{s})", text)]
    return {
        "chars": chars,
        "tables": tables,
        "figures": figures,
        "blockquote_placeholder": text.count("待补充"),
        "has_formula": bool(re.search(r"\$|\\frac|\\sum|\\nabla", text)),
    }, found


def _template_scoring(text: str, stats: dict, found: list) -> dict:
    placeholders = stats.get("blockquote_placeholder", 0)
    has_formula = stats.get("has_formula", False)
    tables = stats.get("tables", 0)
    figures = stats.get("figures", 0)

    # novelty: 有方法推导/公式给基础分，缺背景再扣
    novelty = 6.0
    if has_formula:
        novelty += 0.5
    if placeholders:
        novelty -= 0.5

    rigor = 6.0
    rigor += 0.5 if tables else 0
    rigor += 0.5 if figures else 0
    rigor -= 0.5 if "参考文献" not in [f for f in found] or not re.search(r"(?i)\[\d+\]|\bdoi\b|\barxiv", text) else 0
    rigor -= 0.5 if placeholders else 0

    clarity = 5.5
    if stat := stats.get("chars", 0):
        clarity += 1.0 if stat > 2000 else 0.5
    clarity -= 0.5 * placeholders

    soundness = 6.0
    if tables and figures:
        soundness += 1.0
    elif figures:
        soundness += 0.5
    soundness -= 0.5 if placeholders else 0

    def clip(x):
        return round(max(1.0, min(10.0, x)), 1)

    scores = {"novelty": clip(novelty), "rigor": clip(rigor),
              "clarity": clip(clarity), "soundness": clip(soundness)}
    avg = sum(scores.values()) / 4
    if placeholders:
        rec = "Major Revision"
    elif avg >= 7.5:
        rec = "Accept (with minor)"
    elif avg >= 6.0:
        rec = "Minor Revision"
    elif avg >= 4.5:
        rec = "Major Revision"
    else:
        rec = "Reject"

    strengths = []
    weaknesses = []
    modifications = []
    if stats.get("has_formula"):
        strengths.append("含形式化建模/公式，方法被明确定义。")
    if tables:
        strengths.append(f"提供了 {tables} 张对比/数据表，支撑论证。")
    if figures:
        strengths.append(f"含 {figures} 处图，直观呈现结果。")
    if len(found) >= 5:
        strengths.append("章节结构基本完整，覆盖主线。")
    if not strengths:
        strengths.append("结构完整，具备进一步打磨基础。")

    if placeholders:
        weaknesses.append(f"存在 {placeholders} 处占位（待补充），而非完整表达。")
        modifications.append("逐章补全占位内容为完整段落。")
    if figures == 0:
        weaknesses.append("缺少图表，结果呈现受限。")
        modifications.append("补充收敛曲线/对比表/消融图。")
    if not re.search(r"(?i)\[\d+\]|\bdoi\b|\barxiv\b", text):
        weaknesses.append("缺少规范参考文献引用。")
        modifications.append("补充文内引用与文献表。")
    if not weaknesses:
        weaknesses.append("未见明显缺陷，仍建议加强实验/分析深度。")
    if len(modifications) < 2:
        modifications.append("加强实验与消融分析，明确对基线增益的来源。")
    return {"scores": scores, "recommendation": rec,
            "strengths": strengths, "weaknesses": weaknesses, "modifications": modifications}


def _llm_review(r: PeerReview, text: str, notes: list) -> None:
    sys = "你是领域内资深审稿人。基于论文正文给出结构化审稿意见。输出严格 JSON。"
    snippet = text[:4000]
    prompt = (
        "论文片段（节选）：\n" + snippet + "\n\n"
        "输出 JSON：\n"
        "{\"scores\":{\"novelty\":0,\"rigor\":0,\"clarity\":0,\"soundness\":0},\n"
        " \"recommendation\":\"Accept|Minor|Major|Reject\",\n"
        " \"strengths\":[\"\"],\"weaknesses\":[\"\"],\"modifications\":[\"\"]}"
    )
    raw = llm.chat(prompt, system=sys, temperature=0.5, max_tokens=1200)
    data = _strip_json_obj(raw)
    if not data:
        notes.append("LLM 输出非合法 JSON，保留模板评分。")
        return
    sc = data.get("scores") or {}
    merged = dict(r.scores)
    for k in ("novelty", "rigor", "clarity", "soundness"):
        if isinstance(sc.get(k), (int, float)):
            merged[k] = round(max(1.0, min(10.0, float(sc[k]))), 1)
    r.scores = merged
    r.recommendation = data.get("recommendation") or r.recommendation
    if data.get("strengths"):
        r.strengths = [str(x) for x in data["strengths"]][:4]
    if data.get("weaknesses"):
        r.weaknesses = [str(x) for x in data["weaknesses"]][:4]
    if data.get("modifications"):
        r.modifications = [str(x) for x in data["modifications"]][:4]


def _strip_json_obj(raw: str) -> dict:
    s = raw.strip()
    if s.startswith("```"):
        s = s.strip("`")
        if s.lower().startswith("json"):
            s = s[4:]
    i, j = s.find("{"), s.rfind("}")
    if i == -1 or j == -1 or j < i:
        return {}
    try:
        d = json.loads(s[i : j + 1])
        return d if isinstance(d, dict) else {}
    except (ValueError, TypeError):
        return {}


def _persist(layout: Layout, paper_id: str, r: PeerReview) -> Path:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    p = root / "peer_review.json"
    p.write_text(json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    md = root / "peer_review.md"
    md.write_text(r.to_markdown(), encoding="utf-8")
    return p