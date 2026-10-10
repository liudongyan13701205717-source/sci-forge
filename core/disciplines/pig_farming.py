"""养猪业学科论文支持：猪育种/营养/健康/行为/福利体裁、ASAS 引用样式与养猪业记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pig_farming",
    aliases=("pig_farming", "养猪业", "猪生产", "pig production", "猪育种", "swine breeding", "生猪养殖", "swine farming", "猪营养", "swine nutrition", "猪健康", "pig health"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与生产问题）", "methodology（试验设计与饲养方案）", "results（生产性能/肉质数据）", "discussion（生产与经济意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（猪场与案例）", "analysis（生产流程与问题）", "results（改进措施效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（育种/营养/健康综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7（国内期刊遵循 GB/T 7714）",
    reporting_standards={"subject_info": "猪只信息（品种、日龄、体重、性别）须报告", "feed_formula": "日粮配方与营养水平须完整报告", "husbandry": "饲养管理（栏位、密度、温度、通风）须给出", "health": "健康/免疫状态与药物使用须说明", "statistics": "统计模型与样本量须给出"},
    conventions=("体重与日龄用 kg 与 d（天数）表示", "饲料配方按风干基 % 报告", "料肉比 FCR 单位 kg/kg 须给出", "免疫程序（疫苗种类、剂量、日龄）须完整", "生产性能指标（ADG、DMI、FCR、窝均断奶数）标准化"),
    key_venues=("Journal of Animal Science", "Swine Health and Production", "Animal Production Science", "Journal of Applied Animal Welfare Science", "Asian-Australasian Journal of Animal Sciences"),
    units_and_formulas_notes=("体重 kg；日龄 d；ADG g/d", "DMI kg/d；FCR kg/kg", "温度 ℃；湿度 %RH；氨 NH3 ppm", "公式用 amsmath；能量代谢与遗传模型须明确"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Visor", "PIGscan", "Genomax", "AfiFarm PigVision", "PigPro", "SwineScan", "Herdmate", "PIGdata", "PLINK", "GCTA", "GEMMA", "Illumina PorcineHD", "Illumina Porcine65K SNP", "DeLaval ProSow", "DeLaval Porcine Feeding", "Vaisala Environmental Sensors", "Honeywell Sensors", "Fera Animal Health", "Zoetis Porcine Diagnostics", "R/Bioconductor"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
