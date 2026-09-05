import pytest
from sciforge.science import get_registry
from sciforge.science.sources import proteins


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
    monkeypatch.setattr("sciforge.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("uniprot")
    hits = c.search("kinase", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Kinase X"
    assert hits[0]["url"] == "https://www.uniprot.org/uniprotkb/P12345"


def test_uniprot_fetch_fasta(monkeypatch):
    fake = ">sp|P12345|KINH_HUMAN\nMKWVTFISLL"
    monkeypatch.setattr("sciforge.science.sources.proteins.http_get_text",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("uniprot")
    data = c.fetch("P12345", "fasta")
    assert data["format"] == "fasta"
    assert "MKWVTFISLL" in data["data"]


def test_rcsb_pdb_search_parses(monkeypatch):
    fake = {"result_set": [{"identifier": "1ABC", "score": 1.0}]}
    monkeypatch.setattr("sciforge.science.sources.proteins.http_get_json",
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
    monkeypatch.setattr("sciforge.science.sources.proteins.http_get_json",
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
    monkeypatch.setattr("sciforge.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("interpro")
    hits = c.search("kinase", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Kinase dom"


def test_pdbe_search_parses(monkeypatch):
    fake = {"1abc": {"title": "Heme binding protein"}}
    monkeypatch.setattr("sciforge.science.sources.proteins.http_get_json",
                        lambda url, **kw: fake)
    proteins.register()
    c = get_registry().get("pdbe")
    hits = c.search("heme", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Heme binding protein"
