<div align="center">

# sci-forge

**One MCP, the entire research pipeline from "an idea" to "a submitted paper"**

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](./pyproject.toml)
[![MCP Tools](https://img.shields.io/badge/MCP%20tools-75-green.svg)](./docs/mcp-tools.md)
[![Disciplines](https://img.shields.io/badge/disciplines-1538-green.svg)](./docs/disciplines.md)
[![Connectors](https://img.shields.io/badge/connectors-46-green.svg)](./docs/connectors.md)

[中文](README.md) · [Installation](docs/installation.md) · [Quickstart](docs/quickstart.md) · [MCP Tool Catalogue](docs/mcp-tools.md) · [Discipline System](docs/disciplines.md) · [Scientific Data Connectors](docs/connectors.md) · [Contributing](CONTRIBUTING.md) · [Code of Conduct](CODE_OF_CONDUCT.md) · [Security Policy](SECURITY.md) · [Changelog](CHANGELOG.md)

</div>

---

## What this is

`sci-forge` is a **fully local, self-hosted** [Model Context Protocol](https://modelcontextprotocol.io) server that compresses everything between "reading a paper" and "handing in a submittable paper" into a set of tools an AI client can call directly.

It is not a chatbot and not a prompt template — it is a resident process: **paper-convention knowledge for 1538 disciplines**, **direct connectors to 46 public scientific databases**, a **five-step reproduction loop**, and **fail-closed integrity and citation gates**, all exposed as MCP tools.

### Value proposition

| What you want to do | What sci-forge gives you |
| --- | --- |
| Reproduce a paper's experiments | Get the PDF → parse → extract hyper-parameters → generate numpy/torch code → run in a sandbox → compare against the paper's numbers → deliver `results.json` + figures + source |
| Write a paper from scratch | Discipline-aware section templates (driven by the `paper_types` of all 1538 disciplines) + guided authoring + LaTeX/PDF/DOCX export |
| Find a topic or a gap | Key-free OpenAlex/arXiv search → topic scouting → clustering → research gap → candidate hypotheses → experiment plan |
| Self-check before submitting | Simulated peer review (4-dimension scoring), journal fit scoring, a revision coach, rebuttal auditing, journal/conference recommendations |
| Hold the integrity line | claim→source verification, batch DOI verification of the reference list, Stage 2.5 / 4.5 integrity gates, Material Passport |
| Query cross-database scientific data | 46 connectors across 7 domains: single-database search, cross-database lookup, parallel batch search |

### Three design commitments

1. **Usable without an API key.** The core paths (literature search, DOI verification, metadata, citation graphs) go through the key-free public interfaces of OpenAlex / Crossref. An LLM is an **optional enhancement**: write an OpenAI-compatible endpoint into `.sci-forge/env` to enable it; with nothing configured every feature falls back to local templates and no path breaks.
2. **Fail-closed first.** The review intake gate, the integrity gates, and bypass approval all follow "refuse when evidence is insufficient" rather than "let it through when possible".
3. **Declarative discipline knowledge.** The discipline registry is data, not logic. Adding a discipline means adding one `.py` file — the discovery mechanism needs no change.

> Independently developed from public materials and public interfaces. It is not affiliated with, and does not depend on, any official SciForge site or API, and has no association with the SciForge trademark.

---

## Table of contents

- [Quickstart](#quickstart)
- [Architecture](#architecture)
- [MCP tool catalogue](#mcp-tool-catalogue-75-tools)
- [Discipline coverage](#discipline-coverage-1538-disciplines)
- [Scientific data connectors](#scientific-data-connectors-46-connectors)
- [Relationship to the desktop edition](#relationship-to-the-desktop-edition-two-repositories)
- [Roadmap](#roadmap)
- [Development and testing](#development-and-testing)
- [Contributing](#contributing)
- [License](#license)

---

## Quickstart

### Prerequisites

- Python **≥ 3.10** (CI covers 3.11 / 3.12 / 3.13)
- An MCP client that speaks the stdio transport (opencode, Claude Code, Cursor, …)

### Installation

```bash
# Option 1: install straight from git (simplest)
pip install "git+https://github.com/liudongyan13701205717-source/sci-forge.git"

# Option 2: clone and install editable (recommended for development)
git clone https://github.com/liudongyan13701205717-source/sci-forge.git
cd sci-forge
pip install -e ".[reproduce,dev]"

# Option 3: MCP core only, without the numerical dependencies of the reproduce line
pip install -e .
```

| extra | Contents | When you need it |
| --- | --- | --- |
| (none) | `mcp>=1.29.0` only | Discipline registry / connectors / authoring / review only |
| `reproduce` | `pymupdf>=1.24`, `numpy>=1.26`, `matplotlib>=3.8` | PDF parsing, running reproduced code, plotting |
| `export` | No hard dependency today; used when a LaTeX engine (`xelatex` / `pdflatex`) is present, otherwise falls back to the built-in PyMuPDF renderer | PDF export |
| `dev` | `pytest>=8.0` | Running tests and lint |

### Registering it as an MCP server

Installation gives you a `sci-forge` command. It starts an stdio transport, so the configuration needs **neither** `PYTHONPATH` **nor** a `cwd`:

```jsonc
{
  "mcp": {
    "sci-forge": {
      "type": "local",
      "command": ["sci-forge"],
      "enabled": true
    }
  }
}
```

You can also use the module entry point: set `command` to `["python", "-m", "sciforge"]`.

### Verifying the installation

```bash
sci-forge --version      # prints sci-forge 0.1.0
sci-forge --help         # shows usage
SCI_FORGE_OFFLINE=1 python -m pytest tests/ -q    # 268 cases should all pass
```

### Trying it in 60 seconds

Say this in your MCP client's conversation, or call the tools by hand:

```text
list_disciplines()                    # see which disciplines are built in
science_list_dbs("literature")        # see which databases the literature domain offers
ideate_paper("lightweight interpretability for large language models", "demo")   # topic → gap → hypotheses → experiment plan
write_section("demo", "abstract", "write an abstract for 'Lightweight Inference on Edge Devices'", "markdown")
export_document("demo", "pdf")        # produces .sci-forge/projects/demo/doc.pdf
```

A fuller end-to-end walkthrough lives in [docs/quickstart.md](./docs/quickstart.md) and [USAGE.md](./USAGE.md).

---

## Architecture

```
                        ┌─────────────────────────────────────────┐
                        │   MCP client (opencode / Claude Code…)   │
                        └───────────────────┬─────────────────────┘
                                            │ stdio (JSON-RPC)
                        ┌───────────────────▼─────────────────────┐
                        │  sciforge/server.py                      │
                        │  FastMCP("sci-forge")                    │
                        │  75 @mcp.tool  +  2 @mcp.resource        │
                        └──┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┘
       ┌────────────────────┘   │   │   │   │   │   │   │   │   └──────────────┐
       ▼                        ▼   │   │   │   │   │   │   ▼                  ▼
 ┌───────────┐  ┌───────────┐  ┌────▼─┐ │ ┌─────▼─┐ │ ┌─────▼──┐  ┌──────────────────┐
 │reproduce/ │  │research/  │  │write/ │ │ │export/ │ │ │deliver/│  │  disciplines/    │
 │ five-step │  │ research  │  │DocStore│ │ │md→tex  │ │ │submission│  │  1538 disciplines │
 │ loop+crit.│  │ tool set  │  │templates│ │ │/pdf   │ │ │packaging│  │  zero-reg auto    │
 └───────────┘  └───────────┘  └───────┘ │ └───────┘ │ └────────┘  └──────────────────┘
                                           │ ┌─────▼──┐
                                           │ │review/ │ 7-seat panel + intake gate + guides
                                           │ └────────┘
                                           │ ┌─────▼──┐
                                           │ │claims/ │ claim→source verify + Stage 2.5/4.5
                                           │ └────────┘   integrity gates + Material Passport
                                           │ ┌─────▼──┐
                                           │ │venue/  │ journal templates + journal-fit
                                           │ └────────┘
                                           │ ┌─────▼──┐
                                           └─│science/│ 46 connectors / 7 domains / 5 tools
                                             └────────┘
                        ┌────────────────────────┴────────────────────────┐
                        │  core/  workspace_root() + Layout(.sci-forge)     │
                        │         + optional LLM layer (falls back to      │
                        │           templates when no endpoint is set)     │
                        └─────────────────────────────────────────────────┘

 sciforge/parse/       PDF parsing (PyMuPDF; prerequisite of the reproduce line)
 sciforge/__main__.py  python -m sciforge
 sciforge/cli.py       the sci-forge command (stdio / --version / --help)
```

### Storage layout

Everything the tools produce lands under `.sci-forge/` at the workspace root (gitignored):

```
.sci-forge/
├── env                          # optional LLM endpoint config (BASE_URL / API_KEY / MODEL), never committed
├── projects/{paper_id}/
│   ├── doc.md / doc.tex / doc.html / doc.pdf
│   ├── sections/                # per-section intermediate artefacts
│   └── research/                # research artefacts *.json / *.md, reusable and packageable
└── tasks/{task_id}/
    ├── parse/  code/  runs/     # parse results / generated code / per-run records
    └── deliverables/            # figures, data, source code, reports
```

### Optional enhancement: the LLM

Write an OpenAI-compatible endpoint into `.sci-forge/env`:

```
BASE_URL=https://your-endpoint/v1
API_KEY=sk-...
MODEL=...
```

With nothing configured, tools such as `ideate_paper` / `write_section` / `peer_review` / `venue_suggest` fall back to **local templates** and rule engines. Everything stays usable; only the fluency of the generated text drops.

---

## MCP tool catalogue (75 tools)

> The static `@mcp.tool()` decorator count is 75 and the runtime `mcp.list_tools()` count is also 75 — they agree. There are additionally 2 resources: the static `science://databases` and the parameterised template `science://databases/{domain}`.
> Per-tool parameter signatures and behavioural details live in [docs/mcp-tools.md](./docs/mcp-tools.md).

### Reproduce line (2)

| Tool | What it does |
| --- | --- |
| `reproduce_paper` | The five-step reproduction loop: parse the PDF → plan → generate code → run in a sandbox and compare → deliverables |
| `reproduce_status` | Query the async status and stage progress of a reproduction task |

### Writing line (2)

| Tool | What it does |
| --- | --- |
| `write_section` | Generate paper content per section (abstract / problem / modeling / solution / results / references, …) |
| `export_document` | Export the written document to LaTeX / PDF / DOCX / HTML |

### Research line (3)

| Tool | What it does |
| --- | --- |
| `ideate_paper` | Ideation: topic → research gap → candidate hypotheses → multi-perspective review → experiment plan |
| `inject_results` | Fold real experimental results from a reproduction task into the matching paper sections |
| `research_verdict` | Results spin-gate: a PROCEED / REFINE / PIVOT decision recommendation |

### Research / paper line (35)

| Tool | What it does |
| --- | --- |
| `research_plan` | A full research plan (RQ / hypotheses / goals / contributions / method / data / metrics / milestones / risks) |
| `literature_review` | Key-free OpenAlex search producing a review skeleton (representative papers / clusters / gaps / structure) |
| `auto_title_abstract` | Derive title / abstract / keywords from the body text you have already written |
| `peer_review` | Simulated peer review (novelty / rigor / clarity / soundness, 4-dimension scoring + recommendation) |
| `venue_suggest` | Recommend target journals / conferences by topic (built-in mapping table + optional LLM) |
| `paper_polish` | Paper quality checks (completeness / consistency / grammar, three modes) |
| `compare_metrics` | Metric comparison table across tasks / baselines + Welch t and Mann-Whitney U tests |
| `check_novelty` | Search for similar work, report overlap and candidate differentiators |
| `citation_landscape` | Citation neighbourhood and hotness analysis (yearly distribution / highly-cited representatives / primary venues) |
| `project_memory` | Project-progress ledger as a timeline (note / milestone / status) |
| `review_code` | Static critique of reproduced code (random seeds / hard-coding / risks + a confidence score) |
| `ref_to_bibtex` | Generate a BibTeX entry from a DOI |
| `batch_ref_export` | Extract DOIs / citations from text and convert them all to BibTeX |
| `recommend_papers` | Recommend papers around a research topic (optionally filtered by sources) |
| `prisma_review` | The PRISMA systematic-review flow (identify → dedupe → screen → qualify → include → synthesise → document) |
| `convert_citation` | BibTeX → a single style (apa / chicago-author-date / chicago-note-bibliography / mla / ieee / vancouver) |
| `convert_citation_all` | BibTeX → all 6 styles in one call |
| `revision_coach` | Review comments → a structured revision roadmap (CRITICAL / MAJOR / MINOR) |
| `rebuttal_audit` | Point-by-point rebuttal auditing (fail-closed) |
| `detect_style` | Machine-generated prose detection (hedging density + template phrasing + hollow connectives → 0-100 score) |
| `claim_strength` | Detect claims on the 7-level strength ladder and flag unauthorised strengthening |
| `calibrate_style` | Learn an author voice profile (9 dimensions) from existing body text |
| `score_style_text` | Score how close new text is to that author profile (0-100) |
| `verify_citation` | Verify the authenticity of a single DOI (Crossref, key-free) |
| `verify_claim` | Claim verification: search for evidence, then judge SUPPORTED / PARTIAL / UNSUPPORTED |
| `verify_reference_list` | Batch-verify the DOIs in a reference list, returning valid / invalid |
| `paper_metadata` | Fetch title / authors / year / journal / abstract via Crossref |
| `citation_graph` | Fetch citation counts and references via OpenAlex |
| `download_paper_pdf` | Locate and download an open-access PDF via OpenAlex OA |
| `scout_topic` | Topic scouting: multi-source aggregation + dedupe + scored ranking |
| `scout_compare` | Side-by-side comparison of several topics (ordered by hit count, descending) |
| `rag_answer` | Retrieval-augmented QA (local template synthesis, no LLM dependency) |
| `rag_sources` | Retrieve and rank RAG sources only (by citation count, descending) |
| `find_code_for_paper` | Find code / datasets for a paper (HuggingFace / Zenodo) |
| `link_papers_to_code` | Link a body of topic-relevant papers to code / datasets in bulk |

### Review and verification line (10, of which 3 are compatibility aliases)

| Tool | What it does |
| --- | --- |
| `run_panel` | Multi-perspective peer-review panel (7 seats, including Devil's Advocate + an editorial synthesis) |
| `validate_review_intake` | Fail-closed review-intake validation (authorisation / conflicts of interest / external services) |
| `select_reporting_guidelines` | Pick reporting guidelines by study design and audit coverage (date-stamped) |
| `validate_claims_evidence` | Claim / evidence alignment matrix (ALIGNED / PARTIAL / UNSUPPORTED) |
| `verify` | claim → source verification: parse claims and citation anchors, emit gate_refuse |
| `gate_2_5` | Integrity gate Stage 2.5: between code generation and execution |
| `gate_4_5` | Integrity gate Stage 4.5: between results and the paper / the deliverable |
| `run_gates` | Run both gates 2.5 and 4.5 in one call |
| `request_bypass` | Fail-closed bypass: released only with a valid justification |
| `build_passport` | Material Passport: a per-run artifact of record (experiment provenance + claim audit + negative evidence) |

Compatibility aliases (behaviourally identical to the entries above, kept for older clients):

| Alias | Equivalent to |
| --- | --- |
| `review_panel_intake` | `validate_review_intake` |
| `select_guidelines` | `select_reporting_guidelines` |
| `claims_evidence_matrix` | `validate_claims_evidence` |

### Delivery line (2)

| Tool | What it does |
| --- | --- |
| `get_deliverables` | List the deliverables of a task (figures / data / source / reports) |
| `package_submission` | Package submission material as a zip (+ cover letter + checklist) |

### Scientific data line (5)

| Tool | What it does |
| --- | --- |
| `science_list_dbs` | List the available scientific databases, optionally filtered by the 7 domains |
| `science_search` | Keyword search in a given database |
| `science_fetch` | Fetch one full record by record ID |
| `science_cross_lookup` | Query the same keyword across several databases jointly |
| `science_batch_search` | Run the same query across several databases in parallel and summarise |

### Journal fit and disciplines (3)

| Tool | What it does |
| --- | --- |
| `journal_fit` | Score how well a paper fits a target journal / conference (field / genre / method / structure / compliance) |
| `list_disciplines` | List every registered discipline (the `domain` parameter is reserved and currently not used for filtering) |
| `get_discipline` | Fetch the full v2 configuration of a given discipline |

### MCP resources (2)

| URI | Kind | Contents |
| --- | --- | --- |
| `science://databases` | Static resource | The full list of 46 connectors + the 7 domains |
| `science://databases/{domain}` | Parameterised template | The connector list within a single domain |

### Known limitations

- `science_fetch` nominally covers all 46 databases, but **only `uniprot` currently implements a `fetch` callback**; the other 45 are usable through `science_search` only.
- The `domain` parameter of `list_disciplines` is currently ignored; filtering by domain is not implemented.
- The `depth` parameter of `citation_graph` currently expands only one level.

---

## Discipline coverage (1538 disciplines)

`sciforge/disciplines/` ships a paper-support registry for **1538 disciplines**, using zero-registration auto-discovery: adding a discipline means adding a module file in that package that declares a module-level `Discipline` instance (or a `Discipline` dataclass subclass). The discovery mechanism picks it up on its own, with no registry code to change.

### Distribution by category

The `category` field uses Chinese subject-category naming, with 14 distinct values and these **exact counts**:

| Category | Count | Category | Count |
| --- | --- | --- | --- |
| 理学 (Sciences) | 87 | 军事学 (Military Science) | 5 |
| 工学 (Engineering) | 56 | 农学 (Agricultural Science) | 4 |
| 医学 (Medicine) | 30 | 历史学 (History) | 4 |
| 交叉学科 (Interdisciplinary) | 23 | 教育学 (Education) | 4 |
| 法学 (Law) | 12 | 经济学 (Economics) | 3 |
| 文学 (Literature) | 11 | **Total** | **1538** |
| 哲学 (Philosophy) | 9 | | |
| 管理学 (Management) | 7 | | |
| 艺术学 (Arts) | 6 | | |

> ⚠️ Counting caveat: `list_by_category()` matches on **substrings**, so `list_by_category("理学")` also matches `管理学` (whose literal string contains "理学") and returns more than the exact count above. Use exact equality when counting categories, or de-duplicate the result yourself.

### Contribution forms

The `contribution_forms` field takes 10 fixed values (`sciforge/disciplines/contribution_forms.py`):

| Contribution form | Disciplines including it | Contribution form | Count |
| --- | --- | --- | --- |
| 论文 (Paper) | 1538 (100%) | 报告 (Report) | 27 |
| 数据集 (Dataset) | 95 | 艺术作品 (Artwork) | 7 |
| 软件与代码 (Software & Code) | 49 | 文学作品 (Literary work) | 5 |
| 学术专著 (Monograph) | 41 | 译文 (Translation) | 4 |
| 专利 (Patent) | 35 | 教案与教材 (Teaching material) | 3 |

Distribution by number of forms: 37 disciplines with 1, 182 with 2, 42 with 3; no discipline declares more than 3.

### Preferred paper databases

The `databases` field has 22 distinct values, with a long-tail distribution:

| Database | Disciplines | Database | Disciplines |
| --- | --- | --- | --- |
| OpenAlex | 255 | DOAJ | 11 |
| Crossref | 213 | HuggingFace | 6 |
| CNKI | 162 | Ensembl | 4 |
| arXiv | 94 | ChEMBL | 2 |
| 万方 (Wanfang) | 68 | UniProt | 2 |
| PubMed | 63 | ClinVar | 1 |
| Semantic Scholar | 58 | Expression Atlas | 1 |
| Zenodo | 58 | Human Protein Atlas | 1 |
| Europe PMC | 31 | RCSB PDB | 1 |
| PubChem | 16 | Reactome | 1 |
| GEO | 13 | | |
| bioRxiv | 12 | | |

### Field reference

| Field | Type | Meaning |
| --- | --- | --- |
| `name` | `str` | Primary key, lower-case snake_case |
| `aliases` | `tuple[str, ...]` | Aliases and search keywords (Chinese and English) |
| `paper_types` | `dict[str, tuple[str, ...]]` | Genre → section structure |
| `citation_style` | `str` | Primary citation style |
| `reporting_standards` | `dict[str, str]` | Reporting-standard routing (design / topic → standard name) |
| `conventions` | `tuple[str, ...]` | Writing conventions (theorem environments, notation, figures, terminology) |
| `key_venues` | `tuple[str, ...]` | Representative top journals / conferences |
| `units_and_formulas_notes` | `tuple[str, ...]` | Unit and formula notes |
| `paper_capable` | `bool` | Whether papers are the primary output |
| `contribution_forms` | `tuple[str, ...]` | Contribution forms (may hold several values) |
| `tools` | `tuple[str, ...]` | Software / instruments / method platforms used in the discipline |
| `category` | `str` | Subject category |
| `databases` | `tuple[str, ...]` | Preferred paper sources / databases |

### Python API

```python
from sciforge.disciplines import (
    DISCIPLINES,                 # dict[str, Discipline], keyed by lower-case name
    list_disciplines,            # all disciplines, sorted by name
    get_discipline,              # look up by name or alias (case-insensitive)
    list_by_category,            # filter by category (substring match)
    list_by_contribution_form,   # filter by contribution form
    list_by_tool,                # filter by tool
    list_by_database,            # filter by preferred database
)

len(DISCIPLINES)                    # 1538
d = get_discipline("machine_learning")
d.contribution_forms               # ('论文', '软件与代码', '数据集')
list_by_contribution_form("专利")   # disciplines that can produce patents
list_by_tool("PyTorch")            # disciplines bound to PyTorch
list_by_database("PubMed")         # disciplines that prefer PubMed
```

Field-level detail and the guide to extending the registry live in [docs/disciplines.md](./docs/disciplines.md).

---

## Scientific data connectors (46 connectors)

`sciforge/science/` reaches **46 connectors across 7 domains** of public scientific databases, all accessed through public interfaces; 3 of them optionally read environment variables to unlock extra capability.

| Domain | Count | Connector ids |
| --- | --- | --- |
| `literature` | 12 | `openalex`, `arxiv`, `biorxiv`, `crossref`, `europepmc`, `pubmed`, `semantic-scholar`, `unpaywall`, `core`, `opencitations-coci`, `cnki`, `wanfang` |
| `proteins` | 6 | `uniprot`, `rcsb-pdb`, `pdbe`, `alphafold`, `interpro`, `sifts` |
| `chemistry` | 6 | `chembl`, `pubchem`, `chebi`, `bindingdb`, `gtopdb`, `surechembl` |
| `genomics` | 7 | `ensembl`, `eutils`, `mygene`, `myvariant`, `clinvar`, `dbsnp`, `gnomad` |
| `pathways` | 5 | `biogrid`, `intact`, `kegg`, `opentargets`, `reactome` |
| `omics` | 6 | `arrayexpress`, `depmap`, `expression-atlas`, `geo`, `gtex`, `hpa` |
| `datasets` | 4 | `zenodo`, `doaj`, `openaire`, `huggingface` |
| **Total** | **46** | |

### Optional environment variables

| Variable | Connectors affected | When unset |
| --- | --- | --- |
| `CORE_API_KEY` | `core` | Returns an empty result, no error |
| `CNKI_API_URL` | `cnki` | Returns an empty result, no error |
| `WANFANG_API_URL` | `wanfang` | Returns an empty result, no error |
| `SCI_FORGE_OFFLINE=1` | all | Forces offline mode; used by tests and CI |

Per-connector endpoints, returned fields and known gaps live in [docs/connectors.md](./docs/connectors.md).

---

## Relationship to the desktop edition (two repositories)

This repository, `sci-forge`, is the **MCP edition** (core library + server). It forms a two-repository pair with the sibling **desktop edition** `sciforge-desktop` (a PySide6 client).

| Dimension | `sci-forge` (this repo, MCP edition) | `sciforge-desktop` (desktop edition) |
| --- | --- | --- |
| Role | Core library + MCP stdio server | Desktop GUI client + local agent tools |
| Provides | 75 MCP tools, 2 MCP resources, 1538 disciplines, 46 connectors | 6 local agent tools, session storage, GUI shell |
| Python dependency | `mcp>=1.29.0` | `PySide6>=6.6` |
| Command | `sci-forge` | `sciforge-desktop` |
| Communication role | The callee (stdio server) | The caller (JSON-RPC 2.0 over stdio) |

### Collaboration rule: shared core, changed together by default

- **Shared core.** Both repositories target one domain model: the discipline registry, the connector catalogue, tool semantics, and the `.sci-forge` storage layout. The desktop edition consumes core capabilities over the MCP protocol rather than duplicating an implementation.
- **Changed together by default.** Any change that alters a tool signature, tool semantics, a return structure, a discipline field, or the storage layout is **expected to land in both repositories in the same change**, so the two sides cannot drift apart.
- **Exceptions for single-repository changes.** Changes confined to the UI layer, GUI interaction, packaging, or platform concerns may land on one side only; such a PR must state in its description that it "does not affect the MCP contract".

> Observation (inventory date 2026-09-26): as of that date the two repositories had no code-level synchronisation mechanism — `sciforge-desktop`'s `pyproject.toml` does not declare a dependency on `sci-forge`, and its `core/` directory is an empty placeholder, so core consistency currently rests on convention rather than mechanism. Establishing that mechanism is a follow-up work item.

---

## Roadmap

The following are **planned directions**; they are not scheduled and carry no committed dates.

### Available today

- A registry of 1538 disciplines (the Discipline v2 field system)
- 46 scientific database connectors across 7 domains
- 75 MCP tools + 2 MCP resources
- Closed loops along six lines: reproduce / write / research / review-and-verify / deliver / scientific data
- 268 pytest cases (the v2 regression baseline)
- Key-free core paths with optional LLM enhancement

### In progress

- Documentation: bilingual READMEs, user-facing `docs/`, contribution and security processes, CI and release automation
- Landing the two-repository contract (the desktop edition consuming the MCP core)

### Planned

- Growing `science_fetch` coverage from 1/46 to the mainstream databases
- Normalising discipline tool names (of 597 distinct tool strings today, 504 occur exactly once — the naming is visibly fragmented)
- Domain filtering for `list_disciplines` and multi-level expansion for `citation_graph`
- Bringing coverage and static-typing configuration (`ruff` / `mypy` / `coverage`) into CI as gates
- The PyPI publishing flow

### Explicitly out of scope

- Never depending on a closed-source commercial search service as the default backend
- Never blocking a tool call when no LLM is configured

---

## Development and testing

```bash
git clone https://github.com/liudongyan13701205717-source/sci-forge.git
cd sci-forge
pip install -e ".[reproduce,dev]"

# Full test suite (runs offline: literature and reproduction use stub data)
SCI_FORGE_OFFLINE=1 python -m pytest tests/ -q

# Collect only, do not execute
SCI_FORGE_OFFLINE=1 python -m pytest tests/ -q --collect-only

# One file only
SCI_FORGE_OFFLINE=1 python -m pytest tests/test_science_api.py -q
```

CI (`.github/workflows/ci.yml`) runs `ruff` lint plus the pytest command above on Python 3.11 / 3.12 / 3.13.

Current test layout: 26 test files and 268 cases collected by pytest, covering unit tests across the four lines, an end-to-end stdio test that spawns a real MCP server, and scientific data connector tests.

The contribution flow, branch conventions, commit-message conventions and the two-repository sync rule live in [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## Contributing

- **Report a bug / request a feature**: use [GitHub Issues](https://github.com/liudongyan13701205717-source/sci-forge/issues) or one of the templates under `.github/ISSUE_TEMPLATE/`.
- **Security vulnerability**: **do not** open a public issue; follow the private reporting channel in [SECURITY.md](./SECURITY.md).
- **Submit code**: fork → branch → PR. Before submitting, make sure `SCI_FORGE_OFFLINE=1 python -m pytest tests/ -q` is green.
- **Join the discussion**: everyone must follow [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) (Contributor Covenant v2.1).
- **Sponsorship and support**: see [.github/SUPPORT.md](./.github/SUPPORT.md).

---

## License

[Apache License 2.0](./LICENSE) — Copyright 2026 liudongyan13701205717

<sub>This is an independently developed educational / research project, with no association with the SciForge trademark. Copyright in all external databases and APIs remains with their respective rights holders; this project accesses their data only through public interfaces.</sub>
