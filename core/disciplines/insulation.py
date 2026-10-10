"""绝缘学科论文支持：热/电绝缘材料与工艺体裁、IEEE 引用样式与绝缘材料注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="insulation",
    aliases=("insulation", "绝缘", "电气绝缘", "热绝缘", "建筑保温", "insulation engineering", "thermal insulation", "electrical insulation", "电气化", "电工材料", "建筑围护"),
    paper_types={
        "research": ("abstract", "introduction（材料/工艺动机）", "methodology（制备与测试）", "results（性能表征）", "discussion（结构-性能关系）", "references"),
        "case_study": ("abstract", "introduction", "case description（工程应用背景）", "analysis（性能/失效分析）", "results（工程评估结论）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（传热与绝缘机制）", "evidence synthesis（材料体系综述）", "future directions", "references"),
    },
    citation_style="IEEE 样式（编号引用，如 [1]）",
    reporting_standards={"test_standard": "测试须按 ASTM/IEC 标准执行并报告标准号", "test_conditions": "测试温度、湿度、荷载条件须完整披露", "replicates": "样品数量与重复性须报告"},
    conventions=("导热系数记号 λ 或 k 须统一", "电气参数用击穿强度、介质损耗角正切", "样品尺寸、密度、孔隙率须报告", "热图像标注测试环境温度", "老化测试须报告老化时间与判据"),
    key_venues=("Applied Thermal Engineering", "Journal of Building Engineering", "Conduction Heat Transfer", "Materials Science and Engineering R", "Construction and Building Materials"),
    units_and_formulas_notes=("导热系数 W/(m·K)，热阻 m²·K/W，热流密度 W/m²", "电击穿强度 kV/mm，介电常数无量纲", "保温系数 R-value 与 U-value 换算须声明基准", "公式用 amsmath；符号统一 SI"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Guarded Hot Plate", "CASA Heat-Flow Meter", "ASTM C518 Heat-Flow Station", "Diamant LTG-100", "Netzsch LFA 467", "Thermal Properties Analyzer (DCE 3100)", "Thermal Conductivity Analyzer (TPA-1000)", "Thermoscan", "Fluke Ti", "FLIR T1040", "Thermap M90", "IEC 60094 Test Fixture", "IEC 60433 Test Fixture", "IEC 60598 Test Fixture", "IEC 60853 Test Fixture", "ANSYS Fluent", "COMSOL Multiphysics", "SolidWorks Simulation", "MATLAB", "Python (NumPy/SciPy)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
