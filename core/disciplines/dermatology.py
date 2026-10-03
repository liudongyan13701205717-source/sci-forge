"""皮肤病学学科论文支持：皮肤临床/病理体裁、JAAD 引用样式与皮肤病学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dermatology",
    aliases=("dermatology", "皮肤病学", "皮肤科", "皮肤性病学",
             "dermatology clinical", "皮肤医学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与皮肤问题）",
            "methods（研究设计与人群）",
            "results（皮损与疗效数据）",
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
        "case_series": (
            "abstract",
            "introduction",
            "case presentation（病例详述）",
            "discussion（鉴别诊断与治疗）",
            "references",
        ),
    },
    citation_style="JAAD 样式（作者-年份；J Am Acad Dermatol 遵循 AAD 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "diagnostic_accuracy": "诊断准确性研究遵循 STARD 声明",
    },
    conventions=(
        "皮损描述用标准术语（形态、分布、边界）",
        "疾病严重度评分（PASI、DLQI 等）首次出现给出全称",
        "病理描述（表皮/真皮层次）须规范",
        "治疗反应评估标准（如 IGA）须注明",
        "照片/图像须注明拍摄条件与知情同意",
    ),
    key_venues=(
        "Journal of the American Academy of Dermatology",
        "British Journal of Dermatology",
        "JAMA Dermatology",
        "Journal of Investigative Dermatology",
        "Acta Dermato-Venereologica",
        "Dermatologic Surgery",
    ),
    units_and_formulas_notes=(
        "皮损面积用 cm² 或体表面积百分比",
        "公式用 amsmath；PASI/DLQI 评分计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "疗效分析给出 RR/OR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("皮肤镜", "皮肤共聚焦显微镜", "皮肤病理切片工作站", "窄谱 UVB 光疗仪"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC"),
)