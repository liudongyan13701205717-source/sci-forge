"""采矿与开采学科论文支持：采矿方法/矿产开发/开采安全体裁、SME 引用样式与采矿工程参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mining_and_extraction",
    aliases=(
        "mining_and_extraction", "采矿与开采", "采矿", "mining", "extraction",
        "地下开采", "露天开采", "地下开采技术", "矿产开发"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与开采问题）",
            "methodology（开采方法与实验）",
            "results（开采数据）",
            "discussion（工程意义与改进）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（矿山开采案例）",
            "analysis（开采方法与设计）",
            "results（开采效率与经济性）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（采矿理论与方法）",
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
        "岩石力学参数须报告试验方法",
        "采矿方法术语须统一",
        "安全系数与支护设计准则须明确",
        "品位/回收率单位须规范",
    ),
    key_venues=(
        "Mining Engineering",
        "International Journal of Mining Science and Technology",
        "Mining, Metallurgy & Exploration",
        "Resources Policy",
        "International Journal of Rock Mechanics and Mining Sciences",
    ),
    units_and_formulas_notes=(
        "应力用 MPa；深度用 m",
        "储量用 Mt；品位用 % 或 g/t",
        "公式用 amsmath；开采设计方程须编号",
        "数值结果给出均值 ± 不确定度与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSYS", "FLAC3D", "3D MineDesign", "Python", "MATLAB", "三维激光扫描仪", "地质雷达", "岩石力学试验系统", "钻孔摄像系统", "矿井通风模拟软件 Ventsim", "矿山压力监测系统", "采空区充填系统", "液压支架", "掘进机", "采矿钻机", "GIS (ArcGIS/QGIS)", "无人机探测系统", "井下定位系统 UWB", "采掘设备状态监测", "R (数据处理)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
