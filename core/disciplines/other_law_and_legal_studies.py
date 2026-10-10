"""其他法学与法律研究学科论文支持：非主流法学分支：法理、比较法、法律实证与新兴领域。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_law_and_legal_studies",
    aliases=("Other Law And Legal Studies", "其他法学与法律研究", "Comparative Law", "Jurisprudence", "Legal Philosophy", "Law And Economics", "Environmental Law", "Legal Research"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（研究结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Bluebook / OSCOLA",
    reporting_standards={
        "k1": "定量法研究遵循SRA（Standard Reporting Practices）", "k2": "系统性文献综述遵循PRISMA筛选流程", "k3": "实证法研究遵循REVIEW实证报告规范"
    },
    conventions=("法理术语须依所属法系（大陆法系/英美法系）准确使用", "判例引用遵循Bluebook或本地权威格式并附案号与卷期", "比较法研究须明确研究范围、方法与比较维度", "立法文本引用须标注生效日期与所属法域层级", "涉未成年人/隐私个案须匿名化并说明伦理审查"),
    key_venues=("Journal of Legal Studies", "Law and Society Review", "Comparative Law Review", "American Journal of Comparative Law", "Legal Studies", "The Yale Journal on Regulation"),
    units_and_formulas_notes=("法律计量分析须注明数据源、统计口径与样本区间", "引用法律文本须标注立法机构、生效日期与所属法域层级", "法经济学分析涉及效用/成本单位须统一货币基准并标明汇率", "实证法研究须明确变量定义、编码规则与信度指标"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("北大法宝", "威科先行", "Lexis+", "vLex", "LexMachine", "Kira Systems", "ROSS Intelligence", "Zotero", "Endnote", "LaTeX", "Microsoft Word", "Overleaf", "SPSS", "Stata", "R", "Python", "Jupyter Notebook", "Bluebook 引注插件", "Practical Law", "Reflex（法律文本分析）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "HeinOnline"),
)
