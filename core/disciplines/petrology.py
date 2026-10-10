"""岩石学学科论文支持：岩石分类/岩相学/实验岩石学体裁、GSA/Elsevier 引用样式与岩石学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="petrology",
    aliases=("petrology", "岩石学", "实验岩石学", "岩石物理学",
             "petrography", "岩石分类", "火山岩石学", "变质岩石学",
             "igneous petrology", "igneous"),
    paper_types={
        "research": (
            "abstract",
            "introduction（地质背景与研究问题）",
            "methodology（样品采集与分析方法）",
            "results（岩相与地球化学数据）",
            "discussion（成因机制）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（矿区/剖面描述）",
            "analysis（岩相与地球化学分析）",
            "results（矿物与相态）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（成因理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="GSA/Elsevier 样式（Elsevier Numerical 或 GSA Style；矿物缩写遵循 IMA 规范）",
    reporting_standards={
        "geochemistry": "地球化学数据须报告分析方法与不确定度；全岩/微量按 IUPAC 报告",
        "petrography": "薄片描述遵循 RockJuggler/IMA 分类",
        "experimental": "实验条件（P、T、aH2O、时间）须列表",
        "fieldwork": "野外采样点须给出 GPS 与地层位",
        "dating": "定年数据遵循 ICS 年代学指南",
    },
    conventions=(
        "矿物缩写遵循 IMA 规范（Qz、Opx、Cpx、Pl、Ab 等）",
        "岩石分类按 IUGS 命名规范（Igneous/MA/Metamorphic）",
        "样品号与薄片号须统一；薄片扫描仪给分辨率",
        "微量元素用 wt./ppm；同位素用‰",
        "相图数据须给出实验条件与不确定度",
    ),
    key_venues=(
        "Journal of Petrology",
        "Lithos",
        "Contributions to Mineralogy and Petrology",
        "American Journal of Science",
        "Geochimica et Cosmochimica Acta",
        "Journal of Volcanology and Geothermal Research",
    ),
    units_and_formulas_notes=(
        "微量元素 wt./ppm；稀土（REE）用 pmol/mol",
        "同位素用‰（δ）；U-Pb 用 Ma/Ga",
        "温度用 °C 或 K；压力用 kbar/GPa",
        "样品坐标用 GPS WGS84；厚度用 mm",
        "计算式用 amsmath；公式给出反应与平衡常数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SEM-EDS（JEOL JSM-7600F）", "EPMA 电子探针（JEOL JXA-8100）", "TEM 透射电镜（JEOL JEM-2100F）", "XRD 衍射仪（Bruker D8 Advance）", "LA-ICP-MS 激光剥蚀质谱", "Raman 光谱仪（Renishaw inVia）", "FTIR 红外光谱仪", "XRF 荧光光谱仪（PANalytical Axios）", "偏光显微镜（Zeiss Axio Scope A1）", "薄片扫描仪（Karl Stoeckel）", "RockJuggler 岩相学软件", "PetScan 岩相分析软件", "Geochemist's Workbench (GWB)", "Petrotherm 相平衡软件", "Thermo-Calc 相图计算", "IsoplotR 同位素定年", "R 与 matplotlib 绘图", "高温高压合成器（Kirstka）", "ICP-OES 元素分析仪", "岩芯扫描与成像系统"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "GSA Data Repository", "MINERALOGY MAGAZINE", "GeoMakMe 热力学数据库", "PETDB 岩石数据库"),
)
