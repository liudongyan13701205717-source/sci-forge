"""Communication and Media Studies 学科论文支持：传媒/媒体研究体裁、APA 引用样式与传播学统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="communication_and_media_studies",
    aliases=("Communication and Media Studies", "传播与媒体研究", "传媒研究",
             "媒体研究", "communication studies", "media studies",
             "communications studies", "传媒", "新闻与传播", "媒体分析"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "literature review（文献综述）",
            "theoretical framework（理论框架）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusion（结论与建议）",
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
        "媒介效果研究须报告变量操作化与测量",
        "内容分析须报告编码信度与抽样方法",
        "受众研究须说明样本构成与代表性",
        "理论框架与假设须明确",
    ),
    key_venues=(
        "Journal of Communication",
        "New Media & Society",
        "Communication Studies",
        "Media, Culture & Society",
        "Journal of Broadcasting & Electronic Media",
        "International Journal of Communication",
        "Communication Research",
        "Press & Journal",
    ),
    units_and_formulas_notes=(
        "统计量给出 M/SD/SE/CI",
        "效应量用 Cohen's d 或 η²",
        "信度用 Cohen's κ 或 Krippendorff's α",
        "样本量须报告，百分比给出基数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Adobe Creative Suite", "Avid Media Composer", "ENPS", "NVivo", "SPSS", "Stata", "R", "Python", "MAXQDA", "Qualtrics", "Tableau", "Adobe Premiere", "Final Cut Pro", "Pro Tools", "DaVinci Resolve", "OBS Studio", "MediaLab", "ELAN", "Weka", "Adobe InDesign"),
    category="文学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Semantic Scholar"),
)
