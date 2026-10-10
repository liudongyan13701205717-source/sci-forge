"""顺势疗法学科论文支持：顺势疗法药理、临床与循证评价研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="homeopathic_medicine",
    aliases=("homeopathic_medicine", "顺势疗法", "顺势医疗", "Homeopathy", "Homeopathic Medicine", "Boericke Repertory", "Provings", "Individualization"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"k1": "CONSORT 随机对照试验报告规范", "k2": "STROBE 观察性研究报告规范", "k3": "BoNT 顺势疗法研究方案建议"},
    conventions=("处方须标注剂型与稀释度（如 30C、D6）", "药物来源须标注药典版本（HPRH/Ph.Hp.）", "患者记录须遵循个体化治疗记录模板", "对照组须注明安慰剂剂型", "疗效量表须注明计分方向"),
    key_venues=("Homeopathy", "Journal of Clinical Homeopathy", "Evidence-Based Complementary and Alternative Medicine", "PLOS ONE", "British Homeopathic Journal"),
    units_and_formulas_notes=("稀释度：C 制（1:100）或 D 制（1:10）", "制剂体积：mL", "疼痛/症状：NRS 0–10", "疗程：次/月"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R（统计建模）", "JASP", "Stata", "REDCap", "Qualtrics", "OpenClinica", "Boericke MADA REPERTORY", "Kent's Repertory 数字化版", "BoNT Proving Database", "DrugProving.info", "Homeopathic Repertory (Saba Pathology)", "Pawel 顺势处方软件", "Casebook 案例管理工具", "RevMan（Meta 分析）", "Cochrane Risk of Bias Tool", "CONSORT Checklist", "EndNote", "Zotero", "RefWorks"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
