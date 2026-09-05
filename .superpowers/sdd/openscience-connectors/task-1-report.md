# Task 1 Report: Connector 框架

## What Implemented

4 files created:

- `clawsgo_self/science/__init__.py` — package init, exports Connector/ConnectorHit/ConnectorRegistry/DOMAINS, provides module-level `get_registry()` and `register()` helpers
- `clawsgo_self/science/connector.py` — `ConnectorHit` dataclass with `to_dict()`, `Connector` dataclass (id/name/domain/description/search/fetch/requires_key), `ConnectorRegistry` (register/get/has/all/by_domain/catalog), `DOMAINS` constant
- `clawsgo_self/science/http.py` — `http_get_json()` and `http_get_text()` with offline guard, per-host rate limiting, retry/backoff on 429/5xx, `_offline()` helper
- `tests/test_science_framework.py` — 8 tests covering DOMAINS, ConnectorHit.to_dict, registry CRUD, by_domain filter, catalog shape, missing-key handling, duplicate-id last-wins

## TDD Evidence

**RED:** `ModuleNotFoundError: No module named 'clawsgo_self.science.connector'` — confirmed before implementation.

**GREEN:** 8/8 new tests pass. All 69 tests pass (61 existing + 8 new).

## Test Results

```
tests/test_science_framework.py::test_domains_constant PASSED
tests/test_science_framework.py::test_connector_hit_to_dict PASSED
tests/test_science_framework.py::test_registry_register_and_get PASSED
tests/test_science_framework.py::test_registry_by_domain PASSED
tests/test_science_framework.py::test_registry_catalog_shape PASSED
tests/test_science_framework.py::test_registry_get_missing_returns_none PASSED
tests/test_science_framework.py::test_registry_has_missing PASSED
tests/test_science_framework.py::test_registry_duplicate_id_last_wins PASSED

69 passed in 81.79s
```

## Files Changed

| File | Action |
|------|--------|
| `clawsgo_self/science/__init__.py` | create |
| `clawsgo_self/science/connector.py` | create |
| `clawsgo_self/science/http.py` | create |
| `tests/test_science_framework.py` | create |

## Self-Review Findings

- Code matches existing patterns: `_offline()` guard, `_USER_AGENT` header, `urllib.request`, dataclasses with `to_dict()`, graceful `None`/empty returns on failure
- No new dependencies — stdlib only
- `Connector.search` is typed `Callable` (not `Optional[Callable]`) since every connector must implement search; `fetch` is `Optional` since some connectors may not support detail fetch
- Rate limiting uses per-host lock + monotonic clock, matching the spec exactly
- `http_get_json` retry loop: 429/5xx triggers exponential backoff (1s, 2s), other errors return None immediately
- No excess comments, no unrequested abstractions

## Issues or Concerns

None.
