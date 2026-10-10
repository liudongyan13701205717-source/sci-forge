"""航海技艺学科论文支持：导航/操船/避碰/引航/海图作业体裁、IMO 航海报告规范与航海度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="seamanship",
    aliases=("seamanship", "航海技艺", "船舶操舵", "航海术", "ship handling", "navigation"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究意义）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据综合）",
            "future directions（展望）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "maritime": "航海报告遵循 IMO 航海安全报告规范",
        "accident": "事故分析遵循 IMO 事故调查指南（IGME）",
        "simulator": "模拟器训练记录须包含训练参数、学员表现与评估结果",
        "data": "航行数据须报告采集设备、精度与时间戳",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "海图须注明版本、投影方式与水深基准",
        "船舶参数须统一：船长用 m、排水量用 t、吃水用 m",
        "海况报告须遵循 Beaufort 风级与 Douglas 浪级",
        "引航报告须记录引航员资质、航次信息与异常情况",
        "时间戳统一使用 UTC 并注明地方时",
    ),
    key_venues=(
        "Journal of Navigation",
        "Safety Science",
        "Ocean Engineering",
        "Journal of Marine Science and Technology",
        "Nautical Institute Journal",
    ),
    units_and_formulas_notes=(
        "距离用 nmi（海里）；速度用 kn（节）；时间用 UTC",
        "风级用 Beaufort；浪高用 m；能见度用 nmi 或 m",
        "公式用 amsmath；航路计算（大圆/恒向线）须编号",
        "统计结果给出均值 ± 标准差与样本量；显著性用 p 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ECDIS 电子海图系统", "AIS 自动识别系统", "Gyrocompass 陀螺罗经", "GPS 差分定位仪", "Marine Weather Routing System", "Ship Simulator 航海模拟器", "Radar 雷达", "Echo Sounder 测深仪", "Sextant 六分仪", "NavStation 航行数据记录系统", "Dynamics 3D 船舶动力学仿真", "OpenSeaMap 海洋数据平台", "MATLAB 航海计算", "R 统计分析", "LaTeX 排版", "Python 数据分析", "Origin 绘图", "SPSS 统计软件", "QGIS 航路规划", "SimNet 网络仿真"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)