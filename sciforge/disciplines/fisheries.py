"""渔业学科论文支持：渔业资源管理、捕捞技术与渔业经济学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="fisheries",
    aliases=("fisheries", "渔业", "fisheries resource management", "fish stocks",
             "fishery economics", "渔业资源管理", "fish capture", "水产捕捞",
             "fisheries science"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="CSE (Council of Science Editors)",
    reporting_standards={
        "assessment": "渔业资源评估须报告模型类型、输入数据与不确定性分析",
        "survey": "渔业调查须说明调查方法、采样设计与时空范围",
        "catch": "渔获物统计须报告分类标准、数据源与统计口径",
    },
    conventions=(
        "渔获量用 t（吨）或 kg 表示",
        "捕获率用 CPUE = 渔获量/作业量 表示",
        "最大可持续产量用 MSY 表示",
        "评估种群参数须注明置信区间",
        "捕捞努力量用渔船数量×作业天数表示",
    ),
    key_venues=(
        "Fish and Fisheries",
        "Fisheries Research",
        "ICES Journal of Marine Science",
        "Marine Policy",
        "水产学报",
    ),
    units_and_formulas_notes=(
        "捕获率 CPUE = 渔获量(kg) / 作业量(船日)，单位 kg/船日",
        "最大可持续产量 MSY = r·K/4（Logistic 模型）",
        "生物产量用 t/年 表示",
        "渔船马力用 kW 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("渔业资源调查船", "声呐探测仪", "探鱼仪", "曳网采样系统", "刺网采样设备", "流刺网系统", "渔业统计软件", "R (FSA, fishmethods)", "Excel", "SPSS", "Python (Pandas)", "MATLAB", "GIS (ArcGIS/QGIS)", "AutoCAD", "SketchUp", "渔船定位系统 (AIS)", "渔情监测仪", "渔业资源评估模型 (VPA/ASAP)", "渔捞日志系统", "渔业数据管理系统"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)