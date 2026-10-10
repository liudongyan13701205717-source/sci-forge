"""酒店服务学科论文支持：客房/客房服务/设施运维研究体裁、APA 引用样式与物业服务统计口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hotel_services",
    aliases=(
        "hotel_services",
        "酒店服务",
        "客房服务",
        "Hotel Services",
        "Room Service",
        "Housekeeping",
        "Facility Management",
        "Guest Services",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；酒店服务研究常用 APA）",
    reporting_standards={"k1": "清洁度评估须给出评分量表", "k2": "能耗研究须报告计量周期", "k3": "案例须注明酒店星级与房型"},
    conventions=(
        "客房清洁标准须可检验",
        "能耗数据注明计量口径",
        "响应时长给出均值与分位数",
        "满意度评分注明制式",
        "案例须说明酒店规模",
    ),
    key_venues=(
        "International Journal of Hospitality Management",
        "Cornell Hospitality Quarterly",
        "Journal of Hospitality and Tourism Technology",
        "Asia Pacific Journal of Hospitality and Tourism",
        "Culinary Science and Hospitality Management",
    ),
    units_and_formulas_notes=(
        "能耗单位统一为 kWh",
        "响应时长以分钟计",
        "满意度以百分比报告",
        "统计量给出 M/SD 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Opera PMS", "SAP EHS", "Momentum PMS", "MISTral", "Simphony 库存", "Infor HMS", "SPSS", "Stata", "Excel", "NVivo", "Tableau", "Power BI", "Yelp 点评", "TripAdvisor 点评", "Qualtrics", "MATLAB", "Python", "R", "Endnote", "Adobe InDesign"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
