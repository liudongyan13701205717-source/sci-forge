"""病毒学学科论文支持：病毒结构/传染/免疫/治疗体裁、Vancouver 引用与病毒度量记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="virology",
    aliases=("virology", "病毒学", "病毒研究", "viral research",
             "医学病毒学", "医学微生物学", "viral diseases", "病毒感染"),
    paper_types={
        "research": (
            "structured abstract",
            "introduction（病毒学问题与研究假设）",
            "methods（病毒分离、培养、检测、分析）",
            "results（病毒特征、感染动态与免疫应答）",
            "discussion（病毒学与临床意义）",
            "references",
        ),
        "case_report": (
            "abstract",
            "introduction",
            "case presentation（病例、病毒学检查、诊疗）",
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
        "systematic_review": (
            "structured abstract",
            "introduction",
            "methods（PICO、检索、纳排、偏倚评估）",
            "results（森林图、GRADE 证据等级）",
            "discussion",
            "references",
        ),
    },
    citation_style="Vancouver（J Virol/J Infect Dis 体例，按引用顺序编号）",
    reporting_standards={
        "case_report": "CARE",
        "cohort": "STROBE",
        "systematic_review": "PRISMA",
        "laboratory": "ISO 15189 / CAP 实验室标准",
        "vaccine": "ICH E6 / GCP",
    },
    conventions=(
        "病毒命名遵循 ICTV 国际命名委员会规范",
        "病毒分离须在指定生物安全等级（BSL）实验室进行",
        "病毒检测方法须注明灵敏度、特异度与检测限",
        "基因序列须提交 GenBank 并给登录号",
        "动物实验遵循 ARRIVE 2.0 报告条目",
    ),
    key_venues=(
        "Journal of Virology",
        "Journal of Infectious Diseases",
        "Virology",
        "Journal of General Virology",
        "PLOS Pathogens",
    ),
    units_and_formulas_notes=(
        "病毒载量给 copies/mL 或 IU/mL",
        "滴度给 log₁₀ TCID₅₀/mL 或 PFU/mL",
        "病毒复制动力学给 log₁₀ 值并注明时间点",
        "免疫应答给滴度（如 1:32）或 log₂ 值",
        "病毒序列给核苷酸位置并注明参考序列",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "MATLAB", "PCR 仪", "病毒电子显微镜", "病毒荧光显微镜", "病毒荧光定量PCR仪", "病毒基因测序仪", "病毒抗体检测仪", "病毒抗体ELISA仪", "病毒抗体Western blot仪", "病毒抗体血凝抑制仪", "病毒抗体中和抗体仪", "病毒抗体补体结合仪", "病毒抗体免疫印迹仪", "病毒抗体免疫组化仪", "病毒抗体免疫荧光仪", "病毒抗体免疫电镜仪", "病毒荧光原位杂交仪", "病毒流式细胞仪"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
