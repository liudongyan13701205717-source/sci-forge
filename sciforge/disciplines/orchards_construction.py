"""果园建造学科论文支持：果园规划、土壤与灌溉、机械栽培系统。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="orchards_construction",
    aliases=("orchards_construction", "果园建造", "果园建设", "Orchards Construction", "Orchard Establishment", "Orchard Planning", "果园规划", "orchard layout", "orchard infrastructure"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"STROBE": "STROBE 观察性研究规范", "SITRAN": "土壤与灌溉数据规范", "METEOROL": "气象数据报告规范"},
    conventions=("面积单位（ha、m²、亩）与国际标准共存", "生长季与物候阶段（BBCH）标注明确", "田间试验设计（RCBD/Split-plot）声明", "产量按 t/ha 或 kg/ha 换算并给出年际对比", "气象数据引用源（站点/年份）"),
    key_venues=("Computers and Electronics in Agriculture", "Horticulturae", "Agronomy", "Horticultural Technology", "Acta Horticulturae"),
    units_and_formulas_notes=("面积 ha/m²、产量 t/ha、水分 mm/d", "土壤含水率以体积百分数 θ_v (%) 报告", "蒸散发量 ET₀ 按 mm/d 计算", "株行距用 m 表示，冠幅用 m 报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SoilTek 土壤分析仪", "Decagon EC-5 土壤含水率传感器", "Campbell CS655 传感器", "Davis Vantage Pro2 气象站", "DJI Phantom 4 无人机", "DJI Mavic 2 多光谱无人机", "SenseFly S.O.D.A.R.", "LiDAR 激光雷达扫描仪", "ArcGIS Pro", "QGIS", "MATLAB", "Python (NumPy/SciPy)", "R", "SPSS", "Microsoft Excel", "OriginLab", "Netafim 灌溉控制器", "FruitMaster 树体激光测距仪", "LI-6800 光合作用仪", "果实品质分析仪 (Huey USB)"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CABI", "CNKI"),
)
