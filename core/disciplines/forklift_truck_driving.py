"""叉车操作学科论文支持：叉车安全操作、物流叉车使用与叉车维护。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="forklift_truck_driving",
    aliases=("forklift_truck_driving", "forklift", "叉车操作", "叉车驾驶", "叉车安全", "叉车维护", "物流叉车", "叉车安全操作"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methods（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA（作者-年份）",
    reporting_standards={
        "operation": "操作须遵循 ISO 23598 安全标准",
        "training": "培训须遵循国家标准培训规范",
        "maintenance": "维护须遵循制造商维护规范",
        "safety": "安全须遵循国家标准安全规范"
    },
    conventions=(
        "标准引用须用 GB/T 或 ISO 标准号",
        "安全规程须用标准化术语",
        "设备型号须用标准化名称",
        "操作参数须用标准化单位",
        "维护周期须用标准化时间间隔"
    ),
    key_venues=(
        "Ergonomics",
        "Safety Science",
        "Industrial Safety and Health",
        "Human Factors and Ergonomics International",
        "Journal of Safety Research"
    ),
    units_and_formulas_notes=(
        "载重用 kg",
        "速度用 km/h",
        "加速度用 m/s²",
        "角度用 °（度）",
        "力用 N 或 kN"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Forklift simulation software", "Forklift training simulator", "Forklift operational safety software", "Forklift operational maintenance software", "Forklift driver training system", "Forklift safety equipment", "Forklift inspection checklist", "Forklift hazard identification", "Forklift load stability calculator", "Forklift ergonomics assessment", "Forklift training course materials", "Forklift safety assessment tool", "Forklift maintenance schedule", "Forklift operator certification", "Forklift inspection software", "Forklift operational performance monitoring", "Forklift hazard analysis", "Forklift training and certification", "Forklift safety training", "Forklift operational safety equipment"),
    category="工学",
    databases=("OpenAlex", "Crossref"),
)
