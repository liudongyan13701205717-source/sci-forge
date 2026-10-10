"""冶金技术学科论文支持：冶金加工技术与材料试验体系、工艺验证与报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="metallurgical_technology",
    aliases=("metallurgical_technology", "冶金技术", "metallurgical_process", "metallurgical_industry", "ferrous_processing", "non_ferrous_processing", "metallurgical_craft", "metallurgical_operation", "metallurgical_production", "metallurgical_application", "metallurgical_practice"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）", "methodology（工艺设计与试验方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（车间工艺实例）", "analysis（工艺质量与效能分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（冶金技术路线综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"k1": "工艺参数报告遵循 ISO 9001 质量管理体系", "k2": "材料检验遵循 ASTM / ISO 标准", "k3": "环保与能效报告遵循 ISO 14001 / ISO 50001"},
    conventions=("工艺路线须以流程图表示", "材料牌号与规格须注明", "试验条件（温度、时间、载荷）须说明", "结果须附不确定度与样本量", "安全与职业健康风险须评估"),
    key_venues=("Journal of Materials Processing Technology", "Materials Technology", "International Journal of Metalworking", "Iron and Steel", "Steel Research International"),
    units_and_formulas_notes=("应力用 MPa；硬度须注明试验方法（HV / HB / HR）", "工艺参数须标注温度、速度、压力单位", "成分用质量分数（%）并说明检测依据", "试验结果用均值 ± 标准差与样本量表示"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Universal testing machine", "Scanning electron microscope", "X-ray diffraction", "Spectroanalyzer", "Thermal analyzer", "Optical microscope", "Ultrasonic flaw detector", "Hardness tester", "CNC machine tool", "Hydraulic press", "Quenching furnace", "Surface treatment equipment", "Laser cleaning machine", "Additive manufacturing machine", "Metallographic preparation equipment", "Fatigue testing machine", "Tensile testing machine", "Welding testing equipment", "Coordinate measuring machine", "Heat treatment equipment"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
