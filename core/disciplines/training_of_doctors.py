"""医师规范化培训学科论文支持：住院医师规范化培训/临床技能评估体裁、AAPC/ACGME 与模拟训练注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="training_of_doctors",
    aliases=("training_of_doctors", "医师规范化培训", "住院医师培训",
             "住院医师规范化培训", "临床医师培养",
             "residency training", "residency education", "postgraduate medical training",
             "clinical training", "doctor training"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "methods（培训项目描述、样本与评估工具）",
            "results（技能与知识评估数据）",
            "discussion（培训效果与改进建议）",
            "references",
        ),
        "program_evaluation": (
            "abstract",
            "introduction",
            "program description",
            "evaluation framework（如 Miller 金字塔）",
            "results",
            "discussion（局限与改进）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "clinical scenario and learning objectives",
            "intervention and simulation",
            "debriefing and reflection",
            "references",
        ),
    },
    citation_style="Vancouver 或 APA 7",
    reporting_standards={
        "simulation": "模拟教学须遵循 DOPS/mini-CEX/OSCE 等评估工具规范",
        "curriculum": "课程开发遵循 Miller 能力金字塔（knows→does→practice）",
        "evaluation": "培训评估须报告评估工具信效度",
        "program_effectiveness": "项目效果评估须报告前测/后测与对照",
    },
    conventions=(
        "临床技能术语须按专科规范（如 ACGME 能力框架）标注",
        "评估工具须注明名称、版本与信效度来源",
        "模拟场景须报告难度分级与评估标准",
        "统计结果给出均值 ± SD 与样本量",
        "培训方案须说明学习迁移与维持策略",
    ),
    key_venues=(
        "Academic Medicine",
        "Medical Education",
        "BMC Medical Education",
        "中国医科大学学报",
        "中华医学教育杂志",
        "SimulHealthc",
    ),
    units_and_formulas_notes=(
        "技能评分用 1-5 或 1-9 量表报告，须注明评分标准",
        "培训前后差异用均值 ± SD 与效应量（Cohen's d）报告",
        "OSCE 工作站得分须注明时间限制与评分细则",
        "统计检验须报告 α 水平与多重校正方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("高仿真模拟人", "手术模拟器", "腹腔镜模拟器", "超声探头模拟器", "心肺复苏训练器", "插管训练模型", "内镜模拟训练系统", "虚拟手术平台", "解剖学虚拟仿真系统", "医学知识图谱系统", "临床决策支持系统", "病例讨论系统", "住院医师规范化培训管理平台", "出科考核系统", "360 评估系统", "学习管理系统（LMS）", "SPSS", "NVivo", "R", "Excel"),
    category="医学",
    databases=("PubMed", "CNKI", "OpenAlex", "万方", "ERIC"),
)
