### Task 4: Dataset / Open-Access Sources (4 extra connectors)

**Files:**
- Create: `clawsgo_self/science/sources/datasets.py`
- Create: `tests/test_science_datasets.py`

**Interfaces:**
- Produces: `sources.datasets.register()` registering zenodo, doaj, openaire, huggingface

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_datasets.py`:

```python
import pytest
from clawsgo_self.science import get_registry
from clawsgo_self.science.sources import datasets


def test_datasets_registers_4():
    before = len(get_registry().all())
    datasets.register()
    after = len(get_registry().all())
    assert after - before == 4


def test_zenodo_search_parses(monkeypatch):
    fake = {"hits": {"hits": [
        {"id": 12345, "metadata": {"title": "My Dataset", "description": "desc",
                                    "creators": [{"name": "Lee"}]}}
    ]}}
    monkeypatch.setattr("clawsgo_self.science.sources.datasets.http_get_json",
                        lambda url, **kw: fake)
    datasets.register()
    c = get_registry().get("zenodo")
    hits = c.search("climate", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "My Dataset"
    assert hits[0]["url"] == "https://zenodo.org/record/12345"


def test_doaj_search_parses(monkeypatch):
    fake = {"results": [
        {"bibjson": {"title": "Open Paper", "year": "2022",
                     "journal": {"title": "PLOS ONE"},
                     "author": [{"name": "Kim"}], "abstract": "open science"}}
    ]}
    monkeypatch.setattr("clawsgo_self.science.sources.datasets.http_get_json",
                        lambda url, **kw: fake)
    datasets.register()
    c = get_registry().get("doaj")
    hits = c.search("open", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Open Paper"
    assert "Kim" in hits[0]["authors"]


def test_openaire_search_parses(monkeypatch):
    fake = {"response": {"results": {"result": [
        {"metadata": {"oaf:entity": {"oaf:result":
            {"title": {"$": "EU Project"}}}}
    ]}}}
    monkeypatch.setattr("clawsgo_self.science.sources.datasets.http_get_json",
                        lambda url, **kw: fake)
    datasets.register()
    c = get_registry().get("openaire")
    hits = c.search("energy", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "EU Project"


def test_huggingface_search_parses(monkeypatch):
    fake = [
        {"id": "squad", "title": "SQuAD", "description": "QA dataset",
         "author": "stanford", "downloads": 100000, "likes": 500}
    ]
    monkeypatch.setattr("clawsgo_self.science.sources.datasets.http_get_json",
                        lambda url, **kw: fake)
    datasets.register()
    c = get_registry().get("huggingface")
    hits = c.search("qa", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "SQuAD"
    assert hits[0]["url"] == "https://huggingface.co/datasets/squad"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_datasets.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write datasets.py**

Create `clawsgo_self/science/sources/datasets.py`:

```python
from __future__ import annotations

import urllib.parse
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _zenodo_search(query, limit):
    params = {"q": query, "size": str(limit), "type": "dataset"}
    url = "https://zenodo.org/api/records?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
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
    data = sci_http.http_get_json(url)
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
    data = sci_http.http_get_json(url)
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
    data = sci_http.http_get_json(url)
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
        register(Connector(id=cid, name=name, domain="datasets",
                           description=desc, search=fn))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_science_datasets.py -v`
Expected: 5 passed

- [ ] **Step 5: Commit**

```bash
git add clawsgo_self/science/sources/datasets.py tests/test_science_datasets.py
git commit -m "feat(science): add 4 dataset/open-access connectors (zenodo/doaj/openaire/huggingface)"
```

---
