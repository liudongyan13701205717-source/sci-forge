"""公共政策研究学科论文支持：政策周期/政策评估/政策实验体裁、PRISMA 与政策分析框架注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="public_policy_studies",
    aliases=("public_policy_studies", "公共政策研究", "政策学", "政策分析", "政策评估", "policy analysis", "policy evaluation"),
    paper_types={
        "research": ("abstract", "introduction（政策问题与背景）", "methodology（政策分析框架）", "results（政策结果）", "discussion（政策含义）", "references"),
        "case_study": ("abstract", "introduction", "case description（政策案例）", "analysis（政策过程分析）", "results（政策效果）", "discussion（经验与教训）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions（政策展望）", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"policy_review": "政策综述遵循 PRISMA 系统综述规范", "policy_evaluation": "政策评估遵循逻辑模型/反事实框架", "policy_experiment": "随机试验遵循 CONSORT 报告"},
    conventions=("政策周期（议程-制定-执行-评估）阶段须明确", "利益相关者与制度环境须交代", "证据等级（实验/准实验/描述）须标注", "政策效果表述区分净效应与毛效应", "数据年份与口径须注明"),
    key_venues=("Journal of Public Policy", "Policy Studies", "Governance", "Public Administration Review", "中国公共政策评论"),
    units_and_formulas_notes=("政策指标给出基线值与变化量（含置信区间）", "评估方法注明反事实构造（DID/RDD/匹配）", "成本效益分析注明贴现率与货币口径", "样本量与失访率须报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Stata", "R", "SPSS", "NVivo", "ATLAS.ti", "Excel", "Tableau", "QGIS", "EViews", "Qualtrics", "SurveyMonkey", "Minitab", "JMP", "Python", "Word", "LaTeX", "EndNote", "Zotero", "PowerPoint", "ArcGIS"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
