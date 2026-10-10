"""狩猎与陷阱学科论文支持：野外观察/生态学/资源管理体裁、APA 引用样式与猎获度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="hunting_and_trapping",
    aliases=("hunting_and_trapping", "狩猎与陷阱", "狩猎", "陷阱", "野生动物管理", "猎获调查", "兽类学", "猎兽", "狩猎业"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与研究问题）", "methodology（样地、陷阱与调查）", "results（猎获与种群数据）", "discussion（生态与种群意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（区域与猎季）", "analysis（猎获分析）", "results（管理评估）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（种群与生境框架）", "evidence synthesis（文献综合）", "future directions", "references"),
    },
    citation_style="APA 样式（动物学与野外生态学常用）",
    reporting_standards={
        "field_observation": "野外观察遵循样地/样线报告规范",
        "trapping": "陷阱与猎获遵循猎获登记与许可规范",
        "population": "种群估计遵循标记重捕报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "ethics": "猎获与陷阱须报告许可与伦理审查",
    },
    conventions=(
        "样地/样线与坐标须报告",
        "猎获种类与计数须逐条登记",
        "标记重捕方法与捕获率须给出",
        "猎季与许可编号须注明",
        "单位换算（头、kg）须规范",
    ),
    key_venues=(
        "Journal of Wildlife Management",
        "Wildlife Biology",
        "Oryx",
        "Mammalia",
        "Journal of Applied Ecology",
        "Conservation Biology",
    ),
    units_and_formulas_notes=(
        "个体数用头/只；体重用 kg",
        "面积用 km²；密度用 头/km²",
        "公式用 amsmath；捕获率与置信区间须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "时间序列注明猎季与时段",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("R", "Python", "QGIS", "ArcGIS", "SPSS", "MATLAB", "MarkRecap", "Distance Sampling", "Camera Trap 相机", "GPS 颈圈", "声学记录器", "无人机", "GPS 定位仪", "望远镜", "测距仪", "激光测距", "Excel", "LaTeX", "EndNote", "Git"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
