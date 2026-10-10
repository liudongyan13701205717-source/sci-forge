"""Teacher Training Courses for University 学科论文支持：大学师资培训课程设计论文体裁、APA 引用样式与高等教育培训研究方法论记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_courses_for_university",
    aliases=(
        "teacher_training_courses_for_university",
        "Teacher training courses for university",
        "大学教师培训课程",
        "高等教育教学能力培训",
        "university teacher development",
        "higher education teaching",
        "teaching and learning in higher education",
        "大学师资培训",
        "teaching academy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与大学师资培训问题）",
            "literature review",
            "methodology（研究设计与参与）",
            "findings",
            "discussion（对高等教育政策与教学实践的意义）",
            "references",
        ),
        "course_design": (
            "abstract",
            "introduction",
            "course rationale",
            "curriculum design（培训目标与模块）",
            "implementation",
            "evaluation",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "literature review",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（Higher Education、Studies in Higher Education、IJATE 遵循期刊规范）",
    reporting_standards={
        "sample": "样本须报告：参与者类型（新入职/资深教授、教研员）、人数 n、机构类型（研究型/教学型）、国家/地区",
        "design": "研究设计须报告：混合/质性/量化、数据收集方法（问卷/焦点小组/日志/课堂录像）、信效度检验",
        "ethics": "伦理审查须报告：机构审查（IRB/ERB）、知情同意、数据匿名",
        "course_design": "课程设计须报告：培训目标、模块、学时、教学法（如反向设计、行动研究、同伴观察）",
        "systematic_review": "系统综述遵循 PRISMA 2020 声明",
    },
    conventions=(
        "大学师资培训研究遵循 Higher Education Academy（HEA）、QAA、AAHE、AUEB、CTLT 等认证机构框架",
        "教师专业发展框架遵循 Hattie Visible Learning、TPACK、Schön 反思性实践、Kolb 经验学习循环",
        "课程设计遵循反向设计（Backward Design）、布鲁姆分类（修订版）与 ADDIE 模型",
        "课堂观察量表遵循 CLASS、CIT、FROG、OER 与 Peer Review 量表",
        "研究遵循 Kaupapa Māori 等本位研究法如涉原住民教育；伦理审查遵循 APA 伦理准则",
        "符号约定：TPACK、TPeCK、PCK 首次出现须给出全称；效应量与 p 值遵循 APA 报告规范",
    ),
    key_venues=(
        "Higher Education",
        "Studies in Higher Education",
        "International Journal for Academic Teaching and Learning (IJATL)",
        "Journal of University Teaching & Learning",
        "Teaching in Higher Education",
        "New Directions for Teaching and Learning",
    ),
    units_and_formulas_notes=(
        "样本量报告 n 与观测数 N；培训效果用 TOSI/CIRPI（培训-组织-战略-人员指标）四层次评估",
        "公式用 amsmath；效应量用 Cohen's d、η²、r；混合效应模型（HLM）须报告随机截距与斜率",
        "显著性用 *, **, *** 对应 10%/5%/1%；p 值报告精确值（p < .001 或 p = .032）",
        "所有比率与效应量保留 3 位小数；样本量 N 与参与者人数 n 须完整标注",
        "问卷量表用 Likert 5/7 点；描述性统计报告 M ± SD 与 n；Cronbach α ≥ .70 为量表可接受信度阈值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Moodle", "Canvas LMS", "Google Classroom", "Zoom", "Google Forms", "SurveyMonkey", "NVivo", "Atlas.ti", "Zotero", "EndNote", "SPSS", "R", "Stata", "Excel", "Power BI", "Tableau", "Google Docs", "Overleaf", "Kahoot", "Mentimeter"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "ProQuest"),
)
