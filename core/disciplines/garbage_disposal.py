"""废弃物处理学科论文支持：废物分类、减量化、资源化与无害化处理技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="garbage_disposal",
    aliases=("garbage_disposal", "waste management", "废弃物处理", "垃圾处理", "废物管理", "固废处理", "废物资源化", "废物分类"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "characterization": "废物特性须报告成分分析、采样方法与检测标准",
        "treatment": "处理工艺须报告工艺参数、去除效率与排放标准",
        "lifecycle": "生命周期评估须遵循 ISO 14040/14044 标准"
    },
    conventions=(
        "废物分类须遵循国家标准分类法",
        "处理量须用 t/d 或 kg 标注",
        "污染物浓度须注明单位和检测方法",
        "排放限值须引用现行环保标准",
        "能量回收效率须用百分比表示"
    ),
    key_venues=(
        "Waste Management",
        "Journal of Cleaner Production",
        "Waste Management and Research",
        "Resources, Conservation and Recycling",
        "Journal of Hazardous Materials"
    ),
    units_and_formulas_notes=(
        "废物量用 kg 或 t",
        "浓度用 mg/L 或 μg/m³",
        "处理量用 t/d",
        "回收率用 %",
        "热值用 MJ/kg"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Waste Sorting Machine", "Garbage Collection System", "Waste Disposal Equipment", "Recycling Equipment", "Composting Equipment", "Incineration System", "Landfill Management System", "Waste Treatment Plant", "Waste Recovery Equipment", "Waste Conversion Equipment", "Waste Analysis Equipment", "Waste Tracking System", "Waste Management Software", "Waste Sorting Software", "Waste Reduction Software", "Waste Treatment Software", "Waste Disposal Software", "Waste Recycling Software", "Waste Management Platform", "Waste Monitoring System"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
