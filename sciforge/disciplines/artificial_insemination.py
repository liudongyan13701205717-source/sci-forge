"""Artificial insemination (of animals) 学科论文支持：家畜人工授精/繁殖管理/精液冷冻保存/遗传评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="artificial_insemination",
    aliases=(
        "artificial_insemination",
        "artificial insemination (of animals)",
        "家畜人工授精",
        "畜禽人工授精",
        "动物繁殖学",
        "animal reproduction",
        "livestock insemination",
        "精液冷冻保存",
        "semen cryopreservation",
        "生殖技术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（动物来源、精液采集与评价、处理与保存、授精操作）",
            "results（精液品质、授精与受胎率、后代数据）",
            "discussion",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technical developments",
            "comparisons across species",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 7th（畜牧兽医药学期刊通用）",
    reporting_standards={
        "animal_use": "涉及实验动物须报告伦理审批、动物数量、饲养管理与福利条件",
        "semen_handling": "精液采集、稀释、冷冻程序（液氮温度、解冻方法）须完整记录",
        "sperm_analysis": "精液品质评价须报告 CASA 参数（活力、速度、浓度）与样本量",
        "breeding_performance": "受胎率/产犊率须报告统计口径（分母、观察天数）与置信区间",
        "genetics": "分子标记/基因分型须报告引物、平台与基因型确认方法",
    },
    conventions=(
        "家畜用学名斜体（Bos taurus、Sus scrofa domesticus）；品种缩写首次出现时给出全称",
        "精液参数首次出现给出符号与单位：活力 %、VSL μm/s、浓度 ×10⁶/mL、pH、渗透压 mOsm/kg",
        "受胎率/产犊率用百分数并附样本量 n 与 95% CI；比较结果报告 P 值与效应量",
        "统计软件与版本须注明；模型（如混合线性模型）给出完整公式",
        "表格：物种/品种/处理/样本量/均值±SD 或中位数(IQR) 列齐全；正文不重复表格全部数据",
        "冷冻保存用 −196 ℃ 或 液氮 表述一致；单位 SI",
    ),
    key_venues=(
        "Theriogenology",
        "Journal of Animal Reproduction and Development",
        "Reproduction in Domestic Animals",
        "Animal Reproduction Science",
        "Journal of Dairy Science",
        "Journal of Animal Science",
    ),
    units_and_formulas_notes=(
        "温度用 ℃ 或 K；液氮温度记 −196 ℃",
        "浓度 ×10⁶/mL；体积 μL/mL；速度 μm/s",
        "受胎率 = 受胎数/配种次数 × 100%，公式须给出并统一口径",
        "混合线性模型用 REML 估方差分量；公式按 nomenclature 标注",
        "P 值报告格式：P < 0.001 / P = 0.032（三位有效数字）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("IVOS CASA", "HOSPEM CASA", "MotaLab", "FlowJo", "BD FACS Diva", "GeneMarker", "Geneious Prime", "BioNumerics", "Thermo Fisher MALDI Biotyper", "Thermo Fisher STRbase", "Applied Biosystems QuantStudio", "Zeiss LSM 900", "Olympus CellSens", "LabVIEW", "IBM SPSS Statistics", "Minitab", "RStudio / R (lme4, brms)", "Python (pandas, statsmodels, NumPy)", "BCFtools", "GATK"),
    category="农学",
    databases=("OpenAlex", "PubMed", "AGRIS", "Web of Science"),
)
