"""论文润色与检查（paper_polish）：对已有正文做三类质量检查并产出建议。

mode:
  - completeness：完整性检查（缺哪些关键章节/图表/引用）
  - consistency：一致性检查（术语/编号/公式/单位重复或矛盾）
  - grammar：语言润色（惯用语、冗余、被动语态等提示）
无 LLM 时全部基于规则做确定性检查；可 LLM 增强润色示例。
落盘 projects/{paper_id}/research/polish_{mode}.json + md。
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from sciforge.core import Layout
from sciforge.core import model as llm
from sciforge.write.doc import DocStore

_SECTIONS = ["摘要", "引言", "研究问题", "建模", "求解", "实验", "结果", "结论",
             "abstract", "introduction", "method", "experiments", "results", "conclusion"]
_MODES = ("completeness", "consistency", "grammar")


@dataclass
class PolishResult:
    ok: bool
    paper_id: str = ""
    mode: str = ""
    score: float = 0.0
    issues: list = field(default_factory=list)
    rewritten: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    error: str = ""
    llm_used: bool = False

    def to_dict(self) -> dict:
        return {k: getattr(self, k) for k in (
            "ok", "paper_id", "mode", "score", "issues", "rewritten",
            "notes", "error", "llm_used",
        )}

    def to_markdown(self) -> str:
        def bullet(xs):
            return "\n".join(f"- {x}" for x in xs) if xs else "- （暂无）"

        return "\n\n".join([
            f"# 论文检查：{self.mode}（{self.paper_id}）",
            f"**质量分：** {self.score}/10",
            f"## 问题清单\n{bullet(self.issues)}",
            f"## 润色示例\n{bullet(self.rewritten)}",
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


def paper_polish(
    *,
    paper_id: str,
    layout: Layout,
    mode: str = "completeness",
) -> PolishResult:
    mode = mode if mode in _MODES else "completeness"
    r = PolishResult(ok=False, paper_id=paper_id, mode=mode)
    notes: list = []
    text = _read_doc(layout, paper_id)
    if not text.strip():
        r.error = f"项目 {paper_id} 尚无正文，请先写入内容。"
        r.ok = False
        return r

    issues, score = _check(text, mode)
    r.issues = issues
    r.score = score

    if llm.configured() and mode == "grammar":
        try:
            _llm_polish(r, text, notes)
            r.llm_used = True
        except RuntimeError as e:
            notes.append(f"LLM 润色不可用，保留规则结果：{e}")

    r.notes = notes
    r.ok = True
    _persist(layout, paper_id, r)
    return r


def _check(text: str, mode: str) -> tuple[list, float]:
    issues: list = []
    if mode == "completeness":
        missing = [s for s in ("摘要", "引言", "实验", "结果", "结论")
                   if not re.search(rf"(?i)#+\s*.*{s}", text)]
        issues += [f"缺少关键章节：{m}" for m in missing]
        if text.count("|") > 3 and text.count("|") // 10 < 1:
            issues.append("存在表格标记但结构可能不完整，请核对列对齐。")
        if not re.search(r"(?i)\[\d+\]|\bdoi\b|\barxiv\b", text):
            issues.append("缺少规范参考文献引用。")
        if text.count("待补充") > 0:
            issues.append(f"存在 {text.count('待补充')} 处占位（待补充）未替换。")
        if text.count("![" ) < 1 and not re.search(r"\\includegraphics|\\begin\{figure\}", text):
            issues.append("缺少图（可用收敛曲线/对比图/框架图）。")

    elif mode == "consistency":
        # 检查公式编号重复、术语口径不一、占位符残留
        eqs = re.findall(r"\(\s*(\d+)\s*\)", text)
        dup = {n for n in set(eqs) if eqs.count(n) > 1}
        if dup:
            issues.append(f"公式/编号重复使用：{sorted(dup, key=int)[:8]}，请统一编号。")
        if "{" in text and re.search(r"\{\{\s*[a-zA-Z_]+\s*\}\}", text):
            issues.append("存在未替换的模板占位符 {{...}}。")
        if re.search(r"(?i)\byour model\b|your approach\b|\bTODO\b", text):
            issues.append("存在留给读者的指代（your model/TODO），应改为确定名称。")
        if "图 1" in text and "图 1" not in text and re.search(r"图\s+1", text):
            pass
        if not issues:
            issues.append("未发现明显一致性问题，术语/编号统一。")

    else:  # grammar
        if re.search(r"\b(a a|the the|is is|of of)\b", text, re.I):
            issues.append("发现重复词组（如 a a / the the），请删除其一。")
        if re.search(r"(?i)\b(very|really|quite|pretty)\b", text):
            issues.append("存在口语化程度副词（very/really/quite），学术写作建议替换。")
        if re.search(r"[，,]\s*并且\s*[，,]", text) or text.count("并且") > 6:
            issues.append("「并且」使用偏多，建议多样化连接词。")
    if re.search(r"(?i)\b(utilize)\b", text):
        issues.append("utilize 可简化为 use，更简洁。")
    if not issues:
        issues.append("语言整体规范，无明显冗余或口语化表达。")

    # 得分：100 满分按问题数扣
    base = 8.0 if len(issues) else 9.0
    score = round(max(3.0, min(10.0, base - 0.8 * len(issues))), 1)
    return issues, score


def _llm_polish(r: PolishResult, text: str, notes: list) -> None:
    sys = "你是学术写作编辑。仅针对给出的段落给出润色建议，不扩大范围。输出严格 JSON。"
    # 取正文开头与结尾两段
    paras = [p for p in re.split(r"\n\s*\n", text) if len(p.strip()) > 60][:4]
    snippet = "\n\n".join(paras)
    prompt = (
        "段落：\n" + snippet + "\n\n"
        "输出 JSON：\n{\"issues\":[\"问题:建议\"],\"rewritten\":[\"擦净后的示例段（任选1-2段）\"]}"
    )
    raw = llm.chat(prompt, system=sys, temperature=0.5, max_tokens=1400)
    data = _strip_json_obj(raw)
    if not data:
        notes.append("LLM 输出非合法 JSON，保留规则结果。")
        return
    if data.get("issues"):
        r.issues = ([str(x) for x in data["issues"]][:6]
                    + [i for i in r.issues if i not in [str(x) for x in data["issues"]]])
    if data.get("rewritten"):
        r.rewritten = [str(x) for x in data["rewritten"]][:3]
        if not r.issues:
            r.score = round(min(10.0, r.score + 0.5), 1)


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


def _persist(layout: Layout, paper_id: str, r: PolishResult) -> Path:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    p = root / f"polish_{r.mode}.json"
    p.write_text(json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    md = root / f"polish_{r.mode}.md"
    md.write_text(r.to_markdown(), encoding="utf-8")
    return p
