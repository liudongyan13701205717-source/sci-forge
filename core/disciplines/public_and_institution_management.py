"""公共管理与机构管理学科论文支持：治理/制度/组织管理体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="public_and_institution_management",
    aliases=("public_and_institution_management", "公共管理与机构管理", "机构管理", "公共机构", "组织管理", "非营利管理", "制度管理", "institutional management"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）", "methodology（方法设计）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（结果）", "discussion（讨论）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions（未来方向）", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"qualitative": "质性研究遵循 COREQ/SRQR 报告规范", "survey": "调查研究遵循 AAPOR 报告规范", "case_study": "案例研究遵循案例研究报告规范"},
    conventions=("治理与制度背景须交代", "组织层级与权责边界须说明", "数据来源与样本须报告", "因果识别策略须明确", "局限与推广性须讨论"),
    key_venues=("Public Administration Review", "Public Management Review", "Journal of Public Administration Research and Theory", "Administrative Science Quarterly", "Governance"),
    units_and_formulas_notes=("统计量给出 M/SD/SE/CI", "效应量用 Cohen's d 或 η²", "回归系数给出标准误与显著性", "货币用统一币种并注明年份"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "NVivo", "R", "Python（Pandas/Statsmodels）", "Excel", "Word", "PowerPoint", "Gmail", "Google Drive", "Zoom", "Slack", "Tableau", "JMP", "Minitab", "QGIS", "ATLAS.ti", "MAXQDA", "EndNote", "Zotero"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
