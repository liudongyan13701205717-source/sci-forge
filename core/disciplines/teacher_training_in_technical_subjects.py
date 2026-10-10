"""技术学科教师教育论文支持：工程技术教育领域教师培养、实践课程设计与技能评估的论文写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_in_technical_subjects",
    aliases=("teacher_training_in_technical_subjects", "Teacher training in technical subjects", "技术学科教师教育", "工程技术教师培养", "技术教学"),
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
            "project design（项目设计）",
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
    citation_style="IEEE",
    reporting_standards={
        "project_design": "实践项目须描述技术目标、约束条件、评估标准与安全要求",
        "lab_instruction": "实验指导须包含设备清单、操作步骤、数据记录与安全注意事项",
        "skill_assessment": "技能评估须使用实操考核与理论测试相结合，标注评分标准",
        "safety": "涉及危险操作须声明安全预案、防护设备与应急预案",
    },
    conventions=(
        "技术术语须使用行业标准术语，英文缩写须首次出现时标注全称",
        "实验数据须标注仪器型号、量程、精度与校准信息",
        "电路图与程序代码须附完整清单与版本说明，确保可复现",
        "模拟软件输出须标注参数设定、边界条件与仿真时间步长",
        "安全注意事项须前置标注，使用警示符号（⚠️）突出显示",
    ),
    key_venues=(
        "Journal of Engineering Education",
        "IEEE Transactions on Education",
        "International Journal of Engineering Education",
        "Journal of Pre-Engineering Research",
        "Engineering Science and Technology",
    ),
    units_and_formulas_notes=(
        "物理量须使用国际单位制（SI），非SI单位须标注换算关系",
        "测量精度须标注不确定度（绝对误差、相对误差或置信区间）",
        "程序代码须使用缩进对齐，关键算法须附伪代码或流程图",
        "模拟输出须注明初始条件、边界条件、时间步长与收敛判据",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "AutoCAD", "SolidWorks", "ANSYS", "NX", "CATIA", "Fusion 360", "Simulink", "Proteus", "LabVIEW", "Keil", "Multisim", "PSpice", "OpenModelica", "Python", "TensorFlow", "ROS", "Unity", "Arduino", "Raspberry Pi"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
