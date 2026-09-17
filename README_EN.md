# sci-forge

> SciForge — One MCP from "Idea" to "Paper Delivery": a full-pipeline research workbench.

A **fully local, self-hosted** [MCP](https://modelcontextprotocol.io) server providing end-to-end automation for the paper lifecycle:

- 🧪 **Reproduction Line** — Feed it a paper PDF, close the loop in five steps: parse → plan → generate code → sandbox run & compare → deliverables
- ✍️ **Writing Line** — Section-by-section guided paper writing, export to LaTeX / PDF / DOCX
- 🔬 **Research Line** — Ideate → select topic → multi-perspective hypothesis debate → experiment design → result spin-gate decision
- 🧭 **Research/Paper Line** — Research proposals, literature reviews, title/abstract distillation, simulated peer review, venue matching, paper polishing
- 📦 **Delivery Line** — Package every artifact (source / data / reports / figures / exports) into categorized deliverables

**Key feature: no API key required.** Literature search uses the OpenAlex unauthenticated API (covering arXiv preprints); LLM capability is an **optional enhancement** — without an LLM it automatically falls back to local templates and the whole pipeline still works.

> Independently built from public materials only; not affiliated with, and not dependent on, the official SciForge site or API.

---

## Feature Overview

| Tool | Line | Purpose |
| --- | --- | --- |
| `reproduce_paper` | Reproduction | Parse PDF → reproduction plan → generate code → sandbox run & compare → deliverables |
| `reproduce_status` | Reproduction | Query async reproduction task status & stage progress |
| `write_section` | Writing | Guided section writing (abstract/problem/…/results/references) |
| `export_document` | Writing | Export written doc to LaTeX / PDF / DOCX |
| `ideate_paper` | Research | Ideate → topic → research gap → candidate hypotheses → multi-perspective review → experiment plan |
| `inject_results` | Research | Merge real reproduction results into the paper's corresponding sections |
| `research_verdict` | Research | Result spin-gate: PROCEED / REFINE / PIVOT decision advice |
| `research_plan` | Research/Paper | Full research proposal (RQ/hypotheses/goals/contributions/methods/data/milestones/risks) |
| `literature_review` | Research/Paper | Literature review (OpenAlex key-free search: representative works/clusters/gaps/structure) |
| `auto_title_abstract` | Research/Paper | Distill title/abstract/keywords from body text |
| `peer_review` | Research/Paper | Simulated peer review (4-dimension scoring + recommendation + strengths/weaknesses/revision advice) |
| `venue_suggest` | Research/Paper | Venue/journal matching (built-in mapping library + optional LLM) |
| `paper_polish` | Research/Paper | Polish/consistency/completeness checks |
| `compare_metrics` | Research/Paper | Multi-task metric comparison table + Welch t / Mann-Whitney U significance tests |
| `check_novelty` | Research/Paper | Novelty check: search similar work and suggest candidate differentiators |
| `citation_landscape` | Research/Paper | Citation heat analysis (yearly distribution/highly-cited representatives/major venues) |
| `project_memory` | Research/Paper | Project progress ledger (milestones/status/notes timeline) |
| `prisma_review` | Research/Paper | PRISMA systematic review workflow |
| `convert_citation` | Research/Paper | Convert BibTeX to a single citation style |
| `convert_citation_all` | Research/Paper | Convert BibTeX to 6 citation styles at once |
| `revision_coach` | Research/Paper | Paper revision coach |
| `rebuttal_audit` | Research/Paper | Reviewer-comment rebuttal audit |
| `detect_style` | Research/Paper | Machine-writing style detection |
| `claim_strength` | Research/Paper | Claim strength ladder assessment |
| `calibrate_style` | Research/Paper | Author voice calibration profile |
| `score_style_text` | Research/Paper | Writing style scoring |
| `package_submission` | Delivery | Submission package (zip + Cover Letter + Checklist) |
| `review_code` | Delivery | Reproduction code static review (seed/hardcode/risk + credibility score) |
| `get_deliverables` | Delivery | List task (reproduction/writing) deliverables, categorized by type |
| `science_list_dbs` | Science Data | List available databases (filter by domain) |
| `science_search` | Science Data | Single-database search |
| `science_fetch` | Science Data | Fetch record by ID |
| `science_cross_lookup` | Science Data | Cross-database joint query |

### Full Pipeline: From Idea to Paper

```
ideate_paper（ideate/hypotheses/experiment plan）
      │
      ▼
reproduce_paper ──► reproduce_status（async polling, five-step loop）
      │
      ├────────────────────────────┐
      ▼                            ▼
research_verdict（PROCEED/REFINE/PIVOT）   write_section（write each section）
      │                                   │
      ▼                                   ▼
inject_results（merge experiment data into results）      export_document（LaTeX/PDF/DOCX）
      │                                   │
      └──────────────► get_deliverables（deliver all artifacts）
```

---

## Quick Start

> 👉 **Install in 3 minutes, then call tools directly in conversation (standard MCP tool calls — no commands/files):**
> See [**MCP_QUICKSTART.md**](./MCP_QUICKSTART.md).
>
> For a more detailed usage guide, end-to-end examples and FAQs see [**USAGE.md**](./USAGE.md).

### Installation

Requires Python ≥ 3.10.

```bash
# First-time install (simplest):
pip install "git+https://github.com/liudongyan13701205717-source/sci-forge.git"

# Or clone locally and install (also get the source):
git clone https://github.com/liudongyan13701205717-source/sci-forge.git
cd sci-forge
pip install -e .            # minimal install (MCP core only)

# For the reproduction line, install runtime deps (recommended):
pip install -e ".[reproduce,dev]"
```

After install you get the `sci-forge` command; register it directly as a local MCP (**no** `PYTHONPATH` / `cwd` needed — this is a standard portable config):

```jsonc
{
  "mcp": {
    "sci-forge": { "type": "local", "command": ["sci-forge"], "enabled": true }
  }
}
```

**Verify installation**:

```bash
sci-forge --version                     # prints version (also --help usage)
python -m pytest tests/ -q              # run built-in tests, should be all green
```

---

## Real Usage Examples

### 1. Have the MCP write a paper

```text
paper_id = "demo"
write_section(paper_id, "abstract",   "Write an abstract for 'Lightweight Inference on Edge Devices', topic=inference speed optimization", "markdown")
write_section(paper_id, "problem",    "Problem definition: latency and energy bottlenecks of edge-device inference", "markdown")
write_section(paper_id, "modeling",   "Modeling: lightweight networks and quantization schemes", "markdown")
write_section(paper_id, "solution",   "Solution: combined pruning/distillation/quantization strategy", "markdown")
write_section(paper_id, "results",    "Experimental setup and evaluation metrics", "markdown")
write_section(paper_id, "references", "References", "markdown")

export_document(paper_id, "pdf")      # produces demo/doc.pdf + doc.tex + doc.html
```

### 2. Ideate a research topic

```text
ideate_paper("Lightweight interpretable methods for large language models", "my_proj")
# Returns: research gaps, candidate hypotheses, multi-perspective review (novelty/rigor/feasibility weighted), experiment plan
```

### 3. Reproduce a paper and inject results

```text
tid = reproduce_paper("path/to/paper.pdf")["task_id"]
# Poll reproduce_status(tid) until done

research_verdict(tid)             # PROCEED/REFINE/PIVOT based on experiment results
inject_results("my_proj", tid)    # write real metric tables + convergence plots into my_proj's results section

get_deliverables(tid)             # get all reproduction deliverables
```

### 4. Full research/paper pipeline (no key, agent writes directly)

```text
ideate_paper(topic, paper_id)          # topic selection & gaps
research_plan(topic, paper_id)         # research proposal
literature_review(topic, paper_id)     # literature review
# agent follows WRITING_PROTOCOL and uses write_section to fill complete body text (no LLM config)
auto_title_abstract(paper_id)          # distill title/abstract/keywords
peer_review(paper_id)                  # simulated review, revise per feedback
paper_polish(paper_id, "completeness") # completeness check
paper_polish(paper_id, "grammar")      # language polish
venue_suggest(topic, paper_id)         # submission advice
export_document(paper_id, "pdf")       # final export
```

> Quickly start a writable paper project: `python scripts/agent_write_paper.py <paper_id> --topic "..."`.

---

## Papers & Templates

SciForge ships discipline-aware paper templates and writing scaffolds:

- **60 disciplines** (`sciforge/disciplines/`) — each discipline declares its paper genres, section structures, citation style, reporting standards, writing conventions, key venues, and units/formulas notes. The registry auto-discovers new discipline modules — zero registration needed.
- **Journal writing templates** (`sciforge/venue/`) — venue-specific templates plus journal-fit matching (`venue_suggest`).
- **Section scaffolds** (`sciforge/write/templates/`) — per-section guidance used by `write_section`.
- **Reproduction protocol** (`sciforge/reproduce/`) — five-step closed loop with code generation, sandbox harness, and static code review.

### Example Papers

**Example A — A full paper from scratch (edge inference):**

```text
paper_id = "edge-inference"
write_section(paper_id, "abstract",   "Abstract for lightweight edge inference paper", "markdown")
write_section(paper_id, "problem",    "Problem: latency/energy bottlenecks", "markdown")
write_section(paper_id, "modeling",   "Modeling: quantization + pruning", "markdown")
write_section(paper_id, "solution",   "Solution: hybrid compression strategy", "markdown")
write_section(paper_id, "results",    "Results: accuracy/latency trade-off table", "markdown")
write_section(paper_id, "references", "References", "markdown")
export_document(paper_id, "pdf")
```

**Example B — Reproduce + verdict + inject (reproducibility study):**

```text
tid = reproduce_paper("paper.pdf")["task_id"]      # five-step loop
research_verdict(tid)                                # PROCEED/REFINE/PIVOT
inject_results("repro-study", tid)                   # merge real metrics
package_submission("repro-study", "iclr")            # submission zip + cover letter
```

**Example C — Systematic review with PRISMA:**

```text
prisma_review("LLM evaluation benchmarks", "sysrev")   # PRISMA flow: identify→screen→eligibility→included
literature_review("LLM evaluation benchmarks", "sysrev")
convert_citation_all("sysrev/refs.bib")                # BibTeX → 6 styles
```

### Related Academic Work

SciForge builds on and relates to the following academic work (for further reading):

1. Anthropic. *Model Context Protocol (MCP)*. https://modelcontextprotocol.io — the protocol standard SciForge implements.
2. OpenAlex. *OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts*. https://openalex.org — the key-free literature source used by `literature_review`.
3. Page, M. J., et al. *The PRISMA 2020 statement: an updated guideline for reporting systematic reviews*. BMJ, 2021, 372:n71. — the reporting standard behind `prisma_review`.
4. Liberati, A., et al. *The PRISMA statement for reporting systematic reviews and meta-analyses of studies that evaluate health care interventions*. PLoS Medicine, 2009, 6(7):e1000100.
5. Moher, D., et al. *Preferred reporting items for systematic reviews and meta-analyses: the PRISMA statement*. Annals of Internal Medicine, 2009, 151(4):264–269.
6. Borenstein, M., et al. *Introduction to Meta-Analysis*. Wiley, 2009. — methodological background for `compare_metrics` significance tests.
7. Cohen, J. *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum, 1988. — background for effect-size and power considerations in `compare_metrics`.
8. Wager, E., & Wiffen, P. J. *Ethical issues in preparing and publishing systematic reviews*. Journal of Evidence-Based Medicine, 2011, 4(3):130–134. — ethics background for the review/rebuttal tooling.

---

## Architecture

```
sciforge/
├── server.py           # MCP stdio server, registers 53 tools + 2 resources
├── review/             # multi-perspective review panel (7 seats + Devil's Advocate + editor synthesis)
├── claims/             # claim→source verification + completeness gates + Material Passport
├── venue/              # journal writing templates + journal-fit matching
├── disciplines/        # discipline paper support registry (60 disciplines auto-discovered)
├── core/            # layout/storage/Layout + optional LLM connection layer (falls back to templates without key)
├── parse/           # paper PDF parsing (PyMuPDF)
├── reproduce/       # five-step reproduction loop: tasks/codegen/harness/pipeline + codereview static review
│   ├── codegen.py   #   extract hyperparameters + generate numpy/torch reproduction code
│   ├── harness.py   #   sandbox execution + self-healing retry + metrics/plots collection
│   └── pipeline.py  #   orchestrates five steps, produces results.json / plan.json / deliverables/
├── write/           # writing: doc(DocStore)/templates/validate
├── export/          # export: md→latex/html/docx + PDF rendering
├── research/        # research line: lit/ideate/hypoth/design/inject + stats/bench/novelty/community
│   └── (plan/survey/extract/review/venue/polish  # research/paper toolset)
├── deliver/         # delivery: get_deliverables + package_submission (submission packaging)
└── science/         # science data query: 41 connectors covering literature/proteins/chemistry/genomics/pathways/omics/datasets
```

## Science Data Query (science)

Via 41 connectors covering 7 domains of public scientific databases:

| Domain | Connectors |
| --- | --- |
| literature | openalex, arxiv, biorxiv, crossref, europepmc, pubmed, semantic-scholar |
| proteins | uniprot, rcsb-pdb, pdbe, alphafold, interpro, sifts |
| chemistry | chembl, pubchem, chebi, bindingdb, gtopdb, surechembl |
| genomics | ensembl, eutils, mygene, myvariant, clinvar, dbsnp, gnomad |
| pathways | biogrid, intact, kegg, opentargets, reactome |
| omics | arrayexpress, depmap, expression-atlas, geo, gtex, hpa |
| datasets | zenodo, doaj, openaire, huggingface |

Provides 4 MCP tools:

| Tool | Description |
| --- | --- |
| `science_list_dbs(domain?)` | List available databases, filterable by domain |
| `science_search(database, query, limit)` | Single-database search |
| `science_fetch(database, id, format)` | Fetch record by ID |
| `science_cross_lookup(query, databases?, limit)` | Cross-database joint query |

### Storage Layout

```
.sci-forge/                  # runtime artifacts, gitignored
├── env                         # local config (optional LLM endpoint), not committed
├── projects/{paper_id}/        # writing projects: doc.md / doc.pdf / doc.tex / sections/
│   └── research/               #   research artifacts: *.json + *.md (reusable/packable)
└── tasks/{task_id}/            # reproduction tasks: parse/ code/ runs/ deliverables/
```

### Optional Enhancement: LLM

Write an OpenAI-compatible endpoint into `.sci-forge/env` to enable LLM enhancement (more natural section generation/review/ideation):

```
BASE_URL=https://.../v1
API_KEY=sk-...
MODEL=...
```

When not configured, all lines automatically fall back to **local templates** — functionality is never blocked.

---

## Testing

```bash
pip install -e ".[dev]"
python -m pytest tests/ -q      # full test suite, fully offline-runnable (literature/reproduction use mock data)
```

Tests cover unit tests on all four lines + stdio end-to-end (actually spawns the MCP server and calls tools) + science data connectors.

---

## Feedback & Contributions

Bugs, feature suggestions, or any questions — welcome via **GitHub Issues**:

👉 [https://github.com/liudongyan13701205717-source/sci-forge/issues](https://github.com/liudongyan13701205717-source/sci-forge/issues)

- 🐛 **Bug**: include reproduction steps, error output (with `File "...", line ...` stack) and the relevant `paper_id`/`task_id`.
- 💡 **Feature**: describe your use case and expected behavior.
- 🤝 **Contribute**: fork and open a PR; please run `python -m pytest tests/ -q` first to ensure all green.

---

## License

[MIT](./LICENSE)

<sub>This project is an independent educational/research work, unaffiliated with SciForge and its trademarks.</sub>