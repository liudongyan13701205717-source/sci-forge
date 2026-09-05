### Task 3: Literature Sources (7 connectors)

**Files:**
- Create: `clawsgo_self/science/sources/__init__.py`
- Create: `clawsgo_self/science/sources/literature.py`
- Create: `tests/test_science_literature.py`

**Interfaces:**
- Produces: `sources.literature.register()` registering openalex, arxiv, biorxiv, crossref, europepmc, pubmed, semantic-scholar

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_literature.py`:

```python
import pytest
from clawsgo_self.science import register, get_registry
from clawsgo_self.science.connector import Connector
from clawsgo_self.science.sources import literature


def test_literature_registers_7():
    before = len(get_registry().all())
    literature.register()
    after = len(get_registry().all())
    assert after - before == 7


def test_openalex_search_offline(monkeypatch):
    monkeypatch.setenv("CLAWSGO_SELF_OFFLINE", "1")
    literature.register()
    c = get_registry().get("openalex")
    assert c is not None
    hits = c.search("cancer", 5)
    assert hits == []


def test_openalex_search_parses(monkeypatch):
    fake = {"results": [
        {"title": "Deep Learning for Cells", "publication_year": 2023,
         "doi": "10.1234/x", "id": "https://openalex.org/W1",
         "primary_location": {"display_name": "Nature"},
         "authorships": [{"author": {"display_name": "Smith"}}],
         "cited_by_count": 42, "abstract_inverted_index": None}
    ]}
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_json",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("openalex")
    hits = c.search("cells", 5)
    assert len(hits) == 1
    h = hits[0]
    assert h["title"] == "Deep Learning for Cells"
    assert h["year"] == 2023
    assert h["doi"] == "10.1234/x"
    assert h["cited_by"] == 42
    assert h["venue"] == "Nature"
    assert "Smith" in h["authors"]


def test_arxiv_search_parses(monkeypatch):
    fake = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <title>Quantum ML</title>
    <id>http://arxiv.org/abs/2301.00001</id>
    <link rel="alternate" href="http://arxiv.org/abs/2301.00001"/>
  </entry>
</feed>"""
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_text",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("arxiv")
    hits = c.search("quantum", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Quantum ML"


def test_biorxiv_search_parses(monkeypatch):
    fake = {"collection": [
        {"title": "COVID Study", "doi": "10.1101/2023.01.01",
         "abstract": "virus research", "category": "microbiology"}
    ]}
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_json",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("biorxiv")
    hits = c.search("covid", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "COVID Study"


def test_crossref_search_parses(monkeypatch):
    fake = {"message": {"items": [
        {"title": ["Protein Folding"], "DOI": "10.1000/abc",
         "published": {"date-parts": [[2022]]},
         "container-title": ["Science"],
         "author": [{"given": "Jane", "family": "Doe"}]}
    ]}}
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_json",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("crossref")
    hits = c.search("protein", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Protein Folding"
    assert hits[0]["year"] == 2022
    assert "Jane Doe" in hits[0]["authors"]


def test_europepmc_search_parses(monkeypatch):
    fake = {"resultList": {"result": [
        {"title": "Gene Therapy", "id": "12345", "doi": "10.123/xyz",
         "pubYear": "2021", "journalInfo": {"journal": {"title": "Cell"}},
         "authorString": "Lee K", "citedByCount": 10}
    ]}}
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_json",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("europepmc")
    hits = c.search("gene", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Gene Therapy"
    assert hits[0]["cited_by"] == 10


def test_pubmed_search_parses(monkeypatch):
    search_fake = {"esearchresult": {"idlist": ["999888"]}}
    summ_fake = {"result": {"999888": {"title": "Brain Mapping",
                                       "pubdate": "2020 Jan",
                                       "fulljournalname": "Nature Neuro",
                                       "authors": [{"name": "Wu S"}]}}}
    call_count = [0]
    def fake_json(url, **kw):
        call_count[0] += 1
        if "esearch" in url:
            return search_fake
        return summ_fake
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_json",
                        fake_json)
    literature.register()
    c = get_registry().get("pubmed")
    hits = c.search("brain", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Brain Mapping"
    assert hits[0]["venue"] == "Nature Neuro"


def test_semantic_scholar_search_parses(monkeypatch):
    fake = {"data": [
        {"title": "Attention Nets", "year": 2019, "url": "http://s2/1",
         "venue": "NeurIPS", "citationCount": 500,
         "externalIds": {"DOI": "10.1234/attn"}}
    ]}
    monkeypatch.setattr("clawsgo_self.science.sources.literature.http_get_json",
                        lambda url, **kw: fake)
    literature.register()
    c = get_registry().get("semantic-scholar")
    hits = c.search("attention", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Attention Nets"
    assert hits[0]["cited_by"] == 500
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_literature.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write sources/__init__.py**

Create `clawsgo_self/science/sources/__init__.py`:

```python
```

- [ ] **Step 4: Write literature.py**

Create `clawsgo_self/science/sources/literature.py`:

```python
from __future__ import annotations

import urllib.parse
import xml.etree.ElementTree as ET
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _truncate(inv_index) -> str:
    if not inv_index:
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
    data = sci_http.http_get_json(url)
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
    body = sci_http.http_get_text(url)
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
    data = sci_http.http_get_json(url + "?q=" + urllib.parse.quote(query))
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
    data = sci_http.http_get_json(url)
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
    data = sci_http.http_get_json(url)
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
    search_data = sci_http.http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "pubmed", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = sci_http.http_get_json(summ_url)
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
    data = sci_http.http_get_json(url)
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
        register(Connector(id=cid, name=name, domain="literature",
                           description=desc, search=fn))
```

- [ ] **Step 5: Run test to verify it passes**

Run: `pytest tests/test_science_literature.py -v`
Expected: 9 passed

- [ ] **Step 6: Commit**

```bash
git add clawsgo_self/science/sources/__init__.py clawsgo_self/science/sources/literature.py tests/test_science_literature.py
git commit -m "feat(science): add 7 literature connectors (openalex/arxiv/biorxiv/crossref/europepmc/pubmed/semantic-scholar)"
```

---
