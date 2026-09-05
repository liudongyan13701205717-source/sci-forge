import pytest
from sciforge.science import get_registry
from sciforge.science.sources import pathways, omics


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
    monkeypatch.setattr("sciforge.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("biogrid")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "P67890"


def test_intact_search_parses(monkeypatch):
    fake = {"data": [{"id": "EBI-12345", "label": "BRCA1-BRCA2"}]}
    monkeypatch.setattr("sciforge.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("intact")
    hits = c.search("BRCA1", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "EBI-12345"


def test_kegg_search_parses(monkeypatch):
    fake = [["hsa:7157\tTP53 tumor protein p53"]]
    monkeypatch.setattr("sciforge.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("kegg")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert "TP53" in hits[0]["title"]


def test_opentargets_search_parses(monkeypatch):
    fake = {"data": [{"id": "ENSG00000141510", "name": "TP53", "symbol": "TP53"}]}
    monkeypatch.setattr("sciforge.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("opentargets")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "TP53"


def test_reactome_search_parses(monkeypatch):
    fake = {"results": [{"dbId": 12345, "displayName": "DNA Repair"}]}
    monkeypatch.setattr("sciforge.science.sources.pathways.http_get_json",
                        lambda url, **kw: fake)
    pathways.register()
    c = get_registry().get("reactome")
    hits = c.search("DNA repair", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "DNA Repair"


def test_arrayexpress_search_parses(monkeypatch):
    fake = {"hits": [{"accession": "E-MTAB-1234", "title": "RNA-seq of cancer"}]}
    monkeypatch.setattr("sciforge.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("arrayexpress")
    hits = c.search("cancer", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "RNA-seq of cancer"


def test_depmap_search_parses(monkeypatch):
    fake = {"data": [{"DepMap_ID": "ACH-000001", "cell_line_name": "A549"}]}
    monkeypatch.setattr("sciforge.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("depmap")
    hits = c.search("A549", 5)
    assert len(hits) == 1
    assert hits[0]["id"] == "ACH-000001"


def test_expression_atlas_search_parses(monkeypatch):
    fake = {"results": [{"experimentAccession": "E-GEOD-12345", "description": "gene expr"}]}
    monkeypatch.setattr("sciforge.science.sources.omics.http_get_json",
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
    monkeypatch.setattr("sciforge.science.sources.omics.http_get_json", fake_json)
    omics.register()
    c = get_registry().get("geo")
    hits = c.search("breast cancer", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Breast cancer GEO series"


def test_gtex_search_parses(monkeypatch):
    fake = {"geneSymbol": "TP53", "tissueSiteDetailId": "Lung", "tpkm": 12.5}
    monkeypatch.setattr("sciforge.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("gtex")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "TP53 - Lung"


def test_hpa_search_parses(monkeypatch):
    fake = [{"gene": "TP53", "tissue": "Lung", "celltype": "alveolar"}]
    monkeypatch.setattr("sciforge.science.sources.omics.http_get_json",
                        lambda url, **kw: fake)
    omics.register()
    c = get_registry().get("hpa")
    hits = c.search("TP53", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "TP53"
