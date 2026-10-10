"""兽医医学学科论文支持：临床诊疗与动物医学研究体裁、Vancouver 引用与临床度量记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="veterinary_medicine",
    aliases=("veterinary medicine", "兽医医学", "动物医学", "animal medicine",
             "临床兽医学", "veterinary clinical", "小动物医学", "companion animal"),
    paper_types={
        "research": (
            "structured abstract",
            "introduction（临床问题与研究假设）",
            "methods（设计、动物群、分组、结局指标）",
            "results（流程图、基线表、疗效与安全性）",
            "discussion（外推性与临床意义）",
            "references",
        ),
        "case_report": (
            "abstract",
            "introduction",
            "case presentation（物种、品种、年龄、病史、检查与诊疗）",
            "discussion（鉴别诊断与文献对照）",
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
        "diagnostic_accuracy": (
            "abstract",
            "introduction",
            "methods（参考标准、样本、盲法、STARD 流程）",
            "results（敏感度/特异度、ROC、似然比）",
            "discussion",
            "references",
        ),
    },
    citation_style="Vancouver（JAVMA 体例，按引用顺序编号）",
    reporting_standards={
        "case_report": "CARE",
        "cohort": "STROBE",
        "randomized_trial": "REFLECT / CONSORT",
        "systematic_review": "PRISMA",
        "diagnostic_accuracy": "STARD",
        "animal_research": "ARRIVE 2.0",
    },
    conventions=(
        "动物伦理：IACUC/伦理委员会批准号；遵循 3R 原则",
        "物种与群体描述完整：品种、年龄、性别、体重、饲养背景",
        "实验单位明确（个体/栏/群），必要时说明聚类效应校正",
        "动物福利与人道终点预先定义并报告",
        "病例报告去标识化：不披露畜主可识别信息",
    ),
    key_venues=(
        "Journal of Veterinary Internal Medicine",
        "Veterinary Radiology & Ultrasound",
        "Veterinary Surgery",
        "Journal of Small Animal Practice",
        "Veterinary Clinics of North America",
    ),
    units_and_formulas_notes=(
        "药物剂量统一 mg/kg 并给给药途径与频次；体重给 kg",
        "实验室结果给参考区间与检测方法（如 ELISA、PCR）",
        "影像报告给分级或评分标准并注明体位",
        "病理分级给具体分级标准与组织学参数",
        "临床评分给评分表与评分者盲法说明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "MATLAB", "兽用超声诊断仪", "兽用X射线机", "兽用CT扫描仪", "兽用监护仪", "兽用麻醉机", "兽用呼吸机", "兽用电子血压计", "兽用生化分析仪", "兽用血气分析仪", "兽用内窥镜", "显微镜", "PCR 仪", "酶联免疫分析仪", "兽用超声心动图仪", "兽用内窥镜手术系统", "兽用电子手术刀", "兽用激光治疗仪"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
