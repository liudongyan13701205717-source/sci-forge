"""考古学论文支持：田野发掘、年代测定、物质文化分析、聚落形态研究。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="archaeology",
    aliases=("archaeology", "archeology", "考古学", "考古"),
    paper_types={
        "research": ("abstract", "introduction", "site description", "methods", "analysis", "discussion", "conclusions", "references"),
        "report": ("abstract", "introduction", "stratigraphy", "finds", "analysis", "interpretation", "conclusions", "references"),
        "theoretical": ("abstract", "introduction", "theory", "case studies", "discussion", "conclusions", "references"),
    },
    citation_style="Chicago/Turabian（编号），如 [1] 或 (Author Year)",
    reporting_standards={
        "stratigraphy": "地层学须报告发掘单位（探方/层位）、土壤描述（Munsell色卡）与层序关系",
        "dating": "测年结果须报告校正曲线（Calib/INTCAL20）、误差范围（1σ/2σ）与实验室编号",
        "artifact": "器物分析须报告采样位置、数量、类型学分期与制作工艺",
        "survey": "调查须报告调查方法（系统/采样）、区域面积与采集密度",
    },
    conventions=(
        "地层编号用大写罗马数字（Ⅰ/Ⅱ/Ⅲ）；遗迹编号用 F+数字（F1/F2）",
        "探方编号用 T+坐标（T12N-E5）；方向用 N/E/S/W",
        "器物描述用标准术语（口沿/腹/底/耳/足）；测量单位用 cm",
        "图版编号用 Pl. + 数字；地图比例尺和指北针必须标注",
        "遗址名称用正式地名（中英文），括注省县",
    ),
    key_venues=(
        "Journal of Archaeological Science",
        "American Antiquity",
        "Journal of Field Archaeology",
        "Antiquity",
        "World Archaeology",
    ),
    units_and_formulas_notes=(
        "长度用 cm/m；重量用 g/kg；容积用 mL/L",
        "碳14年代用 BP（Before Present, 1950）或 cal BP/cal BC",
        "地层深度用 m below surface (mbs)；海拔用 m asl",
    ),
)
