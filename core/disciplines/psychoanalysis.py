"""精神分析学科论文支持：临床/临床案例体裁、APA 引用样式与经典文献注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="psychoanalysis",
    aliases=(
        "psychoanalysis",
        "精神分析",
        "Psychoanalysis",
        "Psychoanalytic theory",
        "精神分析学",
        "弗洛伊德",
        "Psychoanalytic psychotherapy",
        "精神分析治疗",
        "Psychoanalytic psychology",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与理论问题）",
            "methodology（分析或研究方法）",
            "results（临床或实证结果）",
            "discussion（理论意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（临床案例描述）",
            "analysis（精神分析分析）",
            "results（疗效结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；精神分析期刊亦可采用 Chicago 样式）",
    reporting_standards={
        "qualitative": "质性研究遵循 COREQ 指南",
        "case_study": "临床案例遵循 DSR-CASE 规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "clinical_review": "临床评论遵循 SRQR 指南",
        "ethics": "伦理声明须符合当地精神分析学会规范",
    },
    conventions=(
        "术语须遵循经典精神分析术语（如移情、阻抗）",
        "临床材料须去标识化并获患者书面同意",
        "移情与反移情须明确区分",
        "自由联想材料须说明节选范围",
        "理论归属须注明学派（弗洛伊德、拉康等）",
    ),
    key_venues=(
        "Psychoanalysis and Contemporary Thought",
        "The International Journal of Psychoanalysis",
        "Psychoanalytic Review",
        "Psychoanalytic Dialogues",
        "Contemporary Psychoanalysis",
    ),
    units_and_formulas_notes=(
        "量表分数无量纲，须报告量表名称与版本",
        "治疗时长以小时计（单次 45-60 分钟）",
        "公式用 amsmath；概念定义须给出",
        "案例材料须注明节选范围与处理方式",
        "伦理审批与知情同意须声明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Freud Complete Works", "Anna Freud Papers", "Psychoanalytic Electronic Publishing", "Psychoanalytic Dictionary", "The International Psychoanalytical Association", "British Psychoanalytical Society", "Lacan Online", "Transference Recording", "Audio Recording", "Video Recording", "Free Association", "Dream Analysis", "Text Analysis", "Coding System", "ATLAS.ti", "NVivo", "SPSS", "R", "MAXQDA", "Excel"),
    category="理学",
    databases=("OpenAlex", "Crossref", "Psychoanalytic Electronic Publishing"),
)
