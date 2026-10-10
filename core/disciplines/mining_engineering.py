"""采矿工程学科论文支持：采矿方法/岩石力学/选矿体裁、SME 引用样式与采矿记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mining_engineering",
    aliases=(
        "mining_engineering", "采矿工程", "采矿", "选矿", "岩石力学",
        "矿山安全", "mining engineering", "rock mechanics", "矿山工程"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与采矿问题）",
            "methods（实验、建模与参数）",
            "results（岩体/工艺数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（矿山工程案例）",
            "analysis（采矿方法与支护）",
            "results（工程性能与安全）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（采矿工程理论）",
            "evidence synthesis（采矿技术综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="SME 样式（作者-年份；SME 期刊遵循 SME 规范）",
    reporting_standards={
        "experimental": "岩石力学实验遵循 ISRM 建议方法",
        "geotechnical": "岩土工程遵循 ISRM/ISSMGE 规范",
        "safety": "矿山安全遵循 MSHA 报告规范",
    },
    conventions=(
        "矿体产状与储量分级（JORC/储量规范）须注明",
        "岩石力学参数（强度、模量）须报告试验方法",
        "采矿方法术语须统一",
        "安全系数与支护设计准则须明确",
        "品位/回收率单位须规范",
    ),
    key_venues=(
        "Mining Engineering",
        "International Journal of Mining Science and Technology",
        "Minerals Engineering",
        "International Journal of Rock Mechanics and Mining Sciences",
        "Mining, Metallurgy & Exploration",
    ),
    units_and_formulas_notes=(
        "应力用 MPa；深度用 m；品位用 % 或 g/t",
        "公式用 amsmath；强度准则与稳定性方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSYS", "FLAC3D", "3D MineDesign", "Python", "MATLAB", "UDEC", "RS3 (Rock Sciences 3D)", "Dips (节理分析)", "MicMAC (三维建模)", "PitSlice", "Leapfrog Geology", "Surpac", "Datamine", "VentSim", "MinerSim", "岩石力学试验系统", "三维激光扫描仪", "无人机探测", "矿山压力监测系统", "R (数据处理)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
