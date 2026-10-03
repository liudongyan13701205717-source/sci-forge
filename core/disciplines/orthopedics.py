"""骨科学学科论文支持：骨科临床/生物力学体裁、JBJS 引用样式与骨科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="orthopedics",
    aliases=("orthopedics", "骨科学", "骨科", "矫形外科学", "运动骨科",
             "orthopaedic surgery", "骨科临床"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与骨科问题）",
            "methods（研究设计与人群）",
            "results（功能评分与影像数据）",
            "discussion（机理与临床意义）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、盲法与统计）",
            "results（疗效与安全性终点）",
            "discussion（与既往试验对比）",
            "references",
        ),
        "biomechanics": (
            "abstract",
            "introduction",
            "methods（力学测试方案）",
            "results（载荷/应变数据）",
            "discussion（生物力学意义）",
            "references",
        ),
    },
    citation_style="JBJS 样式（作者-年份；J Bone Joint Surg 遵循 JBJS 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "biomechanics": "生物力学研究须报告测试机与加载方案",
    },
    conventions=(
        "功能评分（HSS、KSS、VAS 等）首次出现给出全称与范围",
        "影像分级（Kellgren-Lawrence 等）须注明版本",
        "内固定/假体型号与厂商须报告",
        "随访时间与失访率须报告",
        "生物力学参数（载荷、扭矩）单位须规范",
    ),
    key_venues=(
        "Journal of Bone and Joint Surgery",
        "Clinical Orthopaedics and Related Research",
        "The American Journal of Sports Medicine",
        "Journal of Orthopaedic Research",
        "Arthroscopy",
        "The Bone & Joint Journal",
    ),
    units_and_formulas_notes=(
        "载荷用 N；扭矩用 N·m；角度用 °",
        "公式用 amsmath；力学计算式与评分公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "生存/翻修分析给出 HR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("关节镜", "SPSS", "R", "运动生物力学分析系统", "术后影像测量软件"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Europe PMC", "CNKI"),
)