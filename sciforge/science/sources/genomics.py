from __future__ import annotations

import urllib.parse
from sciforge.science import register as _register
from sciforge.science.connector import Connector
from sciforge.science.http import http_get_json


def _ensembl_search(query, limit):
    url = f"https://rest.ensembl.org/xrefs/symbol/homo_sapiens/{urllib.parse.quote(query)}?content-type=application/json"
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for r in data[:limit]:
        out.append({
            "id": r.get("id", ""),
            "title": r.get("display_name", "") or r.get("id", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ensembl.org/Homo_sapiens/Gene/Summary?g={r.get('id','')}",
            "venue": r.get("species", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": r.get("biotype", ""),
        })
    return out


def _eutils_search(query, limit):
    params = {"db": "gene", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "gene", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        out.append({
            "id": uid,
            "title": s.get("name", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ncbi.nlm.nih.gov/gene/{uid}",
            "venue": s.get("description", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": s.get("summary", ""),
        })
    return out


def _mygene_search(query, limit):
    params = {"q": query, "size": str(limit), "species": "human"}
    url = "https://mygene.info/v3/query?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for h in data.get("hits", []):
        out.append({
            "id": h.get("_id", ""),
            "title": h.get("name", "") or h.get("symbol", ""),
            "year": None,
            "doi": None,
            "url": f"https://mygene.info/v3/gene/{h.get('_id','')}",
            "venue": str(h.get("taxid", "")),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _myvariant_search(query, limit):
    params = {"q": query, "size": str(limit)}
    url = "https://myvariant.info/v1/query?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    for h in data.get("hits", []):
        out.append({
            "id": h.get("_id", ""),
            "title": h.get("_id", ""),
            "year": None,
            "doi": None,
            "url": f"https://myvariant.info/v1/variant/{h.get('_id','')}",
            "venue": "MyVariant",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _clinvar_search(query, limit):
    params = {"db": "clinvar", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "clinvar", "id": ",".join(ids), "retmode": "json"}
    summ_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summ_params)
    summ_data = http_get_json(summ_url)
    if not summ_data:
        return []
    out = []
    for uid in ids:
        s = summ_data.get("result", {}).get(uid, {})
        out.append({
            "id": uid,
            "title": s.get("title", ""),
            "year": None,
            "doi": None,
            "url": f"https://www.ncbi.nlm.nih.gov/clinvar/variation/{uid}",
            "venue": (s.get("clinical_significance") or {}).get("description", ""),
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _dbsnp_search(query, limit):
    params = {"db": "snp", "term": query, "retmode": "json", "retmax": str(limit)}
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params)
    search_data = http_get_json(search_url)
    if not search_data:
        return []
    ids = search_data.get("esearchresult", {}).get("idlist", [])
    if not ids:
        return []
    summ_params = {"db": "snp", "id": ",".join(ids), "retmode": "json"}
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
            "url": f"https://www.ncbi.nlm.nih.gov/snp/rs{uid}",
            "venue": "dbSNP",
            "authors": [],
            "cited_by": 0,
            "abstract": "",
        })
    return out


def _gnomad_search(query, limit):
    params = {"variant": query}
    url = "https://gnomad.broadinstitute.org/api/v2/variant?" + urllib.parse.urlencode(params)
    data = http_get_json(url)
    if not data:
        return []
    out = []
    variant = data.get("data", {}).get("variant", {})
    if variant:
        out.append({
            "id": variant.get("variantId", ""),
            "title": variant.get("variantId", ""),
            "year": None,
            "doi": None,
            "url": f"https://gnomad.broadinstitute.org/variant/{variant.get('variantId','')}",
            "venue": "gnomAD",
            "authors": [],
            "cited_by": 0,
            "abstract": variant.get("consequence", ""),
        })
    return out


def register():
    specs = [
        ("ensembl", "Ensembl", "Ensembl genome browser", _ensembl_search),
        ("eutils", "NCBI eutils", "NCBI Entrez utilities", _eutils_search),
        ("mygene", "MyGene.info", "Gene annotation service", _mygene_search),
        ("myvariant", "MyVariant.info", "Variant annotation service", _myvariant_search),
        ("clinvar", "ClinVar", "Clinical variant interpretations", _clinvar_search),
        ("dbsnp", "dbSNP", "Short genetic variations", _dbsnp_search),
        ("gnomad", "gnomAD", "Genome aggregation database", _gnomad_search),
    ]
    for cid, name, desc, fn in specs:
        _register(Connector(id=cid, name=name, domain="genomics",
                            description=desc, search=fn))
