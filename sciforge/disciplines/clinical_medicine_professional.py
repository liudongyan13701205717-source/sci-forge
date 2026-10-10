"""临床医学（同时设专业学位类别，代码为1051） 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="clinical_medicine_professional",
    aliases=(
        "临床医学（同时设专业学位类别，代码为1051）",
        "临床医学",
        "Clinical Medicine",
        "临床",
        "内科学",
        "外科学",
        "临床医学研究",
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
        "consort": "随机对照试验须遵循 CONSORT 声明",
        "stard": "诊断试验研究须遵循 STARD 声明",
        "strobe": "观察性研究须遵循 STROBE 声明",
        "prisma": "系统综述须遵循 PRISMA 声明",
        "care": "病例报告须遵循 CARE 声明",
        "ich": "个体患者数据须遵循 ICH E9 声明",
    },
    conventions=(
        "临床试验须在临床试验注册平台（如ClinicalTrials.gov、中国临床试验注册中心）登记并报告注册号",
        "病例对照与横断面研究须报告样本量、入选与排除标准及随访缺失情况",
        "诊断试验研究须遵循STARD声明，观察性研究须遵循STROBE声明，系统综述须遵循PRISMA声明",
        "报告不良事件与患者安全数据须遵循CONSORT声明（针对随机对照试验）",
    ),
    key_venues=(
        "The Lancet",
        "The New England Journal of Medicine",
        "JAMA",
        "The BMJ",
        "中国循环杂志",
        "中华医学杂志",
    ),
    units_and_formulas_notes=(
        "临床计量单位采用国际单位制（SI），血生化浓度以 mmol/L 或 mg/dL 注明",
        "生存分析须报告中位生存时间（月）与 5 年生存率（%），并附 95% 置信区间",
        "效应量须报告 hazard ratio（HR）或 odds ratio（OR）及 95% CI，p 值须双尾检验",
        "剂量-反应关系须注明给药途径、频率与疗程，不良事件按 CTCAE 分级标准报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Stata", "SAS", "Epic", "Cerner", "SAP EHR", "Carevue", "Microsoft Power BI", "Tableau", "Python（pandas/scikit-learn）", "RevMan", "JBI Systematic Review Software", "EndNote", "MetaAnalyst", "Microsoft Excel", "JMP", "REDCap", "Epi Info", "GraphPad Prism"),
    category="医学",
    databases=("OpenAlex",),
)
