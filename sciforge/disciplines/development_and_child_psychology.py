"""发展与儿童心理学学科论文支持：认知/情绪/社会性发展研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="development_and_child_psychology",
    aliases=(
        "development_and_child_psychology", "发展与儿童心理学",
        "developmental psychology", "发展心理学",
        "child psychology", "儿童心理学",
        "cognitive development", "认知发展",
        "social development", "社会性发展",
        "emotional development", "情绪发展",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（发展问题与理论背景）",
            "method（参与者、任务/测量、程序、伦理）",
            "results（描述性统计与推断统计）",
            "discussion（发展规律与理论意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（个案背景与评估）",
            "intervention（干预方案）",
            "outcome（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical overview（发展理论脉络）",
            "main findings（主要发现）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "empirical": "报告遵循 APA 第 7 版规范",
        "ethics": "儿童研究须声明 IRB 批准与家长知情同意",
        "measurement": "量表须注明信效度指标（α、Cronbach's alpha）",
        "developmental": "年龄分组须注明月龄/岁与抽样方法",
        "statistical": "报告 t/F/χ² 值、p 值、效应量（d/η²）",
    },
    conventions=(
        "年龄描述用 岁 x 月 格式（如 3 岁 6 个月）",
        "参与者信息须匿名化处理（代号标识）",
        "量表首次出现给出中英文全称与信度指标",
        "发育评估注明工具名称与标准化年份",
        "干预研究须注明干预频率、时长与随访时间",
    ),
    key_venues=(
        "Child Development",
        "Developmental Psychology",
        "Monographs of the Society for Research in Child Development",
        "Journal of Experimental Child Psychology",
        "Developmental and Psychopathology",
        "Journal of Child Psychology and Psychiatry",
    ),
    units_and_formulas_notes=(
        "年龄用 岁 x 月 表示",
        "得分用 原始分/标准分/Z 分数 表示",
        "效应量用 Cohen's d 或 η² 表示",
        "统计检验注明 α=0.05 与双尾/单尾",
        "相关系数用 Pearson r 或 Spearman ρ",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "PsychoPy", "OpenSesame", "E-Prime", "G*Power", "AMOS", "Mplus", "HLM", "NLSY", "Cognitive Task Analysis", "Eye Tracking Software", "Matlab", "Sage Stats", "Python (pandas, scikit-learn)", "Microsoft Excel", "Weibel Saccade Tracker", "Tobii Eye Tracker", "Barnes & Noble Early Childhood Curriculum"),
    category="理学",
    databases=("PubMed", "OpenAlex", "CNKI", "PsycINFO", "Google Scholar"),
)
