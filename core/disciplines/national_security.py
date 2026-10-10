"""国家安全学科论文支持：安全研究/威胁评估体裁、情报分析规范与政策记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="national_security",
    aliases=("national_security", "国家安全", "公共安全", "国土安全",
             "战略研究", "威胁评估", "情报分析", "风险管理"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与安全议题）",
            "methodology（分析方法与数据源）",
            "results（威胁评估与政策结果）",
            "discussion（政策含义与局限）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景与冲突进程）",
            "analysis（结构与因果分析）",
            "results（案例结论）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（安全理论综述）",
            "evidence synthesis（多案例证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式（政治学与安全研究常用）",
    reporting_standards={
        "threat_assessment": "威胁评估遵循情报分析规范",
        "case_study": "案例研究遵循安全研究案例规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "policy_analysis": "政策分析遵循政策分析规范",
        "decision_making": "决策分析遵循结构化分析技术（IARPA）",
    },
    conventions=(
        "数据敏感性与来源须注明",
        "案例研究方法与样本须说明",
        "政策建议须分层并给出优先级",
        "时间/地点须精确",
        "不确定性与假设须报告",
    ),
    key_venues=(
        "Journal of Strategic Studies",
        "International Security",
        "Security Studies",
        "Strategic Studies Quarterly",
        "Terrorism and Political Violence",
    ),
    units_and_formulas_notes=(
        "案例研究须报告案例数与选样",
        "公式用 amsmath；风险方程须编号",
        "百分比/概率须定义",
        "时间序列须定义时间尺度",
        "空间数据须注明精度",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Maltego", "Palantir Gotham", "Tableau", "Gephi", "ArcGIS", "OpenRefine", "Python（Pandas/NumPy）", "R", "Stata", "Microsoft Excel", "Neo4j", "Twitter/X API", "Google Earth", "威胁情报平台", "LaTeX", "Zotero", "Tableau Public", "ScreamingFrog（OSINT 工具）", "加密与保密软件", "Shodan（OSINT 扫描）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "SAGE", "JSTOR"),
)
