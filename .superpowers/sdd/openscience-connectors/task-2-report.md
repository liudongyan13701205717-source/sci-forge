# Task 2 Report: API 层（4 个 MCP 工具 + server.py 注册）

## What I implemented

1. **`clawsgo_self/science/api.py`** — 5 functions:
   - `science_list_dbs(domain?)` — list all DBs or filter by domain
   - `science_search(database, query, limit)` — single-db search with offline gate
   - `science_fetch(database, id, format)` — fetch by id, rejects unsupported
   - `science_cross_lookup(query, databases?, limit)` — multi-db merge with dedup
   - `cross_lookup(query, databases, limit)` — research-line helper, output same shape as `lit.search_openalex()`

2. **`clawsgo_self/server.py`** — registered 4 MCP tools after `review_code`, before `def run()`.

3. **`tests/test_science_api.py`** — 8 tests covering all functions.

## What I tested and test results

```
tests/test_science_api.py::test_science_list_dbs_all PASSED
tests/test_science_api.py::test_science_list_dbs_by_domain PASSED
tests/test_science_api.py::test_science_search_hits PASSED
tests/test_science_api.py::test_science_search_unknown_db PASSED
tests/test_science_api.py::test_science_search_offline PASSED
tests/test_science_api.py::test_science_fetch_not_supported PASSED
tests/test_science_api.py::test_science_cross_lookup_merges PASSED
tests/test_science_api.py::test_cross_lookup_normal_shape PASSED

8 passed in 0.45s
```

Existing tests also green:
```
tests/test_science_framework.py — 8 passed
```

## TDD Evidence

**RED**: First run after writing test — `ImportError: cannot import name 'api'` (ModuleNotFoundError equivalent on Python 3.14).

**GREEN**: After creating `api.py` + registering tools — 7 passed, 1 failed (`test_science_fetch_not_supported` because error message was "does not support fetch" vs expected "not supported").

**Fix**: Changed error message to `"fetch not supported"` — 8 passed.

## Files changed

- Create: `clawsgo_self/science/api.py` (79 lines)
- Modify: `clawsgo_self/server.py` (+20 lines, 4 MCP tool registrations)
- Create: `tests/test_science_api.py` (91 lines)

## Self-review findings

- All 8 tests pass, existing tests untouched.
- `_normalize_hit` handles both dict and `ConnectorHit` inputs.
- `cross_lookup` dedupes by doi/url/title, same shape as `lit.search_openalex()`.
- Offline gate works: `CLAWSGO_SELF_OFFLINE=1` returns empty hits gracefully.
- `science_fetch` properly rejects connectors without a `fetch` callable.

## Issues or concerns

None.
