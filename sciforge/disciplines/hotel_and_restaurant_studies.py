"""酒店与餐厅学学科论文支持：酒店管理/餐饮运营案例与服务质量研究体裁、APA 引用样式与服务业统计口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hotel_and_restaurant_studies",
    aliases=(
        "hotel_and_restaurant_studies",
        "酒店与餐厅学",
        "酒店餐饮管理",
        "Hotel and Restaurant Studies",
        "Hospitality Management",
        "餐饮运营",
        "Hotel Operations",
        "Culinary Management",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；Int. J. of Hospitality Management 等从 APA）",
    reporting_standards={"k1": "服务质量研究须报告量表信效度", "k2": "案例研究须说明资料来源与多源验证", "k3": "综述须说明检索策略与筛选流程"},
    conventions=(
        "服务指标给出统计期与口径",
        "顾客满意度报告信度系数",
        "案例须说明匿名化处理",
        "收益指标注明币种与年份",
        "样本与测量工具须说明",
    ),
    key_venues=(
        "International Journal of Hospitality Management",
        "Cornell Hospitality Quarterly",
        "Tourism Management",
        "International Journal of Contemporary Hospitality Management",
        "Cornell Hospitality Research",
    ),
    units_and_formulas_notes=(
        "RevPAR 等指标给出口径与计算式",
        "满意度量表注明李克特制式",
        "财务比率注明会计年度",
        "统计量给出 M/SD 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "Stata", "Excel", "NVivo（访谈编码）", "Momentum 酒店 PMS", "Opera PMS", "SAP EHS", "Tableau", "Power BI", "REVEL 餐饮 POS", "Toast 餐饮系统", "MISHAWAK", "Mistral 厨房排程", "Yelp 点评数据", "TripAdvisor 点评数据", "MATLAB", "Python", "R", "Endnote", "Qualtrics"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
