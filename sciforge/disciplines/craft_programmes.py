"""工艺项目学科论文支持：手工艺制造/工艺项目管理体裁、APA 引用样式与工艺研究约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="craft_programmes",
    aliases=(
        "工艺项目", "手工艺项目", "工艺生产项目", "Craft programmes",
        "Craft Programs", "Craft Production Programmes", "工艺计划",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
        "project_report": (
            "项目概述",
            "工艺设计",
            "材料与设备",
            "生产过程",
            "质量控制",
            "成本分析",
            "结论",
        ),
        "review": (
            "摘要",
            "引言",
            "工艺方法综述",
            "项目案例综述",
            "整合与讨论",
            "参考文献",
        ),
    },
    citation_style="APA 第 7 版",
    reporting_standards={
        "materials": "原材料须注明材质、规格与来源",
        "process": "工艺流程须标注关键参数（温度、压力、时间）",
        "quality": "质量指标须使用标准化检测方法",
        "cost": "成本数据须注明统计范围与计价方式",
    },
    conventions=(
        "原材料须注明标准编号（如 GB、ASTM、ISO）",
        "工艺参数须注明单位与测量方法",
        "成品检验须注明检测标准与合格判定准则",
        "项目时间线须标注里程碑节点",
        "工艺改进须报告改进前后对比数据",
    ),
    key_venues=(
        "Journal of the Society for Industrial and Applied Math",
        "Manufacturing Engineering",
        "International Journal of Production Research",
        "Journal of Materials Processing Technology",
        "International Journal of Design Manufacture and Design Management",
        "中国工艺集",
    ),
    units_and_formulas_notes=(
        "材料力学性能按 ISO/ASTM 标准报告",
        "成本数据使用标准货币单位",
        "工艺良率使用百分比表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CAD (Computer-Aided Design)", "AutoCAD（工艺设计）", "SolidWorks（3D 建模与仿真）", "CATIA（工艺设计系统）", "UG NX（数控加工编程）", "Pro/E（工艺模拟）", "Mastercam（数控编程）", "Fusion 360（工艺设计）", "3D 打印机（桌面工艺制造）", "CNC 机床（数控加工设备）", "激光切割机（材料加工）", "数控车床（金属加工）", "注塑机（塑料成型）", "Moldflow（注塑工艺模拟）", "Ansys（工艺仿真分析）", "NX Nastran（有限元分析）", "Tableau（工艺数据可视化）", "SPSS", "R（统计分析）", "Python（工艺优化）", "MATLAB（工艺建模）", "Origin（数据绘图）", "Excel（工艺数据管理）", "SAP（工艺管理系统）", "Mendix（低代码工艺开发）"),
    category="工学",
    databases=("ScienceDirect", "IEEE Xplore", "Web of Science", "中国知网"),
)
