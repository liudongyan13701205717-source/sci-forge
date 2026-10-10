"""玻璃工艺学科论文支持：玻璃艺术/手工艺体裁、CIE 色度引用样式与玻璃工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="glass_arts_and_craft",
    aliases=("glass arts and craft", "玻璃工艺", "玻璃艺术", "玻璃手工艺", "吹制玻璃", "窑铸玻璃", "玻璃设计"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（材料与工艺）", "results（作品与性能）", "discussion（美学与工艺意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（作品描述）", "analysis（工艺分析）", "results（成型与性能）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（玻璃美学与技法）", "evidence synthesis（技法综述）", "future directions", "references"),
    },
    citation_style="CIE 色度 + 材料学作者-年份样式（玻璃工艺与材料学通用）",
    reporting_standards={"k1": "工艺实验须记录配方/温度/时间", "k2": "性能测试遵循 ASTM C 系列", "k3": "作品描述须交代尺寸与材质"},
    conventions=("玻璃配方成分须列明（%wt）", "退火制度须报告", "成型技法须定义", "颜色须给色度坐标", "工艺参数须可复现"),
    key_venues=("International Studio", "Glass Studies", "Jornal de Vidro", "Ceramics International（玻璃方向）", "Materials Design"),
    units_and_formulas_notes=("配方以 %wt 表示，温度用 °C", "公式用 amsmath，粘度-温度须明确", "尺寸给 mm 与测量方法", "硬度/热膨胀给单位"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("电熔炉（玻璃熔制）", "真空成形机", "热台（hot bench）", "风枪（hot air pen）", "窑炉（kiln）", "退火炉（annealing oven）", "XRF 成分分析", "热膨胀仪（dilatometer）", "示差扫描量热仪（DSC）", "偏光显微镜（晶相分析）", "粘度-温度计量（viscometer）", "硬度计（Vickers）", "CIE 测色仪（spectrophotometer）", "激光烧结（玻璃 3D 打印）", "热成像仪（退火监控）", "金相抛光与蚀刻（配方）", "拉晶炉（lehr）", "水切割（玻璃成形）", "数字设计（Rhino/Blender）", "熔制记录表（recipe log）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
