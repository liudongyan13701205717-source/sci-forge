import json
import os
import tempfile
from unittest.mock import patch

from sciforge.science import cache


def test_store_and_search_cache():
    with tempfile.TemporaryDirectory() as tmp:
        with patch.object(cache, "_CACHE_PATH", os.path.join(tmp, "test_cache.db")):
            hits = [{"title": "Paper A", "doi": "10/a", "url": "http://a"}]
            cache.store_cache("query1", "openalex", hits)

            results = cache.search_cache("query1", ["openalex"], limit=5)
            assert len(results) == 1
            assert results[0]["title"] == "Paper A"


def test_search_cache_no_match():
    with tempfile.TemporaryDirectory() as tmp:
        with patch.object(cache, "_CACHE_PATH", os.path.join(tmp, "test_cache.db")):
            results = cache.search_cache("nonexistent", ["openalex"], limit=5)
            assert len(results) == 0


def test_search_cache_dedup():
    with tempfile.TemporaryDirectory() as tmp:
        with patch.object(cache, "_CACHE_PATH", os.path.join(tmp, "test_cache.db")):
            hits_a = [{"title": "Dup", "doi": "10/x", "url": "http://x"}]
            hits_b = [{"title": "Dup", "doi": "10/x", "url": "http://x"}]
            cache.store_cache("q", "openalex", hits_a)
            cache.store_cache("q", "crossref", hits_b)
            results = cache.search_cache("q", ["openalex", "crossref"], limit=5)
            assert len(results) == 1


def test_search_cache_empty_databases():
    results = cache.search_cache("test", [], limit=5)
    assert results == []
