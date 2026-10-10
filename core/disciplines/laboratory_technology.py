"""实验室技术学科论文支持：仪器分析、样品前处理、流程验证与检测方法学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="laboratory_technology",
    aliases=(
        "laboratory_technology",
        "实验室技术",
        "Laboratory Science",
        "Clinical Laboratory Science",
        "Medical Laboratory Technology",
        "Applied Laboratory Technology",
        "Biomedical Laboratory Technology",
        "Analytical Laboratory Technology",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（绪论）",
            "methodology（研究方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "k1": "CLSI EP05 定量检测精密度与正确度",
        "k2": "ICH Q2(R2) 分析方法验证",
        "k3": "ISO/IEC 17025 检测和校准实验室要求",
    },
    conventions=(
        "方法验证须覆盖线性、精密度、正确度、LOD/LOQ",
        "仪器使用前须进行日常性能验证",
        "样品前处理须记录回收率",
        "定量结果须标注不确定度",
        "异常值判定采用Grubbs或Dixon准则",
    ),
    key_venues=(
        "Clinical Chemistry",
        "Analytical Chemistry",
        "Analytica Chimica Acta",
        "Journal of Chromatography B",
        "TrAC Trends in Analytical Chemistry",
    ),
    units_and_formulas_notes=(
        "检测限：3σ/k（斜率）",
        "定量限：10σ/k",
        "回收率：测定值/加标值 × 100%",
        "变异系数CV：SD/mean × 100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("LabWare", "Benchling", "LabArchives", "SmartLab", "Dotmatics", "STARLIMS", "SciGenie", "Agilent 1260 Infinity II", "Waters ACQUITY UPLC", "Thermo Fisher Vanquish", "Agilent 6470 TripleTOF", "Thermo Fisher Q Exactive", "Waters Xevo G2", "Shimadzu LC-30AD", "Beckman Coulter Biomek", "Hamilton STAR", "Tecan Fluent", "Hamilton Microlab", "SPT-Lab Tecan Harmony", "Qualitas"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
