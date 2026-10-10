"""摩托车工程学科论文支持：摩托车设计/制造/动力性体裁、SAE 引用样式与摩托车工程参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="motorcycle_engineering",
    aliases=(
        "motorcycle_engineering", "摩托车工程", "摩托车制造", "motorcycle", "motorcycle design",
        "摩托车设计", "two-wheeler engineering", "摩托车动力学", "摩托车技术"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与工程问题）",
            "methodology（工程方法与实验）",
            "results（试验与仿真数据）",
            "discussion（性能分析与改进）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（摩托车工程案例）",
            "analysis（设计/结构/性能分析）",
            "results（性能测试结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（摩托车工程理论）",
            "evidence synthesis（摩托车技术综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="SAE 样式（作者-年份；SAE 期刊遵循 SAE 规范）",
    reporting_standards={
        "experimental": "摩托车试验遵循 ISO/SAE 报告规范",
        "simulation": "仿真遵循工程仿真报告规范",
        "safety": "交通安全遵循 ISO/GB 报告规范",
    },
    conventions=(
        "摩托车参数须完整（排量/功率/质量/尺寸）",
        "仿真软件与网格信息须报告",
        "单位与量纲须统一（SI 制）",
        "试验条件（温度/湿度/载荷）须明确",
        "术语（车型/排量/挡位）须界定",
    ),
    key_venues=(
        "SAE International Journal of Transportation",
        "Vehicle System Dynamics",
        "Proceedings of the Institution of Mechanical Engineers Part D",
        "International Journal of Vehicle Design",
        "Journal of Multibody System Dynamics",
    ),
    units_and_formulas_notes=(
        "排量用 mL；功率用 kW；扭矩用 N·m",
        "速度用 km/h；加速度用 m/s²",
        "公式用 amsmath；动力学方程须编号",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB/Simulink", "ANSYS", "CATIA", "SolidWorks", "三维激光扫描仪", "风洞试验装置", "台架试验系统", "SimMoto (摩托车动力学仿真)", "车辆行驶模拟器", "NVH 噪声测试系统", "车辆性能测试系统", "Abaqus (疲劳分析)", "Simulink", "NI 数据采集系统", "UG NX", "EASY5 (发动机分析)", "摩托车轮胎力学分析系统", "车辆排放测试系统", "摩托车试验道路", "R (数据处理)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
