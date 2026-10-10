"""观赏植物生产学科论文支持：观花与观叶植物繁育、栽培调控与品质管理研究体裁、APA 引用样式与栽培生理注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="production_of_ornamental_plants",
    aliases=("production_of_ornamental_plants", "观赏植物生产", "观赏植物栽培", "ornamental plant production", "cut flower production", "盆栽花卉生产", "观赏植物繁育", "flower production", "花卉生产"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "品种须标注学名与栽培品种名", "k2": "处理须注明重复数与随机化设计", "k3": "产量与品质须注明取样标准与成熟度"},
    conventions=("物候期须使用 BBCH 编码", "基质配方须注明容重与 EC/pH", "光照处理须注明光质、光强与光周期", "产量须注明取样面积与取样时间", "花期与花器官须注明观测节点"),
    key_venues=("Acta Horticulturae", "HortScience", "Scientia Horticulturae", "Journal of Plant Physiology", "Journal of Horticultural Science and Biotechnology"),
    units_and_formulas_notes=("产量：kg/m²", "光照：μmol·m⁻²·s⁻¹", "基质容重：g/cm³", "水肥 EC：mS/cm"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("温室环境监控系统", "光照光度计", "温湿度记录仪", "土壤水分传感器", "手持叶绿素仪", "手持荧光仪（FIAR）", "植物生长箱", "光周期人工气候箱", "育苗穴盘播种机", "灌溉控制系统", "基质物理性质测定仪", "土壤 pH/EC 计", "多光谱相机", "无人机遥感", "Li-Cor LI-6800 光合测定仪", "SPSS", "R（统计建模）", "Origin", "Excel", "EndNote"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
