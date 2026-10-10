"""Career advising 学科论文支持：职业咨询/生涯辅导体裁、测评量表注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="career_advising",
    aliases=("career advising", "职业咨询", "生涯辅导", "职业规划",
             "career counseling", "career guidance", "career development",
             "生涯规划"),
    paper_types={
        "research": (
            "abstract",
            "introduction（咨询背景与问题）",
            "方法（研究设计与测评工具）",
            "结果（咨询效果与数据）",
            "讨论（咨询实践与改进）",
            "references",
        ),
        "report": (
            "abstract",
            "个案/项目概述",
            "咨询方案与执行",
            "评估与调整",
            "经验总结",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；测评须可复核）",
    reporting_standards={
        "case_study": "个案须说明咨询目标与过程",
        "outcome_report": "结局报告须给出量表前后对比",
        "process_log": "咨询日志须含时间线与频次",
    },
    conventions=(
        "测评量表（MBTI、Strong Interest Inventory、霍兰德等）须标注版本与信效度",
        "咨询理论取向（人本、认知行为、计划理论等）须声明",
        "干预措施须具体可复现",
        "保密与知情同意须说明",
        "术语须与职业咨询界一致",
    ),
    key_venues=(
        "Journal of Vocational Behavior",
        "Career Development International",
        "The Career Development Quarterly",
        "Journal of Career Counseling",
        "Vocational Behavior",
        "Contemporary Career & Technical Education",
    ),
    units_and_formulas_notes=(
        "量表分数须注明满分与计分方式",
        "咨询频次用 次/阶段，须注明",
        "结局指标须给出统计检验（t/卡方）与效应量",
        "统计量给出均值 ± SD 与样本量",
        "引用理论须注明出处与适用条件",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("MBTI 类型指标", "Strong Interest Inventory", "霍兰德职业兴趣测试", "职业测评软件", "SAP SuccessFactors 职业管理", "CareerBuilder 职业评估", "Occupational Outlook Handbook", "SPSS", "R", "Python", "Excel", "GraphPad Prism", "Qualtrics 问卷平台", "NotebookLM", "NVivo", "QResearch", "LinkedIn Learning", "Tableau", "Obsidian", "Compass 职业评估系统"),
    category="教育学",
    databases=("OpenAlex", "CNKI", "Semantic Scholar", "O*NET 职业信息数据库"),
)
