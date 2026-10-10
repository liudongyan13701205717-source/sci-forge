"""职场欺凌学科论文支持：职场欺凌/职场心理健康体裁、APA 引用样式与心理测量学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mobbing",
    aliases=(
        "mobbing", "职场欺凌", "职场霸凌", "workplace bullying", "组织欺凌",
        "psychological violence", "psychological harassment", "组织压力", "组织欺凌"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与研究问题）",
            "methodology（测量方法与统计）",
            "results（量化数据与显著性）",
            "discussion（机制与干预）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（职场欺凌案例）",
            "analysis（欺凌行为与影响）",
            "results（心理健康结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（欺凌理论模型）",
            "evidence synthesis（研究证据综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份；心理学期刊遵循 APA 规范）",
    reporting_standards={
        "experimental": "实验遵循 APA 心理学实验报告规范",
        "survey": "问卷调查遵循 SAGE Survey Research 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "测量工具与量表信度须报告",
        "样本描述须含人口学特征",
        "统计方法须明确报告",
        "伦理审批与知情同意须说明",
        "欺凌行为术语须统一",
    ),
    key_venues=(
        "Workplace Health",
        "Journal of Occupational Health",
        "Personnel Psychology",
        "European Journal of Work and Organizational Psychology",
        "Aggression and Violent Behavior",
    ),
    units_and_formulas_notes=(
        "量表得分用原始分或百分位",
        "效应量用 Cohen's d 或 η²",
        "公式用 amsmath；量表计分公式须明确",
        "数值结果给出均值 ± SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("心理测评量表 (MBI/GMBS)", "结构方程模型 SEM", "LISREL", "Mplus", "SPSS", "R (lavaan)", "NVivo", "Qualtrics", "Google Forms", "神经电生理记录仪 EEG", "眼动仪", "唾液皮质醇检测", "HRV 心变异性分析", "组织行为学调查工具", "员工满意度测量系统", "组织网络分析 ONA", "Python (NLTK)", "JADT", "文本情感分析 Python (spaCy)", "混合研究方法 Meta 分析工具"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
