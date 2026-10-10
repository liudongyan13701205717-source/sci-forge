"""实践教学学科论文支持：教学法、课程设计与学习效果实证研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="practical_paedagogical_courses",
    aliases=(
        "practical paedagogical courses", "实践教学", "教学法实践",
        "didactics", "教学论",
        "practice teaching", "教育实习",
        "microteaching", "微格教学",
        "curriculum implementation", "课程实施",
        "pedagogical practice", "教学实践研究",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（教学问题与理论框架）",
            "methodology（准实验/教学干预设计与测量工具）",
            "results（学习成效与教学效果）",
            "discussion（教学法讨论与局限）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（课程与学情背景）",
            "analysis（教学过程与课堂观察记录）",
            "results（学生学习与教师成长证据）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（教学法理论谱系）",
            "evidence synthesis（教学干预证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "教育实验须报告分组方式、效度威胁与效应量",
        "k2": "质性研究须报告编码过程、信度与研究者反思",
        "k3": "案例研究须说明取样理由、资料来源与可迁移性",
    },
    conventions=(
        "学情须交代生源结构、前置知识水平与班额",
        "教学干预须报告课时数、教案版本与实施周期",
        "学习成效测量须报告前测/后测与信度",
        "质性分析须注明编码层级、示例与代码簿",
        "伦理须说明知情同意、匿名化与未成年人保护",
    ),
    key_venues=(
        "Teaching and Teacher Education",
        "Teaching and Education",
        "Journal of Experimental Education",
        "Instructional Science",
        "Educational Action Research",
    ),
    units_and_formulas_notes=(
        "学习成效以得分率或前后测差值表示并附 95% CI",
        "效应量优先报告 Cohen's d / Hedges' g 与 η²",
        "班级间比较注明显著性水平 α 与多重比较校正",
        "课堂观察工具须报告编码类别、样本量与编码一致性",
        "教学时间以分钟计量并注明是否为净上课时间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "Jamovi", "NVivo", "ATLAS.ti", "MAXQDA", "Delphi Expert 系统", "MindMap 教学概念图工具", "GeoGebra", "ClassIn 智慧课堂", "iSpring Suite 微课制作", "Camtasia 录课工具", "Qualtrics", "SurveyMonkey", "Moodle LMS", "H5P 互动学习", "Obs 课堂录制", "OBS-Video 课堂录音", "Python (pandas, scipy)"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
