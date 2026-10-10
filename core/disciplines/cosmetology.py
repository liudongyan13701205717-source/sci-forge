"""美容学学科论文支持：皮肤科学/化妆品科学/美容医学体裁、ICD 引用样式与实验写作约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cosmetology",
    aliases=(
        "美容学", "美容学", "化妆品科学", "皮肤美容学",
        "Cosmetology", "Cosmetic Science", "Dermatology Cosmetology",
        "皮肤美容", "Beauty Science",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
        "clinical_trial": (
            "摘要",
            "引言",
            "方法",
            "结果",
            "讨论",
            "参考文献",
        ),
        "product_review": (
            "产品概述",
            "配方分析",
            "功效评估",
            "安全性评估",
            "结论",
        ),
    },
    citation_style="APA 第 7 版（化妆品科学期刊可采用 ICD 样式）",
    reporting_standards={
        "ingredients": "成分须注明 INCI 名称与 CAS 号",
        "dosage": "浓度与用量须注明单位",
        "efficacy": "功效评估须遵循标准化方法（如 ISO 16128）",
        "safety": "安全性评估须遵循相关法规（如 EU Cosmetics Regulation）",
    },
    conventions=(
        "成分名称使用 INCI 标准，首次出现附 CAS 号",
        "功效评估须注明测试方法标准（如 ISO、JIS）",
        "临床数据须报告样本量、测试周期与统计检验",
        "pH 值须注明测量温度（通常 25°C）",
        "引用法规须注明版本与生效日期",
    ),
    key_venues=(
        "International Journal of Cosmetic Science",
        "Journal of Cosmetic Dermatology",
        "Skin Research and Technology",
        "Cosmetic, Toiletry & Fragrance Journal",
        "Journal of Investigative Dermatology",
        "中国皮肤性病学杂志",
    ),
    units_and_formulas_notes=(
        "浓度使用百分比（w/w 或 w/v）或 mg/mL",
        "pH 值测量温度须标注",
        "功效评分使用标准化标度（如 1-10）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("VISIA（皮肤影像分析系统）", "Cutometer（皮肤弹性质测仪）", "Corneometer（皮肤水分计）", "Tewameter（经皮水分流失测量仪）", "SkinScope（皮肤显微成像）", "MoxiLab（皮肤老化分析系统）", "PhisioDerm（皮肤微生物分析）", "DermDetect（皮肤图像分析）", "Cosmelight（肤色分析仪）", "Skintific（皮肤检测仪）", "Fresenius Kabi（化妆品原料分析仪）", "Anton Paar（化妆品流变仪）", "TA Instruments（化妆品质地分析仪）", "Shimadzu（化妆品成分 HPLC 分析）", "PerkinElmer（化妆品光谱分析）", "SPSS", "R（统计分析）", "SAS", "NVivo", "BeautyTech（化妆品研发平台）"),
    category="医学",
    databases=("PubMed", "Web of Science", "Scopus", "CNKI"),
)
