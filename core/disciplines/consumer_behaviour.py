"""消费者行为学科论文支持：问卷、实验、眼动与质性研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="consumer_behaviour",
    aliases=(
        "consumer behaviour",
        "consumer behavior",
        "consumer psychology",
        "消费者行为",
        "消费者心理",
        "消费者研究",
        "购买决策",
        "customer behaviour",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与假设）",
            "theory and hypotheses（理论与假设）",
            "study design（研究设计与量表）",
            "results（描述统计、回归、SEM）",
            "discussion",
            "references",
        ),
        "experimental_study": (
            "abstract",
            "introduction",
            "study 1",
            "study 2",
            "general discussion",
            "references",
        ),
        "qualitative_study": (
            "abstract",
            "introduction",
            "data collection（访谈/焦点小组/眼动）",
            "data analysis（编码、主题）",
            "findings",
            "references",
        ),
        "meta_analysis": (
            "abstract",
            "methods（检索、纳入、提取、分析）",
            "results（森林图、异质性、亚组）",
            "discussion",
            "references",
        ),
    },
    citation_style="APA 7 样式，社科类主流规范",
    reporting_standards={
        "survey": "调查研究遵循 AAPOR 报告规范，标注样本量、招募方式与响应率",
        "experiment": "实验研究须报告随机分配、操纵检验与效应量",
        "scale": "量表须报告 Cronbach's α、AVE、CR 与 discriminant validity",
        "SEM": "结构方程模型须报告 CFI、TLI、RMSEA、SRMR 与拟合指标",
        "qualitative": "质性研究遵循 COREQ 或 SRQR 报告规范",
        "meta_analysis": "元分析遵循 PRISMA 声明与 RoB 工具",
    },
    conventions=(
        "遵循 APA 7 报告规范，构念命名与量表版本一致",
        "样本报告 N、招募平台、筛选条件与响应率",
        "量表信效度须报告 Cronbach's α、AVE、CR 与 HTMT",
        "效应量用 Cohen's d、η² 或 R²；显著性用 p<.05 或 .001",
        "缺失数据处理用多重插补或 FIML，须在方法章节说明",
        "预注册研究须在 OSF 或 AsPredicted 平台公开",
    ),
    key_venues=(
        "Journal of Consumer Research",
        "Journal of Consumer Psychology",
        "Journal of Marketing Research",
        "Journal of Consumer Behaviour",
        "Journal of Business Research",
        "Marketing Letters",
        "International Journal of Consumer Studies",
        "中国消费者研究",
        "心理学报",
        "管理世界",
    ),
    units_and_formulas_notes=(
        "连续变量报告 M、SD、95% CI",
        "相关用 r 或 β；效应量 Cohen's d、η²、ω²",
        "序数变量用 Median、IQR 或 Kendall's τ",
        "量表用 5/7 点 Likert；信度 Cronbach's α 或 ω_t",
        "显著性用 p<.05 或 .001，双尾检验默认",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "IBM SPSS Amos", "AMOS", "R", "RStudio", "lavaan", "semTools", "Psych", "Mplus", "LISREL", "Stata", "SAS", "JASP", "JAMovi", "Jasp", "R Commander", "NVivo", "Atlas.ti", "MAXQDA", "Qualtrics", "SurveyMonkey", "Qualtrics XM", "QuestionPro", "LimeSurvey", "Webropol", "Typeform", "Google Forms", "Tobii Pro", "Tobii Pro 5", "Tobii Pro Fusion", "Tobii Pro Lab", "GazeLab", "EyeLink 1000 Plus", "EyeLink Mini", "Pupil Eye Tracker", "iKeyEye", "OpenFace", "FaceReader", "E-Prime", "Inquisit", "PsychoPy", "Qualtrics X", "SurveyLegend 问卷星", "Zutopia", "OSF Pre-Registration", "AsPredicted"),
    category="管理学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Web of Science", "PsycINFO", "Semantic Scholar"),
)
