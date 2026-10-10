"""社会工作与辅导学科论文支持：干预/辅导/评估体裁、APA 7 引用样式与咨询伦理注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_work_and_counselling",
    aliases=("social_work_and_counselling", "社会工作与辅导", "社会工作与咨询", "个案辅导", "咨询辅导", "辅导教育"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7（作者-年份，如 Smith, 2020；悬挂缩进；p 值去前导零）",
    reporting_standards={
        "ethics": "伦理审查批准号、知情同意与被访者隐私保护须报告",
        "intervention": "辅导方案手册化、疗程次数与保真度须说明",
        "measurement": "量表须注明条目数、计分方向与信度（Cronbach's α/ω）",
    },
    conventions=(
        "案例叙述去标识化，代号规则全文一致",
        "干预过程按阶段（接案/评估/介入/结案）时序呈现",
        "多重关系与利益冲突须声明",
        "辅导结局区分症状改善与功能恢复两个维度",
        "量表版本与常模来源必须标注",
    ),
    key_venues=(
        "Australian Journal of Social Work",
        "Journal of Social Work in Collegiate Settings",
        "Counselling and Psychotherapy Research",
        "British Journal of Social Work",
        "Research on Social Work Practice",
    ),
    units_and_formulas_notes=(
        "量表分数给原始分、标准分与理论范围",
        "统计量给 M/SD/SE/95% CI",
        "前后测比较给配对 t 检验、效应量（Cohen's d）与显著性",
        "流失样本按阶段报告，并说明缺失机制处理",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("StatCrunch", "R", "G*Power", "PSPP", "JASP", "SurveyMonkey", "Google Forms", "OpenRefine", "RefWorks", "EndNote", "LaTeX", "Microsoft OneNote", "REDCap", "Kognito", "NVivo", "SimplePractice", "MyCounselor", "Karon Health", "Sycamore Health", "TherapyNote"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
