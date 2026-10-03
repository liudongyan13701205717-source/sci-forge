"""论文↔代码关联层（免 key 开源接口）。

  - find_code_for_paper: 定位论文并检索关联代码/数据集
  - link_papers_to_code: 主题论文批量关联代码

离线可用、免 key：SCI_FORGE_OFFLINE=1 或检索为空时返回空列表 + 说明。
"""

from __future__ import annotations

from sciforge.research.lit import _offline, search_openalex
from sciforge.science.api import science_batch_search

_CODE_DBS = ["huggingface", "zenodo"]


def _search_code(query: str, limit: int) -> list[dict]:
    """内部助手：检索代码/数据集并归一化。"""
    if _offline():
        return []
    res = science_batch_search(query, databases=_CODE_DBS, limit=limit)
    out = []
    for h in res.get("hits") or []:
        out.append({
            "title": h.get("title") or "",
            "url": h.get("url") or h.get("doi") or "",
            "source": "science",
        })
    return out


def find_code_for_paper(title: str, limit: int = 5) -> dict:
    """定位论文并检索其关联代码/数据集。离线可用、免 key。

    Args:
        title: 论文标题。
        limit: 代码检索条数上限。

    Returns:
        {"ok": bool, "paper": {...}|None, "code_links": [...], "notes": [str]}
    """
    notes: list[str] = []
    paper = None
    if not _offline():
        hits = search_openalex(title, limit=1)
        if hits:
            p = hits[0]
            paper = {"title": p.get("title") or "", "doi": p.get("doi") or "",
                     "year": p.get("year")}
    links = _search_code(title, limit)
    if not paper:
        notes.append("未定位到论文（离线或检索失败）")
    if not links:
        notes.append("未检索到关联代码/数据集")
    return {"ok": True, "paper": paper, "code_links": links, "notes": notes}


def link_papers_to_code(topic: str, limit: int = 5) -> dict:
    """主题论文批量关联代码。离线可用、免 key。

    Args:
        topic: 检索主题。
        limit: 论文条数上限。

    Returns:
        {"ok": bool, "topic": str, "links": [...], "notes": [str]}
    """
    notes: list[str] = []
    papers = search_openalex(topic, limit=limit) if not _offline() else []
    if not papers:
        notes.append("离线模式或未检索到论文")
    links = []
    for p in papers:
        links.append({
            "paper": p.get("title") or "",
            "doi": p.get("doi") or "",
            "code_links": _search_code(p.get("title") or "", limit=2),
        })
    notes.append(f"处理 {len(papers)} 篇论文")
    return {"ok": True, "topic": topic, "links": links, "notes": notes}
