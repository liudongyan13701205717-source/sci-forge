"""文献检索层（免 key 开源接口）。

以 OpenAlex 为主源（公开、免 key、稳定、覆盖 arXiv 预印本/期刊/会议）。
可选尝试 arXiv API（本环境 export.arxiv.org 可能不稳，连不上不强依赖）。

不引入任何 API key。全部走公开只读接口。
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from typing import Optional

_USER_AGENT = "sci-forge/0.1 (+research-ideation; no-key-public-api)"


class LitError(Exception):
    pass


def _get_json(url: str, timeout: int = 20) -> Optional[dict]:
    req = urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, OSError, ValueError) as e:
        return None


def _offline() -> bool:
    return os.environ.get("CLAWSGO_SELF_OFFLINE") == "1"


def search_openalex(query: str, *, limit: int = 8, timeout: int = 20) -> list[dict]:
    """OpenAlex works 检索，返回精简结构。失败返回空列表（不抛错）。

    返回每项：{title, year, doi, url, venue, authors[], cited_by, abstract}
    """
    if _offline():
        return []
    params = {
        "search": query,
        "per-page": str(limit),
        "mailto": "research@localhost",
    }
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = _get_json(url, timeout=timeout)
    if not data:
        return []
    out: list[dict] = []
    for w in data.get("results", []):
        auths = []
        for a in (w.get("authorships") or [])[:12]:
            au = a.get("author") or {}
            nm = au.get("display_name")
            if nm:
                auths.append(nm)
        out.append(
            {
                "title": w.get("title") or "",
                "year": w.get("publication_year"),
                "doi": w.get("doi"),
                "url": w.get("id"),
                "venue": (w.get("primary_location") or {}).get("display_name") or "",
                "authors": auths,
                "cited_by": w.get("cited_by_count") or 0,
                "abstract": _truncate(w.get("abstract_inverted_index")),
            }
        )
    return out


def _truncate(inv_index) -> str:
    """OpenAlex 倒排索引 -> 纯文本短文。"""
    if not inv_index:
        return ""
    pos: dict[int, str] = {}
    for word, idxs in inv_index.items():
        for i in idxs:
            pos[i] = word
    s = " ".join(pos[i] for i in sorted(pos))
    return s[:600]


def search_arxiv(query: str, *, limit: int = 4, timeout: int = 20) -> list[dict]:
    """arXiv API（免 key）。连接不稳时返回空。"""
    if _offline():
        return []
    q = urllib.parse.quote(query)
    url = (
        "https://export.arxiv.org/api/query?"
        f"search_query=all:{q}&max_results={limit}"
        "&sortBy=submittedDate&sortOrder=descending"
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", "ignore")
    except (urllib.error.URLError, urllib.error.HTTPError, OSError):
        return []
    import re
    import xml.etree.ElementTree as ET

    ns = {"a": "http://www.w3.org/2005/Atom"}
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return []
    out = []
    for e in root.findall("a:entry", ns):
        title = (e.findtext("a:title", "", ns) or "").strip().replace("\n", " ")
        link = ""
        for l_ in e.findall("a:link", ns):
            if l_.get("rel") == "alternate":
                link = l_.get("href") or ""
                break
        out.append({"title": title, "url": link, "authors": [], "year": None})
    return out


def dedupe(papers: list[dict], key="title") -> list[dict]:
    """按标题去重（大小写/空白归一）。保留首次出现。"""
    seen: set[str] = set()
    out = []
    for p in papers:
        t = (p.get(key) or "").strip().lower()
        t = " ".join(t.split())
        if not t or t in seen:
            continue
        seen.add(t)
        out.append(p)
    return out


def verify_doi(doi: str, timeout: int = 15) -> dict:
    """引文核验：通过 Crossref 校验 DOI 是否真实存在。免 key。"""
    import re

    m = re.search(r"(10\.\d{4,9}/[^\s]+)", doi or "")
    if not m:
        return {"ok": False, "reason": "不是合法 DOI 格式"}
    clean = m.group(1).rstrip(".,)")
    url = "https://api.crossref.org/works/" + urllib.parse.quote(clean)
    req = urllib.request.Request(
        url, headers={"User-Agent": _USER_AGENT + " (mailto:research@localhost)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status == 200:
                return {"ok": True, "doi": clean}
            return {"ok": False, "reason": f"HTTP {resp.status}"}
    except urllib.error.HTTPError as e:
        return {"ok": False, "reason": f"HTTP {e.code}"}
    except (urllib.error.URLError, OSError) as e:
        return {"ok": False, "reason": f"网络错误：{e}"}
