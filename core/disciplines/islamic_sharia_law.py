"""伊斯兰沙里亚法学科论文支持：教法、金融合规与比较法研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="islamic_sharia_law",
    aliases=("islamic sharia law", "沙里亚法", "伊斯兰法", "教法", "伊斯兰金融法", "伊斯兰教法", "Sharia", "伊斯兰经济"),
    paper_types={
        "research": ("abstract", "introduction（背景与教法问题）", "methodology（教法分析、比较法与数据）", "results（教法裁定与实务发现）", "discussion（合规与政策含义）", "references"),
        "case_study": ("abstract", "introduction", "case description（金融工具、合同或裁决）", "analysis（教法分析与合规评估）", "results（合规结论与整改）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（伊斯兰法学流派）", "evidence synthesis（多源证据汇总）", "future directions", "references"),
    },
    citation_style="伊斯兰法学引注（含阿拉伯语原典、罗马数字页码）与 Bluebook 混合",
    reporting_standards={
        "k1": "教法证据给出处（《古兰经》、圣训或学者著述）",
        "k2": "合规裁定给 shariah board 依据",
        "k3": "比较法学派差异说明",
    },
    conventions=(
        "阿拉伯原文与罗马数字转写并列",
        "学者与学派（哈乃斐、马立克、沙斐仪、罕百里）标注",
        "教法术语首次出现给阿拉伯原文与英文解释",
        "合规裁定给依据与理由",
        "金融工具按伊斯兰银行惯例分析"
    ),
    key_venues=(
        "International Journal of Islamic Finance",
        "Islamic Economic Studies",
        "Journal of Islamic Economics and Finance",
        "Journal of Islamic Accounting and Business Research",
        "Islamic Financial Management Review"
    ),
    units_and_formulas_notes=(
        "利率禁令（riba）与合规收益口径区分",
        "利润与亏损分担（Mudarabah、Musharakah）给份额",
        "合规工具给合同类型与要素",
        "样本地区与年份给出"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Al-Islam.org", "Bayyinah", "Tanzil.net", "Sunnah.com", "Dar al-Ifta", "AAOIFI Standards", "Islamic Research and Training Institute", "World Bank Lexeme", "World Bank IFC", "Islamic Window", "ResearchGate", "Al-Mada Publishing", "Zaynab Library", "Islamic Web", "Reflex（法律文本分析）", "Zotero", "NVivo", "SPSS", "Bluebook 引注插件", "LaTeX"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "LexisNexis", "Westlaw International", "HeinOnline", "Google Scholar", "JSTOR"),
)
