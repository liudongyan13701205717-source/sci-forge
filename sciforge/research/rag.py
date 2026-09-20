"""检索增强问答层（免 key、无 LLM，本地模板合成）。

  - rag_answer:  检索相关文献 → 摘要片段 → 本地模板合成答案
  - rag_sources: 仅检索并排序来源

离线可用、免 key、无 LLM：SCI_FORGE_OFFLINE=1 或检索为空时给出诚实回答。
"""

from __future__ import annotations

from sciforge.research.lit import _offline, search_openalex


def _clip(text: str, n: int = 300) -> str:
    t = (text or "").strip()
    if not t:
        return "（无摘要）"
    return t[:n] + ("…" if len(t) > n else "")


def _retrieve(question: str, limit: int) -> list[dict]:
    if _offline():
        return []
    query = question[:80]
    papers = search_openalex(query, limit=limit)
    out = []
    for p in papers:
        out.append({
            "title": p.get("title") or "",
            "year": p.get("year"),
            "doi": p.get("doi") or "",
            "abstract": _clip(p.get("abstract") or ""),
            "cited_by": p.get("cited_by") or 0,
        })
    out.sort(key=lambda x: x["cited_by"], reverse=True)
    return out


def rag_answer(question: str, topic: str = "", limit: int = 5) -> dict:
    """检索增强问答：检索相关文献并用本地模板合成答案。离线可用、免 key、无 LLM。

    Args:
        question: 用户问题。
        topic: 检索主题（为空时用问题前 80 字符）。
        limit: 检索条数上限。

    Returns:
        {"ok": bool, "question": str, "sources": [...], "answer": str,
         "method": "local-template", "notes": [str]}
    """
    notes: list[str] = []
    if _offline():
        notes.append("离线模式")
    sources = _retrieve(topic or question, limit)
    if not sources:
        answer = "当前处于离线模式或未检索到直接相关文献，无法给出有依据的回答。"
        return {"ok": True, "question": question, "sources": [],
                "answer": answer, "method": "local-template", "notes": notes}
    top_cited = sources[0]["cited_by"]
    lines = [f"基于检索到的 {len(sources)} 篇文献（最高被引 {top_cited} 次），相关证据如下："]
    for i, s in enumerate(sources, 1):
        yr = f"({s['year']})" if s["year"] else ""
        lines.append(f"{i}. 《{s['title']}》{yr} —— {s['abstract']}")
    lines.append("结论：以上文献可作为回答该问题的参考依据，建议结合原文进一步核实。")
    notes.append(f"命中 {len(sources)} 篇")
    return {"ok": True, "question": question, "sources": sources,
            "answer": "\n".join(lines), "method": "local-template", "notes": notes}


def rag_sources(question: str, limit: int = 5) -> dict:
    """仅检索并排序相关来源（按被引降序）。离线可用、免 key。

    Args:
        question: 检索问题/主题。
        limit: 检索条数上限。

    Returns:
        {"ok": bool, "question": str, "sources": [...], "notes": [str]}
    """
    notes: list[str] = []
    if _offline():
        notes.append("离线模式")
    sources = _retrieve(question, limit)
    notes.append(f"命中 {len(sources)} 篇")
    return {"ok": True, "question": question, "sources": sources, "notes": notes}
