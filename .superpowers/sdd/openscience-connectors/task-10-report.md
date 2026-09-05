# Task 10 Report: 文档更新 + 全量回归

## Status: DONE

## Commits Created

- `4c58fc6` — `docs: update README and USAGE for science connector layer; fix test offline flag`

## Changes

### README.md
- Added 4 new tool rows to the feature table: `science_list_dbs`, `science_search`, `science_fetch`, `science_cross_lookup`
- Updated tool count from 20 → 4 in "重启客户端后即可看到全部 24 个工具"
- Added new `## 科学数据查询（science）` section with domain/connector table and tool descriptions
- Updated architecture tree to include `science/` package
- Updated test count description (removed hardcoded "61 项", replaced with generic description)

### USAGE.md
- Updated tool count references from 20 → 24
- Updated tool list to include 4 science tools
- Added new `## 7. 科学数据查询` section with usage examples for all 4 tools (`science_list_dbs`, `science_search`, `science_fetch`, `science_cross_lookup`)

### tests/test_science_api.py
- Fixed 3 tests that assumed offline=False but were running under `CLAWSGO_SELF_OFFLINE=1`:
  - `test_science_search_hits`
  - `test_science_cross_lookup_merges`
  - `test_cross_lookup_normal_shape`
- Added `monkeypatch.setattr(api, "_offline", lambda: False)` to each

## Test Summary

**127 passed in 60.95s** — all existing 61 tests + new science connector tests pass with `CLAWSGO_SELF_OFFLINE=1`.

## Report File

`.superpowers/sdd/openscience-connectors/task-10-report.md`
