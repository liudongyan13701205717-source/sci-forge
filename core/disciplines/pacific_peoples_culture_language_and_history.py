"""太平洋人民文化、语言与历史学科论文支持：太平洋岛屿文化的语言学、口头历史与文化遗产数字化。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pacific_peoples_culture_language_and_history",
    aliases=("Pacific Peoples Culture, Language And History", "太平洋人民文化、语言与历史", "Pacific Studies", "Pacific Island Studies", "Pacific Linguistics", "Pacific Heritage", "Oceanian Studies", "Indigenous Pacific Studies"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（研究结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "定性民族志研究遵循OERAS（原住民研究伦理准则）", "k2": "传统知识保护遵循IRPA太平洋研究伦理", "k3": "口述历史遵循OHPA（口述历史协会）录制规范"
    },
    conventions=("使用太平洋语言ISO 639-3代码与音译体系（如Te Reo/Polynesian）", "涉及传统知识须获得社区知情同意并注明知识归属", "口述历史引用须标注讲述人、地点、日期与许可范围", "文化叙事须区分事实陈述与文化解释两种类型", "涉及殖民地/去殖民化叙事须采用原住民视角优先"),
    key_venues=("Journal of Pacific History", "Pacific Studies", "The Journal of the Polynesian Society", "Ethnohistory", "Pacific Arts Quarterly", "History New Zealand"),
    units_and_formulas_notes=("口述历史引用须标注讲述人姓名、语言代码、日期与许可", "涉及传统文化知识须注明社区归属与访问权限", "语言材料须遵循IPA转写与ISO 639-3代码双标注", "去殖民化研究须明确史料来源与研究者位置性"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("ELAN", "PRAGMA", "TEpac", "Pacific Digital Atlas", "Pacific Languages Digital Library", "Pacifica Online", "Pacific Heritage Online", "Pacific Arts Online", "Pacific Oral History Project", "Pacific Genealogy", "Museum Victoria Collections", "NZ eLibrary", "ANU Canberra Pacific Library", "Zotero", "Endnote", "LaTeX", "Overleaf", "Microsoft Word", "Google Drive", "Audacity"),
    category="历史学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
