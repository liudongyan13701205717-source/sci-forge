"""护理教师教育论文支持：护理教育领域教师培养、模拟教学与临床能力评估的论文写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_in_nursing",
    aliases=("teacher_training_in_nursing", "Teacher training in nursing", "护理教师教育", "护理教育培养", "临床护理教学"),
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
            "teaching implementation（教学实施）",
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
    citation_style="Vancouver",
    reporting_standards={
        "simulation": "模拟教学须描述模拟场景、设备型号、学员背景与观察指标",
        "clinical_skill": "临床技能评估须使用标准化评分量表，标注评分者与评分者间一致性",
        "competency": "能力达标须描述评估维度（知识、技能、态度）与达标标准",
        "ethics": "涉及患者信息须匿名化处理，声明伦理审查与知情同意",
    },
    conventions=(
        "护理操作须按标准流程描述步骤，标注安全注意事项与禁忌",
        "模拟教学须区分高仿真模拟与任务训练模拟，注明模拟设备型号",
        "临床能力评估须使用标准化量表，标注评分者信度与评分者间一致性",
        "患者案例须匿名化处理，隐去姓名、住院号等可识别信息",
        "引用护理指南须标注版本与更新日期，确保使用最新版证据",
    ),
    key_venues=(
        "Journal of Nursing Education",
        "Nurse Education Today",
        "Journal of Advanced Nursing",
        "Nursing Education Perspectives",
        "Clinical Simulation in Nursing",
    ),
    units_and_formulas_notes=(
        "药物剂量以毫克（mg）、毫升（mL）或国际单位（IU）标注，须明确换算关系",
        "生命体征（体温、脉搏、呼吸、血压）须使用国际单位制（SI）",
        "模拟场景描述须标注设备型号、软件版本与场景编号",
        "评分量表须明确评分等级与权重，总分计算方式须详细说明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Skills Tutor", "Laerdal SimMan", "CAE iSimulate", "UWorld", "Kaplan NCLEX", "Elsevier Evolve", "Anki", "Virtual Patient", "SimBox", "NCLEX-RN Prep", "ANCC E-Learning", "Nursing Central", "Clinical Simulation Station", "VR Nursing Simulator", "Patient Simulator", "Clinical Documentation Tool", "Nursing Assessment Tool", "Nursing Informatics System", "Nursing Education Platform", "Skills Assessment Tool"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
