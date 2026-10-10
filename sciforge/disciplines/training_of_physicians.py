"""医师培训学科论文支持：继续教育/专科培训/临床能力发展体裁、ACGME/AAPC 与评估注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="training_of_physicians",
    aliases=("training_of_physicians", "医师培训", "医师继续教育",
             "专科医师培训", "医生培养",
             "physician training", "medical education", "continuing medical education",
             "specialty training", "physician development", "CME",
             "专科医师规范化培训"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "methods（培训项目描述、样本与评估工具）",
            "results（知识、技能与态度评估数据）",
            "discussion（培训效果与改进建议）",
            "references",
        ),
        "program_evaluation": (
            "abstract",
            "introduction",
            "program description",
            "evaluation framework（Miller 金字塔 / ACGME 六大核心能力）",
            "results",
            "discussion（局限与改进）",
            "references",
        ),
        "simulation_based": (
            "abstract",
            "introduction",
            "simulation scenario and learning objectives",
            "intervention and debriefing",
            "outcomes",
            "references",
        ),
    },
    citation_style="Vancouver 或 APA 7",
    reporting_standards={
        "simulation": "模拟教学须遵循 DOPS/mini-CEX/OSCE 评估规范",
        "curriculum": "课程开发遵循 ACGME 六大核心能力框架",
        "cme": "继续教育须报告学分类型与有效期",
        "evaluation": "培训评估须报告工具信效度与前测/后测对照",
    },
    conventions=(
        "临床能力术语须按专科核心能力框架统一标注",
        "评估工具须注明名称、版本与信效度来源",
        "模拟场景须报告难度分级与评估标准",
        "统计结果给出均值 ± SD 与样本量",
        "培训方案须说明学习迁移与持续改进机制",
    ),
    key_venues=(
        "Academic Medicine",
        "Medical Education",
        "BMC Medical Education",
        "Perspectives on Medical Education",
        "中华医学教育杂志",
        "中国医学教育技术",
    ),
    units_and_formulas_notes=(
        "能力评分用 1-5 或 1-9 量表报告，须注明评分标准",
        "培训前后差异用均值 ± SD 与效应量（Cohen's d）报告",
        "OSCE 得分须注明时间限制与评分细则",
        "统计检验须报告 α 水平与多重校正方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("高仿真模拟人", "手术模拟器", "腹腔镜模拟训练系统", "超声模拟训练系统", "虚拟手术平台", "手术视频教学平台", "医学知识图谱系统", "临床路径管理平台", "医师继续教育学分管理系统", "临床技能考核系统", "病例讨论系统", "多学科会诊系统", "医患沟通训练系统", "360 评估系统", "学习管理系统（LMS）", "SPSS", "NVivo", "R", "Excel", "Canva"),
    category="医学",
    databases=("PubMed", "CNKI", "OpenAlex", "万方", "ERIC"),
)
