"""奶酪生产学科论文支持：乳制品加工/发酵工艺/成熟风味/食品安全体裁与引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cheese_production",
    aliases=(
        "cheese production",
        "cheesemaking",
        "dairy processing",
        "cheese aging",
        "cheese ripening",
        "奶酪生产",
        "干酪制造",
        "乳制品加工",
        "奶酪熟成",
        "奶酪熟制",
        "奶酪工艺",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（乳制品加工与工艺问题）",
            "materials and methods（原料乳、发酵剂、工艺参数）",
            "results（理化、微生物与感官数据）",
            "discussion（工艺-品质关系与机制）",
            "conclusions",
            "references",
        ),
        "process": (
            "abstract",
            "introduction",
            "processing conditions（发酵、凝乳、脱水、成熟）",
            "product characterization（理化、微生物、感官）",
            "shelf life and safety（货架期与安全性）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "taxonomy（按工艺/奶酪种类分类）",
            "flavor chemistry",
            "challenges and outlook",
            "references",
        ),
    },
    citation_style="LWT 样式（Elsevier 编号）；食品微生物引用 Food Microbiology",
    reporting_standards={
        "milk": "原料乳须报告乳脂率、乳蛋白率与菌落总数",
        "starter": "发酵剂须标注菌种（保加利亚乳杆菌等）与接种量",
        "coagulation": "凝乳过程须报告 pH、温度、凝乳酶用量与凝固时间",
        "ripening": "成熟条件须记录温度、湿度、时长与翻转频率",
        "salt": "盐分须区分表面加盐与乳清盐水盐，报告 wt%",
    },
    conventions=(
        "原料乳须报告乳脂率、乳蛋白率与菌落总数",
        "发酵剂须标注菌种（保加利亚乳杆菌等）与接种量",
        "凝乳过程须报告 pH、温度、凝乳酶用量与凝固时间",
        "成熟条件须记录温度、湿度、时长与翻转频率",
        "盐分须区分表面加盐与乳清盐水盐，报告 wt%",
    ),
    key_venues=(
        "LWT - Food Science and Technology",
        "Food Research International",
        "Journal of Dairy Science",
        "International Journal of Food Microbiology",
        "Journal of Food Engineering",
        "Journal of Food Protection",
    ),
    units_and_formulas_notes=(
        "乳脂率、乳蛋白率用 %；菌落总数用 CFU/mL",
        "pH 无量纲；温度用 ℃；时间为 min/h 或天",
        "盐分用 wt%；成熟期用 天/月",
        "风味化合物须报告定量方法与检出限",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Foss Babcock 乳脂分析仪", "Foss MilkAnalyzer 乳成分仪", "SCILaser 激光乳分析仪", "乳品高温灭菌器", "发酵剂发酵罐", "凝乳切割器", "乳清分离离心机", "成熟室温湿度控制器", "奶酪真空包装机", "超声波清洗机", "冷冻干燥机", "红外光谱仪（FTIR）", "流式细胞仪", "乳蛋白分析仪", "膜浓缩装置", "乳清蛋白分离器", "乳清脱盐膜", "奶酪切刀与压模", "成熟室温湿度记录仪", "奶酪质构仪（TA.XT Plus）"),
    category="工学",
    databases=("PubMed", "OpenAlex", "Crossref", "CNKI"),
)
