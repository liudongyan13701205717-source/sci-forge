from __future__ import annotations

import urllib.parse
from sciforge.science import register as _register
from sciforge.science.connector import Connector
from sciforge.science.http import http_get_json


def _zenodo_search(query, limit):
    params = {"q": query, "size": str(limit), "type": "dataset"}
    url = "https://zenodo.org/api/records?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for h in data.get("hits", {}).get("hits", []):
        meta = h.get("metadata", {})
        out.append({
            "title": meta.get("title", ""),
            "year": None,
            "doi": meta.get("doi"),
            "url": h.get("links", {}).get("html", f"https://zenodo.org/record/{h.get('id','')}"),
            "venue": "Zenodo",
            "authors": [c.get("name", "") for c in meta.get("creators", [])[:12]],
            "cited_by": 0,
            "abstract": meta.get("description", ""),
        })
    return out


def _doaj_search(query, limit):
    url = f"https://doaj.org/api/v2/search/articles/{urllib.parse.quote(query)}?pageSize={limit}"
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", []):
        bib = r.get("bibjson", {})
        doi = (bib.get("identifier") or [{}])[0].get("id") if bib.get("identifier") else None
        link = (bib.get("link") or [{}])[0].get("url", "") if bib.get("link") else ""
        out.append({
            "title": bib.get("title", ""),
            "year": bib.get("year"),
            "doi": doi,
            "url": link,
            "venue": (bib.get("journal", {}) or {}).get("title", ""),
            "authors": [a.get("name", "") for a in bib.get("author", [])[:12]],
            "cited_by": 0,
            "abstract": bib.get("abstract", ""),
        })
    return out


def _openaire_search(query, limit):
    params = {"keywords": query, "format": "json", "pageSize": str(limit)}
    url = "https://api.openaire.eu/search/publications?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("response", {}).get("results", {}).get("result", []):
        meta = r.get("metadata", {}).get("oaf:entity", {}).get("oaf:result", {})
        title_obj = meta.get("title", {})
        title = title_obj.get("$", "") if isinstance(title_obj, dict) else ""
        out.append({
            "title": title,
            "year": None,
            "doi": "",
            "url": "",
            "venue": "",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _huggingface_search(query, limit):
    params = {"search": query, "limit": str(limit)}
    url = "https://huggingface.co/api/datasets?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for d in data:
        did = d.get("id", "")
        out.append({
            "title": d.get("title") or did,
            "year": None,
            "doi": None,
            "url": f"https://huggingface.co/datasets/{did}" if did else "",
            "venue": "Hugging Face",
            "authors": [d.get("author", "")] if d.get("author") else [],
            "cited_by": d.get("downloads") or 0,
            "abstract": d.get("description", ""),
        })
    return out


def register():
    specs = [
        ("zenodo", "Zenodo", "Zenodo research data", _zenodo_search),
        ("doaj", "DOAJ", "Directory of Open Access Journals", _doaj_search),
        ("openaire", "OpenAIRE", "OpenAIRE research graph", _openaire_search),
        ("huggingface", "Hugging Face", "Hugging Face datasets", _huggingface_search),
    ]
    for cid, name, desc, fn in specs:
        _register(Connector(id=cid, name=name, domain="datasets",
                            description=desc, search=fn))
