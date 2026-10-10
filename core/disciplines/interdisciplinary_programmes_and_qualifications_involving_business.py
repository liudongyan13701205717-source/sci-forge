"""商务类跨学科项目与学位：研究、案例、综述体裁，APA 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interdisciplinary_programmes_and_qualifications_involving_business",
    aliases=(
        "interdisciplinary_programmes_and_qualifications_involving_business",
        "商务类跨学科项目与学位",
        "Business Interdisciplinary Programmes",
        "Business Degree",
        "Business Degree Programme",
        "Cross-disciplinary Business",
        "商业跨学科",
        "商科跨学科",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（案例分析）",
            "results（发现）",
            "discussion（启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "PRISMA（系统综述）",
        "k2": "CIPP（项目评价）",
        "k3": "AACSB（商科教育认证）",
    },
    conventions=(
        "跨学科课程模块与先修关系须明示",
        "样本与数据来源须报告",
        "统计口径与货币单位统一",
        "跨机构比较须说明背景差异",
        "伦理审查编号须标注",
    ),
    key_venues=(
        "Academy of Management Learning & Education (AMLE)",
        "Journal of Management Education",
        "Academy of Management Journal",
        "Strategic Management Journal",
        "Journal of International Business Education",
    ),
    units_and_formulas_notes=(
        "金额用统一币种并标注年份",
        "统计量报告 M/SD/SE/CI",
        "效应量给出 Cohen's d 或 r",
        "样本量与失效率须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Stata", "SPSS", "R", "Python（Pandas）", "MATLAB", "Excel", "Tableau", "Power BI", "NVivo", "Mplus", "Harvard Business Publishing Case Services", "Bloomberg Terminal", "Wind 资讯", "Moodle", "Canvas LMS", "SAP Learning", "Blackboard", "RefWorks", "Zotero", "EndNote"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
