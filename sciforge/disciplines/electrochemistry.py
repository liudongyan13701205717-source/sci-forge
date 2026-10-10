"""电化学学科论文支持：电化学原理、电池技术与电催化研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="electrochemistry",
    aliases=(
        "electrochemistry", "电化学", "电化学技术",
        "electrochemical technology", "电化学技术",
        "battery technology", "电池技术",
        "electrocatalysis", "电催化",
        "electrochemical energy", "电化学能源",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（电化学问题与背景）",
            "methodology（实验设计、电极制备、测试方法）",
            "results（电化学性能与机理分析）",
            "discussion（技术改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "electrochemical analysis（电化学分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（技术对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="ACS",
    reporting_standards={
        "electrode": "电极材料、尺寸与制备方法须完整",
        "electrolyte": "电解液组成与浓度须注明",
        "testing": "测试方法须注明（CV、EIS、充放电等）",
    },
    conventions=(
        "电位用 V 表示（vs. RHE 或 Ag/AgCl）",
        "电流密度用 mA/cm² 表示",
        "比容量用 mAh/g 表示",
        "能量密度用 Wh/kg 表示",
        "功率密度用 W/kg 表示",
    ),
    key_venues=(
        "Journal of the Electrochemical Society",
        "Electrochimica Acta",
        "Journal of Power Sources",
        "Batteries & Supercaps",
        "ACS Applied Materials & Interfaces",
        "Nature Energy",
    ),
    units_and_formulas_notes=(
        "电位用 V 表示（vs. RHE 或 Ag/AgCl）",
        "电流密度用 mA/cm² 表示",
        "比容量用 mAh/g 表示",
        "能量密度与功率密度用 Wh/kg、W/kg 表示"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Excel", "SPSS", "Origin", "EC-Lab", "Gamry Framework", "CH Instruments", "Autolab", "Zahner", "Ivium", "Pine Research", "Potentiostat", "Solartron 1260 FRA", "PGSTAT30", "Neware Battery Cycler", "Arbin LCT", "XRD (X-ray Diffraction)", "SEM (Scanning Electron Microscope)"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "ACS Publications"),
)
