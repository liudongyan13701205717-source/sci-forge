"""冰川学学科论文支持：冰川/冰盖/冰芯体裁、AGU 引用样式与冰体度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="glaciology",
    aliases=("glaciology", "冰川学", "冰川", "冰盖", "冰芯", "冰川学服务"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（数据与方法）", "results（质量平衡与流动）", "discussion（机制与意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（研究区描述）", "analysis（冰川动力学分析）", "results（质量平衡结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（冰川理论）", "evidence synthesis（证据综述）", "future directions", "references"),
    },
    citation_style="AGU 样式（作者-年份；JGR-Earth Surface 遵循 AGU 规范）",
    reporting_standards={"k1": "观测研究遵循冰川观测数据规范", "k2": "模式研究遵循模式评估规范", "k3": "野外研究遵循冰川测量规范"},
    conventions=("冰川与冰盖须明确标识", "观测手段（遥感/地面/冰芯）须报告", "质量平衡定义须一致", "模式配置与强迫数据须说明", "不确定性须报告"),
    key_venues=("Journal of Glaciology", "Journal of Geophysical Research: Earth Surface", "The Cryosphere", "Annals of Glaciology", "Geophysical Research Letters"),
    units_and_formulas_notes=("质量平衡用 m w.e./a，流速用 m/a", "厚度用 m，面积用 km²", "公式用 amsmath，冰流方程须编号", "时间注明观测时段与基准期"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R（统计与栅格分析）", "Python（xarray/rasterio/NumPy）", "卫星遥感（Sentinel-1/2、Landsat）", "航空激光雷达冰厚测量系统", "冰芯连续流分析系统（CFA）", "差分 GPS 表面位移监测", "PISM 冰盖模式", "PISM3D 二维冰流模式", "冰芯同位素分析（IRMS）", "InSAR 形变监测（Sentinel）", "机载测冰雷达（Barnett）", "冰川物质平衡站（自动测雪）", "光学遥感（ASTER/WorldView）", "冰流数值模式（Elmer/Ice）", "冰芯钻取系统（EDM 钻）", "GPS 冰表位移网", "冰川动力学诊断（Nye 方程）", "冰下含水层探测（GPR）", "冰芯年代学（Bchron）", "无人机（UAV）冰川测绘"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI", "全球冰量数据库（GLIMS）"),
)
