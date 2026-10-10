"""地球化学学科论文支持：岩石地球化学、稳定同位素与流体地球化学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geochemistry",
    aliases=("geochemistry", "地球化学", "岩石地球化学", "geochemistry", "稳定同位素", "流体地球化学", "沉积地球化学", "实验地球化学"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="AGU 样式（作者-年份）",
    reporting_standards={"k1": "主量/微量元素须报告检测方法与检出限（检测报告）", "k2": "同位素须报告标准物质/归一化/分馏系数（同位素报告）", "k3": "实验条件须报告压力/温度/时长/初始组成（实验报告）"},
    conventions=("元素符号与同位素质量数须按 IUPAC 规范书写", "同位素 δ 值须注明标准物质（VSMOW/VBO）与分馏符号", "岩石名称须按 IUGS 分类", "实验条件（P/T/时长/组成）须完整列出", "数据精度须报告 2σ 或 1σ 不确定度"),
    key_venues=("Geochimica et Cosmochimica Acta", "Contributions to Mineralogy and Petrology", "Earth and Planetary Science Letters", "Journal of Petrology", "Chemical Geology"),
    units_and_formulas_notes=("微量元素用 ppm（μg/g）", "痕量元素用 ppb（ng/g）", "同位素用 δ 记法（‰）", "氧逸度用 Δlog fO₂（QMFM 偏差）", "公式用 amsmath；分馏方程须明确"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ICP-MS 电感耦合等离子体质谱仪", "XRF X 射线荧光光谱仪", "EDS 能量色散 X 射线能谱仪", "TIMS 热离子探针", "SIMS 二次离子探针", "IRMS 同位素比值质谱仪", "电子探针 EPMA", "激光剥蚀 ICP-MS（LA-ICP-MS）", "X 射线衍射仪 XRD", "高温高压实验装置（多面压）", "热重分析 TGA", "扫描电镜 SEM", "透射电镜 TEM", "GIS（QGIS/ArcGIS）", "Python（NumPy/Pandas）", "R（ggplot2）", "MATLAB", "Excel（数据整理）", "LaTeX（公式排版）", "Surfer（三维地质建模）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
