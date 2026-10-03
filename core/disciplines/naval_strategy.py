"""海军战略学科论文支持：海军战略/海权研究体裁、Chicago 引用样式与海军战略记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="naval_strategy",
    aliases=("naval_strategy", "海军战略", "海权研究", "海上战略", "naval warfare"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与海军战略问题）",
            "methods（研究设计与分析框架）",
            "results（海权态势与舰队数据）",
            "discussion（战略意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（海战/海上行动背景）",
            "analysis（作战与决策分析）",
            "conclusions（战略启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份；Naval War Coll Rev 遵循 Chicago 规范）",
    reporting_standards={
        "case_study": "海战案例研究遵循案例研究报告规范",
        "historical": "海军史研究遵循史料来源报告规范",
        "analytical": "海权分析遵循模型设定报告规范",
        "comparative": "比较海军战略遵循比较研究报告规范",
        "simulation": "海战仿真遵循仿真实验报告规范",
    },
    conventions=(
        "海权理论框架（马汉、科贝特等）须定义",
        "舰队编制与舰艇数据须注明来源",
        "海上行动时间线与阶段划分须明确",
        "涉密信息处理与脱密声明须注明",
        "制海权与力量投送概念须界定",
    ),
    key_venues=(
        "Naval War College Review",
        "The RUSI Journal",
        "Journal of Strategic Studies",
        "U.S. Naval Institute Proceedings",
        "Defense Studies",
        "The Mariner's Mirror",
    ),
    units_and_formulas_notes=(
        "舰艇用吨位/数量；航程用海里；速度用节",
        "公式用 amsmath；舰队对比与损耗计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本量",
        "仿真结果给出置信区间与运行次数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "报告"),
    tools=(
        "海图与航行分析软件",
        "GIS 空间分析（ArcGIS）",
        "态势感知与仿真系统",
        "水文海洋数据处理（MATLAB）",
    ),
    category="军事学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)