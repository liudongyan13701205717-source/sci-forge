"""酒店、餐厅与餐饮学科论文支持：餐饮服务运营/厨房/宴会管理研究体裁、APA 引用样式与餐饮统计口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hotel_restaurants_and_catering",
    aliases=(
        "hotel_restaurants_and_catering",
        "酒店餐厅与餐饮",
        "餐饮与宴会管理",
        "Hotels Restaurants and Catering",
        "Catering Management",
        "Restaurant Management",
        "Hospitality Operations",
        "Banquet Management",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；餐饮运营研究常用 APA）",
    reporting_standards={"k1": "财务分析须说明会计期", "k2": "食品安全研究须报告检查记录", "k3": "案例须说明宴会/餐厅类型与规模"},
    conventions=(
        "毛利率/成本率注明计算式",
        "食品安全温度给出单位",
        "份量标准须可复现",
        "样本量与统计期须报告",
        "案例须说明匿名化处理",
    ),
    key_venues=(
        "International Journal of Hospitality Management",
        "Cornell Hospitality Quarterly",
        "Food Service Hospitality Journal",
        "International Journal of Contemporary Hospitality Management",
        "Culinary Science and Hospitality Management",
    ),
    units_and_formulas_notes=(
        "成本率/毛利率给出口径",
        "份量以克/毫升标注",
        "食品安全温度给出摄氏度",
        "统计量给出 M/SD 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Opera PMS", "MISTral 餐饮", "Simphony 厨房", "SAP EHS", "Momentum PMS", "MISHAWAK 宴会", "SPSS", "Stata", "Excel", "NVivo", "Tableau", "Power BI", "Yelp 点评", "TripAdvisor 点评", "Qualtrics", "MATLAB", "Python", "R", "Endnote", "Adobe InDesign"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
