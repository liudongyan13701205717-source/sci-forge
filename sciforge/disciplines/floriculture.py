"""花卉栽培学科论文支持：花卉育种、栽培生理与设施农业研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="floriculture",
    aliases=("floriculture", "花卉栽培", "园艺花卉", "观赏植物", "切花生产", "盆栽花卉", "花卉育种", "设施花卉"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "MEE 60 花卉栽培试验报告规范", "k2": "FAO 切花质量标准", "k3": "GB/T 18133 设施园艺标准"},
    conventions=("品种须标注学名与栽培品种名", "光周期处理须注明光照时间（h/d）与光质", "株型指标须注明取样节点（如第 N 片展开叶）", "生根率统计须注明分母", "花期相关指标须标注观测起止日期"),
    key_venues=("Acta Horticulturae", "HortScience", "Scientia Horticulturae", "Journal of the American Society for Horticultural Science", "Euphytica"),
    units_and_formulas_notes=("光合速率：μmol CO₂·m⁻²·s⁻¹", "蒸腾速率：mmol H₂O·m⁻²·s⁻¹", "光强：μmol·m⁻²·s⁻¹", "株高/冠幅：cm"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Li-Cor 6800 光合测定仪", "LI-6800 光合系统", "DeltaC 手持叶绿素仪", "PR-1000 便携式气孔孔径仪", "温室环境监控系统", "光谱分析仪 (Spectral Instrument)", "液相色谱仪 (HPLC)", "气质联用仪 (GC-MS)", "RT-PCR 仪", "流式细胞仪 (FACS)", "植物组织培养设备", "植物生长箱 (Plant Growth Chamber)", "多光谱相机", "土壤水分传感器", "温度-湿度记录仪", "RStudio（统计建模）", "Origin（数据绘图）", "GraphPad Prism", "SPSS", "Geneious（序列分析）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
