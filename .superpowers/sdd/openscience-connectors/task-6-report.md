# Task 6 Report: Protein Sources (6 connectors)

## Status: DONE

## Files Created

- `clawsgo_self/science/sources/proteins.py` — 6 protein connectors: uniprot, rcsb-pdb, pdbe, alphafold, interpro, sifts
- `tests/test_science_proteins.py` — 7 tests covering registration, search parsing for each, and uniprot fasta fetch

## Implementation Notes

The task brief's template used `from clawsgo_self.science import register` and then called `register(c)` inside `register()`, which shadows the module-level `register` function and causes a `TypeError`. Fixed by aliasing the import as `_register` and using `from clawsgo_self.science.http import http_get_json, http_get_text` (matching the monkeypatch style used in `test_science_datasets.py`). This also ensures `monkeypatch.setattr("clawsgo_self.science.sources.proteins.http_get_json", ...)` resolves correctly.

## Test Results

```
7 passed in 0.81s
```

Full suite: **96 passed** (no regressions).

## Commits

```
git add clawsgo_self/science/sources/proteins.py tests/test_science_proteins.py
git commit -m "feat(science): add 6 protein connectors (uniprot/rcsb-pdb/pdbe/alphafold/interpro/sifts)"
```
