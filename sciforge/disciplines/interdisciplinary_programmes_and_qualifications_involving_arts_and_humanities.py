"""跨学科课程与资格（涉及艺术与人文）学科论文支持：艺术人文整合体裁、APA 引用样式与跨学科研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interdisciplinary_programmes_and_qualifications_involving_arts_and_humanities",
    aliases=("interdisciplinary_programmes_and_qualifications_involving_arts_and_humanities", "艺术人文跨学科", "arts humanities interdisciplinary", "艺术人文综合", "人文学科整合", "art and humanities interdisciplinary", "艺术人文研究", "艺术史与人文", "视觉文化", "数字人文", "cultural studies"),
    paper_types={
        "research": ("abstract", "introduction（艺术人文问题与整合逻辑）", "methodology（跨学科方法整合）", "results（整合性发现）", "discussion（跨学科启示与局限）", "references"),
        "case_study": ("abstract", "introduction", "case description（艺术人文实践背景）", "analysis（学科间对话分析）", "results（整合成效）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（艺术与人文理论谱系）", "evidence synthesis（跨学科证据综述）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"method_integration": "跨学科方法须声明来源学科与整合策略", "terminology": "跨学科术语（艺术/人文学科）首次出现处标注来源", "acknowledgement": "致谢与学术伦理声明完整"},
    conventions=("跨学科问题须明确界定与来源学科", "术语在首次出现处标注来源学科", "方法整合逻辑须显式陈述", "参考文献按来源学科均衡分布", "研究局限须说明跨学科整合的挑战"),
    key_venues=("Journal of Interdisciplinary Arts", "Arts and Humanities in Higher Education", "Studies in Arts and Humanities", "European Journal of Cultural Studies", "Journal of Aesthetics and Art Criticism"),
    units_and_formulas_notes=("各学科指标须标注来源学科与换算关系", "跨学科数据口径须统一声明", "引用密度与学科分布须披露", "公式用 amsmath；记法与来源学科一致"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Zotero", "NVivo", "Atlas.ti", "MAXQDA", "Tropy", "Transkribus", "Omeka S", "Gephi", "Voyant Tools", "AntConc", "R", "Python", "QGIS", "Juxta", "CollateX", "FairCopy", "LaTeX", "Nodegoat", "Recogito", "Dia"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR"),
)
