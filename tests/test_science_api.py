import pytest
from sciforge.science.connector import Connector, ConnectorRegistry
from sciforge.science import api


def _reg() -> ConnectorRegistry:
    reg = ConnectorRegistry()
    reg.register(Connector(id="openalex", name="OpenAlex", domain="literature",
                            description="OpenAlex works", search=lambda q, n: [
                                {"title": "T", "year": 2024, "doi": "10/x",
                                 "url": "http://x", "venue": "V", "authors": ["A"],
                                 "cited_by": 5, "abstract": "ab"}]))
    reg.register(Connector(id="uniprot", name="UniProt", domain="proteins",
                            description="UniProt KB", search=lambda q, n: [
                                {"id": "P12345", "title": "Protein X",
                                 "summary": "desc", "url": "http://u"}]))
    reg.register(Connector(id="chembl", name="ChEMBL", domain="chemistry",
                            description="ChEMBL", search=lambda q, n: []))
    return reg


def test_science_list_dbs_all(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    r = api.science_list_dbs("")
    assert r["ok"] is True
    assert r["count"] == 3
    assert any(d["id"] == "openalex" for d in r["databases"])


def test_science_list_dbs_by_domain(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    r = api.science_list_dbs("proteins")
    assert r["count"] == 1
    assert r["databases"][0]["id"] == "uniprot"


def test_science_search_hits(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    monkeypatch.setattr(api, "_offline", lambda: False)
    r = api.science_search("openalex", "test", limit=5)
    assert r["ok"] is True
    assert r["database"] == "openalex"
    assert r["hits"][0]["title"] == "T"


def test_science_search_unknown_db(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    r = api.science_search("nonexistent", "test")
    assert r["ok"] is False
    assert "not found" in r["error"] or "不存在" in r["error"]


def test_science_search_offline(monkeypatch):
    monkeypatch.setenv("CLAWSGO_SELF_OFFLINE", "1")
    reg = _reg()
    reg.register(Connector(id="o", name="O", domain="literature",
                            description="", search=lambda q, n: []))
    monkeypatch.setattr(api, "get_registry", lambda: reg)
    r = api.science_search("o", "test")
    assert r["ok"] is True
    assert r["offline"] is True
    assert r["hits"] == []


def test_science_fetch_not_supported(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    r = api.science_fetch("openalex", "W123")
    assert r["ok"] is False
    assert "not supported" in r["error"] or "不支持" in r["error"]


def test_science_cross_lookup_merges(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    monkeypatch.setattr(api, "_offline", lambda: False)
    r = api.science_cross_lookup("test", databases=["openalex", "uniprot"], limit=5)
    assert r["ok"] is True
    assert r["total"] >= 2
    titles = [h["title"] for h in r["hits"]]
    assert "T" in titles and "Protein X" in titles


def test_cross_lookup_normal_shape(monkeypatch):
    monkeypatch.setattr(api, "get_registry", _reg)
    monkeypatch.setattr(api, "_offline", lambda: False)
    r = api.cross_lookup("test", databases=["openalex"], limit=5)
    assert len(r) == 1
    assert r[0]["title"] == "T"
    assert r[0]["year"] == 2024
    assert r[0]["doi"] == "10/x"
    assert r[0]["cited_by"] == 5
