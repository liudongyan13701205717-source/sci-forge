"""兽医护理学科论文支持：动物护理实践与研究体裁、Nursing 报告规范与临床护理度量记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="veterinary_nursing",
    aliases=("veterinary nursing", "兽医护理", "动物护理", "animal nursing",
             "veterinary technician", "兽医技术员", "animal health technician"),
    paper_types={
        "research": (
            "structured abstract",
            "introduction（护理问题与研究假设）",
            "methods（设计、动物群、护理干预、结局指标）",
            "results（流程图、基线表、护理效果与安全性）",
            "discussion（护理外推性与临床意义）",
            "references",
        ),
        "case_report": (
            "abstract",
            "introduction",
            "case presentation（物种、品种、年龄、病史、护理过程）",
            "discussion（护理决策与文献对照）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
        "quality_improvement": (
            "abstract",
            "introduction",
            "setting and baseline",
            "intervention",
            "results（过程与效果指标）",
            "discussion",
            "references",
        ),
    },
    citation_style="APA 7（护理研究常用）",
    reporting_standards={
        "quality_improvement": "SQUIRE 2.0",
        "case_report": "CARE",
        "systematic_review": "PRISMA",
        "animal_research": "ARRIVE 2.0",
        "cohort": "STROBE",
    },
    conventions=(
        "动物伦理：IACUC/伦理委员会批准号；遵循 3R 原则",
        "护理干预描述完整：操作内容、频次、执行者资质",
        "动物福利与人道终点预先定义并报告",
        "护理效果指标（疼痛评分、恢复时间等）须预先定义",
        "病例报告去标识化：不披露畜主可识别信息",
    ),
    key_venues=(
        "Journal of Veterinary Emergency and Critical Care",
        "VETERINARY NURSE",
        "Journal of Animal Welfare",
        "Veterinary Nursing Education",
        "Animal Welfare",
    ),
    units_and_formulas_notes=(
        "护理操作时间给分钟（min）",
        "疼痛评分给分级标准（0-10 或 0-3）并注明评估工具",
        "液体复苏量给 mL/kg/h 并注明液体类型",
        "康复进度给百分比或天数并注明测量方法",
        "护理人力配置给 FTE 或小时/动物",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "兽用监护仪", "兽用麻醉机", "兽用呼吸机", "兽用电子血压计", "兽用电子体温计", "兽用电子秤", "兽用输液泵", "兽用注射泵", "兽用吸痰器", "兽用氧疗设备", "兽用超声诊断仪", "兽用X射线机", "兽用生化分析仪", "兽用血气分析仪", "显微镜", "兽用内窥镜", "兽用超声心动图仪", "兽用激光治疗仪"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
