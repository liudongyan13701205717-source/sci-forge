"""基础识字教育学科论文支持：成人识字教育、扫盲教学法与读写能力测评体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="simple_literacy",
    aliases=(
        "simple_literacy",
        "基础识字",
        "识字教育",
        "扫盲",
        "Adult Literacy",
        "Basic Literacy",
        "Functional Literacy",
        "读写能力",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methods（准实验/随机对照/质性方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（社区/学习者案例）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份）",
    reporting_standards={
        "experimental": "识字干预实验须报告前后测、控制组与效应量（d 值）",
        "survey": "读写能力评估须采用标准化测试工具（如 FAST、PIAT）",
        "ethics": "涉及成人参与者的研究须说明知情同意与隐私保护",
        "review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "识字率按 UNESCO UIS 定义报告（识字人口/总人口 × 100%）",
        "读写能力按 INL 功能识字分级报告（1-8 级）",
        "干预研究须报告接触时长（hours of contact）与学习产出",
        "样本须描述教育背景、年龄、社会经济地位",
        "效应量以 Cohen's d 或 Hedges' g 报告",
    ),
    key_venues=(
        "Literacy Research",
        "Journal of Adult and Continuing Education",
        "Adult Education Quarterly",
        "Literacy",
        "教育研究",
    ),
    units_and_formulas_notes=(
        "识字率以 % 计；教育年限以年计",
        "阅读流畅度以 words per minute (wpm) 报告",
        "阅读准确度以 % correct 报告",
        "效应量 Cohen's d = (M₁ - M₂) / SD_pooled",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Kahoot!", "Duolingo", "LearningApps", "Quizlet", "Google Classroom", "ClassDojo", "Edmodo", "Moodle", "Canvas", "Blackboard", "Microsoft Teams", "Google Docs", "Canva", "Photoshop", "LaTeX", "Python（pandas）", "RStudio", "SPSS", "Endnote", "Anki"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scopus", "ERIC"),
)
