"""地质学学科论文支持：岩石学、构造地质、沉积学、地层学、古生物学与地球化学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geology",
    aliases=(
        "geology",
        "地质学",
        "petrology",
        "岩石学",
        "sedimentology",
        "沉积学",
        "stratigraphy",
        "地层学",
        "tectonics",
        "构造地质",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（样品、测年与分析方法）",
            "results（岩石学、地球化学与年代学）",
            "discussion（成因与构造意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（区域地质背景）",
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
    citation_style="AGU（期刊遵循 AGU 手册或 GSA 规范）",
    reporting_standards={
        "samples": "样品编号、SI/GPS 坐标、岩性描述须全；照片含比例尺",
        "dating": "测年方法与 2σ 误差须给（Ar-Ar/U-Pb/C14）；衰变常数写明",
        "analysis": "主量/微量元素给 XRF/ICP-MS 仪器型号与检出限",
    },
    conventions=(
        "地层单位给正式名称与代号；沉积环境柱状图示",
        "仪器型号与实验室名字写全",
        "薄片照片给定性薄片鉴定；矿物代号用标准缩写（IMA 缩写）",
        "同位素给 δ 值与标准物质（SMOW/PDB）；年龄给 Ma",
        "地质图含比例尺、坐标系、图例；剖面给深度比例",
    ),
    key_venues=(
        "Earth and Planetary Science Letters",
        "Geology",
        "Journal of Petrology",
        "Journal of Geophysical Research: Solid Earth",
        "Sedimentology",
    ),
    units_and_formulas_notes=(
        "深度/长度 km；速率 mm/yr；年代 Ma 或 ka",
        "同位素给 δ 值与标准物质（SMOW/PDB/VSMOW）",
        "热史模拟给温度-时间路径与置信区间",
        "元素含量用 wt% 或 ppm；同位素比值用 ‰",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "Petrel", "GOCAD", "Kingdom", "Oasis montaj", "GeoMapApp", "Python", "MATLAB", "Surfer", "RockWorks", "偏光显微镜", "SEM/EDS 扫描电镜", "XRF 荧光光谱仪", "ICP-MS 质谱仪", "LA-ICP-MS 激光剥蚀", "地质雷达 GPR", "电阻率仪", "地震仪", "偏光显微镜（交叉正交）", "Python (NumPy/SciPy)"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
