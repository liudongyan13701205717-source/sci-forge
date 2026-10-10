"""海军战略学科论文支持：海权研究/海上战略体裁、Chicago 引用样式与海军战略记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="naval_strategy",
    aliases=("naval_strategy", "海军战略", "海权研究", "海上战略", "naval warfare",
             "maritime strategy", "navy strategy", "海战研究", "海权论"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与海军战略问题）", "methodology（研究设计与分析框架）", "results（海权态势与舰队数据）", "discussion（战略意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（海战/海上行动背景）", "analysis（作战与决策分析）", "results（战略启示）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（战略思想与理论综述）", "evidence synthesis（历史与实证证据综合）", "future directions", "references"),
    },
    citation_style="Chicago 样式（作者-年份；Naval War College Review 遵循 Chicago 规范）",
    reporting_standards={
        "case_study": "海战案例研究须遵循案例研究报告规范与史料来源说明",
        "historical": "海军史研究须遵循史料来源报告规范",
        "simulation": "海战仿真须遵循仿真实验报告规范并给出置信区间",
    },
    conventions=(
        "海权理论框架（马汉、科贝特、照屋宗一郎等）须定义并给出出处",
        "舰队编制与舰艇数据须注明来源与统计口径",
        "海上行动时间线与阶段划分须明确",
        "涉密信息须处理并给出脱密声明",
        "制海权、海上拒止与力量投送概念须界定",
    ),
    key_venues=(
        "Naval War College Review",
        "The RUSI Journal",
        "Journal of Strategic Studies",
        "U.S. Naval Institute Proceedings",
        "Defense Studies",
    ),
    units_and_formulas_notes=(
        "舰艇用排水量/数量、航程用海里、速度用节",
        "公式用 amsmath；舰队对比与损耗计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "仿真结果给出置信区间与运行次数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SIPRI Yearbook", "Correlates of War Project", "Blue Force Tracker", "Maritime Domain Awareness System", "ArcGIS Maritime", "NaviStar Pro", "Google Earth Pro", "NetLogo", "AnyLogic", "Mesa", "NVivo", "Tableau", "Gephi", "R", "MATLAB", "Excel", "STIX/TLP", "ICM", "RAND War Games", "Maritime Strategy Simulator"),
    category="军事学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
