"""人类社会学科论文支持：社会结构/文化认同/社会变迁研究体裁、ASA/APA 引用样式与社科问卷口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="human_society",
    aliases=(
        "human_society",
        "人类社会",
        "社会研究",
        "Human Society",
        "Sociology of Society",
        "Social Studies",
        "社区研究",
        "Cultural Studies",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ASA/APA 样式（作者-年份；社会学经典常用 ASA 规范）",
    reporting_standards={"k1": "问卷研究须报告抽样与信度", "k2": "访谈研究须报告知情同意与匿名化", "k3": "综述须报告检索与筛选流程"},
    conventions=(
        "样本量与抽样框须说明",
        "统计量给出 M/SD 与 CI",
        "访谈编码须报告信度",
        "文化/地域案例须注明语境",
        "伦理与知情同意须说明",
    ),
    key_venues=(
        "American Sociological Review",
        "British Journal of Sociology",
        "Society",
        "Social Problems",
        "American Anthropologist",
    ),
    units_and_formulas_notes=(
        "比率/比例给出百分比口径",
        "问卷量表给出制式",
        "时间序列注明起止年份",
        "统计量给出 M/SD 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "R", "Python", "NVivo", "Atlas.ti", "MAXQDA", "Excel", "Tableau", "Power BI", "MATLAB", "Qualtrics", "SurveyMonkey", "Endnote", "RefWorks", "Mendeley", "CGSS", "CHNS", "UCinet", "NepGraph"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "Google Scholar", "JSTOR"),
)
