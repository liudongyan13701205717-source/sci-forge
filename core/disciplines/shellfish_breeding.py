"""贝类养殖学科论文支持：贝类育种/苗种繁育/水质管理/遗传选择体裁、APA 引用样式与水产学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="shellfish_breeding",
    aliases=("shellfish_breeding", "贝类养殖", "贝类育苗", "贝类育种",
             "shellfish aquaculture", "bivalve aquaculture", "贝类遗传育种"),
    paper_types={
        "research": (
            "abstract",
            "introduction（贝类问题与养殖情境）",
            "methods（品种、苗种、水质与遗传设计）",
            "results（生长、存活、遗传与产量结果）",
            "discussion（养殖意义与推广建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（养殖区/养殖系统案例）",
            "analysis（生态与生产管理评估）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（贝类水产学理论谱系）",
            "evidence synthesis（跨研究证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份，水产学主流）",
    reporting_standards={
        "water_quality": "水质监测遵循 FAO 水产养殖水质指南（温度、盐度、DO、pH、氨氮）",
        "genetics": "遗传育种须报告谱系、选择强度与遗传力（heritability）",
        "disease": "疾病研究遵循 OIE/WOAH 水产动物诊断标准",
    },
    conventions=(
        "贝类物种按学名（斜体）与俗名标注；报告采样点、水深与底质类型",
        "生长指标按壳长、壳高、鲜重、干重分组报告，含采样时间",
        "遗传选择须报告谱系深度、家系数、遗传力 h² 与选择响应",
        "病害须按病原学名、发病期与发病率报告",
        "试验须报告样本量、随机化与重复组数（n ≥ 30）",
    ),
    key_venues=(
        "Aquaculture",
        "Aquaculture International",
        "Marine Biology",
        "Aquaculture Research",
        "Reviews in Aquaculture",
    ),
    units_and_formulas_notes=(
        "水温用 °C；盐度用 PSU；溶解氧用 mg/L；pH 用无量纲值",
        "生长用 mm/月 或 g/月；体长/体高用 mm；重量用 g",
        "遗传力 h² 用 0-1 无量纲；选择响应 R = i × h² × σp",
        "发病率用 %；存活率用 %；样本量 n ≥ 30；置信区间 95%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Excel", "R", "RStudio", "SPSS", "SAS", "ArcGIS", "QGIS", "Google Earth Pro", "Geneious", "PCR Thermal Cycler", "DNA Sequencer", "BD FACSCanto Flow Cytometer", "HydroBios Water Quality Monitor", "UV Sterilizer", "Microscope", "Spectrofluorometer", "Aqualogic", "FishBase", "Sea-Farm", "AcquaNet"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
