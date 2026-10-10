"""工作生活学科论文支持：工作生活平衡与工作福祉研究、APA 引用样式与员工体验注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="working_life",
    aliases=("working_life", "工作生活", "工作生活平衡", "work-life balance", "work-life integration", "work-life conflict"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "literature review（工作生活研究综述）",
            "methods（方法与设计）",
            "results（结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context（组织情境）",
            "case description（案例描述）",
            "analysis（分析）",
            "implications（意义）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and search（范围与检索）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="APA 第 7 版样式（作者-年份）",
    reporting_standards={
        "worklife_measurement": "工作生活平衡须报告量表、信效度与维度",
        "wellbeing_assessment": "工作福祉须遵循 WHO 定义与评估标准",
        "policy_impact": "工作生活政策须报告实施条件与影响",
        "ethics": "研究伦理审批与知情同意须给出",
        "statistics": "统计检验与样本量须报告",
    },
    conventions=(
        "工作生活平衡与冲突术语区分（balance vs conflict）",
        "工作福祉遵循 WHO/ICNR 等定义",
        "工作生活量表信效度须报告",
        "组织情境描述完整（行业、规模、政策）",
        "工作生活政策须明确实施条件与影响"
    ),
    key_venues=(
        "Journal of Occupational Health Psychology",
        "Journal of Applied Psychology",
        "Journal of Organizational Behavior",
        "Work, Employment and Society",
        "Journal of Managerial Psychology"
    ),
    units_and_formulas_notes=(
        "工作生活平衡用李克特量表（1-5 或 1-7）",
        "工作时间用小时/周表示",
        "样本量 n 与置信区间须给出",
        "p 值用 <0.05/<0.01/<0.001 表示显著性"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Qualtrics", "SurveyMonkey", "SPSS", "Stata", "R (lme4)", "MPlus", "SmartPLS", "NVivo", "Atlas.ti", "Dedoose", "Tableau", "Power BI", "Excel", "Culture Amp", "Officevibe", "BetterWorks", "WorkBright", "15Five", "Lattice", "Glint"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
