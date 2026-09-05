from __future__ import annotations

import urllib.parse
from sciforge.science import register as _register
from sciforge.science.connector import Connector
from sciforge.science.http import http_get_json, http_get_text


def _uniprot_search(query, limit):
    params = {"query": query, "format": "json", "size": str(limit)}
    url = "https://rest.uniprot.org/uniprotkb/search?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", []):
        acc = r.get("primaryAccession", "")
        desc = r.get("proteinDescription", {}).get("recommendedName", {}).get("fullName", {})
        title = desc.get("value", acc) if isinstance(desc, dict) else acc
        out.append({
            "id": acc,
            "title": title,
            "year": None,
            "doi": None,
            "url": f"https://www.uniprot.org/uniprotkb/{acc}" if acc else "",
            "venue": r.get("organism", {}).get("scientificName", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _uniprot_fetch(id, fmt=""):
    if fmt == "fasta":
        url = f"https://rest.uniprot.org/uniprotkb/{id}.fasta"
        text = http_get_text(url)
        return {"format": "fasta", "data": text or ""}
    url = f"https://rest.uniprot.org/uniprotkb/{id}.json"
    data = http_get_json(url)
    return {"format": "json", "data": data}


def _rcsb_pdb_search(query, limit):
    q = urllib.parse.quote(query)
    url = f"https://search.rcsb.org/rcsbsearch/v2/query?json=%7B%22query%22%3A%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22full_text%22%2C%22parameters%22%3A%7B%22value%22%3A%22{q}%22%7D%7D%2C%22return_type%22%3A%22entry%22%7D"
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("result_set", []):
        ident = r.get("identifier", "")
        out.append({
            "id": ident,
            "title": f"PDB {ident}",
            "year": None,
            "doi": None,
            "url": f"https://www.rcsb.org/structure/{ident}" if ident else "",
            "venue": "RCSB PDB",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _pdbe_search(query, limit):
    url = f"https://www.ebi.ac.uk/pdbe/api/search/pdb/entry_details/{urllib.parse.quote(query)}"
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for pdb_id, info in data.items():
        title = info.get("title", "") if isinstance(info, dict) else ""
        out.append({
            "id": pdb_id,
            "title": title or f"PDB {pdb_id}",
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/pdbe/entry-files/download/pdb{pdb_id}.ent",
            "venue": "PDBe",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _alphafold_search(query, limit):
    url = f"https://alphafold.ebi.ac.uk/api/prediction/{urllib.parse.quote(query)}"
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for entry in data:
        out.append({
            "id": entry.get("entryId", ""),
            "title": entry.get("uniprotDescription", ""),
            "year": None,
            "doi": None,
            "url": entry.get("pdbUrl", ""),
            "venue": entry.get("organismScientificName", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _interpro_search(query, limit):
    params = {"search": query, "page_size": str(limit)}
    url = "https://www.ebi.ac.uk/interpro/api/search/all/?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", []):
        meta = r.get("metadata", {})
        out.append({
            "id": meta.get("accession", ""),
            "title": meta.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/interpro/entry/{meta.get('accession','')}",
            "venue": meta.get("source_database", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _sifts_search(query, limit):
    url = f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{urllib.parse.quote(query)}"
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for pdb_id in data:
        out.append({
            "id": pdb_id,
            "title": f"SIFTS mapping {pdb_id}",
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{pdb_id}",
            "venue": "PDBe SIFTS",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def register():
    specs = [
        ("uniprot", "UniProt", "UniProt protein knowledgebase", _uniprot_search),
        ("rcsb-pdb", "RCSB PDB", "Protein Data Bank", _rcsb_pdb_search),
        ("pdbe", "PDBe", "Protein Data Bank in Europe", _pdbe_search),
        ("alphafold", "AlphaFold DB", "AlphaFold protein structures", _alphafold_search),
        ("interpro", "InterPro", "Protein families and domains", _interpro_search),
        ("sifts", "PDBe SIFTS", "Structure integration with function", _sifts_search),
    ]
    for cid, name, desc, fn in specs:
        c = Connector(id=cid, name=name, domain="proteins", description=desc, search=fn)
        if cid == "uniprot":
            c.fetch = _uniprot_fetch
        _register(c)
