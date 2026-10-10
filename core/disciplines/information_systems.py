"""信息系统学科论文支持：IS 研究方法与行动研究体裁、APA 引用样式与 IS 记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="information_systems",
    aliases=("information_systems", "信息系统", "IS", "管理信息系统", "MIS", "信息系统研究", "企业信息系统", "信息系统管理", "digital transformation", "信息治理"),
    paper_types={
        "research": ("abstract", "introduction（现象与理论贡献）", "methodology（研究设计与数据采集）", "results（假设检验结果）", "discussion（理论与实践启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（组织/系统背景）", "analysis（理论框架分析）", "results（发现与命题）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（IS 理论谱系）", "evidence synthesis（实证证据综述）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"positivist": "量化研究须报告样本量、信效度与假设检验", "design_science": "设计科学须说明工件、评价与理论化环节", "mixed_methods": "混合方法须说明数据整合策略与序列"},
    conventions=("理论贡献须明确（模型/机制/边界条件）", "研究设计须声明验证范式与抽样", "量表题项与信度系数（Cronbach α）须报告", "组织情境脱敏处理", "效应量与 CI 与 p 值并列报告"),
    key_venues=("MIS Quarterly", "Information Systems Research", "European Journal of Information Systems", "Journal of the Association for Information Systems", "Information & Management"),
    units_and_formulas_notes=("统计检验方法（SEM/Logit/PLS）须声明", "模型拟合指标报告完整", "百分比/比率注明分母口径", "公式用 amsmath；潜变量记法一致"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "AMOS", "SmartPLS", "Stata", "NVivo", "R (lavaan/plssem)", "Mplus", "G*Power", "Python (Pandas/SciPy)", "Qualtrics", "JMP", "ATLAS.ti", "Dedoose", "Minitab", "OpenRefine", "Zotero", "JASP", "Harvard Case Study Repository", "Qualtrics Survey", "IBM SPSS Sampling"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
