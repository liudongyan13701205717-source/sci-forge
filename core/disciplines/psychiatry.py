"""精神病学学科论文支持：精神临床/流行病学体裁、CONSORT 报告规范与精神医学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="psychiatry",
    aliases=(
        "psychiatry",
        "精神病学",
        "精神医学",
        "Psychiatry",
        "Mental health",
        "精神卫生",
        "临床精神病学",
        "精神科",
        "Psychopharmacology",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methodology（研究设计与人群）",
            "results（量表与统计结果）",
            "discussion（机制与临床意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例描述）",
            "analysis（鉴别与诊断分析）",
            "results（诊疗结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（病因与机制综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；Am J Psychiatry 遵循 APA 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "qualitative": "质性研究遵循 COREQ/SRQR 指南",
    },
    conventions=(
        "诊断标准（DSM-5/ICD-11）须注明版本",
        "量表（HAMD、HAMA、PANSS 等）首次出现给出全称与评分范围",
        "效应量（Cohen's d 等）须报告",
        "伦理审批与知情同意须声明",
        "药物剂量与滴定方案须完整报告",
    ),
    key_venues=(
        "American Journal of Psychiatry",
        "JAMA Psychiatry",
        "The Lancet Psychiatry",
        "Psychological Medicine",
        "World Psychiatry",
        "British Journal of Psychiatry",
    ),
    units_and_formulas_notes=(
        "量表分数无量纲；时间用周/月",
        "公式用 amsmath；量表总分与因子分计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "效应量与 95% CI 须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SCID-5", "MINI", "HAMD", "HAMA", "PANSS", "YMRS", "Y-BOC", "BPRS", "CGI", "MADRS", "SCL-90", "PHQ-9", "GAD-7", "AUDIT", "NIMH Repository", "SPSS", "R", "SAS", "fMRI 脑功能成像", "G*Power"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC", "Semantic Scholar", "DrugBank"),
)
