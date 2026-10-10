"""体育领导学科论文支持：组织治理/教练领导力/体育管理与绩效体裁、APA 7 与 SQUIRE 注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sport_leadership",
    aliases=(
        "sport_leadership",
        "体育领导",
        "Sport Leadership",
        "体育管理",
        "教练领导力",
        "运动队管理",
        "sports management",
        "coaching",
        "体育组织治理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份）",
    reporting_standards={
        "intervention": "SQUIRE 2.0（运动干预与训练方案改进型研究）",
        "systematic_review": "PRISMA",
        "qualitative": "COREQ/SRQR",
    },
    conventions=(
        "领导力理论框架须声明（变革型、道德型、共享、情境领导等）并注明提出者与年份",
        "量表用官方英文简称与版本（如 LSS-44、LQI-40），并附 Cronbach's α",
        "运动队绩效同时报告比赛成绩与技术统计（如有效进攻/防守、投篮命中率）",
        "伦理批准与运动员/教练知情同意须说明，个人信息去标识化",
        "教练与队员关系研究须区分性别、层级（一线教练/助理/主教练）与运动项目",
    ),
    key_venues=(
        "Journal of Sport Management",
        "Sport Management Review",
        "International Sport Studies Journal",
        "Management and Sportology",
        "Journal of Applied Sport Psychology",
    ),
    units_and_formulas_notes=(
        "量表分用 M (SD)，效应量报 Cohen's d 与 95% CI，r 标双尾检验 p 值",
        "比赛数据报 场均值、命中率 %、正负值 +/−",
        "生理负荷标 RPE（Borg 6–20 或 CR10）、心率区间（%HRmax）与心率变异性 HRV",
        "多变量分析报 η²p、F 与 df，模型拟合报 R²、RMSEA、CFI/TLI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "JASP", "AMOS", "Mplus", "NVivo", "ATLAS.ti", "MaxQDA", "Catapult Vector", "Styx 20 生理监测", "Kowa Locus", "Kinexon 惯性传感器", "Dartfish 视频分析", "Hudl Sportscode", "Kinovea 运动分析", "MATLAB", "LaTeX", "EndNote", "Zotero", "Microsoft Excel"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
