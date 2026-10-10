"""社会科学、新闻学与传播学科论文支持：新闻研究/媒介分析/话语研究体裁、Chicago 引用样式与内容分析规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_sciences_journalism_and",
    aliases=("social_sciences_journalism_and", "社会科学、新闻学与传播", "新闻学", "传播学", "journalism studies", "communication studies", "media studies", "media and communication"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与媒介/话语框架）",
            "methods（数据、语料、编码、模型）",
            "results（结果与稳健性）",
            "discussion（讨论与媒介含义）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（媒介事件、报道与平台）",
            "analysis（话语、文本与内容分析）",
            "results",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "literature search（文献检索）",
            "evidence synthesis（跨案例媒介证据综合）",
            "future directions",
            "references"
        )
    },
    citation_style="Chicago 作者-年份（Journalism Studies 遵循 Chicago；Media, Culture & Society 遵循 APA 7）",
    reporting_standards={
        "content_analysis": "内容分析遵循 Manifestation & Interpretation 规范：编码手册、样本选择、编码者信度（Kappa）",
        "interviews": "新闻从业者/受众访谈遵循 COREQ 清单：抽样、访谈时长、反思性",
        "digital_methods": "数字媒介研究遵循 Computational Social Science 透明性原则：爬虫参数、去标识化、平台条款遵从",
        "mixed_methods": "混合设计用联合展示表整合量化编码与质性叙述"
    },
    conventions=(
        "语料采集须报告：平台、时间窗口、检索式、爬取参数与去重策略",
        "编码手册给出操作化定义、示例、Kappa 值；分歧须在附录展示",
        "新闻学伦理须报告：知情同意、二次利用许可、平台条款遵从",
        "定量表格三线制；类别变量给频数与百分比（注明基数 N）",
        "视觉与听觉材料使用截图/音频片段，标注时间戳与来源"
    ),
    key_venues=(
        "Journalism Studies",
        "New Media & Society",
        "Media, Culture & Society",
        "Journal of Communication",
        "Communication Studies"
    ),
    units_and_formulas_notes=(
        "语料规模（文章数、字符数、时长）须在方法中报告；编码频次给出百分比与基数",
        "Cohen's Kappa 与 Krippendorff's Alpha 分别用于两名与多名编码者",
        "样本权重、去重策略、平台 API 限制须声明",
        "百分比给出基数 N；定量表三线制"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo", "MAXQDA", "Dedoose", "ATLAS.ti", "Transana", "SPSS", "R", "Stata", "Python", "Tableau", "Power BI", "Adobe InDesign", "Adobe Premiere Pro", "DaVinci Resolve", "Final Cut Pro", "Grammarly", "ProWritingAid", "BuzzSumo", "Meltwater", "Scrapy"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI")
)
