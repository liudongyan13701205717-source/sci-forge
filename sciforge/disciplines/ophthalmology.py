"""眼科学学科论文支持：眼科临床/视觉科学体裁、AAO/Ophthalmology 引用样式与眼科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ophthalmology",
    aliases=("ophthalmology", "眼科学", "眼科", "视觉科学",
             "visual science", "眼科临床"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与眼科问题）",
            "methods（研究设计与人群）",
            "results（视力与眼底数据）",
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
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="AAO/Ophthalmology 样式（作者-年份；Ophthalmology 遵循 AAO 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "diagnostic_accuracy": "诊断准确性研究遵循 STARD 声明",
    },
    conventions=(
        "视力记录用小数/对数（logMAR）并注明换算",
        "眼压单位 mmHg；视野参数（MD、PSD）须报告",
        "眼底/影像（OCT、OCTA）参数须完整",
        "手术方式（白内障、青光眼等）与分级须报告",
        "屈光状态（球镜/柱镜）符号规范须注明",
    ),
    key_venues=(
        "Ophthalmology",
        "American Journal of Ophthalmology",
        "Investigative Ophthalmology & Visual Science",
        "JAMA Ophthalmology",
        "British Journal of Ophthalmology",
        "Retina",
    ),
    units_and_formulas_notes=(
        "眼压用 mmHg；视力用 logMAR 或小数",
        "公式用 amsmath；logMAR 与视力换算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "疗效分析给出 RR/OR 与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("光学相干断层扫描仪（OCT）", "眼底照相机", "视觉电生理检查仪（ERG/VEP）", "眼压计", "裂隙灯显微镜"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC", "Zenodo"),
)