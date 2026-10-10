"""其他教育学学科论文支持：未被细类归入的教学、课程与教育评估研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_education",
    aliases=(
        "other_education", "其他教育学",
        "other education", "其他教育学",
        "education not elsewhere classified", "教育学未另分类",
        "curriculum and pedagogy", "课程与教学论",
        "educational research", "教育研究",
        "learning sciences", "学习科学",
        "instructional design", "教学设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（教育问题与理论背景）",
            "methodology（研究设计与样本）",
            "results（成效数据与分析）",
            "discussion（教育意义与推广性）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（学校/课堂/学习者个案）",
            "analysis（编码与主题分析）",
            "results（教学成效）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（学习理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "混合研究设计须按 CONSORT 与 COREQ 分别报告量化与质性部分",
        "k2": "多组对比须报告基线均衡性检验与组内组间效应量",
        "k3": "质性编码须报告编码者信度（如 Cohen's κ 或 Krippendorff's α）",
    },
    conventions=(
        "样本须报告 N、班级数与年级分布及缺失情况",
        "量表须报告信度系数（如 Cronbach's α）与效度来源",
        "干预前后比较注明测量工具与施测时间",
        "伦理审查与知情同意须明确说明",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "Review of Educational Research",
        "Educational Researcher",
        "British Journal of Educational Psychology",
        "Educational Technology Research and Development",
        "Comparative Education Review",
        "《教育研究》",
    ),
    units_and_formulas_notes=(
        "标准分用 M (SD) 报告并说明参照组",
        "效应量注明 Cohen's d 或 η²",
        "时间变量以课时或学时为单位标注",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "MAXQDA", "SPSS", "R (RStudio)", "Stata", "HLM", "Mplus", "AMOS", "Qualtrics", "SurveyMonkey", "Moodle", "NetLogo", "Python (pandas)", "Microsoft Excel", "LaTeX", "Zotero", "EndNote", "IRBmanager", "Open Science Framework (OSF)"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
