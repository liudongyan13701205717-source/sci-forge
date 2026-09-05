"""引文邻域与热度分析（community）：围绕一个 DOI 或主题词，分析相关工作的
被引热度、年度分布与载体分布，辅助判断选题冷热与切入时机。

复用 lit.py 的 OpenAlex 免 key 通道，离线时回退启发式模板。
"""

from __future__ import annotations

import json
import re
import urllib.parse
from dataclasses import dataclass, field
from collections import Counter

from sciforge.core import Layout
from sciforge.research import lit


@dataclass
class CitationLandscape:
    ok: bool
    paper_id: str = ""
    source: str = ""          # 传入的 doi 或 topic
    mode: str = "topic"       # doi | topic
    headline: str = ""
    total_works: int = 0
    max_cited: int = 0
    works_by_year: list = field(default_factory=list)
    top_cited: list = field(default_factory=list)
    venues: list = field(default_factory=list)
    notes: list = field(default_factory=list)
    error: str = ""
    offline: bool = False

    def to_dict(self) -> dict:
        return {
            "ok": self.ok, "paper_id": self.paper_id, "source": self.source,
            "mode": self.mode, "headline": self.headline,
            "total_works": self.total_works, "max_cited": self.max_cited,
            "works_by_year": self.works_by_year, "top_cited": self.top_cited,
            "venues": self.venues, "notes": self.notes,
            "error": self.error, "offline": self.offline,
        }

    def to_markdown(self) -> str:
        y = "\n".join(
            f"- {d['year']}: {d['count']} 篇" for d in self.works_by_year
        ) or "- （无年度数据）"
        top = "\n".join(
            f"- [{p.get('year','?')}] {p.get('title','')} — "
            f"{p.get('venue','')}，被引 {p.get('cited_by',0)}"
            for p in self.top_cited[:10]
        ) or "- （无相关作品）"
        ven = "\n".join(
            f"- {v['venue']}: {v['count']} 篇" for v in self.venues[:10]
        ) or "- （无载体数据）"
        notes = "\n".join(f"- {n}" for n in self.notes) or "- （无额外说明）"
        return "\n\n".join([
            f"# 引文邻域分析：{self.paper_id}",
            f"## 概览\n{self.headline or '（无数据）'}\n\n"
            f"- 有效作品数：{self.total_works}\n- 最高被引：{self.max_cited}",
            f"## 年度分布\n{y}",
            f"## 高被引代表\n{top}",
            f"## 主要载体\n{ven}",
            f"## 结论与提示\n{notes}",
        ])


def _fetch_work_by_doi(doi: str, timeout: int = 20) -> dict:
    if lit._offline():
        return {}
    clean = re.search(r"(10\.\d{4,9}/[^\s]+)", doi or "")
    if not clean:
        return {}
    d = clean.group(1).rstrip(".,)")
    url = "https://api.openalex.org/works?filter=doi:" + urllib.parse.quote(d) + "&per-page=1"
    data = lit._get_json(url, timeout=timeout)
    for w in (data.get("results") if data else []) or []:
        return {"title": w.get("title") or "",
                "year": w.get("publication_year"),
                "doi": w.get("doi"),
                "venue": (w.get("primary_location") or {}).get("display_name") or "",
                "cited_by": w.get("cited_by_count") or 0}
    return {}


def _time_window(total: int, max_cited: int) -> str:
    if total < 30:
        return "邻域仍较小，属于早期/长尾方向：机会大但读者基数有限，建议借热点场景切入。"
    if max_cited >= 1000:
        return "邻域高热（存在千人引代表作）：建议避开硬刚，找子问题/专用场景做差异化。"
    return "邻域中等偏热：有对话者、有可对比基线，适合快速产出发文。"


def citation_landscape(
    *,
    paper_id: str,
    layout: Layout,
    doi_or_topic: str,
    sources: list[str] | None = None,
) -> CitationLandscape:
    """引文热度分析：DOI 用 OpenAlex 精确查；否则按主题检索。"""
    r = CitationLandscape(ok=False, paper_id=paper_id, source=doi_or_topic)

    doi_like = bool(re.search(r"10\.\d{4,9}/", doi_or_topic or ""))
    r.mode = "doi" if doi_like else "topic"

    works: list[dict] = []
    if r.mode == "doi":
        seed = _fetch_work_by_doi(doi_or_topic)
        if not seed:
            r.offline = lit._offline()
            r.notes.append("DOI 在 OpenAlex 未命中（可能离线/拼写问题）。")
            r.headline = "无法定位该 DOI 的引文邻域，请检查 DOI 或改用主题关键词。"
        else:
            works.append(seed)
            r.notes.append(f"以 DOI 定位到「{seed.get('title','')[:60]}」，"
                           f"被引 {seed.get('cited_by',0)}。")
    else:
        from sciforge.science.api import cross_lookup
        if sources:
            works = cross_lookup(doi_or_topic, databases=sources, limit=40)
        else:
            works = lit.search_openalex(doi_or_topic, limit=40)
        if not works:
            r.offline = lit._offline()
            r.notes.append("主题检索无结果（离线或关键词过冷门）。")
            r.headline = "未检索到相关作品，建议更换关键词后再试。"
        else:
            r.notes.append("基于主题检索 top 作品的被引量判断领域热度。")

    if not works:
        r.error = "无可用引文数据（离线或未命中）。"
        return r

    r.total_works = len(works)
    r.max_cited = max(w.get("cited_by", 0) for w in works)
    r.headline = _time_window(r.total_works, r.max_cited)

    by_year = Counter()
    for w in works:
        yr = w.get("year")
        if yr:
            by_year[yr] += 1
    r.works_by_year = [{"year": y, "count": c} for y, c in sorted(by_year.items())]

    r.top_cited = sorted(works, key=lambda w: w.get("cited_by", 0), reverse=True)[:15]

    venues = Counter()
    for w in works:
        v = (w.get("venue") or "").strip()
        if v:
            venues[v] += 1
    r.venues = [{"venue": v, "count": c} for v, c in venues.most_common()]

    _persist(layout, paper_id, r)
    r.ok = True
    return r


def _persist(layout: Layout, paper_id: str, r: CitationLandscape):
    root = layout.project_dir(paper_id) / "research"
    root.mkdir(parents=True, exist_ok=True)
    (root / "citation_landscape.json").write_text(
        json.dumps(r.to_dict(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (root / "citation_landscape.md").write_text(r.to_markdown(), encoding="utf-8")