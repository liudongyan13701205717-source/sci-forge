"""眼科学学科论文支持：眼科临床/视觉科学体裁、AAO/Ophthalmology 引用样式与眼科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ophthalmology",
    aliases=("ophthalmology", "眼科学", "眼科", "视觉科学", "Visual Science", "Ophthalmology", "眼科临床", "Ophthalmic Research"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"k1": "CONSORT（随机试验）", "k2": "STROBE（观察性研究）", "k3": "CARE（病例报告）"},
    conventions=("视力记录用logMAR并注明换算", "眼压单位mmHg", "OCT/OCTA参数完整", "屈光状态符号规范注明"),
    key_venues=("Ophthalmology", "American Journal of Ophthalmology", "Investigative Ophthalmology & Visual Science", "JAMA Ophthalmology", "British Journal of Ophthalmology"),
    units_and_formulas_notes=("眼压用mmHg", "视力用logMAR或小数", "OCT参数标注", "疗效分析给出RR/OR与95%CI"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("OCT (Zeiss)", "Fundus Camera (Heidelberg)", "ERG/VEP", "Tonometer (iCare)", "Slit Lamp (Zeiss)", "Visual Field Analyzer (Humphrey)", "Autorefractor (Nidek)", "Corneal Topographer (Pentacam)", "DORC (Digital Ophthalmic)", "A-Scan Biometry", "Amsler Grid", "Perimetry", "OCTA (AngioScan)", "Fundus Autofluorescence (FAF)", "Biometry (IOLMaster)", "EndNote", "Zotero", "SPSS", "R", "ImageJ"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
