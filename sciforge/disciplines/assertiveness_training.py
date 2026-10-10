"""Assertiveness training 学科论文支持：行为/认知心理学的自我主张技能训练、人际效能与情绪表达训练研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="assertiveness_training",
    aliases=(
        "assertiveness_training",
        "assertiveness training",
        "自我主张训练",
        "断言训练",
        "assertive behavior",
        "interpersonal skills training",
        "沟通技能训练",
        "assertiveness therapy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "method（被试、干预、测量、伦理与随机化）",
            "results（描述性、组间比较、随访）",
            "discussion",
            "conclusion",
            "references",
        ),
        "meta_analysis": (
            "abstract",
            "introduction",
            "search and eligibility",
            "study characteristics",
            "meta-analysis results（效应量、异质性）",
            "discussion",
            "limitations",
            "references",
        ),
        "intervention_report": (
            "abstract",
            "rationale",
            "protocol",
            "implementation and fidelity",
            "outcomes",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7th",
    reporting_standards={
        "intervention": "干预方案、剂量（次数/时长）、提供者资质、实施保真度须完整报告",
        "measures": "量表名称、版本、维度、信度（α、Cronbach's α）与效度证据须报告",
        "participants": "样本量、纳入排除标准、脱落率与随访比例须报告",
        "randomization": "随机分配方法、盲法（评估者/被试）与组间基线须报告",
        "ethics": "伦理审批、知情同意与替代方案须报告；IRB 编号给出",
        "outcomes": "主要结局、次要结局与效应量（Cohen's d / η²p）须报告并附 95% CI",
    },
    conventions=(
        "量表首次出现给出全称、缩写与版本（如 SASS, Roster & Muncer 1997）；量表条目数与得分范围须注明",
        "统计报告：t/χ²/F 值、自由度、P 值、效应量与 95% CI 完整；α 值统一 0.05 或预先声明",
        "组间差异用均值±SD 或中位数(IQR)；组内比较给配对 t 与 Wilcoxon",
        "干预与对照流程用流程图（CONSORT 声明）；缺失数据处理策略（MI、MMRM）须报告",
        "量表引用给出版权/许可信息；二次使用须标注许可类型",
        "结论段须明确外部效度、临床意义与实践建议",
    ),
    key_venues=(
        "Journal of Consulting and Clinical Psychology",
        "Behavior Therapy",
        "Journal of Behavior Therapy and Experimental Psychiatry",
        "Clinical Psychology Review",
        "Clinical Psychology: Science and Practice",
        "Personality and Social Psychology Bulletin",
        "Cognitive Therapy and Research",
    ),
    units_and_formulas_notes=(
        "P 值报告格式统一：P < 0.001 / P = 0.032",
        "效应量：Cohen's d / η²p / dz；小/中/大按 0.2 / 0.5 / 0.8 参考",
        "量表分给出满分与计分方式（0–4、1–5、Likert）",
        "α 值预先声明；多重比较校正（Bonferroni / FDR）须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("IBM SPSS Statistics", "PSPP", "RStudio / R", "JASP", "Jamovi", "Qualtrics", "SurveyMonkey", "REDCap", "NVivo", "MAXQDA", "ATLAS.ti", "QDA Miner", "PsychoPy", "Cedrus E-Prime", "Cedrus Inquisit", "Lighthouse Scientific", "G*Power", "OpenSesame", "SASS (Self-Assessment of Assertiveness)", "Interpersonal Performance Program (IIP)", "STAR-ICE", "Behavioral Skills Rating (BSR)", "Zotero", "EndNote"),
    category="理学",
    databases=("OpenAlex", "PubMed", "PsycINFO", "PsycARTICLES", "Cochrane Library", "PROSPERO"),
)
