"""职场技能学科论文支持：工作场所技能迁移与职业能力研究、APA 引用样式与能力框架注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="work_place_skills",
    aliases=("work_place_skills", "职场技能", "工作场所技能", "workplace skills", "技能迁移", "employability"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与技能问题）",
            "literature review（技能研究综述）",
            "methods（方法与设计）",
            "results（结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context（职场情境）",
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
        "skills_measurement": "技能测量须报告工具、信度与效度",
        "competency_framework": "能力框架须遵循 ESCO/NVQ 等标准",
        "skills_transfer": "技能迁移须明确情境与条件",
        "ethics": "研究伦理审批与知情同意须给出",
        "statistics": "统计检验与样本量须报告",
    },
    conventions=(
        "技能与能力术语区分（skill vs competency）",
        "能力框架遵循 ESCO/NVQ 等标准",
        "技能测量工具信效度须报告",
        "职场情境描述完整（行业、岗位、任务）",
        "技能迁移须明确条件与情境"
    ),
    key_venues=(
        "Journal of Vocational Behavior",
        "Human Resource Development International",
        "Journal of Workplace Learning",
        "Personnel Psychology",
        "Journal of Applied Psychology"
    ),
    units_and_formulas_notes=(
        "技能水平用李克特量表（1-5 或 1-7）",
        "时间用年/月表示职业发展周期",
        "样本量 n 与置信区间须给出",
        "p 值用 <0.05/<0.01/<0.001 表示显著性"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Qualtrics", "SPSS", "R (lme4)", "Stata", "SmartPLS", "MPlus", "NVivo", "Atlas.ti", "Tableau", "Power BI", "Excel", "SCORM 合规播放器", "ESCO Mapping Tool", "NVQ 技能评估平台", "eAssess", "Articulate Storyline", "LinkedIn Learning", "TalentLMS", "Moodle", "Canvas LMS"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
