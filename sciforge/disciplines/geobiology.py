"""地球生物学学科论文支持：微生物与地球过程交互、生物标志物与古环境重建。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geobiology",
    aliases=("geobiology", "地球生物学", "生物地球化学", "geobiology", "地质微生物学", "微生物古生物学", "同位素地球化学", "微生物化石"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="AGU 样式（作者-年份）",
    reporting_standards={"k1": "野外采样须报告地层背景/采样位置/测年方法（野外报告）", "k2": "同位素分析须报告标准物质与归一化方法（同位素报告）", "k3": "微生物分子数据须报告测序深度/质控/数据库（分子报告）"},
    conventions=("同位素用 δ 记法（‰）；标准物质与归一化须明确", "采样位置与地层背景须报告", "测年方法与 2σ 误差须注明", "微生物分子数据须说明提取/扩增/测序流程", "地质时间尺度与分期须规范"),
    key_venues=("Geobiology", "Geochimica et Cosmochimica Acta", "Astrobiology", "Frontiers in Microbiology", "Chemical Geology"),
    units_and_formulas_notes=("同位素用 δ 记法（‰）", "浓度用 ppm/ppb", "菌量用 cells/g 或 CFU/g", "公式用 amsmath；分馏与年龄计算式须明确", "数值结果给出均值 ± SD 与样本量"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ICP-MS 电感耦合等离子体质谱仪", "TIMS 热离子探针", "SIMS 二次离子质谱仪", "SEM-EDS 扫描电镜能谱", "TEM 透射电镜", "激光共聚焦显微镜", "PCR 仪（古 DNA）", "高通量测序平台（Illumina）", "气相色谱-质谱联用仪 GC-MS", "同位素比值质谱仪 IRMS", "GIS（QGIS/ArcGIS）", "Python（NumPy/Pandas）", "R（ggplot2）", "MATLAB", "GIS 三维建模（Surfer）", "X 射线荧光光谱仪 XRF", "电子探针 EPMA", "拉曼光谱仪", "扫描探针显微镜", "DNA 提取试剂盒（古 DNA）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
