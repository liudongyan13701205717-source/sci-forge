from __future__ import annotations

import urllib.parse
from sciforge.science import register as _register
from sciforge.science.connector import Connector
from sciforge.science.http import http_get_json


def _chembl_search(query, limit):
    params = {"q": query, "format": "json", "limit": str(limit)}
    url = "https://www.ebi.ac.uk/chembl/api/data/molecule/search?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for m in data.get("molecules", []):
        out.append({
            "id": m.get("molecule_chembl_id", ""),
            "title": m.get("pref_name", "") or m.get("molecule_chembl_id", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/chembl/compound_report_card/{m.get('molecule_chembl_id','')}",
            "venue": "ChEMBL",
            "authors": [],
            "cited_by": 0,
            "abstract": (m.get("molecule_structures") or {}).get("canonical_smiles", ""),
        })
    return out


def _pubchem_search(query, limit):
    url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/" + urllib.parse.quote(query) + "/cids/JSON"
    data = http_get_json(url)
    if not data:
        return []
    cids = data.get("IdentifierList", {}).get("CID", [])[:limit]
    if not cids:
        return []
    prop_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{','.join(map(str, cids))}/property/Title/JSON"
    prop_data = http_get_json(prop_url)
    if not prop_data:
        return []
    out = []
    for p in prop_data.get("PropertyTable", {}).get("Properties", []):
        out.append({
            "id": str(p.get("CID", "")),
            "title": p.get("Title", ""),
            "year": None,
            "doi": None,
            "url": f"https://pubchem.ncbi.nlm.nih.gov/compound/{p.get('CID','')}",
            "venue": "PubChem",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _chebi_search(query, limit):
    params = {"q": query, "maxRows": str(limit)}
    url = "https://www.ebi.ac.uk/chebi/ws/rest/search?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("List", {}).get("item", []):
        out.append({
            "id": item.get("chebiId", ""),
            "title": item.get("chebiAsciiName", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ebi.ac.uk/chebi/searchId.do?chebiId={item.get('chebiId','')}",
            "venue": "ChEBI",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _bindingdb_search(query, limit):
    params = {"q": query, "limit": str(limit)}
    url = "https://www.bindingdb.org/bind/webservices/v1/homologySearch?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("results", []):
        out.append({
            "id": item.get("ligand_id", ""),
            "title": item.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.bindingdb.org/bind/ligand/{item.get('ligand_id','')}",
            "venue": "BindingDB",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _gtopdb_search(query, limit):
    params = {"q": query, "limit": str(limit)}
    url = "https://www.guidetopharmacology.org/services/ligands?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("ligands", []):
        out.append({
            "id": item.get("ligandId", ""),
            "title": item.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.guidetopharmacology.org/GRAC/LigandDisplayForward?ligandId={item.get('ligandId','')}",
            "venue": "GuideToPharmacology",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _surechembl_search(query, limit):
    params = {"q": query, "limit": str(limit)}
    url = "https://www.surechembl.org/api/chemical?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for item in data.get("results", []):
        out.append({
            "id": item.get("surechembl_id", ""),
            "title": item.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.surechembl.org/chemical/{item.get('surechembl_id','')}",
            "venue": "SureChEMBL",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def register():
    specs = [
        ("chembl", "ChEMBL", "Bioactive drug-like compounds", _chembl_search),
        ("pubchem", "PubChem", "Chemical molecules and bioactivities", _pubchem_search),
        ("chebi", "ChEBI", "Chemical entities of biological interest", _chebi_search),
        ("bindingdb", "BindingDB", "Protein-ligand binding affinities", _bindingdb_search),
        ("gtopdb", "GuideToPharmacology", "Drug targets and ligands", _gtopdb_search),
        ("surechembl", "SureChEMBL", "Patent chemistry", _surechembl_search),
    ]
    for cid, name, desc, fn in specs:
        _register(Connector(id=cid, name=name, domain="chemistry",
                            description=desc, search=fn))
