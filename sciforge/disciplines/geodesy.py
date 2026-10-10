"""大地测量学科论文支持：GNSS、参考框架、重力与大地形变监测。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geodesy",
    aliases=("geodesy", "大地测量学", "GNSS", "geodesy", "测量学", "重力测量", "卫星测地", "大地参考框架"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="AGU 样式（作者-年份）",
    reporting_standards={"k1": "观测研究须报告 GNSS 处理软件与策略（观测报告）", "k2": "参考框架须注明 ITRF 版本与坐标基准（框架报告）", "k3": "误差与不确定性须报告 1σ/2σ（不确定度报告）"},
    conventions=("参考框架（ITRF 等）须注明", "处理软件与策略须报告", "误差与不确定性须报告", "时间序列须注明时段与采样", "坐标基准须一致"),
    key_venues=("Journal of Geodesy", "Journal of Geophysical Research: Solid Earth", "Geophysical Journal International", "GPS Solutions", "Journal of Geodynamics"),
    units_and_formulas_notes=("坐标用 m；速度用 mm/a", "重力用 mGal 或 μGal", "精度用 mm 或 ppb", "公式用 amsmath；平差方程须编号", "数值结果给出均值 ± 标准差与样本量"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("GNSS 接收机（Trimble/Leica）", "Bernese GPS 处理软件", "GAMIT/GLOBK", "精确重力仪（FG5 绝对重力仪）", "超导重力仪", "InSAR（ENVISAR/COSMO）", "LiDAR 激光雷达（机载）", "水准仪（数字/激光）", "全站仪（徕卡/拓普康）", "RTK 基站与流动站", "GNSS 天线（扼流圈型）", "PyGMTSAR/PyGMT", "MATLAB", "Python（NumPy/PyTorch）", "GSRTS（GTS-RINEX 处理）", "ITRF 参考框架软件", "GRACE 重力卫星数据", "VLBI（甚长基干涉仪）", "SLR（卫星激光测距）", "InSAR 干涉软件（SNAP/GAMMA）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
