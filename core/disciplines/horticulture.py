"""园艺学学科论文支持：园艺作物生理、栽培与育种研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="horticulture",
    aliases=("horticulture", "园艺学", "园艺", "园艺植物", "果蔬园艺", "Horticulture", "Horticultural Science", "Vegetable Science", "Fruit Science", "Ornamental Horticulture"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "ASA 园艺试验报告规范", "k2": "FAO 园艺作物栽培指南", "k3": "GB/T 18407 农产品安全"},
    conventions=("品种须标注学名与栽培品种名", "处理须注明重复数与随机化设计", "物候期须使用 BBCH 编码", "果实品质须注明采样部位与成熟度", "土壤与基质须注明理化性质"),
    key_venues=("HortScience", "Journal of the American Society for Horticultural Science", "Acta Horticola", "Journal of Experimental Botany", "Scientia Horticulturae"),
    units_and_formulas_notes=("光合速率：μmol CO₂·m⁻²·s⁻¹", "气孔导度：mol H₂O·m⁻²·s⁻¹", "果实可溶性固形物：°Brix", "株高/冠幅：cm"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Li-Cor LI-6800 光合测定仪", "Penetrometer 果实硬度计", "Refractometer 果实糖度仪", "Colorimeter 色差仪", "HPLC 液相色谱仪", "GC-MS 气质联用仪", "RT-PCR 仪", "流式细胞仪", "植物组织培养设备", "植物生长箱", "温室环境监控系统", "多光谱相机", "土壤水分传感器", "气象站", "SPSS", "R（统计建模）", "Origin（数据绘图）", "Excel", "EndNote", "Geneious（序列分析）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
