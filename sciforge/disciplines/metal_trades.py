"""金属加工技术学科论文支持：金属加工技术（金工）工艺、材料与检验规范及行业报告体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="metal_trades",
    aliases=("metal_trades", "金属加工", "金工", "金属工艺", "metal_trade", "metalworking", "metal_craft", "metal_industry", "metal_products", "metal_processing", "metal_work"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）", "methodology（材料、工艺参数与试验方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（车间、设备与工艺实例）", "analysis（工艺与质量分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（金属成形与材料学综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"k1": "材料试验遵循 ASTM / ISO 标准", "k2": "工艺参数报告遵循 ISO 9001 质量管理体系", "k3": "安全与职业健康遵循 OSHA / ISO 45001"},
    conventions=("材料牌号须用 ISO 或 ASTM 标准标注", "试验条件（温度、载荷、速率）须说明", "工艺参数用 SI 单位并标注", "结果须附不确定度与样本量", "图表须标明设备型号与量程"),
    key_venues=("Materials and Design", "Journal of Materials Processing Technology", "International Journal of Metalworking", "Iron and Steel", "Welding Journal"),
    units_and_formulas_notes=("应力用 MPa；硬度和强度须注明试验方法（HV / HB / HR）", "工艺参数须标注温度、压力、速度单位", "化学成分用质量分数（%）并说明检测依据", "试验结果用均值 ± 标准差与样本量表示"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Universal testing machine", "Scanning electron microscope", "X-ray diffraction", "Spectroanalyzer", "Coordinate measuring machine", "Welding testing equipment", "Thermal analyzer", "Optical microscope", "Ultrasonic flaw detector", "Hardness tester", "Tensile testing machine", "Fatigue testing machine", "Metallographic preparation equipment", "Laser cleaning machine", "Additive manufacturing machine", "CNC machine tool", "Hydraulic press", "Rolling mill", "Quenching furnace", "Surface treatment equipment"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
