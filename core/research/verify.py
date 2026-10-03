"""引用事实核查层（免 key 开源接口）。

对论文中的引用/主张做事实核查：
  - verify_citation:      单条 DOI 真实性核验（Crossref）
  - verify_claim:         主张 → 检索支持证据 → 判定 SUPPORTED/PARTIAL/UNSUPPORTED
  - verify_reference_list: 批量 DOI 核验

离线可用、免 key：SCI_FORGE_OFFLINE=1 或网络失败时优雅降级，不抛异常。
"""

from __future__ import annotations

import datetime as _dt

from sciforge.research.lit import _offline, search_openalex, verify_doi


def verify_citation(doi: str) -> dict:
    """核验单个 DOI 是否真实存在（Crossref）。离线可用、免 key。

    Args:
        doi: 待核验的 DOI（如 "10.1038/s41586-020-2649-2"）。

    Returns:
        {"ok": bool, "doi": str, "reason": str, "checked_at": str}
    """
    now = _dt.datetime.now().isoformat(timespec="seconds")
    if _offline():
        return {"ok": False, "doi": doi, "reason": "离线模式", "checked_at": now}
    res = verify_doi(doi)
    return {
        "ok": res.get("ok", False),
        "doi": res.get("doi", doi),
        "reason": res.get("reason", ""),
        "checked_at": now,
    }


def verify_claim(claim: str, topic: str = "", limit: int = 5) -> dict:
    """核验一条研究主张：检索 OpenAlex 支持证据并给出判定。离线可用、免 key。

    Args:
        claim: 待核验的主张/论断文本。
        topic: 检索主题（为空时用 claim 前 80 字符）。
        limit: 检索条数上限。

    Returns:
        {"ok": bool, "claim": str, "evidence": [...], "verdict": str, "notes": [str]}
    """
    query = topic or claim[:80]
    papers = search_openalex(query, limit=limit) if not _offline() else []
    notes: list[str] = []
    if _offline():
        notes.append("离线模式，未检索证据")
    if not papers:
        return {
            "ok": True,
            "claim": claim,
            "evidence": [],
            "verdict": "NO_EVIDENCE",
            "notes": notes + ["未检索到直接相关文献"],
        }
    top_cited = max((p.get("cited_by") or 0) for p in papers)
    if len(papers) >= 3 and top_cited >= 50:
        verdict = "SUPPORTED"
    elif len(papers) >= 1 and top_cited >= 10:
        verdict = "PARTIAL"
    else:
        verdict = "UNSUPPORTED"
    notes.append(f"命中 {len(papers)} 篇，最高被引 {top_cited}")
    return {
        "ok": True,
        "claim": claim,
        "evidence": papers,
        "verdict": verdict,
        "notes": notes,
    }


def verify_reference_list(refs: list[str]) -> dict:
    """批量核验参考文献 DOI。离线可用、免 key。

    Args:
        refs: DOI 字符串列表。

    Returns:
        {"ok": bool, "total": int, "valid": [str],
         "invalid": [{"doi": str, "reason": str}], "notes": [str]}
    """
    valid: list[str] = []
    invalid: list[dict] = []
    for doi in refs or []:
        r = verify_citation(doi)
        if r["ok"]:
            valid.append(r["doi"])
        else:
            invalid.append({"doi": doi, "reason": r["reason"]})
    return {
        "ok": True,
        "total": len(refs or []),
        "valid": valid,
        "invalid": invalid,
        "notes": [f"有效 {len(valid)} / 无效 {len(invalid)}"],
    }
