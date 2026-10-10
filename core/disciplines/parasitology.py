"""寄生虫学学科论文支持：寄生虫生物学与寄生虫病诊断治疗研究体裁、寄生虫临床试验与流行病学报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="parasitology",
    aliases=(
        "parasitology",
        "寄生虫学",
        "Parasitology",
        "寄生虫病",
        "Parasitology and Vector Biology",
        "医学寄生虫学",
        "Neglected Tropical Diseases",
        "寄生虫学与媒介生物学",
        "parasite disease"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（材料与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references"
        ),
    },
    citation_style="Vancouver 样式",
    reporting_standards={
        "k1": "临床试验遵循 CONSORT，病例报告遵循 CARE",
        "k2": "诊断试验评估遵循 STARD 声明",
        "k3": "流行病学研究遵循 STROBE 声明"
    },
    conventions=(
        "寄生虫命名遵循国际命名法规",
        "感染宿主与实验动物须报告物种、品系、来源与适应情况",
        "实验设计须报告样本量、对照组与随机化方法",
        "感染强度与疾病严重程度须报告分级标准",
        "涉及人类受试须报告伦理批准与知情同意"
    ),
    key_venues=(
        "PLOS Neglected Tropical Diseases",
        "Acta Tropica",
        "Parasite",
        "Parasitology",
        "中华寄生虫学杂志"
    ),
    units_and_formulas_notes=(
        "感染强度以卵/克（opg）或虫体计数报告",
        "感染率与患病率以 % 报告并给出基数 N",
        "药物浓度以 μg/mL 或 mg/kg 报告",
        "时间以天或周报告并注明感染阶段"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("光学显微镜", "荧光显微镜", "扫描电镜（SEM）", "透射电镜（TEM）", "聚合酶链反应（PCR）", "实时荧光定量 PCR（qPCR）", "凝胶电泳仪", "流式细胞仪", "酶标仪（ELISA）", "Kato-Katz 虫卵计数装置", "McMaster 虫卵定量装置", "寄生虫培养箱", "离心机", "生物安全柜（BSL-2/3）", "SPSS", "R", "GraphPad Prism", "EndNote", "NCBI GenBank", "GBIF（寄生虫数据集）"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
