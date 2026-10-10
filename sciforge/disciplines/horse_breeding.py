"""马匹育种学科论文支持：种质资源、遗传评估与繁殖技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="horse_breeding",
    aliases=("horse_breeding", "马匹育种", "马育种", "马属育种", "Horse Breeding", "Equine Genetics", "Equine Reproduction", "Pony Breeding", "Horse Stud Book"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "FAO 家畜遗传资源报告规范", "k2": "ISHA 马属评估指南", "k3": "GB/T 22370 马匹系谱标准"},
    conventions=("系谱编号须使用国际唯一马耳标号", "遗传参数须注明模型与数据量", "性染色体标记须标注 SNP 位点", "繁殖记录须注明配种日期与受孕确认方式", "样本采集须注明知情同意"),
    key_venues=("Journal of Equine Veterinary Science", "Animal Genetics", "Equine Veterinary Journal", "Animal", "Theriogenology"),
    units_and_formulas_notes=("体高：cm", "体重：kg", "遗传力：h²", "预期改良值：EBV"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("BLUPF90（遗传评估）", "DMU Tools", "R（遗传建模）", "PLINK（群体遗传学）", "BEAGLE（基因型填充）", "EquiMark 马匹基因检测", "DNA Markers 等位基因检测", "Thermo Fisher RealTime PCR 仪", "Illumina iDRBT 芯片", "Horse ID 数字化档案", "EquiTech 系谱管理", "SPSS", "EndNote", "Zotero", "Origin（数据绘图）", "Python（遗传数据整理）", "Excel（家系表录入）", "QGIS（种质地理分布）", "Equine Genome Browser", "Thermo Fisher 基因分型芯片（Axiom）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI", "Digital Bloodstallion Book 数据库"),
)
