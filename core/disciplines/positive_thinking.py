"""积极思维学科论文支持：积极心理学取向的思维干预、主观幸福感与认知重评研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="positive_thinking",
    aliases=(
        "positive thinking", "积极思维", "积极思考",
        "positive psychology", "积极心理学",
        "optimism", "乐观主义研究",
        "cognitive reappraisal", "认知重评",
        "gratitude", "感恩干预",
        "subjective well-being",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题与理论依据）",
            "methodology（被试、量表、干预设计与分析）",
            "results（干预前后差异与效应量）",
            "discussion（机制解释与局限性）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（个案背景与基线评估）",
            "analysis（思维模式与行为证据）",
            "results（干预历程与结局）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（积极心理学理论谱系）",
            "evidence synthesis（干预研究证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "CARE（个案报告条目清单）",
        "k2": "CONSORT（随机对照干预试验报告）",
        "k3": "PRISMA（系统综述与 meta 分析）",
    },
    conventions=(
        "干预研究须报告基线测量、干预剂量与随访时点",
        "幸福感量表须注明量表版本与文化常模来源",
        "区分特质性乐观与状态性乐观，避免单一刻画",
        "批判性看待毒鸡汤式乐观偏差，报告效应量而非仅 p 值",
        "伦理与知情同意在在线问卷/远程干预中同样需说明",
    ),
    key_venues=(
        "Journal of Positive Psychology",
        "Journal of Happiness Studies",
        "Positive Psychology (Springer)",
        "Review of General Psychology",
        "Psychological Science",
    ),
    units_and_formulas_notes=(
        "量表得分报告均值与标准差，含理论取值范围",
        "效应量用 Cohen's d 或 Hedges' g，附 95% CI",
        "meta 分析注明合并模型（随机/固定效应）与异质性 I²",
        "心理测量工具须报告内部一致性 Cronbach's α 与信效度证据",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "JASP", "PsychoPy", "Qualtrics", "SurveyMonkey", "PREDICT", "Psytest", "E-Prime", "CogniFlex", "Mental Measurement Centre (MMC)", "Pavilion Software", "NVivo", "ATLAS.ti", "MATLAB", "Python (pandas, statsmodels)", "OpenSesame", "Stata", "Jamovi", "Excel"),
    category="理学",
    databases=("PubMed", "OpenAlex", "CNKI"),
)
