"""其他健康科学学科论文支持：未被细类归入的公共卫生与临床辅助健康研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_health_sciences",
    aliases=(
        "other_health_sciences", "其他健康科学",
        "other health sciences", "其他健康科学",
        "health sciences not elsewhere classified", "健康科学未另分类",
        "public health", "公共卫生",
        "health services research", "卫生服务研究",
        "epidemiology", "流行病学",
        "health promotion", "健康促进",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（健康问题与理论背景）",
            "methodology（设计与统计方法）",
            "results（效应估计与结果）",
            "discussion（公共卫生意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（服务对象与场景）",
            "analysis（干预分析与评估）",
            "results（健康结局）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与模型综述）",
            "evidence synthesis（证据综合与质量评估）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "k1": "观察性研究须遵循 STROBE 声明，RCT 须遵循 CONSORT 声明",
        "k2": "系统综述与 Meta 分析须遵循 PRISMA 2020 声明",
        "k3": "诊断准确性研究须遵循 STARD 声明",
    },
    conventions=(
        "研究须报告注册号（如 ClinicalTrials.gov 或 ChiCTR）",
        "结局指标须报告 OR/HR/RR 及 95% CI",
        "样本须报告 N、入选排除标准与失访情况",
        "伦理审查与知情同意须明确说明",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "The Lancet",
        "JAMA",
        "The BMJ",
        "American Journal of Public Health",
        "Preventive Medicine",
        "《中华流行病学杂志》",
    ),
    units_and_formulas_notes=(
        "发病率/患病率注明人口学与时间口径",
        "风险指标用 OR/HR/RR 及 95% CI 报告",
        "时间单位用月或年并注明随访起止",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "Stata", "SAS", "Epi Info", "JMV", "Jamovi", "RevMan", "JBI Systematic Review Software", "CINAHL", "EndNote", "Zotero", "NVivo", "Microsoft Excel", "Tableau", "Power BI", "LaTeX", "OpenEpi", "EpiTools", "REDCap（数据采集）"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "PubMed", "Cochrane Library", "EMBASE"),
)
