"""酒店、餐厅与餐饮学科论文支持：餐饮运营/宴会/厨房管理研究体裁、APA 引用样式与食品服务统计口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hotel_restaurant_and_catering",
    aliases=(
        "hotel_restaurant_and_catering",
        "酒店餐厅与餐饮",
        "餐饮管理",
        "Hotel Restaurant and Catering",
        "Catering Management",
        "宴会管理",
        "Kitchen Operations",
        "Banquet Operations",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；餐饮管理学研究常用 APA）",
    reporting_standards={"k1": "成本研究须说明会计口径", "k2": "食品安全须报告 HACCP 检查项", "k3": "案例须说明宴会规模与类型"},
    conventions=(
        "食材成本率注明计算口径",
        "份量标准须可复现",
        "食品安全指标给出检查记录",
        "宴会案例注明人数与菜式数",
        "统计期与币种须统一",
    ),
    key_venues=(
        "International Journal of Hospitality Management",
        "Cornell Hospitality Quarterly",
        "Food Service Hospitality Journal",
        "Journal of Foodservice Business Research",
        "Culinary Science and Hospitality Management",
    ),
    units_and_formulas_notes=(
        "成本率/毛利率给出口径",
        "份量以克/毫升标注",
        "食品安全温度给出单位",
        "统计量给出 M/SD 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("MISHAWAK 宴会管理", "Mistral 餐饮", "REVEL POS", "Toast POS", "SAP EHS", "Opera PMS", "SPSS", "Stata", "Excel", "NVivo", "Tableau", "Power BI", "Kysely 餐饮库存", "ChefTo 厨房排班", "Yelp 点评", "TripAdvisor 点评", "MATLAB", "Python", "R", "Endnote"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
