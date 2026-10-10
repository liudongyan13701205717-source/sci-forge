"""专业理论教师教育论文支持：理论教育学领域教师培养、知识建构与专业发展的论文写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_in_specific_theoretical",
    aliases=("teacher_training_in_specific_theoretical", "Teacher training in specific theoretical", "专业理论教师教育", "理论教育培养", "专业理论教学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "literature review（文献综述）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "conclusion",
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
    citation_style="APA 7",
    reporting_standards={
        "theoretical_framework": "理论框架须明确知识建构路径、核心概念与理论边界",
        "professional_development": "教师专业发展须描述发展阶段、影响因素与评估指标",
        "epistemology": "知识论立场须明确建构主义/实用主义等认识论立场及其对教学的影响",
        "evidence_base": "教学建议须基于实证研究，区分经验总结与证据支持的结论",
    },
    conventions=(
        "理论概念首次出现须给出定义与出处，区分核心概念与衍生概念",
        "引用他人理论须注明作者、出版年份与具体版本",
        "研究设计须区分质性研究、量化研究与混合方法，说明方法论依据",
        "概念地图须标注层级关系与连接类型，避免交叉重复",
        "教师专业发展须区分阶段（新手→熟练→专家），标注评估标准",
    ),
    key_venues=(
        "Teachers College Record",
        "Educational Theory",
        "Theory & Research in Education",
        "Journal of Curriculum Studies",
        "Professional Development in Education",
    ),
    units_and_formulas_notes=(
        "概念层级须明确标注一级概念、二级概念与三级概念",
        "质性编码须说明编码单位（文本行、语义段）、编码者与一致性系数",
        "理论框架图示须注明概念间关系类型（从属、并列、因果等）",
        "文献综述须按时间/主题/理论框架组织，标注关键节点与转折点",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("CmapTools", "MindManager", "Xmind", "Lucidchart", "Miro", "Google Docs", "LaTeX", "Zotero", "Mendeley", "EndNote", "NVivo", "MAXQDA", "ATLAS.ti", "Dedoose", "QualCoder", "FreeMind", "Curriki", "Notion", "Grammarly", "RefWorks"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
