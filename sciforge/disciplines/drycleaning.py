"""干洗学科论文支持：干洗技术、纺织品护理与化学工艺研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="drycleaning",
    aliases=(
        "drycleaning", "干洗", "干洗技术",
        "dry cleaning", "干洗",
        "textile care", "纺织品护理",
        "laundry science", "洗衣科学",
        "garment care", "服装护理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（干洗问题与背景）",
            "methodology（工艺设计、实验条件、效果评估）",
            "results（洗涤效果与面料保护）",
            "discussion（工艺优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "process analysis（工艺分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（工艺对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="ACS",
    reporting_standards={
        "solvent": "溶剂类型、浓度与用量须注明",
        "washing": "洗涤温度、时间与机器参数须记录",
        "testing": "洗涤效果测试须注明标准与方法",
    },
    conventions=(
        "温度用 °C 表示",
        "时间用 min 表示",
        "溶剂用量用 mL 或 L 表示",
        "pH 用 1-14 范围表示",
        "色牢度用 1-5 级表示",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of Textile and Apparel Technology Management",
        "Dyeing and Colouring",
        "Journal of Cleaner Production",
        "International Journal of Environmental Science and Technology",
    ),
    units_and_formulas_notes=(
        "温度用 °C 表示",
        "时间用 min 表示",
        "溶剂用量用 mL 或 L 表示",
        "pH 用 1-14 范围表示",
        "色牢度用 1-5 级表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "Excel", "SPSS", "Dry Cleaning Machine", "Washing Machine", "Pressing Machine", "Textile Testing Machine", "Colorimeter", "pH Meter", "Viscometer", "Tensile Tester", "Rubbing Tester", "Washing Tester", "Drying Machine", "Steam Press", "Solvent Recovery System", "Garment Steamer", "Fabric Analyzer", "Dye Analysis Software"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "ACS Publications"),
)
