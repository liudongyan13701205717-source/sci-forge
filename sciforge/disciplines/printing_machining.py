"""印刷机械制造学科论文支持：印刷机组件设计、精密加工与装配调试的工艺、公差与测试注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="printing_machining",
    aliases=("printing_machining", "印刷机械制造", "印刷机械", "印刷设备加工", "printing machinery", "印刷机组件", "精密加工", "mechanical design of printing", "印刷机械装调"),
    paper_types={
        "research": ("abstract", "introduction（部件功能与研究动机）", "methodology（设计、加工与试验方案）", "results（几何精度、刚度与运行性能）", "discussion（结构与工艺参数影响）", "references"),
        "case_study": ("abstract", "introduction", "case description（部件用途、材料与工况）", "analysis（结构设计、加工工艺与装配分析）", "results（精度与稳定性实测结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（机械制造与结构设计原理）", "evidence synthesis（工艺与设备文献综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714",
    reporting_standards={"k1": "设备参数与试验条件须完整声明（含工况与温湿条件）", "k2": "精度与稳定性须给出均值 ± SD 与样本量", "k3": "安全与可靠性须注明试验标准与判定方法"},
    conventions=("尺寸与公差用 mm 与 μm 表示并注明极限偏差", "转速用 r/min、压力用 MPa、温度用 ℃", "精度与稳定性给均值 ± SD 与测试次数", "结构图与原理图须编号并在正文中引用", "引用标准须写明编号与年份"),
    key_venues=("机械工程学报", "包装工程", "印刷学报", "Journal of Materials Processing Technology", "Precision Engineering"),
    units_and_formulas_notes=("尺寸与公差：mm 与 μm；表面粗糙度：Ra μm", "转速：r/min；压力：MPa；温度：℃", "刚度：N/mm；疲劳寿命：次", "公式用 LaTeX（amsmath）并给出定义"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SolidWorks", "CATIA V5", "Siemens NX", "AutoCAD Mechanical", "Creo Parametric", "ANSYS Mechanical", "Abaqus", "MATLAB/Simulink", "三坐标测量机（CMM）", "激光干涉仪", "表面粗糙度仪", "洛氏硬度计", "振动分析仪", "CNC 加工中心", "海德堡 Speedmaster", "Komori Lithrone", "张力控制系统", "印刷机组装测试台", "EndNote", "Zotero"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
