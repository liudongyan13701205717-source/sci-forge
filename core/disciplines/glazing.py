"""玻璃贴膜学科论文支持：玻璃幕墙/贴膜安装体裁、材料学引用样式与玻璃贴膜记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="glazing",
    aliases=("glazing", "玻璃贴膜", "玻璃幕墙", "玻璃安装", "窗玻璃", "玻璃密封", "玻璃隔断"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（设计与安装）", "results（密封与性能）", "discussion（机理与意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（工程描述）", "analysis（性能分析）", "results（安装结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（玻璃贴膜理论）", "evidence synthesis（工程综述）", "future directions", "references"),
    },
    citation_style="IUPAP/建材学作者-年份样式（玻璃贴膜与建材通用）",
    reporting_standards={"k1": "安装须记录密封/垫片/间隔", "k2": "性能测试遵循 ISO 1396", "k3": "工程描述须交代尺寸与规格"},
    conventions=("玻璃规格（厚度/透光率）须报告", "密封材料须定义", "安装工艺须说明", "透光率/隔热须给方法", "工程参数须可复现"),
    key_venues=("Construction and Building Materials", "Energy and Buildings", "Building Research & Information", "Facade Engineering", "Glass Technology"),
    units_and_formulas_notes=("玻璃规格以 mm 厚表示，透光率给 %", "公式用 amsmath，传热系数 U 值须明确", "尺寸给 mm 与安装方法", "隔热性能给 U 值 W/(m²·K)"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("幕墙设计软件（Tiger）", "玻璃透光率测量（integrating sphere）", "U 值测试舱（hot box）", "密封胶性能仪（tensile）", "玻璃强度计（four-point bend）", "玻璃间隔条（spacer）检测", "热成像（密封缺陷）", "玻璃贴膜机（laminator）", "玻璃幕墙模拟（EN 1396）", "玻璃尺寸测量（laser scanner）", "玻璃安装定位（laser alignment）", "玻璃贴膜记录（installation log）", "玻璃贴膜软件（Autodesk Revit）", "玻璃贴膜质量检查（NDT）", "玻璃贴膜材料库（GlazingDB）", "玻璃贴膜应力分析（ANSYS）", "玻璃贴膜施工监测（BIM）", "玻璃贴膜验收标准（EN 1015）", "玻璃贴膜耐久老化试验箱", "幕墙气密性测试设备"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "玻璃幕墙数据库（FacadeBase）", "玻璃贴膜性能数据库（GlassDB）"),
)
