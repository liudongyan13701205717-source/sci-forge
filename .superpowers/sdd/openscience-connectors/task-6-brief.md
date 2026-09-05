### Task 6: Protein Sources (6 connectors)

**Files:**
- Create: `clawsgo_self/science/sources/proteins.py`
- Create: `tests/test_science_proteins.py`

**Interfaces:**
- Produces: `sources.proteins.register()` registering uniprot, rcsb-pdb, pdbe, alphafold, interpro, sifts

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_proteins.py`:

```python
import pytest
from clawsgo_self.science import get_registry
from clawsgo_self.science.sources import proteins


def test_proteins_registers_6():
    before = len(get_registry().all())
    proteins.register()
    after = len(get_registry().all())
    assert after - before == 6


def test_uniprot_search_parses(monkeypatch):
    fake = {"results": [
        {"primaryAccession": "P12345",
         "proteinDescription": {"recommendedName": {"fullName": {"value": "Kinase X"}}},
         "organism": {"scientificName": "Homo sapiens"}}
    ]}
    monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("uniprot")
    hits = c.search("kinase", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Kinase X"
    assert hits[0]["url"] == "https://www.uniprot.org/uniprotkb/P12345"


def test_uniprot_fetch_fasta(monkeypatch):
    fake = ">sp|P12345|KINH_HUMAN\nMKWVTFISLL"
    monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_text",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("uniprot")
    data = c.fetch("P12345", "fasta")
    assert data["format"] == "fasta"
    assert "MKWVTFISLL" in data["data"]


def test_rcsb_pdb_search_parses(monkeypatch):
    fake = {"result_set": [{"identifier": "1ABC", "score": 1.0}]}
    monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("rcsb-pdb")
    hits = c.search("hemoglobin", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "1ABC"


def test_alphafold_search_parses(monkeypatch):
    fake = [{"entryId": "AF-P12345-F1",
             "uniprotDescription": "Protein structure",
             "organismScientificName": "Human",
             "pdbUrl": "http://pdb/1abc"}]
    monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("alphafold")
    hits = c.search("P12345", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Protein structure"


def test_interpro_search_parses(monkeypatch):
    fake = {"results": [
        {"metadata": {"accession": "IPR000001", "name": "Kinase dom",
                       "source_database": "Pfam", "protein_count": 500}}
    ]}
    monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("interpro")
    hits = c.search("kinase", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Kinase dom"


def test_pdbe_search_parses(monkeypatch):
    fake = {"1abc": {"title": "Heme binding protein"}}
    monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("pdbe")
    hits = c.search("heme", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Heme binding protein"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_proteins.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write proteins.py**

Create `clawsgo_self/science/sources/proteins.py`:

```python
from __future__ import annotations

import urllib.parse
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _uniprot_search(query, limit):
    params = {"query": query, "format": "json", "size": str(limit)}
    url = "https://rest.uniprot.org/uniprotkb/search?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", []):
        acc = r.get("primaryAccession", "")
        desc = r.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {})
        title = desc.get("value", acc) if isinstance(desc, dict) else acc
        out.append({
            "id": acc,
            "title": title,
            "year": None,
            "doi": None,
            "url": f"https://www.uniprot.org/uniprotkb/{acc}" if acc else "",
            "venue": r.get("organism", {}).get("scientificName", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _uniprot_fetch(id, format):
    if format == "fasta":
        url = f"https://rest.uniprot.org/uniprotkb/{id}.fasta"
        text = sci_http.http_get_text(url)
        return {"format": "fasta", "data": text or ""}
    url = f"https://rest.uniprot.org/uniprotkb/{id}.json"
    data = sci_http.http_get_json(url)
    return {"format": "json", "data": data}


def _rcsb_pdb_search(query, limit):
    q = urllib.parse.quote(query)
    url = f"https://search.rcsb.org/rcsbsearch/v2/query?json=%7B%22query%22%3A%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22full_text%22%2C%22parameters%22%3A%7B%22value%22%3A%22{q}%22%7D%7D%2C%22return_type%22%3A%22entry%22%7D"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("result_set", []):
        ident = r.get("identifier", "")
        out.append({
            "id": ident,
            "title": f"PDB {ident}",
            "year": None,
            "doi": None,
            "url": f"https://www.rcsb.org/structure/{ident}" if ident else "",
            "venue": "RCSB PDB",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _pdbe_search(query, limit):
    url = f"https://www.ebi.ac.uk/pdbe/api/search/pdb/entry_details/{urllib.parse.quote(query)}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for pdb_id, info in data.items():
        title = info.get("title", "") if isinstance(info, dict) else ""
        out.append({
            "id": pdb_id,
            "title": title or f"PDB {pdb_id}",
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/pdbe/entry-files/download/pdb{pdb_id}.ent",
            "venue": "PDBe",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _alphafold_search(query, limit):
    url = f"https://alphafold.ebi.ac.uk/api/prediction/{urllib.parse.quote(query)}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for entry in data:
        out.append({
            "id": entry.get("entryId", ""),
            "title": entry.get("uniprotDescription", ""),
            "year": None,
            "doi": None,
            "url": entry.get("pdbUrl", ""),
            "venue": entry.get("organismScientificName", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _interpro_search(query, limit):
    params = {"search": query, "page_size": str(limit)}
    url = "https://www.ebi.ac.uk/interpro/api/search/all/?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", []):
        meta = r.get("metadata", {})
        out.append({
            "id": meta.get("accession", ""),
            "title": meta.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/interpro/entry/{meta.get('accession','')}",
            "venue": meta.get("source_database", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _sifts_search(query, limit):
    url = f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{urllib.parse.quote(query)}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for pdb_id in data:
        out.append({
            "id": pdb_id,
            "title": f"SIFTS mapping {pdb_id}",
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{pdb_id}",
            "venue": "PDBe SIFTS",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def register():
    specs = [
        ("uniprot", "UniProt", "UniProt protein knowledgebase", _uniprot_search),
        ("rcsb-pdb", "RCSB PDB", "Protein Data Bank", _rcsb_pdb_search),
        ("pdbe", "PDBe", "Protein Data Bank in Europe", _pdbe_search),
        ("alphafold", "AlphaFold DB", "AlphaFold protein structures", _alphafold_search),
        ("interpro", "InterPro", "Protein families and domains", _interpro_search),
        ("sifts", "PDBe SIFTS", "Structure integration with function", _sifts_search),
    ]
    for cid, name, desc, fn in specs:
        c = Connector(id=cid, name=name, domain="proteins", description=desc, search=fn)
        if cid == "uniprot":
            c.fetch = _uniprot_fetch
        register(c)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_science_proteins.py -v`
Expected: 7 passed

- [ ] **Step 5: Commit**

```bash
git add clawsgo_self/science/sources/proteins.py tests/test_science_proteins.py
git commit -m "feat(science): add 6 protein connectors (uniprot/rcsb-pdb/pdbe/alphafold/interpro/sifts)"
```

---
