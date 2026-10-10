"""园艺生产学科论文支持：园艺作物生产管理与生产系统研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="horticultural_production",
    aliases=("horticultural_production", "园艺生产", "园艺作物生产", "设施园艺生产", "果园生产", "Horticultural Production", "Vegetable Production", "Orchard Production", "Greenhouse Production", "Commercial Horticulture"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "FAO Code of Practice for Plant Protection", "k2": "GLOBALG.A.P. 全球良好农业规范", "k3": "GB/T 33123 绿色防控技术规程"},
    conventions=("品种须标注学名与栽培品种名", "处理须注明处理次数与剂量", "产量须注明取样面积与成熟度", "物候期须使用通用编码（BBCH）", "病虫害计数须注明计数单位"),
    key_venues=("Acta Horticulturae", "HortScience", "Journal of Horticultural Science and Biotechnology", "Plant Science", "Agronomy"),
    units_and_formulas_notes=("产量：kg/m² 或 t/ha", "灌溉量：mm", "病虫害发生率：% 或 头/株", "生长速度：cm/d"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("温室环境监控系统", "土壤水分传感器", "气象站（Dwyer/Halma）", "手持叶绿素仪（Chlorophyll Meter）", "果实糖度仪（refractometer）", "硬度计（ penetrometer）", "色差仪（colorimeter）", "多光谱相机", "植物生长箱", "土壤养分速测仪", "EC/pH 计", "虫情测报灯", "SPSS", "R（统计建模）", "Origin（数据绘图）", "Excel", "EndNote", "Zotero", "Drone（无人机遥感）", "Global Mapper（生产布局制图）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
