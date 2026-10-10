"""矿物开采学科论文支持：矿产开采/地下露天开采体裁、SME 引用样式与矿产开发参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mining_of_minerals",
    aliases=(
        "mining_of_minerals", "矿物开采", "采矿", "矿物资源开采", "mining",
        "resource mining", "mineral extraction", "地下开采", "露天开采"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与矿产开发）",
            "methodology（开采方法与实验）",
            "results（开采数据与评价）",
            "discussion（工程意义与改进）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（矿产开采案例）",
            "analysis（开采工艺与技术）",
            "results（开采性能与效益）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（矿产开采理论）",
            "evidence synthesis（开采技术综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="SME 样式（作者-年份；SME 期刊遵循 SME 规范）",
    reporting_standards={
        "experimental": "岩石力学实验遵循 ISRM 建议方法",
        "mine_design": "采矿设计遵循 JORC 储量规范",
        "safety": "矿山安全遵循 MSHA 报告规范",
    },
    conventions=(
        "矿体产状与储量分级须注明",
        "开采方法术语须统一",
        "地下/露天开采术语区分清晰",
        "采矿设备参数须完整",
        "储量/品位单位须规范",
    ),
    key_venues=(
        "Mining Engineering",
        "Mining, Metallurgy & Exploration",
        "Resources Policy",
        "International Journal of Mining and Reclamation",
        "Geomechanics and Tunneling",
    ),
    units_and_formulas_notes=(
        "应力用 MPa；深度用 m",
        "储量用 Mt；品位用 % 或 g/t",
        "公式用 amsmath；开采设计方程须编号",
        "数值结果给出均值 ± 不确定度与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSYS", "FLAC3D", "3D MineDesign", "Python", "MATLAB", "三维激光扫描仪", "地质雷达", "岩石力学试验系统", "矿山压力监测系统", "采空区充填系统", "液压支架", "掘进机", "采矿钻机", "GIS (ArcGIS/QGIS)", "无人机探测系统", "井下定位系统 UWB", "智能矿山调度系统", "R (数据处理)", "地质建模软件 Leapfrog", "矿山生态监测系统"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
