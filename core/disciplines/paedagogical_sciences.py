"""教育学（科学教育）学科论文支持：教学法实验与课堂质性研究体裁、教育测量信效度与效应量报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="paedagogical_sciences",
    aliases=(
        "paedagogical_sciences",
        "教育学",
        "Paedagogical Sciences",
        "教育科学",
        "教学法",
        "Educational Sciences",
        "Paedagogy",
        "教学论",
        "education science"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "methodology（教学方法）",
            "results（结果）",
            "discussion（讨论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（课堂案例描述）",
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
    citation_style="APA 第7版",
    reporting_standards={
        "k1": "教学法实验遵循 CONSORT 与教育实验报告规范",
        "k2": "质性研究遵循 COREQ/SRQR 报告规范",
        "k3": "教育测量须报告信度（α/KR-20）与效度证据"
    },
    conventions=(
        "教学法描述须注明所用框架（如 SOLO、5E、UbD）及其版本",
        "学习者匿名化须声明代号规则与脱敏处理方式",
        "效应量与显著性并行报告并给出 95% 置信区间",
        "涉及未成年被试须报告伦理批号与双知情同意",
        "测验工具须报告常模、计分区间与评分者一致性"
    ),
    key_venues=(
        "Educational Researcher",
        "Educational Research Review",
        "Review of Educational Research",
        "Teachers College Record",
        "Teaching and Teacher Education"
    ),
    units_and_formulas_notes=(
        "教学时长按课时（40/45/50 min）统一计量，跨学期研究注明校历差异",
        "效应量报告 Cohen's d 或 Hedges' g 并给出 95% 置信区间",
        "量表采用标准分（T 分/Z 分）时注明换算公式",
        "百分比给出基数 N，缺失数据须说明处理方式（剔除或插补）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Moodle", "Canvas (Instructure)", "Blackboard Learn", "D2L Brightspace", "Google Classroom", "H5P", "Seesaw", "Kahoot!", "Nearpod", "Padlet", "Flipgrid", "NVivo", "MAXQDA", "ATLAS.ti", "SPSS", "R", "JASP", "Jamovi", "EndNote", "Microsoft Excel"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
