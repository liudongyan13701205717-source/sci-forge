"""文献综述（survey）：基于免 key OpenAlex 检索，生成某主题的综述框架与要点。

对齐 RELATED_WORK / SURVEY：产出
  - 检索到的代表文献（按年份/被引归纳）
  - 按主题聚类后的子方向
  - 研究缺口
  - 综述写作要点（可直接作为 related work 素材）
落盘 projects/{paper_id}/research/literature_review.json + md。
无 LLM 时可确定性生成（基于检索结果直接归纳）。
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from sciforge.core import Layout
from sciforge.core import model as llm
from sciforge.research import lit


@dataclass
class LiteratureReview:
    ok: bool
    topic: str = ""
    papers: list = field(default_factory=list)
    clusters: list = field(default_factory=list)
    gaps: list = field(default_factory=list)
    keyworks: list = field(default_factory=list)
    outline: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    error: str = ""
    llm_used: bool = False

    def to_dict(self) -> dict:
        return {k: getattr(self, k) for k in (
            "ok", "topic", "papers", "clusters", "gaps", "keyworks",
            "outline", "notes", "error", "llm_used",
        )}

    def to_markdown(self) -> str:
        def bullet(xs):
            return "\n".join(f"- {x}" for x in xs) if xs else "- （待补充）"

        pubs = []
        for p in self.papers:
            pubs.append(f"- [{p.get('year','?')}] {p.get('title','')} — {p.get('venue','')} "
                        f"(被引 {p.get('cited_by',0)}) {p.get('doi','') or p.get('url','')}")
        pubs_text = "\n".join(pubs) if pubs else "- （检索无结果，请检查网络或换关键词）"
        return "\n\n".join([
            f"# 文献综述：{self.topic}",
            f"## 代表文献\n{pubs_text}",
            f"## 主题聚类\n{bullet(self.clusters)}",
            f"## 研究缺口\n{bullet(self.gaps)}",
            f"## 关键词\n{bullet(self.keyworks)}",
            f"## 综述结构建议\n{bullet(self.outline)}",
        ])


def literature_review(
    topic: str,
    *,
    paper_id: str,
    layout: Layout,
    limit: int = 10,
    sources: list[str] | None = None,
) -> LiteratureReview:
    r = LiteratureReview(ok=False, topic=topic)
    notes: list = []
    from sciforge.science.api import cross_lookup
    if sources:
        papers = cross_lookup(topic, databases=sources, limit=limit)
    else:
        papers = lit.search_openalex(topic, limit=limit)
    papers = lit.dedupe(papers)
    r.papers = papers
    if not papers:
        notes.append("OpenAlex 检索无结果（离线或网络），综述基于空集，缺口为启发式。")
    r.keyworks = _keywords(topic)

    if llm.configured() and papers:
        try:
            _llm_review(r, notes)
            r.llm_used = True
        except RuntimeError as e:
            notes.append(f"LLM 综述不可用，回退模板：{e}")

    if not r.clusters:
        _template_review(r, notes)

    r.notes = notes
    r.ok = True
    _persist(layout, paper_id, r)
    return r


def _keywords(topic: str) -> list:
    # 简单分词：按空格/逗号/顿号拆分，去重并保留前 6 个
    import re

    toks = re.split(r"[\s,，、;；/]+", topic)
    out = []
    for t in toks:
        t = t.strip()
        if t and t not in out:
            out.append(t)
    return out[:6] or [topic]


def _template_review(r: LiteratureReview, notes: list) -> None:
    papers = r.papers
    # 按年份排序，形成时间线式聚类
    years = sorted({(p.get("year") or 0) for p in papers})
    r.clusters = [f"近年在「{r.topic}」的代表进展（时间线 {y} 前后）" for y in years[-3:]] or [
        "尚无强相关文献，属早期阶段"]
    r.gaps = [
        "现有工作普遍缺少跨领域/大规模泛化验证",
        "统一基准与公平对比不足（指标口径不一）",
        "很少针对资源受限场景做效率-精度联合优化",
    ]
    r.outline = [
        "引言：动机与综述范围",
        "相关方法分类与代表工作综述",
        "方法对比表（方法/数据/指标/结果）",
        "研究缺口与本工作定位",
        "小结与展望",
    ]
    if not papers:
        notes.append("模板综述：未能检索到实际文献，内容为占位框架。")
    else:
        notes.append("无 LLM，基于检索结果做确定性归纳。")
    return


def _llm_review(r: LiteratureReview, notes: list) -> None:
    sys = "你是资深文献综述撰写者。基于给定的文献列表归纳主题聚类、研究缺口、综述结构。输出严格 JSON。"
    pubs = []
    for p in r.papers[:14]:
        pubs.append(f"[{p.get('year','?')}] {p.get('title','')} ({p.get('venue','')}, 被引{p.get('cited_by',0)})")
    prompt = (
        f"主题：{r.topic}\n代表文献：\n" + "\n".join(pubs) + "\n\n"
        "输出 JSON：\n"
        "{\"clusters\":[\"子方向：一句概述\"],\"gaps\":[\"研究缺口\"],"
        "\"outline\":[\"综述章节结构\"]}"
    )
    raw = llm.chat(prompt, system=sys, temperature=0.6, max_tokens=1400)
    data = _strip_json_obj(raw)
    if not data:
        notes.append("LLM 输出非合法 JSON，回退模板。")
        return
    r.clusters = [str(x) for x in data.get("clusters", []) if x]
    r.gaps = [str(x) for x in data.get("gaps", []) if x]
    r.outline = [str(x) for x in data.get("outline", []) if x]


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


def _persist(layout: Layout, paper_id: str, r: LiteratureReview) -> Path:
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    p = root / "literature_review.json"
    p.write_text(json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    md = root / "literature_review.md"
    md.write_text(r.to_markdown(), encoding="utf-8")
    return p
