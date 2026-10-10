"""传播学学科论文支持：媒介/效果/话语体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="communication_studies",
    aliases=("communication_studies", "传播学", "传播研究", "媒介研究",
             "communication science", "mass communication", "媒介效果研究",
             "传播效果研究", "communications research", "传播与媒介研究"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "theory（理论框架）",
            "hypotheses（假设）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "content_analysis": (
            "abstract",
            "introduction",
            "sampling（抽样）",
            "coding scheme（编码方案）",
            "reliability（信度）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "discourse_analysis": (
            "abstract",
            "introduction",
            "corpus（语料）",
            "analytical framework（分析框架）",
            "findings（发现）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 7（Journal of Communication 遵循 APA 规范）",
    reporting_standards={
        "experimental": "实验研究遵循实验报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "content_analysis": "内容分析遵循编码信度报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "理论框架与假设须明确",
        "编码者间信度须报告",
        "抽样与样本须说明",
        "测量工具须注明信效度",
        "效应量与显著性须报告",
    ),
    key_venues=(
        "Journal of Communication",
        "Communication Research",
        "Human Communication Research",
        "Journal of Computer-Mediated Communication",
        "New Media & Society",
        "Communication Theory",
        "Communication Studies",
        "Journal of Communication",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "效应量用 Cohen's d 或 η²",
        "信度用 Cohen's κ 或 Krippendorff's α",
        "样本量须报告",
        "百分比给出基数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo", "R", "Python", "SPSS", "Stata", "MAXQDA", "Qualtrics", "Tableau", "ELAN", "MediaLab", "Weka", "Minitab", "AMOS", "LISREL", "EQS", "Google Analytics", "Adobe Premiere", "DaVinci Resolve", "OBS Studio", "Avid Media Composer"),
    category="文学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)
