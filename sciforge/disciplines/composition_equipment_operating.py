"""化工合成设备操作学科论文支持：化工设备操作/工艺流程体裁、APA 引用样式与工艺操作注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="composition_equipment_operating",
    aliases=(
        "composition_equipment_operating", "化工合成设备操作",
        "chemical synthesis equipment operation", "化工设备操作",
        "process equipment operation", "工艺设备操作",
        "chemical process equipment", "化工工艺设备",
        "equipment operating", "设备操作", "process engineering",
        "工艺工程", "chemical equipment operation", "化工设备运维",
        "process control", "过程控制", "chemical plant operation",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与操作问题）",
            "literature review（文献综述）",
            "methods（方法与实验设计）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction（案例背景）",
            "equipment description（设备描述）",
            "method（操作方法）",
            "results（结果）",
            "analysis（分析）",
            "recommendations（建议）",
            "references",
        ),
        "optimization": (
            "abstract",
            "introduction",
            "problem formulation（问题建模）",
            "optimization approach（优化方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Chemical Engineering Journal 遵循 ACS/Elsevier 规范）",
    reporting_standards={
        "experimental": "实验研究须遵循实验报告规范",
        "simulation": "仿真研究须遵循仿真报告规范",
        "case_study": "案例研究须遵循案例研究规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "设备操作规范须引用国家标准或行业标准编号",
        "工艺参数须标注正常值、报警值与联锁值",
        "涉及危险化学品操作须注明 MSDS 与防护措施",
        "设备变更记录须保留完整可追溯",
        "涉及统计检验时给出效应量与置信区间",
    ),
    key_venues=(
        "Chemical Engineering Journal",
        "Industrial & Engineering Chemistry Research",
        "Chemical Engineering Science",
        "AIChE Journal",
        "Chemical Engineering Research and Design",
        "Computers & Chemical Engineering",
    ),
    units_and_formulas_notes=(
        "温度用 ℃ 或 K；压力用 Pa 或 bar",
        "流量用 m³/h 或 L/min",
        "浓度用 mol/L 或 %（质量或体积）",
        "功率用 kW 或 MW",
        "涉及公式时注明变量定义与单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python", "LabVIEW", "AutoCAD", "SolidWorks", "EPLAN", "Aspen Plus", "Aspen HYSYS", "DWSIM", "Simulink", "Aspen Custom Modeler", "gPROMS", "PRO-II", "KBC Advanced Process Simulator", "Aspen Properties", "LaTeX", "Aspen One", "Aspen PIMS", "Aspen NRTL", "Aspen Radiant"),
    category="工学",
    databases=("OpenAlex", "CNKI", "万方", "Crossref", "ScienceDirect", "Scopus"),
)
