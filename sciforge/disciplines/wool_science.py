"""羊毛科学学科论文支持：羊毛纤维性能与纺织加工体裁、APA 引用样式与纤维测试记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wool_science",
    aliases=("wool science", "羊毛科学", "羊毛学", "羊毛纤维", "毛纺科学",
             "wool technology", "wool fibre science", "毛纺织"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与科学问题）",
            "materials and methods（样品、测试与统计）",
            "results（纤维性能与加工数据）",
            "discussion（纤维机理与应用）",
            "references",
        ),
        "material_study": (
            "abstract",
            "introduction",
            "materials and methods（试样、处理与表征）",
            "results（表征与性能数据）",
            "discussion（材料机理）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Textile Research Journal 多用 SAGE 规范）",
    reporting_standards={
        "fibre_testing": "纤维测试须报告标准（IWTO/ASTM/ISO）、试样与条件",
        "statistical": "须报告重复数、统计方法与显著性",
        "instrumentation": "须报告仪器型号、校准与测量条件",
        "conditioning": "须报告调湿条件（温度、相对湿度）",
    },
    conventions=(
        "羊毛纤维细度用 μm（micron）报告",
        "纤维长度用 mm（Hauteur/Barbe）报告",
        "纤维强度用 cN/tex 或 N/ktex 报告",
        "测试调湿条件（20°C, 65% RH）须注明",
        "羊毛品种与产地须交代",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of the Textile Institute",
        "Wool Technology and Sheep Breeding",
        "Journal of Industrial Textiles",
        "Fibers and Polymers",
        "Cellulose",
    ),
    units_and_formulas_notes=(
        "细度用 μm；长度用 mm；强度用 cN/tex 或 N/ktex",
        "线密度用 tex/dtex；含油脂率用 %",
        "回潮率用 %；调湿条件用 °C / % RH",
        "色差用 ΔE；白度用 %",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("OFDA 纤维细度仪", "Laserscan 激光纤维细度仪", "ATLAS 羊毛强度测试仪", "Almeter 纤维长度仪", "显微投影仪 (microprojection)", "扫描电镜 (SEM)", "FTIR 光谱仪", "近红外光谱仪 (NIR)", "羊毛油脂测定仪", "含水率测定仪", "电子天平", "pH 计", "纤维梳理机 (carding machine)", "USTER 纺织测试仪", "色差仪 (colorimeter)", "ImageJ", "R", "SAS", "SPSS", "羊毛分级软件"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
