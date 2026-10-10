"""Aboriginal And Torres Strait Islander Health And Wellbeing 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aboriginal_and_torres_strait_islander_health_and_wellbeing",
    aliases=(
        "Aboriginal And Torres Strait Islander Health And Wellbeing",
        "原住民健康与福祉",
        "ATSI Health",
        "Indigenous Health",
        "First Nations Health",
        "Aboriginal Health",
        "Torres Strait Islander Health",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA",
    reporting_standards={
        "ocap": "原住民健康数据须遵循 OCAP 原则（所有权、控制权、获取权、占有权）",
        "strobe": "流行病学与观察性研究须遵循 STROBE 声明",
        "consort": "随机对照试验须遵循 CONSORT 声明",
        "care": "原住民数据治理须遵循 CARE 原则（集体性、代理权、互惠、伦理）",
        "indigenous_ethics": "研究须遵循澳大利亚原住民研究伦理指南",
    },
    conventions=(
        "健康研究须遵循OCAP原则及澳大利亚原住民研究伦理指南",
        "社区参与式研究须明确反映原住民决策者（community-controlled）角色",
        "流行病学数据须结合社会决定因素（SDOH）与文化背景进行解释",
        "涉及心理健康须尊重原住民文化对精神与情感健康的理解",
    ),
    key_venues=(
        "Australian and New Zealand Journal of Public Health",
        "Medical Journal of Australia",
        "International Journal for Equity in Health",
        "Health & Transformation",
        "Australian Journal of Primary Health",
        "The Lancet Public Health",
    ),
    units_and_formulas_notes=(
        "患病率与发病率以每千人（per 1000）或每十万人（per 100,000）计量，须注明年龄标准化方法",
        "健康不平等指标须报告风险比（RR）或标准化比例比（SPR）及 95% CI",
        "社会决定因素（SDOH）须报告收入五分位数、教育程度与原住民地域等级（REOGA）",
        "生活质量评估须注明量表（如 SF-36、EQ-5D）与评分时间窗，儿童健康数据须单独标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Stata", "SAS", "NVivo", "JASP", "Microsoft Excel", "EndNote", "RevMan", "JBI Systematic Review Software", "SurveyMonkey", "Qualtrics", "Google Forms", "Tableau", "Microsoft Power BI", "MetaAnalyst", "REDCap", "Epi Info", "Python（pandas/statsmodels）", "ArcGIS"),
    category="医学",
    databases=("OpenAlex",),
)
