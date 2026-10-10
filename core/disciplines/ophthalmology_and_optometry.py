"""眼科学与视光学学科论文支持：眼科与验光配镜联合研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ophthalmology_and_optometry",
    aliases=("ophthalmology_and_optometry", "眼科学", "视光学", "Optometry", "眼视光学", "Ophthalmology & Optometry", "视觉矫正", "Vision Science"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"k1": "CONSORT（随机试验）", "k2": "STROBE（观察性研究）", "k3": "PRISMA（系统综述）"},
    conventions=("视力记录用logMAR并注明换算", "屈光度以D（屈光度）为单位", "散光轴向标注", "OCT参数完整"),
    key_venues=("Ophthalmology", "American Journal of Optometry", "Contact Lens & Anterior Eye", "Optometry & Vision Science", "Eye & Contact Lens"),
    units_and_formulas_notes=("屈光度以D（屈光度）", "视力用logMAR", "眼压mmHg", "矫正前后数据对比"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("OCT (Zeiss)", "Fundus Camera (Heidelberg)", "Autorefractor (Nidek)", "Tonometer (iCare)", "Slit Lamp (Zeiss)", "Visual Field Analyzer (Humphrey)", "Corneal Topographer (Pentacam)", "Biometry (IOLMaster)", "Amsler Grid", "Perimetry", "ERG/VEP", "OCTA (AngioScan)", "Fundus Autofluorescence (FAF)", "SPSS", "R", "GraphPad Prism", "EndNote", "Zotero", "ImageJ", "Python"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
