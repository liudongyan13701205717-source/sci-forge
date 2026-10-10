"""动物繁殖学科论文支持：繁殖生理、遗传育种、辅助生殖、家畜改良方法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="animal_reproduction",
    aliases=(
        "animal reproduction",
        "Animal reproduction (science)",
        "动物繁殖",
        "动物繁殖学",
        "breeding",
        "animal breeding",
        "reproductive physiology",
        "辅助生殖",
        "artificial insemination",
        "胚胎移植",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（实验动物、激素处理、采样方案）",
            "results（生长、发情、妊娠、泌乳、后代表现）",
            "discussion（机制与生产意义）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction（历史脉络与关键节点）",
            "main developments（按技术或器官系统综述）",
            "challenges and perspectives",
            "references",
        ),
        "technical_report": (
            "abstract",
            "site and population",
            "methods and protocols",
            "results and comparison",
            "recommendations",
            "references",
        ),
    },
    citation_style="Vancouver 或 APA 7（农畜类期刊多采用数字编号）",
    reporting_standards={
        "animals": "物种、品种、性别、日龄、来源与饲养条件须说明；伦理审查与动物福利（3R）须披露",
        "hormonal_treatment": "激素名称、剂量、给药途径、时程须完整记录；剂量单位统一 mg/kg 或 IU",
        "sampling": "生殖激素采样时间（发情周期定位）、血清/卵泡液处理须说明",
        "statistics": "组间比较须说明方差齐性检验、事后检验（Tukey/Bonferroni）与效应量",
        "genetic_data": "基因分型须报告引物序列、PCR 条件、多态位点与 Hardy-Weinberg 平衡检验",
    },
    conventions=(
        "实验动物用拉丁学名首次出现标注；家畜品种用中文常用名并括注英文",
        "发情周期、孕产期以天为单位并给出平均值±标准差/标准误",
        "生殖激素统一缩写：FSH/LH/E2/P4/PGF2α/RELAXIN/T3/T4；单位 ng/mL 或 pg/mL",
        "遗传参数以 h²（遗传力）、r（相关性）报告，给出置信区间",
        "图表标题中英对照；图注说明缩写、样本量 n、显著性标记 *p<0.05 **p<0.01",
    ),
    key_venues=(
        "Theriogenology",
        "Animal Reproduction Science",
        "Journal of Animal Science",
        "Reproduction in Domestic Animals",
        "Animal",
        "Journal of Animal Breeding and Genetics",
    ),
    units_and_formulas_notes=(
        "体重 kg，体长 cm，卵泡直径 mm，胎畜数 头/胎",
        "激素：ng/mL 或 pg/mL；维生素：IU 或 mg/kg",
        "繁殖效率：产仔率 %，成活率 %，情期受胎率 %",
        "遗传：个体育种值 BLUP 单位 kg 或 %；遗传趋势 g/年",
        "使用 SPSS/SAS/R/Genetic Analysis Software 说明版本",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("BISACT 精子活力分析", "CASA 计算机辅助精液分析（Hamilton Thorne/IVOS）", "电刺激采精机", "超声波卵泡监测仪（VetUS）", "冷冻精子液氮罐（-196℃）", "显微操作台（Narishige）", "显微注射针（Puller/Sutter）", "IVF 培养箱（Thermo）", "程序降温仪（Cryotop/Planer）", "实时荧光定量 PCR（qPCR）仪", "流式细胞仪（性别鉴定）", "ELISA 酶标仪（Thermo/BD）", "GeneChip/基因芯片扫描", "DNA 测序仪（Illumina/MiSeq）", "BLUPF90", "RR-BLUP", "SPSS", "SAS", "R", "RStudio", "Excel", "MATLAB"),
    category="农学",
    databases=("PubMed", "Web of Science", "CNKI", "万方", "OpenAlex", "Crossref"),
)
