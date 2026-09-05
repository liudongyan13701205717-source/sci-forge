import pytest
from sciforge.science import get_registry
from sciforge.science.sources import genomics


def test_genomics_registers_7():
    before = len(get_registry().all())
    genomics.register()
    after = len(get_registry().all())
    assert after - before == 7


def test_ensembl_search_parses(monkeypatch):
    fake = [{"id": "ENSG00000139618", "display_name": "BRCA2", "species": "homo_sapiens",
             "biotype": "protein_coding"}]
    monkeypatch.setattr("sciforge.science.sources.genomics.http_get_json",
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
    monkeypatch.setattr("sciforge.science.sources.genomics.http_get_json", fake_json)
    genomics.register()
    c = get_registry().get("eutils")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "TP53"


def test_mygene_search_parses(monkeypatch):
    fake = {"hits": [{"_id": "7157", "symbol": "TP53", "name": "tumor protein p53",
                      "taxid": 9606, "entrezgene": "7157"}]}
    monkeypatch.setattr("sciforge.science.sources.genomics.http_get_json",
                        lambda url, **kw: fake)
    genomics.register()
    c = get_registry().get("mygene")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "tumor protein p53"


def test_myvariant_search_parses(monkeypatch):
    fake = {"hits": [{"_id": "chr17:7577121:G:A", "dbsnp": {"rsid": "rs12345"}}]}
    monkeypatch.setattr("sciforge.science.sources.genomics.http_get_json",
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
    monkeypatch.setattr("sciforge.science.sources.genomics.http_get_json", fake_json)
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
    monkeypatch.setattr("sciforge.science.sources.genomics.http_get_json", fake_json)
    genomics.register()
    c = get_registry().get("dbsnp")
    hits = c.search("rs12345", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "rs12345"


def test_gnomad_search_parses(monkeypatch):
    fake = {"data": {"variant": {"variantId": "1-55516888-G-A", "consequence": "missense"}}}
    monkeypatch.setattr("sciforge.science.sources.genomics.http_get_json",
                        lambda url, **kw: fake)
    genomics.register()
    c = get_registry().get("gnomad")
    hits = c.search("1-55516888-G-A", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "1-55516888-G-A"
