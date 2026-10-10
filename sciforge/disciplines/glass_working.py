"""玻璃成型学科论文支持：玻璃热成型/冷加工体裁、材料学引用样式与玻璃工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="glass_working",
    aliases=("glass working", "玻璃成型", "玻璃热加工", "玻璃冷加工", "玻璃吹制", "玻璃雕刻", "玻璃退火"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（成型与工艺）", "results（形貌与性能）", "discussion（机理与工艺意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（件描述）", "analysis（工艺分析）", "results（成型结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（玻璃热力学与成形）", "evidence synthesis（技法综述）", "future directions", "references"),
    },
    citation_style="IUPAP/材料学作者-年份样式（玻璃成型与材料学通用）",
    reporting_standards={"k1": "成型实验须记录温度/时间/应力", "k2": "性能测试遵循 ASTM C 145", "k3": "件描述须交代尺寸与材质"},
    conventions=("玻璃配方与退火制度须报告", "成型技法须定义", "应力须说明分布", "尺寸给 mm 与测量方法", "工艺参数须可复现"),
    key_venues=("Journal of Non-Crystalline Solids", "Glass Technology", "Ceramics International", "Materials Design", "The Glass Science and Technology"),
    units_and_formulas_notes=("配方以 %wt 表示，温度用 °C", "公式用 amsmath，粘度须明确", "应力给 MPa 与测试方法", "尺寸给 mm 与测量方法"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("热台（hot bench）", "风枪（hot air pen）", "退火炉（lehr）", "窑炉（kiln）", "真空成形机", "激光雕刻（glass engraving）", "水切割（玻璃成形）", "XRF 成分分析", "热膨胀仪（dilatometer）", "偏光显微镜（应力分析）", "硬度计（Vickers）", "数字设计（Rhino/Blender）", "熔制记录表（recipe log）", "热成像（退火监控）", "玻璃应力仪（polariscope）", "玻璃抛光机（lapp）", "玻璃 3D 打印（激光烧结）", "件质量缺陷检测（AOI）", "玻璃冷加工机床", "玻璃热成型模拟（Deform）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
