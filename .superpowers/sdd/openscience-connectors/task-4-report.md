# Task 4 Report: Dataset / Open-Access Connectors

## What I Implemented

- `clawsgo_self/science/sources/datasets.py` — 4 connectors: zenodo, doaj, openaire, huggingface
- `tests/test_science_datasets.py` — 5 tests covering registration count and parsing for each connector

## What I Tested and Test Results

```
tests/test_science_datasets.py::test_datasets_registers_4 PASSED
tests/test_science_datasets.py::test_zenodo_search_parses PASSED
tests/test_science_datasets.py::test_doaj_search_parses PASSED
tests/test_science_datasets.py::test_openaire_search_parses PASSED
tests/test_science_datasets.py::test_huggingface_search_parses PASSED
```

All 5 new tests pass. Existing science tests (literature + framework) also pass — 22/22 green.

## TDD Evidence

- **RED**: First test run failed with `ImportError: cannot import name 'datasets'` — module didn't exist yet.
- **GREEN**: After writing `datasets.py`, all 5 tests pass.

## Files Changed

- `clawsgo_self/science/sources/datasets.py` (new, 108 lines)
- `tests/test_science_datasets.py` (new, 70 lines)

## Self-Review Findings

- The brief's openaire test had a bracket mismatch (`]}` vs `]}}}`) — fixed in the test file.
- The brief's `datasets.py` used `from clawsgo_self.science import register` which would shadow the module-level `register()` function. Fixed by aliasing to `_register` (matching `literature.py` pattern).
- The brief's `datasets.py` used `sci_http.http_get_json` but the test mocks `clawsgo_self.science.sources.datasets.http_get_json`. Fixed by importing `http_get_json` directly at module level (matching `literature.py` pattern).
- 3 pre-existing failures in `test_science_api.py` are unrelated to this task (confirmed by running on clean tree).

## Issues or Concerns

None. All connectors follow the existing pattern, output shape matches spec, offline-first behavior preserved.
