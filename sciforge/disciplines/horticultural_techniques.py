"""园艺技术学科论文支持：园艺栽培技术、育苗与设施环境调控研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="horticultural_techniques",
    aliases=("horticultural_techniques", "园艺技术", "栽培技术", "育苗技术", "设施园艺技术", "Horticultural Techniques", "Cultivation Techniques", "Nursery Production", "Protected Cultivation", "Seedling Production"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "FAO 农业技术规程", "k2": "GLOBALG.A.P. 良好农业规范", "k3": "GB/T 23417 蔬菜栽培技术规程"},
    conventions=("育苗床参数须注明基质配方与容重", "移栽须注明苗龄与根系完整度", "水肥一体化须注明 EC/pH 值", "激素处理须注明浓度与方式", "物候节点须使用 BBCH 编码"),
    key_venues=("Acta Horticulturae", "HortScience", "Scientia Horticulturae", "Journal of Plant Nutrition", "Plants"),
    units_and_formulas_notes=("基质容重：g/cm³", "水肥 EC：mS/cm", "激素浓度：mg/L 或 ppm", "苗龄：d"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("温室环境监控系统", "基质水分传感器", "土壤 pH/EC 计", "手持叶绿素仪", "手持荧光仪（FIAR）", "植物生长箱", "育苗穴盘播种机", "灌溉控制系统（Netafim/Rivulis）", "营养液自动配肥系统", "基质物理性质测定仪", "温湿度记录仪", "多光谱相机", "SPSS", "R（统计建模）", "Origin（数据绘图）", "Excel", "EndNote", "Zotero", "GraphPad Prism", "Global Mapper（生产布局制图）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
