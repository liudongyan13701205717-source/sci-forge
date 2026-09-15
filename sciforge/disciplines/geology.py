"""地质学与地球物理论文支持：岩石学、构造地质、地震学。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geology",
    aliases=("geology", "geophysics", "petrology", "geochemistry", "tectonics",
             "sedimentology", "seismology", "地质", "地球物理", "岩石", "构造"),
    paper_types={
        "research": ("abstract", "introduction", "geological setting", "methods", "data", "interpretation", "discussion", "conclusions", "references"),
        "survey": ("abstract", "introduction", "survey design", "data", "interpretation", "references"),
        "fieldwork": ("abstract", "introduction", "fieldwork", "observations", "analysis", "interpretation", "references"),
    },
    citation_style="AGU 或 Geological Society of America",
    reporting_standards={
        "samples": "样品编号、SI/GPS 坐标、岩性描述须全；照片含比例尺",
        "dating": "测年方法与 2σ 误差须给（Ar-Ar/U-Pb/C14）； decay常数写明",
        "analysis": "主量/微量元素给 XRF/ICP-MS 仪器与检出限",
        "seismic": "震相拾取又包含惊变与内部混乱度",
        "mapping": "地质图含比例尺、坐标系、图例；剖面给深度比例",
    },
    conventions=(
        "地层单位给正式名称与代号；沉积环境柱状图示",
        "仪器型号与实验室名字写全",
        "薄片照片给定性薄片鉴定；矿物代号用为标准缩写",
        "采样策略的统计意义须有统计意义说明",
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
        "同位素给 δ 值与标准物质（SMOW/PDB）",
        "热史模拟给温度-时间路径与置信区间",
    ),
)