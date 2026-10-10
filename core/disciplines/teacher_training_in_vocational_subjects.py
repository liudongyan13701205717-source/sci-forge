"""职业技能教师教育论文支持：职业培训领域教师培养、技能认证与产教融合教育的论文写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_in_vocational_subjects",
    aliases=("teacher_training_in_vocational_subjects", "Teacher training in vocational subjects", "职业技能教师教育", "职业培训教师培养", "职业技能教学"),
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
            "training design（培训设计）",
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
        "skills_assessment": "技能认证须描述评估维度（理论、实操、综合应用）与达标标准",
        "curriculum_alignment": "课程须与企业岗位需求对齐，标注能力矩阵与行业认证",
        "industry_integration": "产教融合须描述企业参与方式、实习基地与双师型教师安排",
        "competency_framework": "能力框架须引用国家标准或行业标准，标注版本与适用范围",
    },
    conventions=(
        "技能名称须使用职业分类标准（如国家标准职业分类大典），中英文对照",
        "实训项目须标注设备型号、技术参数与安全操作规程",
        "能力达标须区分理论考核与实操考核，标注评分权重",
        "企业案例须注明企业名称（可匿名）、行业类别与岗位名称",
        "培训效果须描述培训前/培训后评估方式，标注统计检验方法",
    ),
    key_venues=(
        "Journal of Vocational Education and Training",
        "Vocational Training and Education",
        "Journal of Workplace Learning",
        "Education + Training",
        "International Journal of Lifelong Education",
    ),
    units_and_formulas_notes=(
        "能力标准须引用国家职业标准或行业标准的版本与编号",
        "实训设备须标注型号、量程、精度与校准有效期",
        "培训时长以学时（学时=45分钟）标注，区分理论学时与实操学时",
        "评估结果须报告原始分、百分位与等级判定标准",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Moodle", "Canvas", "Blackboard", "Coursera", "LinkedIn Learning", "Udemy", "Siemens PLC", "Fanuc CNC", "Industrial Automation Tool", "VR Training Platform", "Skills Assessment Tool", "Training Management System", "e-Learning Platform", "Skills Verification Tool", "Industry 4.0 Platform", "Simulation Platform", "AR Training Platform", "Vocational Training Tool", "Skill Verification Platform", "Competency Assessment Tool"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
