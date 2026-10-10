"""工业烘焙面粉生产论文支持：小麦加工、面粉品质、烘焙工艺与食品安全。"""
from __future__ import annotations
from sciforge.disciplines.base import Discipline
DISCIPLINE = Discipline(
    name="industrial_bakeryflour_production",
    aliases=("industrial_bakeryflour_production", "工业烘焙面粉生产", "wheat_milling", "baking_flour", "flour_technology", "milling_engineering", "breadmaking", "flour_quality", "grain_processing"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法论）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 或 ACS（食品科学）",
    reporting_standards={"milling": "碾磨工艺须按 AACC/ICC/Codex 报告筛号、转速与水分", "flour_quality": "面粉品质须报告 ICC 标准测定（灰分、湿面筋、FQL、远红外）", "safety": "食品安全须遵循 HACCP/FSSC 22000 报告 CCP 与限值"},
    conventions=("灰分/水分/面筋含量以 ICC/AACC 标准编号引用", "面粉加工度以筛号与百分比表达", "发酵工艺用 dough yield 与温度梯度表达", "图像须标注取样位点与仪器条件"),
    key_venues=("Journal of Cereal Science", "LWT - Food Science and Technology", "Journal of Cereal Chemistry", "Journal of Cereals and Oils", "Cereal Chemistry"),
    units_and_formulas_notes=("水分与灰分以 % 表示（干基/湿基需注明）", "蛋白质含量以 % 或 g/100g 表示", "面粉加工度以 % 表示", "发酵时间以分钟、温度以 °C 表达"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Perten Fibrograph", "BROTEF-4000 面包机", "Alveograph", "Chorleywood Breadmaker", "Farinograph", "Myograph", "Farinograph C", "Staubli 磨粉机", "远红外测水仪", "近红外（NIR）", "气相色谱（GC）", "高效液相色谱（HPLC）", "GC-MS", "XRF", "FTIR", "XRD", "MFT 混水率测定仪", "ICC 制粉机", "Falling Number 测仪", "Alveograph Lab"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
