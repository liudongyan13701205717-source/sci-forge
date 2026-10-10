"""工艺技术学科论文支持：工艺路线设计、过程控制与工艺优化研究体裁、GB/T 7714 引用样式与工艺参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="process_technology",
    aliases=("process_technology", "工艺技术", "过程技术", "process engineering", "工艺流程", "process design", "工艺设计", "工艺控制", "工艺优化"),
    paper_types={
        "research": ("abstract", "introduction（工艺问题与研究动机）", "methodology（工艺路线、试验设计与参数控制）", "results（工艺性能与产品质量）", "discussion（工艺参数影响与优化）", "references"),
        "case_study": ("abstract", "introduction", "case description（工艺方案、材料与工况描述）", "analysis（工艺分析、参数优化与问题分析）", "results（工艺结果与质量评估）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（工艺技术原理综述）", "evidence synthesis（工艺与设备文献综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714",
    reporting_standards={"k1": "工艺参数须完整报告并注明 SI 单位与范围", "k2": "质量指标须给出均值 ± SD 与样本量", "k3": "试验条件须注明随机化与重复次数"},
    conventions=("工艺参数须注明 SI 单位与范围", "工艺流程图须编号并在正文中引用", "试验设计须注明随机化与重复次数", "成本与能耗须注明口径与基准", "引用标准须写明编号与年份"),
    key_venues=("机械工程学报", "化工学报", "包装工程", "Chinese Journal of Chemical Engineering", "Journal of Materials Processing Technology"),
    units_and_formulas_notes=("温度：℃；压力：MPa；流速：m³/h", "能耗：kWh/t；良率：%；公差：μm", "公式用 LaTeX（amsmath）并给出定义", "统计结果给出均值 ± SD 与样本量"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Aspen Plus", "Aspen HYSYS", "MATLAB/Simulink", "COMSOL Multiphysics", "SolidWorks", "ANSYS Fluent", "Abaqus", "AutoCAD", "Siemens STEP 7", "LabVIEW", "三坐标测量机（CMM）", "管式炉", "高压反应釜", "红外热成像仪", "洛氏硬度计", "万能拉力试验机", "振动分析仪", "EndNote", "Zotero", "SPSS"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
