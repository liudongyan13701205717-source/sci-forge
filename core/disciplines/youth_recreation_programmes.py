"""青少年娱乐项目学科论文支持：社区娱乐与课外活动研究、APA 引用样式与项目评估注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="youth_recreation_programmes",
    aliases=("youth_recreation_programmes", "青少年娱乐项目", "青年休闲项目", "youth recreation", "extracurricular activities"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与项目问题）",
            "literature review（娱乐项目研究综述）",
            "methods（方法与设计）",
            "results（结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "program_evaluation": (
            "abstract",
            "introduction",
            "program description（项目描述）",
            "evaluation framework（评估框架）",
            "data collection（数据收集）",
            "findings（发现）",
            "recommendations（建议）",
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
        "program_design": "项目设计须报告目标、内容、对象与情境",
        "outcome_measurement": "成果测量须报告指标、工具与信效度",
        "participation": "参与情况须报告人数、时长与频率",
        "ethics": "青少年研究伦理审批与知情同意须给出",
        "statistics": "统计检验与样本量须报告",
    },
    conventions=(
        "项目类型遵循休闲娱乐/体育/艺术/学术等分类",
        "项目评估遵循逻辑模型（input-activity-output-outcome）",
        "成果测量工具信效度须报告",
        "青少年参与情况须完整报告",
        "项目情境描述完整（社区、年龄、文化）"
    ),
    key_venues=(
        "Journal of Youth and Adolescence",
        "Youth Protection Bulletin",
        "Journal of Park, Recreation and Tourism Impacts",
        "Journal of Outdoor Recreation, Education, and Leadership",
        "Journal of Leisure Research"
    ),
    units_and_formulas_notes=(
        "项目参与用小时/周表示",
        "成果测量用李克特量表（1-5 或 1-7）",
        "样本量 n 与置信区间须给出",
        "p 值用 <0.05/<0.01/<0.001 表示显著性"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Qualtrics", "SurveyMonkey", "SPSS", "R (lme4)", "Stata", "NVivo", "Atlas.ti", "MAXQDA", "Tableau", "Excel", "iRec (社区娱乐管理平台)", "Elmer (娱乐软件)", "ClubExpress", "TeamSnap", "SportsEngine", "LeagueLineup", "Squadhelp", "SportyCoach", "TeamUp", "MyClubhouse"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
