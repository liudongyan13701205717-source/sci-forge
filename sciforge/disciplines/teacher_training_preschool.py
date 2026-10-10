"""学前教育教师教育论文支持：学前阶段教师培养、发展评估与游戏化教学的论文写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_preschool",
    aliases=("teacher_training_preschool", "Teacher training, preschool", "学前教育教师教育", "学前教师培养", "幼儿教育教学"),
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
            "teaching design（教学设计）",
            "implementation（实施）",
            "evaluation（评估）",
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
        "developmental_assessment": "发展评估须区分粗大运动、精细运动、语言、认知与社会性发展维度",
        "play_based_learning": "游戏化教学须描述游戏类型、发展目标、材料准备与观察记录",
        "parent_communication": "家园沟通须描述沟通渠道、频率、内容与安全隐私保护措施",
        "observation": "观察记录须使用标准化观察工具，标注观察情境、时长与行为编码",
    },
    conventions=(
        "发展阶段描述须使用皮亚杰/维果茨基/埃里克森等理论框架，标注具体阶段",
        "发展评估须标注评估工具名称、版本与常模参照",
        "游戏材料须标注安全等级、适龄范围与教育目标",
        "观察记录须使用ABC（前因-行为-后果）格式，标注客观描述与解释区分",
        "家园共育方案须包含家庭活动建议与教师指导策略",
    ),
    key_venues=(
        "Early Childhood Education Journal",
        "Journal of Research in Early Childhood Education",
        "Early Childhood Research Quarterly",
        "Early Education and Development",
        "Young Children",
    ),
    units_and_formulas_notes=(
        "儿童年龄以月龄（月）标注，区分月龄与实足年龄",
        "发展评估须标注常模来源、标准化时间与标准化分数",
        "观察时长以秒/分钟标注，须区分连续观察与时间抽样",
        "游戏材料须标注安全认证（如3C认证）与适龄范围（月）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Moodle", "Canvas", "Google Classroom", "Schoology", "Edmodo", "Blackboard", "PowerSchool", "Brightwheel", "Procare", "Denver Developmental Screening Test", "Assessment of Preschool Competencies", "Early Development Instrument", "Learning Stories", "Play Observation Tool", "Parent Communication Tool", "Child Development Tool", "Early Childhood Education Platform", "Developmental Milestone Tracker", "Early Learning Tool", "Preschool Assessment Tool"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
