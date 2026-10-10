"""养羊业学科论文支持：羊种培育/羊群营养/放牧管理/繁殖体裁、APA 引用样式与畜牧学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sheep_farming",
    aliases=("sheep_farming", "养羊业", "养羊", "羊群管理", "sheep production",
             "sheep husbandry", "小反刍动物养殖"),
    paper_types={
        "research": (
            "abstract",
            "introduction（羊群问题与生产情境）",
            "methods（品种、饲养、样本与统计设计）",
            "results（生长、繁殖、胴体重与效益数据）",
            "discussion（生产意义与推广建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（羊场/牧场案例）",
            "analysis（管理与技术评估）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（羊业理论谱系）",
            "evidence synthesis（跨研究证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份，畜牧学主流）",
    reporting_standards={
        "nutrition": "营养试验遵循 AAFCO/INRA 消化与代谢试验规范",
        "animal_welfare": "动物福利评估遵循 BSAIA 与 WAO 标准",
        "genetics": "育种研究须报告谱系、表型数据与遗传力（heritability）",
    },
    conventions=(
        "品种、年龄、性别与生理阶段（羔、育肥、繁殖）须完整披露",
        "饲养管理按采食量（kg DM/d）、饮水、放牧时间与转群频率报告",
        "繁殖指标（配种率、产羔率、存活率）须按胎次与产羔数分组报告",
        "胴体品质按屠宰重、屠宰率、出肉率与肉色/大理石纹评分报告",
        "试验须报告样本量、随机化方案与重复次数",
    ),
    key_venues=(
        "Small Ruminant Research",
        "Animal",
        "Animal Production Science",
        "Livestock Science",
        "Animal Production and Science",
    ),
    units_and_formulas_notes=(
        "体重用 kg；采食量用 kg DM/d；产奶量用 L/d",
        "生长曲线拟合用 Gompertz 或 Logistic 模型；报告 AIC/BIC",
        "遗传力 h²、遗传相关与 BLUP 估计须报告标准误",
        "饲料配方用 DM 与 CP 百分比；经济分析用元/羊或元/kg 胴体",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Excel", "R", "RStudio", "SPSS", "SAS", "Pasturely", "Flocknote", "Stockman", "SheepSync", "AgriLogiEYE", "SmartSheep", "LivestockID", "EID Reader", "Pregnancy Ultrasound Scanner", "Weighbridge", "Electric Fence Controller", "PastureMeter", "Fertility Test Kit", "Rotational Grazing Planner", "DAF Sheep Management"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
