"""水产养殖学科论文支持：养殖模式、水质、病害与营养体裁、农学口径与采样规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mariculture",
    aliases=("mariculture", "水产养殖", "水产养殖学", "水产畜牧学", "水族养殖",
             "Aquaculture", "Pisciculture", "Marine Farming", "海水养殖", "淡水养殖"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、产业需求与科学问题）",
            "materials and methods（材料与方法：养殖系统、组别与采样）",
            "results（生长、存活、水质与生化结果）",
            "discussion（讨论、生态影响与产业启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（养殖场描述与工艺流程）",
            "analysis（模式改进与效益核算）",
            "results（成活率/产量/成本）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（物种、模式与饲料综述）",
            "evidence synthesis（产量与环境影响证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（水产生态学与营养学主流）",
    reporting_standards={
        "sampling": "水质与生化采样须遵循 ISO 5667（水样采集）与 ASTM 系列",
        "animal_welfare": "涉及动物实验须遵循 ARRIVE 2.0 与所在国动物福利法规",
        "feed_trial": "饲料试验须遵循 NASEM/NRC 鱼类营养试验指南",
        "growth_metrics": "生长报告须给出体长、体重、比生长率 SGR",
        "environmental_impact": "涉环境影响须报告排放（氨氮、总磷、沉积物）",
    },
    conventions=(
        "温度、pH、DO、盐度单位须统一并标注测量深度与时间",
        "动物实验数据须以均值 ± 标准差或标准误报告，n 值明确",
        "饲料配方须给出蛋白质/脂肪/纤维含量与来源",
        "养殖模式须区分网箱、池塘、RAS（循环水）、工厂化",
        "统计检验须说明方法（ANOVA/t/Kruskal-Wallis）与显著性水平",
    ),
    key_venues=(
        "Aquaculture",
        "Aquaculture International",
        "Reviews in Aquaculture",
        "Journal of Applied Ichthyology",
        "Aquaculture Research",
        "Fish & Shellfish Immunology",
    ),
    units_and_formulas_notes=(
        "生长率 SGR = (ln W_f - ln W_i) / (t_f - t_i) × 100（%/day）",
        "特定生长比 SGR 常用单位：%/day；存活率 SR = N_surv / N_initial × 100%",
        "饲料系数 FCR = 投喂总量 / 生长量",
        "溶解氧 DO 单位：mg/L；盐度单位：PSU（实用盐度单位）",
        "水质参数：温度（℃）、pH（无单位）、氨氮 NH₃-N（mg/L）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("溶解氧仪（YSI ProDSS）", "pH 计（Hanna/Hach）", "氨氮/亚硝酸盐分析仪", "分光光度计", "气相色谱仪（GC-MS）", "高效液相色谱（HPLC）", "实时荧光 PCR（qPCR）", "显微镜与图像分析（ImageJ）", "水产饲料制粒机", "循环水养殖系统（RAS）", "网箱养殖平台", "养殖环境控制软件（Aquabotix AquaView）", "鱼类体型测量（Digital Caliper/Fisometrics）", "MatLab 与 R（生长模型）", "Python（数据分析）", "SAS/SPSS（统计）", "水质自动监测仪（In-Situ）", "生物标志物分析平台（MassSpec）", "遥感与 GIS（养殖区规划）", "视频行为分析（DeepLabCut/EthoVision）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "Aquaculture Journals"),
)
