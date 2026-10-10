"""商业学科教师教育论文支持：商科教育领域教师培养、课程设计与教学评估的论文写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_in_commercial_subjects",
    aliases=("teacher_training_in_commercial_subjects", "Teacher training in commercial subjects", "商业学科教师教育", "商科教师培养", "商务教育"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "literature review（文献综述）",
            "methods（方法设计）",
            "results（结果）",
            "discussion（讨论与启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景）",
            "teaching implementation（教学实施）",
            "evaluation results（评估结果）",
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
        "teaching_effectiveness": "教学成效评估须包含量化指标（学生成绩、满意度等）与质性分析相结合",
        "curriculum_design": "课程设计须说明目标受众、能力层次、课时安排与评估方式",
        "practice_integration": "实践环节须描述模拟环境、数据来源、行业专家参与方式与反馈机制",
        "ethics_statement": "涉及商业数据或学生隐私时须声明数据处理与知情同意方式",
    },
    conventions=(
        "商科案例教学须标注案例来源与改编程度，区分原创案例与改编案例",
        "财务模型与模拟软件输出须附参数设定与假设说明",
        "统计推断须注明显著性水平与置信区间，报告效应量而非仅p值",
        "引用真实企业数据时须隐去可识别信息，以匿名化处理方式呈现",
        "图表编号按出现顺序连续编号，标题置于图表下方，单位须明确标注",
    ),
    key_venues=(
        "Journal of Business Case Studies",
        "Academy of Education Leadership",
        "Journal of Management Education",
        "International Journal of Teaching and Learning in Higher Education",
        "Journal of Educational Technology",
    ),
    units_and_formulas_notes=(
        "财务模型中货币单位须统一标注（如人民币元、美元），避免混用",
        "收益率、增长率等比率指标须明确标注百分比或小数形式",
        "模拟软件输出参数须注明初始值、边界条件与随机种子",
        "统计检验的显著性水平须全文统一（通常α=0.05），并在方法部分声明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Excel", "SPSS", "Stata", "R", "Python", "MATLAB", "Power BI", "Tableau", "Google Sheets", "VBA", "EViews", "RAS", "OpenRefine", "LaTeX", "NVivo", "Qualtrics", "Google Slides", "JASP", "Tableau Prep", "Julia"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
