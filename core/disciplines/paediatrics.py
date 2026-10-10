"""儿科学学科论文支持：儿童青少年疾病诊断治疗与生长发育评估体裁、儿科临床与诊断试验报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="paediatrics",
    aliases=(
        "paediatrics",
        "儿科学",
        "Paediatrics",
        "Pediatrics",
        "儿科",
        "儿童医学",
        "儿童与青少年健康",
        "新生儿医学",
        "pediatric medicine"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references"
        ),
    },
    citation_style="Vancouver 样式（AMA 风格亦可）",
    reporting_standards={
        "k1": "儿科随机对照试验遵循 CONSORT 声明并注册临床试验",
        "k2": "病例报告遵循 CARE 声明，病例系列遵循 RECAMC 声明",
        "k3": "诊断试验评估遵循 STARD 声明，观察研究遵循 STROBE"
    },
    conventions=(
        "涉及未成年受试须报告伦理批准、监护人同意与儿童 assent",
        "剂量按体重（mg/kg）或体表面积（mg/m²）报告并注明换算依据",
        "生长发育须报告百分位与 Z 值并说明参考人群",
        "新生儿与婴幼儿研究须报告胎龄校正年龄",
        "疫苗研究须报告批次、接种间隔与冷链记录"
    ),
    key_venues=(
        "The Lancet Child & Adolescent Health",
        "Pediatrics",
        "Journal of Pediatrics",
        "BMJ Paediatrics Open",
        "中华儿科杂志"
    ),
    units_and_formulas_notes=(
        "剂量按 mg/kg 或 mg/m² 报告，体表面积按 Mosteller 公式计算",
        "生长指标报告百分位与 Z 值并注明参考人群与年龄校正",
        "血气与电解质使用 SI 单位并注明年龄特异参考区间",
        "时间以小时或天报告，早产儿须校正胎龄"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("RevMan", "JBI Systematic Review Software", "SPSS", "R", "Stata", "GraphPad Prism", "WHO Anthro", "Bayley Scales of Infant Development", "Ages and Stages Questionnaire (ASQ)", "Denver Developmental Screening Test", "PedsQL", "Youth Self-Report (YSR)", "PASI", "CHOM", "儿科肺功能测试仪（Spirometer）", "脉搏血氧仪（儿科型）", "EndNote", "RefWorks", "儿童心脏超声仪", "儿科电子病历系统"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "PubMed", "Cochrane Library"),
)
