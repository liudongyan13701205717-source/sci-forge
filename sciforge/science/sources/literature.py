from __future__ import annotations

import urllib.parse
import xml.etree.ElementTree as ET
from sciforge.science import register as _register
from sciforge.science.connector import Connector
from sciforge.science.http import http_get_json, http_get_text


def _truncate(inv_index) -> str:
    if not inv_index or not isinstance(inv_index, dict):
        return ""
    pos = {}
    for word, idxs in inv_index.items():
        for i in idxs:
            pos[i] = word
    s = " ".join(pos[i] for i in sorted(pos))
    return s[:600]


def _openalex_search(query, limit):
    params = {"search": query, "per-page": str(limit), "mailto": "research@localhost"}
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for w in data.get("results", []):
        auths = [a.get("author", {}).get("display_name", "")
                 for a in (w.get("authorships") or [])[:12]]
        auths = [x for x in auths if x]
        out.append({
            "title": w.get("title") or "",
            "year": w.get("publication_year"),
            "doi": w.get("doi"),
            "url": w.get("id", ""),
            "venue": (w.get("primary_location") or {}).get("display_name", ""),
            "authors": auths,
            "cited_by": w.get("cited_by_count") or 0,
            "abstract": _truncate(w.get("abstract_inverted_index")),
        })
    return out


def _arxiv_search(query, limit):
    q = urllib.parse.quote(query)
    url = (f"https://export.arxiv.org/api/query?search_query=all:{q}"
           f"&max_results={limit}&sortBy=submittedDate&sortOrder=descending")
    body = http_get_text(url)
    if not body:
        return []
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
                link = l_.get("href", "")
                break
        out.append({"title": title, "url": link, "authors": [], "year": None,
                    "doi": None, "venue": "", "cited_by": 0, "abstract": ""})
    return out


def _biorxiv_search(query, limit):
    url = f"https://api.biorxiv.org/details/biorxiv/0/{limit}"
    data = http_get_json(url + "?q=" + urllib.parse.quote(query))
    if not data:
        return []
    out = []
    for item in data.get("collection", []):
        doi = item.get("doi", "")
        out.append({
            "title": item.get("title", ""),
            "year": None,
            "doi": doi,
            "url": f"https://biorxiv.org/content/{doi}" if doi else "",
            "venue": item.get("category", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": item.get("abstract", ""),
        })
    return out


def _crossref_search(query, limit):
    params = {"query": query, "rows": str(limit), "mailto": "research@localhost"}
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("message", {}).get("items", []):
        authors = []
        for a in item.get("author", [])[:12]:
            name = " ".join(filter(None, [a.get("given"), a.get("family")]))
            if name:
                authors.append(name)
        year = None
        dp = item.get("published", {}).get("date-parts", [[]])
        if dp and dp[0]:
            year = dp[0][0]
        out.append({
            "title": (item.get("title") or [""])[0],
            "year": year,
            "doi": item.get("DOI"),
            "url": item.get("URL", ""),
            "venue": (item.get("container-title") or [""])[0],
            "authors": authors,
            "cited_by": 0,
            "abstract": item.get("abstract", ""),
        })
    return out


def _europepmc_search(query, limit):
    params = {"query": query, "format": "json", "pageSize": str(limit)}
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("resultList", {}).get("result", []):
        out.append({
            "title": r.get("title", ""),
            "year": r.get("pubYear"),
            "doi": r.get("doi"),
            "url": f"https://europepmc.org/article/MED/{r.get('id','')}" if r.get("id") else "",
            "venue": (r.get("journalInfo", {}).get("journal", {}).get("title", "")),
            "authors": [r.get("authorString", "")] if r.get("authorString") else [],
            "cited_by": r.get("citedByCount") or 0,
            "abstract": r.get("abstractText", ""),
        })
    return out


def _pubmed_search(query, limit):
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "pubmed", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        doi = ""
        for aid in s.get("articleids", []):
            if aid.get("idtype") == "doi":
                doi = aid.get("value", "")
                break
        out.append({
            "title": s.get("title", ""),
            "year": s.get("pubdate", "").split(" ")[0] if s.get("pubdate") else None,
            "doi": doi,
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{uid}/",
            "venue": s.get("fulljournalname", ""),
            "authors": [a.get("name", "") for a in s.get("authors", [])[:12]],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _semantic_scholar_search(query, limit):
    params = {"query": query, "limit": str(limit),
              "fields": "title,year,url,citationCount,venue,externalIds"}
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for p in data.get("data", []):
        doi = (p.get("externalIds") or {}).get("DOI", "")
        out.append({
            "title": p.get("title", ""),
            "year": p.get("year"),
            "doi": doi,
            "url": p.get("url", ""),
            "venue": p.get("venue", ""),
            "authors": [],
            "cited_by": p.get("citationCount") or 0,
            "abstract": "",
        })
    return out


def register():
    specs = [
        ("openalex", "OpenAlex", "OpenAlex works catalog", _openalex_search),
        ("arxiv", "arXiv", "arXiv preprints", _arxiv_search),
        ("biorxiv", "bioRxiv", "bioRxiv preprints", _biorxiv_search),
        ("crossref", "Crossref", "Crossref metadata", _crossref_search),
        ("europepmc", "Europe PMC", "Europe PMC literature", _europepmc_search),
        ("pubmed", "PubMed", "PubMed biomedical literature", _pubmed_search),
        ("semantic-scholar", "Semantic Scholar", "Semantic Scholar papers", _semantic_scholar_search),
    ]
    for cid, name, desc, fn in specs:
        _register(Connector(id=cid, name=name, domain="literature",
                           description=desc, search=fn))
