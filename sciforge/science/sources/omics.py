from __future__ import annotations

import urllib.parse
from sciforge.science import register as _register
from sciforge.science.connector import Connector
from sciforge.science.http import http_get_json


def _arrayexpress_search(query, limit):
    url = f"https://www.ebi.ac.uk/biostudies/api/v1/search?query={urllib.parse.quote(query)}&pageSize={limit}"
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for h in data.get("hits", [])[:limit]:
        out.append({
            "id": h.get("accession", ""),
            "title": h.get("title", "") or h.get("accession", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/biostudies/studies/{h.get('accession','')}",
            "venue": "ArrayExpress",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _depmap_search(query, limit):
    url = f"https://depmap.org/portal/api/cell_lines?search={urllib.parse.quote(query)}"
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for cl in data.get("data", [])[:limit]:
        out.append({
            "id": cl.get("DepMap_ID", ""),
            "title": cl.get("cell_line_name", "") or cl.get("DepMap_ID", ""),
            "year": None,
            "doi": None,
            "url": f"https://depmap.org/portal/cell_line/{cl.get('DepMap_ID','')}",
            "venue": "DepMap",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _expression_atlas_search(query, limit):
    url = f"https://www.ebi.ac.uk/gxa/api/v2/search?query={urllib.parse.quote(query)}&limit={limit}"
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", [])[:limit]:
        out.append({
            "id": r.get("experimentAccession", ""),
            "title": r.get("description", "") or r.get("experimentAccession", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/gxa/experiments/{r.get('experimentAccession','')}",
            "venue": "Expression Atlas",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _geo_search(query, limit):
    params = {"db": "gds", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "gds", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        out.append({
            "id": uid,
            "title": s.get("title", "") or uid,
            "year": None,
            "doi": None,
            "url": f"https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={uid}",
            "venue": "GEO",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _gtex_search(query, limit):
    url = f"https://gtexportal.org/api/v2/gene/{urllib.parse.quote(query)}"
    data = http_get_json(url)
    if not data:
        return []
    items = data.get("data", [data]) if isinstance(data, dict) else data
    if not isinstance(items, list):
        items = [items]
    out = []
    for d in items[:limit]:
        tissue = d.get("tissueSiteDetailId", "")
        out.append({
            "id": f"{d.get('geneSymbol','')}-{tissue}",
            "title": f"{d.get('geneSymbol','')} - {tissue}",
            "year": None,
            "doi": None,
            "url": f"https://gtexportal.org/home/gene/{d.get('geneSymbol','')}",
            "venue": "GTEx",
            "authors": [],
            "cited_by": 0,
            "abstract": f"TPM: {d.get('medianTPM', '')}",
        })
    return out


def _hpa_search(query, limit):
    url = f"https://www.proteinatlas.org/api/search_download.php?search={urllib.parse.quote(query)}&format=json&limit={limit}"
    data = http_get_json(url)
    if not data:
        return []
    items = data.get("data", data) if isinstance(data, dict) else data
    if not isinstance(items, list):
        items = [items]
    out = []
    for d in items[:limit]:
        out.append({
            "id": d.get("gene", ""),
            "title": d.get("gene", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.proteinatlas.org/{d.get('gene','')}",
            "venue": "Human Protein Atlas",
            "authors": [],
            "cited_by": 0,
            "abstract": f"tissue: {d.get('tissue','')}",
        })
    return out


def register():
    specs = [
        ("arrayexpress", "ArrayExpress", "Functional genomics experiments", _arrayexpress_search),
        ("depmap", "DepMap", "Cancer dependency map", _depmap_search),
        ("expression-atlas", "Expression Atlas", "Gene expression patterns", _expression_atlas_search),
        ("geo", "GEO", "Gene Expression Omnibus", _geo_search),
        ("gtex", "GTEx", "Genotype-Tissue Expression", _gtex_search),
        ("hpa", "Human Protein Atlas", "Tissue protein expression", _hpa_search),
    ]
    for cid, name, desc, fn in specs:
        _register(Connector(id=cid, name=name, domain="omics",
                            description=desc, search=fn))
