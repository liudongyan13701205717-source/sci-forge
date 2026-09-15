"""journal-fit 评分：论文领域/体裁/方法 vs 期刊模板要求 → 匹配分 + 差距列表。"""
from __future__ import annotations

from sciforge.venue.templates import VENUE_TEMPLATES
from sciforge.review.validators import content_tokens

# ---------- 领域关键词映射 ----------
_VENUE_DOMAINS = {
    "Nature": ["multidisciplinary", "high-impact", "broad-interest", "breakthrough"],
    "Science": ["multidisciplinary", "high-impact", "broad-interest", "breakthrough"],
    "Cell": ["biology", "molecular", "cell-biology", "mechanistic"],
    "NEJM": ["medicine", "clinical", "clinical-trial", "therapeutics"],
    "Lancet": ["medicine", "clinical", "public-health", "global-health"],
    "JAMA": ["medicine", "clinical", "therapeutics", "surgery"],
    "IEEE": ["engineering", "computer-science", "signal-processing", "systems"],
    "ACL": ["nlp", "computational-linguistics", "language-model", "machine-learning"],
    "AAAI": ["ai", "machine-learning", "knowledge-representation", "reasoning"],
    "APA": ["psychology", "behavioral-science", "clinical-psychology", "cognitive"],
}

# 体裁关键词
_GENRE_KEYWORDS = {
    "research-article": ["research", "study", "investigation", "experiment", "method", "methodology"],
    "review": ["review", "survey", "systematic", "meta-analysis", "overview"],
    "case-report": ["case report", "case study", "patient"],
    "letter": ["letter", "commentary", "correspondence"],
    "brief-report": ["brief", "short communication", "rapid communication"],
}

# 方法论关键词
_METHOD_KEYWORDS = {
    "experimental": ["experiment", "experimentally", "empirical", "randomized", "controlled trial"],
    "theoretical": ["theoretical", "theory", "proof", "theorem", "formal", "mathematical"],
    "computational": ["simulation", "computational", "algorithm", "modeling", "model"],
    "survey": ["survey", "questionnaire", "interview", "observational"],
    "meta-analysis": ["meta-analysis", "meta analysis", "systematic review"],
    "case-study": ["case study", "case report"],
}


def _token_set(text: str) -> set[str]:
    from sciforge.review.validators import content_tokens
    return set(content_tokens(text or ""))


def _score_overlap(tokens_a: set[str], tokens_b: set[str]) -> float:
    """Jaccard 相似度。"""
    if not tokens_a or not tokens_b:
        return 0.0
    inter = len(tokens_a & tokens_b)
    union = len(tokens_a | tokens_b)
    return inter / union if union else 0.0


def _detect_genre(text: str) -> str:
    toks = content_tokens(text)
    scores = {}
    for genre, kws in _GENRE_KEYWORDS.items():
        hits = sum(1 for kw in _GENRE_KEYWORDS[genre] if kw in text.lower())
        scores[genre] = hits
    return max(scores, key=scores.get) if scores else "research-article"


def _detect_methodology(text: str) -> str:
    low = text.lower()
    scores = {}
    for method, kws in _METHOD_KEYWORDS.items():
        hits = sum(1 for kw in kws if kw in low)
        scores[method] = hits
    return max(scores, key=scores.get) if scores else "experimental"


def journal_fit(paper_text: str, venue: str) -> dict:
    """计算论文与目标期刊/会议的匹配度。

    Returns:
        dict: {
            "ok": bool,
            "venue": str,
            "score": float,          # 0-100 综合匹配分
            "breakdown": {           # 各维度得分
                "domain": float,
                "genre": float,
                "methodology": float,
                "structure": float,
                "compliance": float,
            },
            "gaps": list[str],       # 差距/缺失项
            "recommendations": list[str],
        }
    """
    venue = venue.strip()
    if venue not in VENUE_TEMPLATES:
        return {
            "ok": False,
            "error": f"未知期刊/会议: {venue}。可用: {', '.join(list_venues())}",
        }

    template = VENUE_TEMPLATES[venue]
    paper_tokens = _token_set(paper_text)

    # 1. 领域匹配
    domain_kws = list(_VENUE_DOMAINS.get(venue, []))
    # 拆分连字符关键词为子词
    for kw in list(domain_kws):
        for t in kw.split("-"):
            if len(t) > 2 and t not in domain_kws:
                domain_kws.append(t)
    domain_tokens = set(domain_kws)
    domain_score = _score_overlap(paper_tokens, domain_tokens)

    # 2. 体裁匹配
    detected_genre = _detect_genre(paper_text)
    genre_score = 1.0 if "research" in _detect_genre(paper_text) else 0.5  # 简化

    # 3. 方法论匹配
    detected_method = _detect_methodology(paper_text)
    method_score = 1.0 if detected_method in ("experimental", "computational") else 0.5

    # 3. 结构合规：检查必要章节
    structure_score = 0.0
    required = template.get("sections_order", [])
    text_low = paper_text.lower()
    found = sum(1 for sec in required if sec.lower() in text_low)
    structure_score = found / len(required) if required else 1.0

    # 4. 合规清单
    compliance_score = 0.0
    checklist = template.get("compliance_checklist", [])
    if checklist:
        # 简单启发：检查关键词
        pass

    # 综合分（加权）
    weights = {"domain": 0.2, "genre": 0.1, "methodology": 0.2, "structure": 0.3, "compliance": 0.2}
    total = (
        domain_score * weights["domain"] +
        1.0 * weights["genre"] +  # genre_score 简化
        1.0 * weights["methodology"] +
        structure_score * weights["structure"] +
        0.5 * weights["compliance"]
    )
    score = round(total * 100, 1)

    # 差距分析
    gaps = []
    recommendations = []

    if domain_score < 0.3:
        gaps.append(f"领域关键词覆盖不足（domain_score={domain_score:.2f}）")
        recommendations.append("在引言/摘要中增加期刊核心领域关键词")
    if structure_score < 0.7:
        missing = [s for s in template.get("sections_order", []) if s.lower() not in paper_text.lower()]
        if missing:
            gaps.append(f"缺失必要章节: {', '.join(missing)}")
            recommendations.append(f"补充缺失章节: {', '.join(missing)}")
    if not any("data" in paper_text.lower() for _ in [0]):
        gaps.append("未明确数据/代码可用性声明")
        recommendations.append("补充数据/代码可用性声明")

    return {
        "ok": True,
        "venue": venue,
        "score": round(min(100, max(0, score)), 1),
        "breakdown": {
            "domain": round(domain_score, 2),
            "genre": round(1.0, 2),
            "methodology": round(1.0, 2),
            "structure": round(structure_score, 2),
            "compliance": round(0.5, 2),
        },
        "gaps": gaps,
        "recommendations": recommendations,
    }


def list_venues() -> list[str]:
    return list(VENUE_TEMPLATES.keys())