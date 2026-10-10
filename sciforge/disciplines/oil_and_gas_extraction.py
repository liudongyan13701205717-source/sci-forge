"""石油与天然气开采学科论文支持：油气开采/增产体裁、SPE 引用样式与开采记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="oil_and_gas_extraction",
    aliases=("oil_and_gas_extraction", "油气开采", "石油开采", "油气生产", "oil extraction", "oil production"),
    paper_types={
        "research": ("abstract", "introduction（背景与开采问题）", "methodology（工艺与实验）", "results（产量与动态）", "discussion（机理与优化）", "references"),
        "case_study": ("abstract", "introduction", "case description（油田与地层）", "analysis（增产措施）", "results（产量提升）", "discussion（经验与改进）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（技术综述）", "evidence synthesis（证据整合）", "future directions", "references"),
    },
    citation_style="SPE 样式",
    reporting_standards={"field_report": "遵循 SPE 采油报告规范", "systematic_review": "遵循 PRISMA 声明", "case_report": "遵循 CARE 指南"},
    conventions=("油藏参数须注明地层", "产量单位须一致（bbl/d 或 t/d）", "采收率给出百分比", "井位坐标须报告", "工具须注明 API 等级"),
    key_venues=("SPE Production & Operations", "Journal of Petroleum Science and Engineering", "SPE Reservoir Evaluation & Engineering", "Journal of Natural Gas Science and Engineering", "Fuel"),
    units_and_formulas_notes=("产量用 bbl/d 或 t/d", "压力用 MPa", "采收率用 %", "孔隙度用 %", "公式用 amsmath"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("油藏模拟软件", "Eclipse Reservoir Simulator", "CMG Stars", "Petrel 油藏建模", "Surfer 建模软件", "Compass 3D", "Petrel 2D 建模", "Hydraulic Fracturing 软件", "CompletionDesigner", "Production Logging 工具", "Mudlog 分析", "RockWorks", "Seismic 解释软件", "Petrel 2D/3D", "Python", "MATLAB", "Petroleum Engineering 计算软件", "SPSS", "Excel", "CAD"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
