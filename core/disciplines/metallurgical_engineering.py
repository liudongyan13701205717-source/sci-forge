"""冶金工程学科论文支持：钢铁/有色金属冶金工艺与资源利用体系、试验与流程建模规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="metallurgical_engineering",
    aliases=("metallurgical_engineering", "冶金工程", "metal_engineering", "metallurgy", "iron_steel_metallurgy", "ferrous_metallurgy", "non_ferrous_metallurgy", "metallurgical_process", "extractive_metallurgy", "industrial_metallurgy", "materials_metallurgy"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）", "methodology（试验材料、工艺与流程建模）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（冶炼厂与流程实例）", "analysis（工艺与能效分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（冶金原理与流程综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 样式",
    reporting_standards={"k1": "试验与流程数据遵循 ASTM / ISO 标准", "k2": "能耗与排放报告遵循 ISO 14001 / 行业规范", "k3": "流程模拟须遵循软件验证与不确定度报告规范"},
    conventions=("矿石/原料牌号与来源须注明", "工艺流程须以流程图表示并标注各工序", "组分用质量分数或摩尔分数并标注基准", "热力学数据须注明温度与压力条件", "结果须附不确定度与重复性验证"),
    key_venues=("Metallurgical Transactions", "Minerals Engineering", "Journal of Chemical Technology and Biotechnology", "Ironmaking Steelmaking", "International Materials Reviews"),
    units_and_formulas_notes=("热力学量用 kJ/mol；温度注明基准（298 K 或工作温度）", "成分用质量分数（%）并说明检测依据", "能耗用 GJ/t 或 kWh/t 并标明范围", "模拟结果须给验证数据与误差来源"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Thermodynamic calculation software", "Phase diagram software", "X-ray diffraction", "Scanning electron microscope", "Mass spectrometer", "Thermal analyzer", "Spectroanalyzer", "Metallographic preparation equipment", "Process simulation software", "Energy analysis software", "Emissions monitoring equipment", "High temperature testing equipment", "Slag analysis equipment", "Ore processing pilot equipment", "Hydrometallurgy testing equipment", "Pyrometallurgy testing equipment", "Electrometallurgy equipment", "Flotation testing machine", "Crushing and grinding equipment", "Sample preparation equipment"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
