from __future__ import annotations

import urllib.parse
from sciforge.science import register as _register
from sciforge.science.connector import Connector
from sciforge.science.http import http_get_json


def _biogrid_search(query, limit):
    params = {"searchNames": "true", "geneList": query, "interSpeciesExcluded": "true"}
    url = "https://webservice.thebiogrid.org/interactions?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    seen = set()
    for int_id, interactions in data.items():
        for ia in interactions:
            ident = ia.get("interactor_b", "")
            if ident and ident not in seen:
                seen.add(ident)
                out.append({
                    "id": ident,
                    "title": f"interactor {ident}",
                    "year": None,
                    "doi": None,
                    "url": f"https://thebiogrid.org/{ident}",
                    "venue": "BioGRID",
                    "authors": [],
                    "cited_by": 0,
                    "abstract": "",
                })
                if len(out) >= limit:
                    break
        if len(out) >= limit:
            break
    return out


def _intact_search(query, limit):
    url = f"https://www.ebi.ac.uk/intact/ws/search/interaction/{urllib.parse.quote(query)}?format=json"
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("data", [])[:limit]:
        out.append({
            "id": r.get("id", ""),
            "title": r.get("label", "") or r.get("id", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/intact/details/{r.get('id','')}",
            "venue": "IntAct",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _kegg_search(query, limit):
    url = f"https://rest.kegg.jp/find/genes/{urllib.parse.quote(query)}"
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for row in data[:limit]:
        line = row[0] if isinstance(row, list) else row
        parts = line.split("\t")
        if len(parts) >= 2:
            out.append({
                "id": parts[0],
                "title": parts[1],
                "year": None,
                "doi": None,
                "url": f"https://www.genome.jp/dbget-bin/www_bget?{parts[0]}",
                "venue": "KEGG",
                "authors": [],
                "cited_by": 0,
                "abstract": "",
            })
    return out


def _opentargets_search(query, limit):
    params = {"q": query, "size": str(limit)}
    url = "https://api.platform.opentargets.org/v3/graphql?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for d in data.get("data", [])[:limit]:
        out.append({
            "id": d.get("id", ""),
            "title": d.get("name", "") or d.get("symbol", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.opentargets.org/target/{d.get('id','')}",
            "venue": d.get("symbol", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _reactome_search(query, limit):
    url = f"https://reactome.org/ContentService/data/search/{urllib.parse.quote(query)}?types=Pathway&cluster=true&species=Homo%20sapiens"
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for r in data.get("results", [])[:limit]:
        out.append({
            "id": str(r.get("dbId", "")),
            "title": r.get("displayName", ""),
            "year": None,
            "doi": None,
            "url": f"https://reactome.org/content/detail/{r.get('dbId','')}",
            "venue": "Reactome",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def register():
    specs = [
        ("biogrid", "BioGRID", "Protein-protein interactions", _biogrid_search),
        ("intact", "IntAct", "Molecular interactions", _intact_search),
        ("kegg", "KEGG", "Kyoto Encyclopedia of Genes and Genomes", _kegg_search),
        ("opentargets", "Open Targets", "Target-disease associations", _opentargets_search),
        ("reactome", "Reactome", "Pathway database", _reactome_search),
    ]
    for cid, name, desc, fn in specs:
        _register(Connector(id=cid, name=name, domain="pathways",
                            description=desc, search=fn))
