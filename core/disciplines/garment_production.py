"""服装生产学科论文支持：设计、材料、成衣工艺、供应链与工业化生产。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="garment_production",
    aliases=("garment_production", "服装生产", "成衣制造", "服装工程", "Garment manufacturing", "Apparel engineering", "服装工艺", "服装制造"),
    paper_types={
        "research": ("abstract", "introduction（材料与工艺背景）", "methodology（试样、工艺参数与测试方法）", "results（性能与成衣质量数据）", "discussion（工艺-性能关系与改进方向）", "references"),
        "case_study": ("abstract", "introduction", "case description（工厂/供应链/生产线概况）", "analysis（工艺流程、产线与质量管理）", "results（效率、成本与合格率）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（服装工程、材料、生产与标准综述）", "evidence synthesis（不同工艺/供应链比较）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份），或纺织/服装行业期刊 GB/T 7714 规范",
    reporting_standards={"fabric": "面料检测须执行 ISO 9237、AATCC 或 GB/T 系列", "sizing": "成衣号型须符合 GB/T 1335 或 ISO 8559", "dyeing": "染整须报告浴比、温度、时间、染料/助剂与水洗牢度测试"},
    conventions=("服装号型按 GB/T 1335 标注", "色牢度等级按 GB/T 3920、3922 等", "缝制牢度用 N（牛顿）", "面料克重用 g/m²", "工艺参数（针距、线张力）须报告具体数值"),
    key_venues=("Textile Research Journal", "Journal of Industrial Textiles", "东华大学学报", "纺织学报", "Journal of Fashion Marketing and Management"),
    units_and_formulas_notes=("面料克重用 g/m²", "拉伸强度用 kN/m 或 N/mm", "色牢度按 GBS 5 级", "缝制强度用 N", "成衣号型以身高/胸围（cm）表示"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Gerber AccuMark（服装CAD）", "Modaris（打版与排料）", "Style3D（3D服装模拟）", "CLO3D（3D服装模拟）", "CAD-CAE 集成系统", "Sewtech 电脑缝纫机", "工业缝纫机（JUKI/Brother）", "激光裁剪机", "面料检测仪器（SGS 测试）", "色牢度测试仪（ATLAS）", "张力仪（Groninger）", "AutoCAD（结构设计）", "SolidWorks（服装设备）", "FlexSim（产线仿真）", "SPSS", "Origin", "R", "MATLAB", "Excel", "Photoshop（设计辅助）", "3D 人体扫描仪"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
