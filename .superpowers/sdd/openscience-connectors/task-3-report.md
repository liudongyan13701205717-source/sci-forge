# Task 3 Report: Literature Sources (7 connectors)

## What I implemented

- `clawsgo_self/science/sources/__init__.py` — empty package marker
- `clawsgo_self/science/sources/literature.py` — 7 literature connectors (openalex, arxiv, biorxiv, crossref, europepmc, pubmed, semantic-scholar) with `register()` function
- `tests/test_science_literature.py` — 9 tests covering registration, offline behavior, and response parsing for each connector

## What I tested and test results

- `CLAWSGO_SELF_OFFLINE=1 pytest tests/test_science_literature.py -v` → **9 passed**
- `pytest tests/test_science_literature.py -v` (no offline) → **9 passed**
- `pytest tests/test_science_api.py -v` (no offline) → **8 passed** (3 failures seen earlier were caused by `CLAWSGO_SELF_OFFLINE=1` env var making `science_search` return empty, not a real regression)

## TDD Evidence (RED/GREEN)

- **RED**: Initial test run failed — `ModuleNotFoundError` because `sources/literature.py` did not exist yet, and `register()` shadowed the imported `register`
- **GREEN**: After implementing `sources/literature.py` with proper imports and the `register()` function, all 9 tests pass

## Files changed

- `clawsgo_self/science/sources/__init__.py` (new, empty)
- `clawsgo_self/science/sources/literature.py` (new, ~212 lines)
- `tests/test_science_literature.py` (new, ~152 lines)

## Self-review findings

- Import shadowing fixed by aliasing the package-level `register` as `_register`
- `http_get_json`/`http_get_text` imported directly (not via `sci_http.` alias) so monkeypatch can replace them as module attributes
- All 7 connectors return the uniform shape: `title/year/doi/url/venue/authors/cited_by/abstract`
- Offline behavior returns `[]` (empty list) as expected by the existing `science_search` wrapper

## Any issues or concerns

None. The task was straightforward and matches the spec exactly.
