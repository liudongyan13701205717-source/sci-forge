"""自然疗法医学学科论文支持：自然疗法/替代医学研究体裁、临床报告规范与草药记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="naturopathic_medicine",
    aliases=("naturopathic_medicine", "自然疗法医学", "自然疗法",
             "顺势疗法", "替代医学", "天然医学", "草药医学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与临床问题）",
            "methodology（设计、干预与测量）",
            "results（疗效与安全性结果）",
            "discussion（临床意义与局限）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例特征与治疗过程）",
            "analysis（疗效分析与机制讨论）",
            "results（治疗结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论基础综述）",
            "evidence synthesis（循证证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver 样式（医学常用）",
    reporting_standards={
        "clinical": "临床研究遵循 CONSORT 声明",
        "herbal": "草药研究遵循 STMG 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "observational": "观察研究遵循 STROBE 声明",
        "case_report": "病例报告遵循 CARE 声明",
    },
    conventions=(
        "生命体征测量须报告",
        "草药名称用拉丁学名（斜体）",
        "剂量/疗程须完整",
        "对照/随机化须说明",
        "副反应/并发症须报告",
    ),
    key_venues=(
        "Journal of Alternative and Complementary Medicine",
        "Complementary Therapies in Medicine",
        "Phytotherapy Research",
        "Journal of Ethnopharmacology",
        "Evidence-Based Complementary and Alternative Medicine",
    ),
    units_and_formulas_notes=(
        "剂量用 mg/mL；生命体征用标准单位",
        "公式用 amsmath；药动学方程须编号",
        "草药剂量须给出范围",
        "数值结果给出均值 ± 标准差",
        "拉丁学名用斜体",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("电子血压计", "听诊器", "显微镜", "尿液分析仪", "血气分析仪", "心电图机（ECG）", "血常规分析仪", "生物共振分析仪", "中医体质辨识仪", "针灸设备", "拔罐设备", "SPSS（统计分析）", "R（统计）", "Excel", "LaTeX", "临床记录软件", "营养分析软件", "草药鉴定工具", "Stata（统计）", "GraphPad Prism"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref", "CNKI", "Cochrane"),
)
