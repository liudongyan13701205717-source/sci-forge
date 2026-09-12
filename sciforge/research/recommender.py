"""论文推荐（recommender）：基于主题检索 + 热度排序，推荐值得读的代表作。

复用 lit.search_openalex / science_batch_search，离线时回退模板。
"""
from __future__ import annotations

from sciforge.research import lit
from sciforge.science.connector import DOMAINS
from sciforge.science import get_registry


def _trending_papers(topic: str, limit: int = 10, sources: list[str] | None = None) -> list[dict]:
    """检索 + 按被引量 + 年度排序，推荐热门+高质论文。"""
    if sources:
        from sciforge.science.api import science_batch_search
        r = science_batch_search(topic, databases=sources, limit=limit * 2)
        papers = r.get("hits", [])
    else:
        papers = lit.search_openalex(topic, limit=limit * 2)

    if not papers:
        return []

    # 按被引量降序 + 年份升序（优先推荐近期热门）
    def _sort_key(p: dict) -> tuple:
        cited = p.get("cited_by", 0) or 0
        year = p.get("year") or 0
        return (-cited, -(year or 0))

    papers.sort(key=_sort_key)
    return papers[:limit]


def recommend_papers(topic: str, limit: int = 5, sources: list[str] | None = None) -> dict:
    """推荐给定主题的热门代表性论文。

    Args:
        topic: 检索主题关键词。
        limit: 推荐数量（最多 20）。
        sources: 指定数据库来源列表，为空则用 OpenAlex。
    """
    limit = min(max(limit, 1), 20)
    offline = lit._offline()
    papers = _trending_papers(topic, limit=limit, sources=sources)

    if not papers:
        if offline:
            return {
                "ok": True, "topic": topic, "offline": True, "count": 0, "papers": [],
                "note": "离线模式：无法检索，建议联网后重试。",
            }
        return {
            "ok": True, "topic": topic, "offline": False, "count": 0, "papers": [],
            "note": f"在 {sources or DOMAINS} 中未检索到与「{topic}」相关文献。",
        }

    return {
        "ok": True,
        "topic": topic,
        "offline": offline,
        "count": len(papers),
        "papers": [
            {
                "title": p.get("title", ""),
                "authors": p.get("authors", []),
                "year": p.get("year"),
                "venue": p.get("venue", ""),
                "cited_by": p.get("cited_by", 0),
                "doi": p.get("doi", ""),
                "url": p.get("url", ""),
                "abstract": p.get("abstract", ""),
            }
            for p in papers
        ],
    }
