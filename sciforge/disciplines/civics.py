"""Civics 学科论文支持：公民教育/公民学/宪法学/公共生活体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="civics",
    aliases=(
        "Civics", "civics", "civics education", "civic education",
        "civic engagement", "civic studies",
        "公民教育", "公民学", "公民素养", "公共生活", "公民参与",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（公民教育的价值/问题/理论框架）",
            "methodology（质性、量化、政策文本、课堂观察）",
            "findings",
            "discussion",
            "conclusion",
            "references",
        ),
        "policy_analysis": (
            "abstract",
            "introduction",
            "policy_context",
            "policy_analysis",
            "recommendations",
            "references",
        ),
        "curriculum_studies": (
            "abstract",
            "introduction",
            "curriculum_description",
            "analysis",
            "pedagogical_implications",
            "references",
        ),
    },
    citation_style="APA 7 样式（政策/法律论著亦常见 Chicago 或 Bluebook）",
    reporting_standards={
        "curriculum": "课程标准引用官方文本版本与年份（如《义务教育品德与社会课程标准（2022 版）》）",
        "survey": "问卷遵循 IRB 审查；量表报告 Cronbach's α 与效度证据",
        "policymaking": "政策建议附成本/收益与实施路径",
        "case_study": "案例给出地域、时间、参与者与背景",
        "classroom_observation": "课堂观察报告观察者背景与三角验证策略",
    },
    conventions=(
        "法律条文引用采用「《法律名》第 X 条」格式；宪法条文引用给出最新版本",
        "公民概念（公民、公民权、公民身份、共同体）首次出现定义并与相关概念区分",
        "价值概念（自由、平等、正义、民主、法治）引用权威来源并标注学派",
        "教育实验报告样本量、班级数、学期数、评价工具与评分一致性",
        "问卷量表报告项目数、Likert 等级、Cronbach's α 与因子分析结果",
    ),
    key_venues=(
        "Journal of Civic Education",
        "Political Studies Review",
        "Journal of Policy Studies",
        "Educational Researcher",
        "Philosophy & Social Criticism",
        "Journal of Legal Studies Education",
        "教学与管理",
    ),
    units_and_formulas_notes=(
        "教育实验报告样本量 n；班级数；学期数；教学时数 h",
        "量表 Likert 5/7 分；报告 Cronbach's α、因子载荷与信度",
        "政策文本引用给出文号与发布机关",
        "统计报告 p 值、95% CI、效应量（Cohen's d、η²）",
        "质性分析给出访谈时长、参与者数量与主题编码树",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "Dedoose", "Atlas.ti", "MAXQDA", "NVivo Transcription", "SPSS Statistics", "Stata", "R 统计软件", "JASP", "AMOS", "Mplus", "HARMONY", "ConQuest（IRT）", "NetLogo", "Gephi", "VosViewer", "Papers with Code", "OSF 预注册", "REDcap（数据采集）", "Qualtrics（在线问卷）", "问卷星（中文在线问卷）", "Adobe Acrobat Pro", "LaTeX", "EndNote", "Zotero", "Mendeley", "Microsoft Forms", "SurveyMonkey", "Google Forms", "ClassIn（课堂互动）", "智慧树", "超星尔雅", "雨课堂"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "SSCI"),
)
