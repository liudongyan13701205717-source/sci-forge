"""Survey design 学科论文支持：问卷设计/抽样框/信效度/数据分析。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="survey_design",
    aliases=(
        "survey_design", "Survey design", "调查设计",
        "问卷设计", "调研设计", "社会调查",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methods（抽样框与问卷设计）",
            "results（调查结果与数据分析）",
            "discussion（讨论与政策建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（调查区域与对象）",
            "analysis（问卷设计与实施）",
            "results（调查结果）",
            "discussion",
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
    citation_style="APA 7（作者-年份；括号式）",
    reporting_standards={
        "sampling": "抽样须报告抽样框、抽样方法、样本量与响应率",
        "questionnaire": "问卷须报告量表来源、改编说明与预试验",
        "psychometric": "量表须报告 Cronbach's α、CR 与 AVE",
        "data_collection": "数据收集须报告时间节点、调查员培训与质量控制",
    },
    conventions=(
        "问卷题目须用统一编号（Q1, Q2, ...）",
        "量表类型（Likert/Rank/Checklist）须注明",
        "样本量计算须报告置信水平与误差范围",
        "缺失值处理须报告方法（删除/插补/多重插补）",
        "伦理审批与知情同意须声明",
    ),
    key_venues=(
        "Public Opinion Quarterly",
        "Survey Research Methods",
        "Journal of Official Statistics",
        "中国民意",
        "社会调查研究与教育",
    ),
    units_and_formulas_notes=(
        "响应率用 %；置信水平用 %",
        "抽样误差用 百分点",
        "信度系数用 Cronbach's α（0-1）",
        "效度指标用 CR/AVE（标准化载荷平方均值）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("问卷星（在线问卷平台）", "Qualtrics（调研管理平台）", "SurveyMonkey（在线问卷）", "SPSS（统计分析与信效度）", "AMOS（结构方程模型）", "R（统计建模）", "Stata（统计建模）", "Mplus（潜变量模型）", "NVivo（定性分析）", "MAXQDA（质性研究）", "ATLAS.ti（定性分析）", "SurveyCTO（在线随机抽样调查）", "KoboToolbox（移动调研采集）", "G*Power（样本量计算）", "项目反应理论（IRT）软件", "抽样框构建工具（Excel）", "问卷预试验平台", "统计建模软件（Mplus）", "信效度分析工具（Cronbach's α/CR）", "数据采集系统（ODK Collect）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
