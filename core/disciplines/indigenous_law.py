"""原住民法论文支持：条约法、土地权利、自决权、原住民司法与文化知识产权保护。"""
from __future__ import annotations
from sciforge.disciplines.base import Discipline
DISCIPLINE = Discipline(
    name="indigenous_law",
    aliases=("indigenous_law", "原住民法", "aboriginal_law", "treaty_law", "native_rights", "indigenous_self_determination", "land_rights", "indigenous_jurisprudence", "UNDRIP_law"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法论）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Bluebook（法学规范）或 OSCOLA",
    reporting_standards={"case_citation": "案例引用须按 Bluebook 格式含卷号、页码与法院", "statutory_citation": "法条引用须含版本年份、法典简称与条款号", "international_law": "国际法规范须引用 UNDRIP/ILC 文本版本与官方译文"},
    conventions=("区分普通法、成文法与习惯法体系", "引用原住民法源须标注部落/社区名称", "案例引用遵循 Bluebook 或 OSCOLA", "翻译法律文本时保留原住民原语并给出译注", "涉及受控文化信息须遵循社区协议而非公开引用"),
    key_venues=("Canadian Journal of Native Law", "Berkeley Journal of International Law", "Stanford Law Review", "Yale Law Journal", "International and Comparative Law Quarterly"),
    units_and_formulas_notes=("引用法条用卷/章/条编号", "案例引用含年份、卷号与页码", "条约版本引用含签署年份与生效年份", "国际公约引用 UN 官方文件编号"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("CanLII", "Lexum", "Bloomberg Law", "vLex", "LegalTrac", "Fastcase", "Zotero", "EndNote", "Oxford Legal Research Library", "Casetext", "CourtListener", "iJuris", "Lexis AU", "北大法宝", "iCourt", "无讼", "中国裁判文书网", "NVivo", "SPSS", "Reflex（法律文本分析）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "HeinOnline", "Google Scholar", "JSTOR", "ProQuest", "EBSCO"),
)
