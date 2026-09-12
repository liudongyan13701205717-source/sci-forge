import pytest
from sciforge.research import references, recommender


def test_ref_to_bibtex_offline():
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = references.ref_to_bibtex("10.1109/1234.5678")
    assert r["ok"] is True
    assert r["bibtex"].startswith("@article{")
    assert "10.1109/1234.5678" in r["bibtex"]
    monkeypatch.undo()


def test_batch_ref_export_no_doi():
    r = references.batch_ref_export("no dois here")
    assert r["ok"] is False
    assert "missing" in r or "error" in r


def test_batch_ref_export_with_doi():
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = references.batch_ref_export("See 10.1109/1234.5678 and 10.1038/nphys1170")
    assert r["ok"] is True
    assert r["count"] == 2
    assert r["bibtex"].count("@article{") == 2
    monkeypatch.undo()


def test_doi_extraction_from_url():
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = references.ref_to_bibtex("https://doi.org/10.1109/1234.5678")
    assert r["ok"] is True
    assert "10.1109/1234.5678" in r["bibtex"]
    monkeypatch.undo()


def test_recommend_offline():
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setenv("SCI_FORGE_OFFLINE", "1")
    r = recommender.recommend_papers("deep learning", limit=3)
    assert r["ok"] is True
    assert r["offline"] is True
    assert r["papers"] == []
    monkeypatch.undo()


def test_recommend_limit_clamp():
    r = recommender.recommend_papers("test", limit=1000)
    assert r["ok"] is True
    assert r["count"] == 0
