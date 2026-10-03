"""主题多源检索打分层（免 key 开源接口）。

  - scout_topic:   多源聚合检索 + 去重 + 评分排序
  - scout_compare: 多主题横向对比

离线可用、免 key：SCI_FORGE_OFFLINE=1 时返回空结果 + 说明。
"""

from __future__ import annotations

from sciforge.research.lit import _offline, dedupe
from sciforge.science.api import science_batch_search

_LIT_DBS = ["openalex", "arxiv", "crossref", "semantic-scholar"]


def _score(p: dict, topic: str, now_year: int = 2026) -> float:
    cited = p.get("cited_by") or 0
    year = p.get("year")
    recency = 0.0
    if year:
        age = now_year - year
        if age <= 3:
            recency = 3.0
        elif age <= 5:
            recency = 1.0
    kw = 0.0
    for w in topic.split():
        if w and w.lower() in (p.get("title") or "").lower():
            kw += 1.0
    kw = min(kw, 5.0)
    return round(cited * 1.0 + recency + kw, 2)


def scout_topic(topic: str, limit: int = 10) -> dict:
    """多源聚合检索主题论文并按相关度/被引/新近度评分排序。离线可用、免 key。

    Args:
        topic: 检索主题/关键词。
        limit: 每源检索条数上限。

    Returns:
        {"ok": bool, "topic": str, "total": int, "ranked": [...], "notes": [str]}
    """
    notes: list[str] = []
    if _offline():
        notes.append("离线模式，无检索结果")
        return {"ok": True, "topic": topic, "total": 0, "ranked": [], "notes": notes}
    res = science_batch_search(topic, databases=_LIT_DBS, limit=limit)
    hits = res.get("hits") or []
    if res.get("offline"):
        notes.append("science 层离线，无检索结果")
        return {"ok": True, "topic": topic, "total": 0, "ranked": [], "notes": notes}
    papers = dedupe(hits)
    ranked = []
    for p in papers:
        ranked.append({
            "title": p.get("title") or "",
            "year": p.get("year"),
            "doi": p.get("doi") or "",
            "venue": p.get("venue") or "",
            "authors": p.get("authors") or [],
            "cited_by": p.get("cited_by") or 0,
            "score": _score(p, topic),
            "source": "science",
        })
    ranked.sort(key=lambda x: x["score"], reverse=True)
    notes.append(f"聚合 {len(hits)} 条，去重后 {len(ranked)} 条")
    return {"ok": True, "topic": topic, "total": len(ranked), "ranked": ranked,
            "notes": notes}


def scout_compare(topics: list[str], limit: int = 5) -> dict:
    """多主题横向对比（按命中数降序）。离线可用、免 key。

    Args:
        topics: 主题列表。
        limit: 每主题检索条数上限。

    Returns:
        {"ok": bool, "topics": [str], "comparison": [...], "notes": [str]}
    """
    comparison = []
    for t in topics or []:
        r = scout_topic(t, limit=limit)
        ranked = r.get("ranked") or []
        comparison.append({
            "topic": t,
            "total": r.get("total", 0),
            "top_hit": ranked[0]["title"] if ranked else "",
            "top_cited": ranked[0]["cited_by"] if ranked else 0,
        })
    comparison.sort(key=lambda x: x["total"], reverse=True)
    return {"ok": True, "topics": list(topics or []), "comparison": comparison,
            "notes": [f"对比 {len(comparison)} 个主题"]}
