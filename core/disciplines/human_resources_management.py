"""人力资源管理学科论文支持：组织行为/人才管理/绩效管理研究体裁、APA 引用样式与人才统计口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="human_resources_management",
    aliases=(
        "human_resources_management",
        "人力资源管理",
        "组织与人力",
        "Human Resource Management",
        "HRM",
        "Talent Management",
        "绩效管理",
        "Organizational Behavior",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；JAP/JOM 等 APA 规范）",
    reporting_standards={"k1": "量表研究须报告信效度", "k2": "纵向研究须报告期次与流失", "k3": "综述须报告 PRISMA 流程"},
    conventions=(
        "量表信度/效度须报告",
        "样本与抽样须说明",
        "绩效指标注明考核口径",
        "内生性问题须讨论",
        "统计量给出 M/SD 与 CI",
    ),
    key_venues=(
        "Academy of Management Journal",
        "Academy of Management Review",
        "Journal of Management",
        "Personnel Psychology",
        "Human Resource Management Journal",
    ),
    units_and_formulas_notes=(
        "绩效评分给出制式与均值",
        "员工规模注明时点",
        "流失率以百分比口径",
        "回归系数给出标准误与显著性",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "R", "Python", "MATLAB", "AMOS", "Mplus", "Excel", "NVivo", "Tableau", "Power BI", "SAP SuccessFactors", "Oracle HCM", "Workday", "Qualtrics", "Endnote", "RefWorks", "Wind 万得", "Bloomberg Terminal", "Harvard Business Review"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
