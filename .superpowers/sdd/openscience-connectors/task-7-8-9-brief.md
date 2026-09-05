### Task 7: Chemistry Sources (6 connectors)

**Files:**
- Create: `clawsgo_self/science/sources/chemistry.py`
- Create: `tests/test_science_chemistry.py`

**Interfaces:**
- Produces: `sources.chemistry.register()` registering chembl, pubchem, chebi, bindingdb, gtopdb, surechembl

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_chemistry.py`:

```python
import pytest
from clawsgo_self.science import get_registry
from clawsgo_self.science.sources import chemistry


def test_chemistry_registers_6():
    before = len(get_registry().all())
    chemistry.register()
    after = len(get_registry().all())
    assert after - before == 6


def test_chembl_search_parses(monkeypatch):
    fake = {"molecules": [
        {"molecule_chembl_id": "CHEMBL123", "pref_name": "Aspirin",
         "molecule_structures": {"canonical_smiles": "CC(=O)OC1=CC=CC=C1C(O)=O"}}
    ]}
    monkeypatch.setattr("clawsgo_self.science.sources.chemistry.http_get_json",
                        lambda url, **kw: fake)
    chemistry.register()
    c = get_registry().get("chembl")
    hits = c.search("aspirin", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Aspirin"
    assert hits[0]["id"] == "CHEMBL123"


def test_pubchem_search_parses(monkeypatch):
    fake_cids = {"IdentifierList": {"CID": [2244]}}
    fake_prop = {"PropertyTable": {"Properties": [{"CID": 2244, "Title": "Acetaminophen"}]}}
    call = [0]
    def fake_json(url, **kw):
        call[0] += 1
        if "cids" in url:
            return fake_cids
        return fake_prop
    monkeypatch.setattr("clawsgo_self.science.sources.chemistry.http_get_json", fake_json)
    chemistry.register()
    c = get_registry().get("pubchem")
    hits = c.search("acetaminophen", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Acetaminophen"


def test_chebi_search_parses(monkeypatch):
    fake = {"List": {"item": [{"chebiId": "CHEBI:12345", "chebiAsciiName": "Caffeine"}]}}
    monkeypatch.setattr("clawsgo_self.science.sources.chemistry.http_get_json",
                        lambda url, **kw: fake)
    chemistry.register()
    c = get_registry().get("chebi")
    hits = c.search("caffeine", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Caffeine"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_chemistry.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write chemistry.py**

Create `clawsgo_self/science/sources/chemistry.py`:

```python
from __future__ import annotations

import urllib.parse
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _chembl_search(query, limit):
    params = {"q": query, "format": "json", "limit": str(limit)}
    url = "https://www.ebi.ac.uk/chembl/api/data/molecule/search?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for m in data.get("molecules", []):
        out.append({
            "id": m.get("molecule_chembl_id", ""),
            "title": m.get("pref_name", "") or m.get("molecule_chembl_id", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/chembl/compound_report_card/{m.get('molecule_chembl_id','')}",
            "venue": "ChEMBL",
            "authors": [],
            "cited_by": 0,
            "abstract": (m.get("molecule_structures") or {}).get("canonical_smiles", ""),
        })
    return out


def _pubchem_search(query, limit):
    params = {"name": query, "operation": "cids", "format": "JSON"}
    url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/" + urllib.parse.quote(query) + "/cids/JSON"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    cids = data.get("IdentifierList", {}).get("CID", [])[:limit]
    if not cids:
        return []
    prop_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{','.join(map(str, cids))}/property/Title/JSON"
    prop_data = sci_http.http_get_json(prop_url)
    if not prop_data:
        return []
    out = []
    for p in prop_data.get("PropertyTable", {}).get("Properties", []):
        out.append({
            "id": str(p.get("CID", "")),
            "title": p.get("Title", ""),
            "year": None,
            "doi": None,
            "url": f"https://pubchem.ncbi.nlm.nih.gov/compound/{p.get('CID','')}",
            "venue": "PubChem",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _chebi_search(query, limit):
    params = {"q": query, "maxRows": str(limit)}
    url = "https://www.ebi.ac.uk/chebi/ws/rest/search?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("List", {}).get("item", []):
        out.append({
            "id": item.get("chebiId", ""),
            "title": item.get("chebiAsciiName", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/chebi/searchId.do?chebiId={item.get('chebiId','')}",
            "venue": "ChEBI",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _bindingdb_search(query, limit):
    params = {"q": query, "limit": str(limit)}
    url = "https://www.bindingdb.org/bind/webservices/v1/homologySearch?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("results", []):
        out.append({
            "id": item.get("ligand_id", ""),
            "title": item.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.bindingdb.org/bind/ligand/{item.get('ligand_id','')}",
            "venue": "BindingDB",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _gtopdb_search(query, limit):
    params = {"q": query, "limit": str(limit)}
    url = "https://www.guidetopharmacology.org/services/ligands?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("ligands", []):
        out.append({
            "id": item.get("ligandId", ""),
            "title": item.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.guidetopharmacology.org/GRAC/LigandDisplayForward?ligandId={item.get('ligandId','')}",
            "venue": "GuideToPharmacology",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _surechembl_search(query, limit):
    params = {"q": query, "limit": str(limit)}
    url = "https://www.surechembl.org/api/chemical?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("results", []):
        out.append({
            "id": item.get("surechembl_id", ""),
            "title": item.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.surechembl.org/chemical/{item.get('surechembl_id','')}",
            "venue": "SureChEMBL",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def register():
    specs = [
        ("chembl", "ChEMBL", "Bioactive drug-like compounds", _chembl_search),
        ("pubchem", "PubChem", "Chemical molecules and bioactivities", _pubchem_search),
        ("chebi", "ChEBI", "Chemical entities of biological interest", _chebi_search),
        ("bindingdb", "BindingDB", "Protein-ligand binding affinities", _bindingdb_search),
        ("gtopdb", "GuideToPharmacology", "Drug targets and ligands", _gtopdb_search),
        ("surechembl", "SureChEMBL", "Patent chemistry", _surechembl_search),
    ]
    for cid, name, desc, fn in specs:
        register(Connector(id=cid, name=name, domain="chemistry",
                           description=desc, search=fn))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_science_chemistry.py -v`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add clawsgo_self/science/sources/chemistry.py tests/test_science_chemistry.py
git commit -m "feat(science): add 6 chemistry connectors (chembl/pubchem/chebi/bindingdb/gtopdb/surechembl)"
```

---

﻿### Task 8: Genomics Sources (7 connectors)

**Files:**
- Create: `clawsgo_self/science/sources/genomics.py`
- Create: `tests/test_science_genomics.py`

**Interfaces:**
- Produces: `sources.genomics.register()` registering ensembl, eutils, mygene, myvariant, clinvar, dbsnp, gnomad

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_genomics.py`:

```python
import pytest
from clawsgo_self.science import get_registry
from clawsgo_self.science.sources import genomics


def test_genomics_registers_7():
    before = len(get_registry().all())
    genomics.register()
    after = len(get_registry().all())
    assert after - before == 7


def test_ensembl_search_parses(monkeypatch):
    fake = [{"id": "ENSG00000139618", "display_name": "BRCA2", "species": "homo_sapiens",
             "biotype": "protein_coding"}]
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json",
                        lambda url, **kw: fake)
    genomics.register()
    c = get_registry().get("ensembl")
    hits = c.search("BRCA2", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "BRCA2"
    assert hits[0]["id"] == "ENSG00000139618"


def test_eutils_search_parses(monkeypatch):
    search_fake = {"esearchresult": {"idlist": ["12345"]}}
    summ_fake = {"result": {"12345": {"name": "TP53", "description": "tumor protein"}}}
    def fake_json(url, **kw):
        if "esearch" in url:
            return search_fake
        return summ_fake
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json", fake_json)
    genomics.register()
    c = get_registry().get("eutils")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "TP53"


def test_mygene_search_parses(monkeypatch):
    fake = {"hits": [{"_id": "7157", "symbol": "TP53", "name": "tumor protein p53",
                      "taxid": 9606, "entrezgene": "7157"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json",
                        lambda url, **kw: fake)
    genomics.register()
    c = get_registry().get("mygene")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "tumor protein p53"


def test_myvariant_search_parses(monkeypatch):
    fake = {"hits": [{"_id": "chr17:7577121:G:A", "dbsnp": {"rsid": "rs12345"}}]}
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json",
                        lambda url, **kw: fake)
    genomics.register()
    c = get_registry().get("myvariant")
    hits = c.search("BRCA1", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "chr17:7577121:G:A"


def test_clinvar_search_parses(monkeypatch):
    search_fake = {"esearchresult": {"idlist": ["1234"]}}
    summ_fake = {"result": {"1234": {"title": "Pathogenic variant",
                                     "clinical_significance": {"description": "Pathogenic"}}}}
    def fake_json(url, **kw):
        if "esearch" in url:
            return search_fake
        return summ_fake
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json", fake_json)
    genomics.register()
    c = get_registry().get("clinvar")
    hits = c.search("BRCA1", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Pathogenic variant"


def test_dbsnp_search_parses(monkeypatch):
    search_fake = {"esearchresult": {"idlist": ["12345"]}}
    summ_fake = {"result": {"12345": {"title": "rs12345"}}}
    def fake_json(url, **kw):
        if "esearch" in url:
            return search_fake
        return summ_fake
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json", fake_json)
    genomics.register()
    c = get_registry().get("dbsnp")
    hits = c.search("rs12345", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "rs12345"


def test_gnomad_search_parses(monkeypatch):
    fake = {"data": {"variant": {"variantId": "1-55516888-G-A", "consequence": "missense"}}}
    monkeypatch.setattr("clawsgo_self.science.sources.genomics.http_get_json",
                        lambda url, **kw: fake)
    genomics.register()
    c = get_registry().get("gnomad")
    hits = c.search("1-55516888-G-A", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "1-55516888-G-A"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_genomics.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write genomics.py**

Create `clawsgo_self/science/sources/genomics.py`:

```python
from __future__ import annotations

import urllib.parse
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _ensembl_search(query, limit):
    url = f"https://rest.ensembl.org/xrefs/symbol/homo_sapiens/{urllib.parse.quote(query)}?content-type=application/json"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data[:limit]:
        out.append({
            "id": r.get("id", ""),
            "title": r.get("display_name", "") or r.get("id", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ensembl.org/Homo_sapiens/Gene/Summary?g={r.get('id','')}",
            "venue": r.get("species", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": r.get("biotype", ""),
        })
    return out


def _eutils_search(query, limit):
    params = {"db": "gene", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = sci_http.http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "gene", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = sci_http.http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        out.append({
            "id": uid,
            "title": s.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ncbi.nlm.nih.gov/gene/{uid}",
            "venue": s.get("description", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": s.get("summary", ""),
        })
    return out


def _mygene_search(query, limit):
    params = {"q": query, "size": str(limit), "species": "human"}
    url = "https://mygene.info/v3/query?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for h in data.get("hits", []):
        out.append({
            "id": h.get("_id", ""),
            "title": h.get("name", "") or h.get("symbol", ""),
            "year": None,
            "doi": None,
            "url": f"https://mygene.info/v3/gene/{h.get('_id','')}",
            "venue": str(h.get("taxid", "")),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _myvariant_search(query, limit):
    params = {"q": query, "size": str(limit)}
    url = "https://myvariant.info/v1/query?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for h in data.get("hits", []):
        out.append({
            "id": h.get("_id", ""),
            "title": h.get("_id", ""),
            "year": None,
            "doi": None,
            "url": f"https://myvariant.info/v1/variant/{h.get('_id','')}",
            "venue": "MyVariant",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _clinvar_search(query, limit):
    params = {"db": "clinvar", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = sci_http.http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "clinvar", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = sci_http.http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        out.append({
            "id": uid,
            "title": s.get("title", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ncbi.nlm.nih.gov/clinvar/variation/{uid}",
            "venue": (s.get("clinical_significance") or {}).get("description", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _dbsnp_search(query, limit):
    params = {"db": "snp", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = sci_http.http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "snp", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = sci_http.http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        out.append({
            "id": uid,
            "title": s.get("title", "") or uid,
            "year": None,
            "doi": None,
            "url": f"https://www.ncbi.nlm.nih.gov/snp/rs{uid}",
            "venue": "dbSNP",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _gnomad_search(query, limit):
    params = {"variant": query}
    url = "https://gnomad.broadinstitute.org/api/v2/variant?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    variant = data.get("data", {}).get("variant", {})
    if variant:
        out.append({
            "id": variant.get("variantId", ""),
            "title": variant.get("variantId", ""),
            "year": None,
            "doi": None,
            "url": f"https://gnomad.broadinstitute.org/variant/{variant.get('variantId','')}",
            "venue": "gnomAD",
            "authors": [],
            "cited_by": 0,
            "abstract": variant.get("consequence", ""),
        })
    return out


def register():
    specs = [
        ("ensembl", "Ensembl", "Ensembl genome browser", _ensembl_search),
        ("eutils", "NCBI eutils", "NCBI Entrez utilities", _eutils_search),
        ("mygene", "MyGene.info", "Gene annotation service", _mygene_search),
        ("myvariant", "MyVariant.info", "Variant annotation service", _myvariant_search),
        ("clinvar", "ClinVar", "Clinical variant interpretations", _clinvar_search),
        ("dbsnp", "dbSNP", "Short genetic variations", _dbsnp_search),
        ("gnomad", "gnomAD", "Genome aggregation database", _gnomad_search),
    ]
    for cid, name, desc, fn in specs:
        register(Connector(id=cid, name=name, domain="genomics",
                           description=desc, search=fn))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_science_genomics.py -v`
Expected: 8 passed

- [ ] **Step 5: Commit**

```bash
git add clawsgo_self/science/sources/genomics.py tests/test_science_genomics.py
git commit -m "feat(science): add 7 genomics connectors (ensembl/eutils/mygene/myvariant/clinvar/dbsnp/gnomad)"
```

---
﻿### Task 9: Pathways & Omics Sources (11 connectors)

**Files:**
- Create: `clawsgo_self/science/sources/pathways.py`
- Create: `clawsgo_self/science/sources/omics.py`
- Create: `tests/test_science_pathways_omics.py`

**Interfaces:**
- Produces: `sources.pathways.register()` registering biogrid, intact, kegg, opentargets, reactome
- Produces: `sources.omics.register()` registering arrayexpress, depmap, expression-atlas, geo, gtex, hpa

- [ ] **Step 1: Write the failing test**

Create `tests/test_science_pathways_omics.py`:

```python
import pytest
from clawsgo_self.science import get_registry
from clawsgo_self.science.sources import pathways, omics


def test_pathways_registers_5():
    before = len(get_registry().all())
    pathways.register()
    after = len(get_registry().all())
    assert after - before == 5


def test_omics_registers_6():
    before = len(get_registry().all())
    omics.register()
    after = len(get_registry().all())
    assert after - before == 6


def test_biogrid_search_parses(monkeypatch):
    fake = {"12345": [{"interactor_a": "P12345", "interactor_b": "P67890"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("biogrid")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "P67890"


def test_intact_search_parses(monkeypatch):
    fake = {"data": [{"id": "EBI-12345", "label": "BRCA1-BRCA2"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("intact")
    hits = c.search("BRCA1", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "EBI-12345"


def test_kegg_search_parses(monkeypatch):
    fake = [["hsa:7157\tTP53 tumor protein p53"]]
    monkeypatch.setattr("clawsgo_self.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("kegg")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert "TP53" in hits[0]["title"]


def test_opentargets_search_parses(monkeypatch):
    fake = {"data": [{"id": "ENSG00000141510", "name": "TP53", "symbol": "TP53"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("opentargets")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "TP53"


def test_reactome_search_parses(monkeypatch):
    fake = {"results": [{"dbId": 12345, "displayName": "DNA Repair"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("reactome")
    hits = c.search("DNA repair", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "DNA Repair"


def test_arrayexpress_search_parses(monkeypatch):
    fake = {"hits": [{"accession": "E-MTAB-1234", "title": "RNA-seq of cancer"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("arrayexpress")
    hits = c.search("cancer", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "RNA-seq of cancer"


def test_depmap_search_parses(monkeypatch):
    fake = {"data": [{"DepMap_ID": "ACH-000001", "cell_line_name": "A549"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("depmap")
    hits = c.search("A549", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "ACH-000001"


def test_expression_atlas_search_parses(monkeypatch):
    fake = {"results": [{"experimentAccession": "E-GEOD-12345", "description": "gene expr"}]}
    monkeypatch.setattr("clawsgo_self.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("expression-atlas")
    hits = c.search("cancer", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "E-GEOD-12345"


def test_geo_search_parses(monkeypatch):
    search_fake = {"esearchresult": {"idlist": ["12345"]}}
    summ_fake = {"result": {"12345": {"title": "Breast cancer GEO series"}}}
    def fake_json(url, **kw):
        if "esearch" in url:
            return search_fake
        return summ_fake
    monkeypatch.setattr("clawsgo_self.science.sources.omics.http_get_json", fake_json)
    omics.register()
    c = get_registry().get("geo")
    hits = c.search("breast cancer", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Breast cancer GEO series"


def test_gtex_search_parses(monkeypatch):
    fake = {"geneSymbol": "TP53", "tissueSiteDetailId": "Lung", "tpkm": 12.5}
    monkeypatch.setattr("clawsgo_self.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("gtex")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "TP53 - Lung"


def test_hpa_search_parses(monkeypatch):
    fake = [{"gene": "TP53", "tissue": "Lung", "celltype": "alveolar"}]
    monkeypatch.setattr("clawsgo_self.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("hpa")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "TP53"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_science_pathways_omics.py -v`
Expected: FAIL -- ModuleNotFoundError

- [ ] **Step 3: Write pathways.py**

Create `clawsgo_self/science/sources/pathways.py`:

```python
from __future__ import annotations

import urllib.parse
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _biogrid_search(query, limit):
    params = {"searchNames": "true", "geneList": query, "interSpeciesExcluded": "true"}
    url = "https://webservice.thebiogrid.org/interactions?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    seen = set()
    for int_id, interactions in data.items():
        for ia in interactions:
            ident = ia.get("interactor_b", "")
            if ident and ident not in seen:
                seen.add(ident)
                out.append({
                    "id": ident,
                    "title": f"interactor {ident}",
                    "year": None,
                    "doi": None,
                    "url": f"https://thebiogrid.org/{ident}",
                    "venue": "BioGRID",
                    "authors": [],
                    "cited_by": 0,
                    "abstract": "",
                })
                if len(out) >= limit:
                    break
        if len(out) >= limit:
            break
    return out


def _intact_search(query, limit):
    url = f"https://www.ebi.ac.uk/intact/ws/search/interaction/{urllib.parse.quote(query)}?format=json"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("data", [])[:limit]:
        out.append({
            "id": r.get("id", ""),
            "title": r.get("label", "") or r.get("id", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/intact/details/{r.get('id','')}",
            "venue": "IntAct",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _kegg_search(query, limit):
    url = f"https://rest.kegg.jp/find/genes/{urllib.parse.quote(query)}"
    text = sci_http.http_get_text(url)
    if not text:
        return []
    out = []
    for line in text.split("\n")[:limit]:
        parts = line.split("\t")
        if len(parts) >= 2:
            out.append({
                "id": parts[0],
                "title": parts[1],
                "year": None,
                "doi": None,
                "url": f"https://www.genome.jp/dbget-bin/www_bget?{parts[0]}",
                "venue": "KEGG",
                "authors": [],
                "cited_by": 0,
                "abstract": "",
            })
    return out


def _opentargets_search(query, limit):
    params = {"q": query, "size": str(limit)}
    url = "https://api.platform.opentargets.org/v3/graphql?" + urllib.parse.urlencode(params)
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for d in data.get("data", [])[:limit]:
        out.append({
            "id": d.get("id", ""),
            "title": d.get("name", "") or d.get("symbol", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.opentargets.org/target/{d.get('id','')}",
            "venue": d.get("symbol", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _reactome_search(query, limit):
    url = f"https://reactome.org/ContentService/data/search/{urllib.parse.quote(query)}?types=Pathway&cluster=true&species=Homo%20sapiens"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", [])[:limit]:
        out.append({
            "id": str(r.get("dbId", "")),
            "title": r.get("displayName", ""),
            "year": None,
            "doi": None,
            "url": f"https://reactome.org/content/detail/{r.get('dbId','')}",
            "venue": "Reactome",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def register():
    specs = [
        ("biogrid", "BioGRID", "Protein-protein interactions", _biogrid_search),
        ("intact", "IntAct", "Molecular interactions", _intact_search),
        ("kegg", "KEGG", "Kyoto Encyclopedia of Genes and Genomes", _kegg_search),
        ("opentargets", "Open Targets", "Target-disease associations", _opentargets_search),
        ("reactome", "Reactome", "Pathway database", _reactome_search),
    ]
    for cid, name, desc, fn in specs:
        register(Connector(id=cid, name=name, domain="pathways",
                           description=desc, search=fn))
```

- [ ] **Step 4: Write omics.py**

Create `clawsgo_self/science/sources/omics.py`:

```python
from __future__ import annotations

import urllib.parse
from clawsgo_self.science import register
from clawsgo_self.science.connector import Connector
from clawsgo_self.science import http as sci_http


def _arrayexpress_search(query, limit):
    url = f"https://www.ebi.ac.uk/biostudies/api/v1/search?query={urllib.parse.quote(query)}&pageSize={limit}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for h in data.get("hits", [])[:limit]:
        out.append({
            "id": h.get("accession", ""),
            "title": h.get("title", "") or h.get("accession", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/biostudies/studies/{h.get('accession','')}",
            "venue": "ArrayExpress",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _depmap_search(query, limit):
    url = f"https://depmap.org/portal/api/cell_lines?search={urllib.parse.quote(query)}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for cl in data.get("data", [])[:limit]:
        out.append({
            "id": cl.get("DepMap_ID", ""),
            "title": cl.get("cell_line_name", "") or cl.get("DepMap_ID", ""),
            "year": None,
            "doi": None,
            "url": f"https://depmap.org/portal/cell_line/{cl.get('DepMap_ID','')}",
            "venue": "DepMap",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _expression_atlas_search(query, limit):
    url = f"https://www.ebi.ac.uk/gxa/api/v2/search?query={urllib.parse.quote(query)}&limit={limit}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", [])[:limit]:
        out.append({
            "id": r.get("experimentAccession", ""),
            "title": r.get("description", "") or r.get("experimentAccession", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/gxa/experiments/{r.get('experimentAccession','')}",
            "venue": "Expression Atlas",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _geo_search(query, limit):
    params = {"db": "gds", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = sci_http.http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "gds", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = sci_http.http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        out.append({
            "id": uid,
            "title": s.get("title", "") or uid,
            "year": None,
            "doi": None,
            "url": f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={uid}",
            "venue": "GEO",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _gtex_search(query, limit):
    url = f"https://gtexportal.org/api/v2/gene/{urllib.parse.quote(query)}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for d in data.get("data", [])[:limit]:
        tissue = d.get("tissueSiteDetailId", "")
        out.append({
            "id": f"{d.get('geneSymbol','')}-{tissue}",
            "title": f"{d.get('geneSymbol','')} - {tissue}",
            "year": None,
            "doi": None,
            "url": f"https://gtexportal.org/home/gene/{d.get('geneSymbol','')}",
            "venue": "GTEx",
            "authors": [],
            "cited_by": 0,
            "abstract": f"TPM: {d.get('medianTPM', '')}",
        })
    return out


def _hpa_search(query, limit):
    url = f"https://www.proteinatlas.org/api/search_download.php?search={urllib.parse.quote(query)}&format=json&limit={limit}"
    data = sci_http.http_get_json(url)
    if not data:
        return []
    out = []
    for d in data.get("data", [])[:limit]:
        out.append({
            "id": d.get("gene", ""),
            "title": d.get("gene", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.proteinatlas.org/{d.get('gene','')}",
            "venue": "Human Protein Atlas",
            "authors": [],
            "cited_by": 0,
            "abstract": f"tissue: {d.get('tissue','')}",
        })
    return out


def register():
    specs = [
        ("arrayexpress", "ArrayExpress", "Functional genomics experiments", _arrayexpress_search),
        ("depmap", "DepMap", "Cancer dependency map", _depmap_search),
        ("expression-atlas", "Expression Atlas", "Gene expression patterns", _expression_atlas_search),
        ("geo", "GEO", "Gene Expression Omnibus", _geo_search),
        ("gtex", "GTEx", "Genotype-Tissue Expression", _gtex_search),
        ("hpa", "Human Protein Atlas", "Tissue protein expression", _hpa_search),
    ]
    for cid, name, desc, fn in specs:
        register(Connector(id=cid, name=name, domain="omics",
                           description=desc, search=fn))
```

- [ ] **Step 5: Run test to verify it passes**

Run: `pytest tests/test_science_pathways_omics.py -v`
Expected: 12 passed

- [ ] **Step 6: Commit**

```bash
git add clawsgo_self/science/sources/pathways.py clawsgo_self/science/sources/omics.py tests/test_science_pathways_omics.py
git commit -m "feat(science): add 11 pathways/omics connectors (biogrid/intact/kegg/opentargets/reactome/arrayexpress/depmap/expression-atlas/geo/gtex/hpa)"
```

---
﻿### Task 10: Documentation and regression

**Files:**
- Modify: `README.md`
- Modify: `USAGE.md`

**Interfaces:**
- Consumes: all science modules (verification only)

- [ ] **Step 1: Update README.md**

Update `README.md` to reflect the new science layer:

1. In the feature table, add a new row for the science data layer:
   ```
   | 科学数据查询 | science_list_dbs / science_search / science_fetch / science_cross_lookup | 41 免 key 连接器（literature/proteins/chemistry/genomics/pathways/omics/datasets） |
   ```

2. Update the tool count from 20 to 24.

3. Add a new section `## 科学数据查询（science）` describing the connector framework:
   ```markdown
   ## 科学数据查询（science）

   移植自 [synthetic-sciences/openscience](https://github.com/synthetic-sciences/openscience) 的科学数据库连接器层，提供 41 个免 key 科学数据源的统一检索接口。

   ### 数据域
   - **literature**: openalex, arxiv, biorxiv, crossref, europepmc, pubmed, semantic-scholar
   - **proteins**: uniprot, rcsb-pdb, pdbe, alphafold, interpro, sifts
   - **chemistry**: chembl, pubchem, chebi, bindingdb, gtopdb, surechembl
   - **genomics**: ensembl, eutils, mygene, myvariant, clinvar, dbsnp, gnomad
   - **pathways**: biogrid, intact, kegg, opentargets, reactome
   - **omics**: arrayexpress, depmap, expression-atlas, geo, gtex, hpa
   - **datasets**: zenodo, doaj, openaire, huggingface

   ### 工具
   | 工具 | 说明 |
   | --- | --- |
   | `science_list_dbs(domain?)` | 列出可用数据库 |
   | `science_search(database, query, limit)` | 单库检索 |
   | `science_fetch(database, id, format)` | 按 id 拉取记录 |
   | `science_cross_lookup(query, databases?, limit)` | 多库联合检索 |
   ```

4. Update the architecture tree to include `science/` package.

- [ ] **Step 2: Update USAGE.md**

Add a new section `## 科学数据查询` with usage examples:

```markdown
## 科学数据查询

### 列出数据库
```
science_list_dbs("literature")  # 列出文献类数据库
science_list_dbs()              # 列出全部数据库
```

### 单库检索
```
science_search("openalex", "quantum computing", limit=10)
science_search("uniprot", "kinase", limit=5)
```

### 多库联合检索
```
science_cross_lookup("BRCA1", databases=["uniprot", "mygene", "clinvar"], limit=5)
```

### 拉取原文
```
science_fetch("uniprot", "P12345", format="fasta")  # 拉取 FASTA 序列
science_fetch("rcsb-pdb", "1ABC", format="pdb")     # 拉取 PDB 结构
```
```

- [ ] **Step 3: Run full regression**

Run: `CLAWSGO_SELF_OFFLINE=1 pytest tests/ -q`
Expected: all tests pass (61 existing + new science tests)

- [ ] **Step 4: Commit**

```bash
git add README.md USAGE.md
git commit -m "feat(docs): update README and USAGE for science data layer (24 tools, 41 connectors)"
```

---


---

