# Task 5 Report: Research-line integration (sources param)

## Status: DONE

## Commits Created
- `5a48e55` feat(science): wire multi-source search into literature_review/novelty/citation_landscape

## Test Summary
- 4 new tests in `tests/test_science_integration.py` — all pass with `CLAWSGO_SELF_OFFLINE=1`
- Existing tests remain green (92 passed, 3 pre-existing failures in `test_science_api.py` caused by `CLAWSGO_SELF_OFFLINE=1` env var, unrelated to this change)

## Changes Made

### `clawsgo_self/research/survey.py`
- Added `sources: list[str] | None = None` parameter to `literature_review()`
- When `sources` is provided, uses `cross_lookup()` from science API instead of `lit.search_openalex()`
- Default `sources=None` preserves existing OpenAlex path

### `clawsgo_self/research/novelty.py`
- Added `sources: list[str] | None = None` parameter to `check_novelty()`
- When `sources` is provided, uses `cross_lookup()` with joined phrases
- Default `sources=None` preserves existing multi-query OpenAlex path

### `clawsgo_self/research/community.py`
- Added `sources: list[str] | None = None` parameter to `citation_landscape()`
- When `sources` is provided (topic mode), uses `cross_lookup()` instead of `lit.search_openalex()`
- Default `sources=None` preserves existing OpenAlex path

### `tests/test_science_integration.py` (new)
- 4 tests covering multi-source and default-source paths for all 3 research tools
- Uses monkeypatch to mock registry, offline flag, and `search_openalex` for deterministic offline execution

## Notes
- Backward compatible: all existing callers work unchanged
- No new dependencies
- Tests run fully offline via `CLAWSGO_SELF_OFFLINE=1`

---

## Fix Report — Reviewer Finding Resolution

**Date:** 2026-09-05
**Commit:** `f06cfff`

### Issue 1: Tautological assertion in `test_citation_landscape_multi_source`

**Before:**
```python
r = citation_landscape(paper_id="p_cit", layout=layout, doi_or_topic="test",
                       sources=["openalex"])
assert r.ok is True or r.mode == "topic"
```

**Problem:** Since `doi_or_topic="test"` is never a DOI, `r.mode` is always `"topic"`, making the assertion always pass regardless of whether multi-source was wired correctly.

**Fix:** Use `sources=["openalex", "crossref"]` and assert specific titles from both sources appear in `r.top_cited`, matching the pattern used in `test_literature_review_multi_source`.

**After:**
```python
r = citation_landscape(paper_id="p_cit", layout=layout, doi_or_topic="test",
                       sources=["openalex", "crossref"])
assert r.ok is True
titles = [p.get("title") for p in r.top_cited]
assert "From OpenAlex" in titles
assert "From Crossref" in titles
```

### Issue 2: Didn't verify multi-source results

**Problem:** The test only checked mode, not whether multi-source search actually merged results.

**Fix:** Same as above — now asserts both "From OpenAlex" and "From Crossref" titles appear in `r.top_cited`, which verifies `cross_lookup` was called and results merged from both sources.

### Verification
All 4 tests pass:
```
tests/test_science_integration.py::test_literature_review_multi_source PASSED
tests/test_science_integration.py::test_literature_review_default_sources PASSED
tests/test_science_integration.py::test_check_novelty_multi_source PASSED
tests/test_science_integration.py::test_citation_landscape_multi_source PASSED
```
