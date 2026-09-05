import pytest
from sciforge.science import get_registry
from sciforge.science.sources import chemistry


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
    monkeypatch.setattr("sciforge.science.sources.chemistry.http_get_json",
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
    monkeypatch.setattr("sciforge.science.sources.chemistry.http_get_json", fake_json)
    chemistry.register()
    c = get_registry().get("pubchem")
    hits = c.search("acetaminophen", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Acetaminophen"


def test_chebi_search_parses(monkeypatch):
    fake = {"List": {"item": [{"chebiId": "CHEBI:12345", "chebiAsciiName": "Caffeine"}]}}
    monkeypatch.setattr("sciforge.science.sources.chemistry.http_get_json",
                        lambda url, **kw: fake)
    chemistry.register()
    c = get_registry().get("chebi")
    hits = c.search("caffeine", 5)
    assert len(hits) == 1
    assert hits[0]["title"] == "Caffeine"
