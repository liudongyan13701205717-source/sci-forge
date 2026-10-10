"""地砖墙面铺贴学科论文支持：铺贴工艺、材料性能与施工质量控制。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="floor_and_wall_tiling",
    aliases=("floor_and_wall_tiling", "地砖墙面铺贴", "tiling technology",
             "floor tiling", "wall tiling", "砖石铺贴",
             "tile installation", "ceramic tiling", "铺贴工程",
             "tile bonding technology"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（研究方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714",
    reporting_standards={
        "materials": "材料试验须报告瓷砖吸水率、抗压强度、耐磨度等参数与测试标准",
        "bonding": "粘贴强度试验须说明试样制备、养护条件与破坏荷载",
        "construction": "施工工艺须记录基层处理、胶黏剂用量与铺贴参数",
    },
    conventions=(
        "瓷砖吸水率用%表示（按 ISO 10545-3）",
        "抗压强度用 MPa 表示（按 ISO 10545-4）",
        "耐磨度用转数或磨耗深度 mm 表示",
        "胶黏剂粘结强度用 MPa 表示",
        "铺贴平整度用 mm 表示（允许偏差 ±2mm/2m）",
    ),
    key_venues=(
        "Construction and Building Materials",
        "Building and Environment",
        "Cement and Concrete Composites",
        "Ceramics International",
        "建筑技术开发",
    ),
    units_and_formulas_notes=(
        "吸水率 A = (m_饱和 - m_干燥) / m_干燥 × 100%，单位 %",
        "抗压强度 σ = F / A，单位 MPa",
        "胶黏剂用量 q = 面积 × 厚度 × 密度，单位 kg/m²",
        "平整度偏差 = 实测值 - 设计值，单位 mm",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("瓷砖切割机", "激光水平仪", "电锤", "角磨机", "瓷砖吸水率测试仪", "瓷砖强度测试仪", "瓷砖耐磨测试仪", "瓷砖防滑测试仪", "SPSS", "R (RStudio)", "Excel", "Python (Pandas)", "MATLAB", "AutoCAD", "SketchUp", "瓷砖铺贴设计软件", "建筑信息模型 (BIM)", "材料试验机", "红外热像仪", "游标卡尺"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)