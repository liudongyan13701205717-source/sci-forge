"""应用与发展心理学学科论文支持：认知发展、社会认知、教育与发展干预。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="applied_and_developmental_psychology",
    aliases=(
        "applied and developmental psychology",
        "Applied And Developmental Psychology",
        "应用心理学",
        "发展心理学",
        "developmental psychology",
        "applied psychology",
        "儿童发展",
        "儿童青少年心理",
        "教育心理学",
        "cognitive development",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（理论依据与研究问题）",
            "participants（样本构成与伦理审查）",
            "method（任务、程序、材料、测量）",
            "results（描述与推断统计）",
            "discussion（理论联系与实践意义）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical framework",
            "empirical evidence synthesis",
            "future directions",
            "references",
        ),
        "meta_analysis": (
            "abstract",
            "introduction",
            "search strategy",
            "inclusion criteria and screening",
            "statistical analysis（异质性、森林图）",
            "discussion",
            "references",
        ),
    },
    citation_style="APA 7（心理学国际通用）",
    reporting_standards={
        "ethics": "伦理审查批准号与知情同意（未成年人含监护人）须声明",
        "participants": "年龄、性别、教育背景、样本量与纳入/排除标准须披露",
        "measures": "量表名称、信度（α/ω）、效度与既往引用来源须说明",
        "analysis": "假设检验类型、统计软件版本、效应量与置信区间须报告",
        "replication": "研究设计与材料若为独立重复须注明是否预注册（OSF）",
    },
    conventions=(
        "统计量报告 M±SD 或 M（95% CI）；连续变量用 t/ANOVA/回归，分类变量用 χ²/关联",
        "效应量 Cohen's d / η² / Hedges' g；报告 95% CI",
        "量表首次出现给原名与作者年；使用中文译本须注明译者与修订年份",
        "未成年数据须匿名化（化名/编号），避免识别性信息",
        "图表标题中英对照；显著性标记 *p<.05 **p<.01 ***p<.001",
    ),
    key_venues=(
        "Child Development",
        "Developmental Psychology",
        "Journal of Applied Developmental Psychology",
        "Journal of Experimental Child Psychology",
        "Monographs of the Society for Research in Child Development",
        "Developmental Review",
    ),
    units_and_formulas_notes=(
        "反应时 ms；正确率 %；量表得分（分/等级）",
        "年龄 月龄或岁；样本量 n；效应量 Cohen's d / η²",
        "统计软件：SPSS/R/JASP/Mplus/AMOS 版本须注明",
        "信度 α、ω；效度 CFA χ²/CFI/RMSEA",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("E-Prime", "PsychoPy", "OpenSesame", "Qualtrics", "SurveyMonkey", "REDCap", "眼动仪 Tobii", "眼动仪 EyeLink", "脑电 EEG（Brain Products）", "近红外 NIRS（Hitachi/NIRSport）", "功能性 MRI（fMRI）", "ERP 分析 ERPAL", "心理量表 MMPI/BAI/BDI", "SPSS", "R", "JASP", "Jamovi", "Mplus", "AMOS", "Metafor (R)", "Stata", "Excel", "LaTeX", "Zotero"),
    category="教育学",
    databases=("PsycINFO", "PubMed", "Web of Science", "OpenAlex", "Crossref", "CNKI", "万方"),
)
