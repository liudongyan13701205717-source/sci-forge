"""期刊写作模板：主流期刊/会议的结构化模板 + 合规清单。

模板字段：
  - structure: 章节结构列表
  - abstract_style: 摘要风格
  - length_limit: 字数/页数限制
  - citation_style: 引用样式
  - sections_order: 章节顺序
  - compliance_checklist: 合规清单
"""
from __future__ import annotations

from typing import Any

# 期刊/会议模板库
VENUE_TEMPLATES: dict[str, dict[str, Any]] = {
    "Nature": {
        "structure": [
            "Title",
            "Author list",
            "Abstract (150-250 words, flowing narrative)",
            "Main text: Introduction, Results, Discussion, Methods",
            "References",
            "Supplementary Information",
        ],
        "abstract_style": "flowing narrative, single paragraph, no subheadings",
        "length_limit": "Main text ~6 pages; Abstract ≤ 250 words",
        "citation_style": "Nature numbered (sequential superscript)",
        "sections_order": ["Abstract", "Introduction", "Results", "Discussion", "Methods"],
        "compliance_checklist": [
            "Single-paragraph abstract ≤ 250 words",
            "No subheadings in abstract",
            "Methods at end of main text",
            "Data/code availability statement",
            "Author contributions statement",
            "Competing interests declaration",
        ],
        "key_features": [
            "Flowing narrative abstract",
            "Integrated figures in main text",
            "Methods at end",
            "Supplementary Information separate",
        ],
    },
    "Science": {
        "structure": [
            "Title",
            "Author list",
            "Abstract (125 words max, structured: Background, Results, Conclusion)",
            "Main text: Introduction, Results, Discussion, Materials & Methods",
            "References",
            "Supplementary Materials",
        ],
        "abstract_style": "structured (Background/Results/Conclusion), ≤125 words",
        "length_limit": "Main text ~4-5 pages; Abstract ≤ 125 words",
        "citation_style": "Science numbered",
        "sections_order": ["Abstract", "Introduction", "Results", "Discussion", "Materials & Methods"],
        "compliance_checklist": [
            "Structured abstract ≤ 125 words",
            "Data/materials availability",
            "Author contributions",
            "Funding statement",
        ],
        "key_features": [
            "Structured abstract",
            "Strict length limits",
            "Supplementary separate",
        ],
    },
    "Cell": {
        "structure": [
            "Title",
            "Author list",
            "Abstract (150 words, single paragraph)",
            "Graphical Abstract (single panel, 90mm wide)",
            "Highlights (3-5 bullet points, 85 chars each)",
            "In Brief (50 words)",
            "Main text: Introduction, Results, Discussion, STAR Methods",
            "References",
            "Supplemental Information",
        ],
        "abstract_style": "single paragraph ≤ 150 words",
        "length_limit": "Main text variable; Abstract ≤ 150 words",
        "citation_style": "Cell numbered",
        "sections_order": ["Abstract", "Highlights", "In Brief", "Introduction", "Results", "Discussion", "STAR Methods"],
        "compliance_checklist": [
            "Graphical Abstract (single panel, 90mm)",
            "3-5 Highlights (≤85 chars each)",
            "In Brief ≤ 50 words",
            "STAR Methods at end",
            "Resource availability",
            "Lead contact",
        ],
        "key_features": [
            "Graphical Abstract",
            "Highlights (3-5 bullets)",
            "STAR Methods format",
        ],
    },
    "NEJM": {
        "structure": [
            "Title",
            "Author list",
            "Structured Abstract (Background, Methods, Results, Conclusion, ≤ 250 words)",
            "Main text: Introduction, Methods, Results, Discussion",
            "References",
        ],
        "abstract_style": "structured (Background/Methods/Results/Conclusion), ≤ 250 words",
        "length_limit": "Main text ~4500 words; Abstract ≤ 250 words",
        "citation_style": "NEJM numbered (Vancouver)",
        "sections_order": ["Abstract", "Introduction", "Methods", "Results", "Discussion"],
        "compliance_checklist": [
            "PRISMA compliance for reviews",
            "Clinical trial registration",
            "Data sharing statement",
            "Funding disclosure",
        ],
        "key_features": [
            "Structured abstract mandatory",
            "PRISMA for systematic reviews",
            "Strict word counts",
        ],
    },
    "Lancet": {
        "structure": [
            "Title",
            "Author list",
            "Structured Abstract (Background, Methods, Findings, Interpretation, ≤ 250 words)",
            "Main text: Introduction, Methods, Results, Discussion",
            "References",
        ],
        "abstract_style": "structured (Background/Methods/Findings/Interpretation), ≤ 250 words",
        "length_limit": "Main text ~3500 words; Abstract ≤ 250 words",
        "citation_style": "Lancet numbered (Vancouver)",
        "sections_order": ["Abstract", "Introduction", "Methods", "Results", "Discussion"],
        "compliance_checklist": [
            "PRISMA compliance for reviews",
            "Clinical trial registration",
            "Patient consent",
            "Ethics approval",
        ],
        "key_features": [
            "Structured abstract with Interpretation",
            "Emphasis on clinical relevance",
        ],
    },
    "JAMA": {
        "structure": [
            "Title",
            "Author list",
            "Structured Abstract (Importance, Objective, Design/Setting/Participants, Main Outcomes, Results, Conclusions, Relevance, ≤ 350 words)",
            "Main text: Introduction, Methods, Results, Discussion",
            "References",
        ],
        "abstract_style": "structured (7 sections), ≤ 350 words",
        "length_limit": "Main text ~3500 words; Abstract ≤ 350 words",
        "citation_style": "JAMA numbered (Vancouver)",
        "sections_order": ["Abstract", "Introduction", "Methods", "Results", "Discussion"],
        "compliance_checklist": [
            "Structured abstract with 7 sections",
            "Clinical trial registration",
            "Data sharing",
        ],
        "key_features": [
            "7-section structured abstract",
            "Importance statement required",
        ],
    },
    "IEEE": {
        "structure": [
            "Title",
            "Author list",
            "Abstract (150-250 words, single paragraph)",
            "Index Terms",
            "Main text: Introduction, Methods, Results, Discussion, Conclusion",
            "Appendices (optional)",
            "References",
        ],
        "abstract_style": "single paragraph, 150-250 words",
        "length_limit": "Variable by conference/journal; Abstract 150-250 words",
        "citation_style": "IEEE numbered",
        "sections_order": ["Abstract", "Index Terms", "Introduction", "Methods", "Results", "Discussion", "Conclusion"],
        "compliance_checklist": [
            "Index Terms (IEEE taxonomy)",
            "Abstract 150-250 words",
            "Author affiliations",
            "Copyright notice",
        ],
        "key_features": [
            "Index Terms required",
            "Conference format common",
        ],
    },
    "ACL": {
        "structure": [
            "Title",
            "Author list (anonymized for review)",
            "Abstract (≤ 200 words)",
            "Main text: Introduction, Related Work, Method, Experiments, Conclusion",
            "Limitations (required)",
            "Ethics Statement (required)",
            "References",
            "Appendix (optional)",
        ],
        "abstract_style": "single paragraph ≤ 200 words",
        "length_limit": "8 pages + unlimited references + appendix",
        "citation_style": "ACL author-year (APA-like)",
        "sections_order": ["Abstract", "Introduction", "Related Work", "Method", "Experiments", "Conclusion", "Limitations", "Ethics Statement"],
        "compliance_checklist": [
            "Anonymized for review",
            "Limitations section required",
            "Ethics Statement required",
            "Reproducibility checklist",
        ],
        "key_features": [
            "Mandatory Limitations + Ethics",
            "Anonymized submission",
        ],
    },
    "AAAI": {
        "structure": [
            "Title",
            "Author list",
            "Abstract (≤ 250 words)",
            "Keywords",
            "Main text: Introduction, Related Work, Method, Experiments, Conclusion",
            "Acknowledgments",
            "References",
        ],
        "abstract_style": "single paragraph ≤ 250 words",
        "length_limit": "7 pages + unlimited references",
        "citation_style": "AAAI numbered",
        "sections_order": ["Abstract", "Keywords", "Introduction", "Related Work", "Method", "Experiments", "Conclusion"],
        "compliance_checklist": [
            "Keywords (3-5)",
            "Page limit strictly enforced",
        ],
        "key_features": [
            "Page limits strictly enforced",
        ],
    },
    "APA": {
        "structure": [
            "Title",
            "Author list",
            "Abstract (≤ 250 words, single paragraph)",
            "Keywords",
            "Main text: Introduction, Method, Results, Discussion",
            "References",
        ],
        "abstract_style": "single paragraph ≤ 250 words",
        "length_limit": "Variable",
        "citation_style": "APA 7th edition (author-year)",
        "sections_order": ["Abstract", "Introduction", "Method", "Results", "Discussion", "References"],
        "compliance_checklist": [
            "DOI in references",
            "Author note if applicable",
        ],
        "key_features": [
            "APA 7th edition style",
        ],
    },
}


def get_template(venue: str) -> dict:
    """获取指定期刊/会议的模板（不区分大小写）。"""
    key = venue.strip().lower()
    for k, v in VENUE_TEMPLATES.items():
        if k.lower() == key:
            return v.copy()
    return {}


def list_venues() -> list[str]:
    """返回支持的期刊/会议名称列表。"""
    return list(VENUE_TEMPLATES.keys())