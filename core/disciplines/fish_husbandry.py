"""鱼类饲养学科论文支持：饲养管理、营养需求与健康管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fish_husbandry",
    aliases=("fish_husbandry", "鱼类饲养", "fish feeding", "fish nutrition",
             "aquaculture management", "水产养殖管理", "fish health management",
             "鱼类营养", "fish welfare"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="CSE (Council of Science Editors)",
    reporting_standards={
        "nutrition": "营养试验须报告饲料配方、氨基酸/脂肪酸含量与投喂率",
        "health": "健康评估须说明疾病观察标准、样品采集方法与检测指标",
        "environment": "饲养环境须记录水温、溶解氧、pH、氨氮、亚硝酸盐等参数",
    },
    conventions=(
        "蛋白质需要量用 g/kg 饲料或 g/kg 日增重表示",
        "饲料消化率用 RD = (I-O)/I × 100% 表示",
        "饵料系数用 FCR 表示",
        "饲料营养水平用百分比(%)表示",
        "饲养密度用尾/m³ 表示",
    ),
    key_venues=(
        "Aquaculture Nutrition",
        "Aquaculture Research",
        "Aquaculture International",
        "Reviews in Aquaculture",
        "水产养殖学报",
    ),
    units_and_formulas_notes=(
        "饲料消化率 RD = (I - O) / I × 100%，I=摄入，O=排出",
        "蛋白质沉积率 PCR = 体重增量中蛋白质/摄入蛋白质 × 100%",
        "饵料系数 FCR = 投喂总量 / 体重总增量",
        "溶解氧饱和度用 % 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("水质监测仪", "溶解氧仪", "pH计", "电导率仪", "氨氮测定仪", "亚硝酸盐测定仪", "硝酸盐测定仪", "自动水质监测站", "显微镜", "电子天平", "饲料颗粒机", "增氧设备", "温控系统", "SPSS", "R (RStudio)", "Excel", "Python (Pandas)", "MATLAB", "环境因子记录仪", "饲料营养成分分析仪"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)