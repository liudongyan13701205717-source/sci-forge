"""非学科专门化方向教师培养学科论文支持：全科/初任教师教育的体裁、APA 7 引用样式与注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_without_subject_specialisation",
    aliases=(
        "teacher_training_without_subject_specialisation",
        "全科教师教育",
        "初任教师培养",
        "通用师范培养",
        "Teacher training without subject specialisation",
        "generalist teacher education",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究问题）",
            "methods（研究设计与实施）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "design_based_research": (
            "abstract",
            "introduction",
            "design rationale（设计原理与学习理论）",
            "implementation（实施与修订轮次）",
            "findings（发现与有效性证据）",
            "design principles",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与筛选方法）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份制，教育研究主流规范）",
    reporting_standards={
        "empirical": "实证研究须报告参与者构成、样本量与数据采集窗口",
        "course_design": "课程与教学设计须随附课程大纲与评价量表",
        "ethics": "课堂与实习资料使用须取得伦理批准与同意",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "curriculum_evaluation": "课程评价遵循 CIPP 或 Kirkpatrick 框架",
    },
    conventions=(
        "全科能力维度须给出操作化定义与观测指标",
        "教学实例须匿名化并注明学段、班额与课时",
        "能力量表题项须在附录完整列出，报告信度",
        "跨学段比较须控制教材版本与课程标准年份",
        "术语全文一致：教学能力、学科知识、跨学科整合分列"
    ),
    key_venues=(
        "Journal of Teacher Education",
        "Studies in Educational Evaluation",
        "Curriculum Journal",
        "Assessment & Evaluation in Higher Education",
        "International Journal of Educational Research",
    ),
    units_and_formulas_notes=(
        "能力得分报告均值 ± 标准差与样本量",
        "公式用 amsmath；加权与评分公式须编号并被引用",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "时间单位统一为课时（注明每课时分钟数）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Moodle", "Blackboard", "Canvas LMS", "Articulate 360", "iSpring Suite", "H5P", "Genially", "Canva", "Mentimeter", "Quizlet", "Padlet", "Kahoot!", "PowerPoint", "Google Docs", "Seesaw", "ClassDojo", "Blooket", "Flipgrid", "Google Sheets", "Overleaf"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
