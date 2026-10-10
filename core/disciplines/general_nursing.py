"""护理学科论文支持：护理评估、干预、临床护理研究与管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="general_nursing",
    aliases=("general_nursing", "护理学", "基础护理", "General nursing", "Clinical nursing", "护士教育", "护理管理"),
    paper_types={
        "research": ("abstract", "introduction（护理问题与研究目的）", "methodology（设计、对象、护理干预与测量）", "results（干预效果与护理结局）", "discussion（护理意义与局限）", "references"),
        "case_study": ("abstract", "introduction", "case description（患者与护理背景）", "analysis（护理评估与干预）", "results（护理结局）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（护理理论与循证综述）", "evidence synthesis（循证证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份），护理期刊主流采用",
    reporting_standards={"randomized": "护理干预试验遵循 CONSORT", "qualitative": "质性护理研究遵循 COREQ", "cohort": "队列研究遵循 STROBE", "meta_analysis": "Meta 分析遵循 PRISMA", "guideline": "护理实践指南遵循 AGREE II"},
    conventions=("护理诊断用 NANDA-I 分类", "疼痛按 NRS/PG 分级", "跌倒用 Morse 评分", "压疮用 Braden 评分", "伦理与知情同意必须报告"),
    key_venues=("International Journal of Nursing Studies", "Journal of Advanced Nursing", "中华护理杂志", "护理学杂志", "Nursing Outlook"),
    units_and_formulas_notes=("疼痛用 NRS 0-10", "生命体征按标准单位（mmHg/℃/bpm）", "药物剂量用 mg/kg 或 μg/kg·min", "评分量表分数无单位", "住院天数用 d"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("NANDA-I 护理诊断库", "PICO 检索工具", "CINAHL", "Nursing & Allied Health Collections", "R（统计分析）", "SPSS", "Stata", "RevMan", "OpenClinica（病例管理）", "REDCap", "GraphPad Prism", "Excel", "Origin", "Meta-analysis（CMA）", "JBI（循证评价）", "OvidSP", "NOC 护理结局分类", "NIC 护理干预分类", "COSMIN 量表评价工具", "SQUIRE 2.0 质控评价清单"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref", "CNKI", "Cochrane Library", "Web of Science"),
)
