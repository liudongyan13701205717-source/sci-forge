"""论文元数据 / PDF 下载 / 引用图谱层（免 key 开源接口）。

  - paper_metadata:     经 Crossref 取论文元数据
  - citation_graph:     经 OpenAlex 取引用关系（被引数 + 参考文献）
  - download_paper_pdf: 经 OpenAlex OA 定位下载开放获取 PDF

离线可用、免 key：SCI_FORGE_OFFLINE=1 或网络失败时优雅降级，不抛异常。
"""

from __future__ import annotations

import os
import re
import urllib.parse
import urllib.request

from sciforge.research.lit import _get_json, _offline

_USER_AGENT = "sci-forge/0.1 (+research-ideation; no-key-public-api)"


def _clean_doi(doi: str) -> str:
    m = re.search(r"(10\.\d{4,9}/[^\s]+)", doi or "")
    if not m:
        return ""
    return m.group(1).rstrip(".,)")


def _openalex_work(clean: str) -> dict | None:
    url = "https://api.openalex.org/works/" + urllib.parse.quote("https://doi.org/" + clean)
    return _get_json(url, timeout=20)


def paper_metadata(doi: str) -> dict:
    """经 Crossref 获取论文元数据。离线可用、免 key。

    Args:
        doi: 论文 DOI。

    Returns:
        {"ok": bool, "title": str, "authors": [str], "year": int|None,
         "venue": str, "doi": str, "url": str, "abstract": str, "notes": [str]}
    """
    clean = _clean_doi(doi)
    if not clean:
        return {"ok": False, "title": "", "authors": [], "year": None,
                "venue": "", "doi": doi, "url": "", "abstract": "",
                "notes": ["不是合法 DOI 格式"]}
    if _offline():
        return {"ok": False, "title": "", "authors": [], "year": None,
                "venue": "", "doi": clean, "url": "", "abstract": "",
                "notes": ["离线模式"]}
    url = "https://api.crossref.org/works/" + urllib.parse.quote(clean)
    data = _get_json(url, timeout=20)
    if not data:
        return {"ok": False, "title": "", "authors": [], "year": None,
                "venue": "", "doi": clean, "url": "", "abstract": "",
                "notes": ["Crossref 查询失败或网络不可用"]}
    msg = data.get("message") or {}
    authors = []
    for a in (msg.get("author") or [])[:12]:
        nm = " ".join(x for x in (a.get("given"), a.get("family")) if x)
        if nm:
            authors.append(nm)
    year = None
    for k in ("published-print", "published-online", "issued"):
        v = (msg.get(k) or {}).get("date-parts") or []
        if v and v[0]:
            year = v[0][0]
            break
    abstract = re.sub(r"<[^>]+>", "", msg.get("abstract") or "")[:600]
    return {
        "ok": True,
        "title": (msg.get("title") or [""])[0],
        "authors": authors,
        "year": year,
        "venue": (msg.get("container-title") or [""])[0],
        "doi": clean,
        "url": msg.get("URL") or f"https://doi.org/{clean}",
        "abstract": abstract,
        "notes": [],
    }


def citation_graph(doi: str, depth: int = 1) -> dict:
    """经 OpenAlex 获取论文引用关系（被引数 + 参考文献）。离线可用、免 key。

    Args:
        doi: 论文 DOI。
        depth: 保留参数（当前仅展开一层，depth>1 时 notes 说明）。

    Returns:
        {"ok": bool, "root": {"title","doi","cited_by"}, "citing_count": int,
         "referenced": [{"title","doi"}], "notes": [str]}
    """
    clean = _clean_doi(doi)
    if not clean:
        return {"ok": False, "root": {}, "citing_count": 0, "referenced": [],
                "notes": ["不是合法 DOI 格式"]}
    if _offline():
        return {"ok": False, "root": {}, "citing_count": 0, "referenced": [],
                "notes": ["离线模式"]}
    work = _openalex_work(clean)
    if not work:
        return {"ok": False, "root": {}, "citing_count": 0, "referenced": [],
                "notes": ["OpenAlex 查询失败或网络不可用"]}
    root = {
        "title": work.get("title") or "",
        "doi": clean,
        "cited_by": work.get("cited_by_count") or 0,
    }
    referenced = []
    for wid in (work.get("referenced_works") or [])[:10]:
        w = _get_json(wid, timeout=15)
        if w:
            referenced.append({"title": w.get("title") or "", "doi": w.get("doi") or ""})
    notes = [f"展开深度 {max(1, depth)} 层（当前实现仅一层）"]
    return {"ok": True, "root": root, "citing_count": root["cited_by"],
            "referenced": referenced, "notes": notes}


def download_paper_pdf(doi: str, out_dir: str = "") -> dict:
    """经 OpenAlex OA 定位并下载开放获取 PDF。离线可用、免 key。

    Args:
        doi: 论文 DOI。
        out_dir: 保存目录（默认当前目录）。

    Returns:
        {"ok": bool, "path": str, "source": str, "size_bytes": int, "notes": [str]}
    """
    clean = _clean_doi(doi)
    if not clean:
        return {"ok": False, "path": "", "source": "", "size_bytes": 0,
                "notes": ["不是合法 DOI 格式"]}
    if _offline():
        return {"ok": False, "path": "", "source": "", "size_bytes": 0,
                "notes": ["离线模式"]}
    work = _openalex_work(clean)
    if not work:
        return {"ok": False, "path": "", "source": "", "size_bytes": 0,
                "notes": ["OpenAlex 查询失败或网络不可用"]}
    loc = work.get("best_oa_location") or {}
    pdf_url = loc.get("pdf_url") or ""
    if not pdf_url:
        return {"ok": False, "path": "", "source": "", "size_bytes": 0,
                "notes": ["该论文无开放获取 PDF 链接"]}
    try:
        req = urllib.request.Request(pdf_url, headers={"User-Agent": _USER_AGENT})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
    except Exception as e:  # noqa: BLE001 - 网络失败优雅降级
        return {"ok": False, "path": "", "source": pdf_url, "size_bytes": 0,
                "notes": [f"PDF 下载失败: {e}"]}
    out = out_dir or "."
    os.makedirs(out, exist_ok=True)
    fname = re.sub(r"[^\w.-]", "_", clean) + ".pdf"
    path = os.path.join(out, fname)
    with open(path, "wb") as f:
        f.write(data)
    return {"ok": True, "path": path, "source": pdf_url,
            "size_bytes": len(data), "notes": []}
