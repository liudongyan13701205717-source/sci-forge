"""食品加工业学科论文支持：食品工厂工艺、生产与质量控制。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_processing_industry",
    aliases=("food_processing_industry", "食品加工业", "食品加工", "食品工业", "food processing", "food industry", "食品加工工程", "食品工厂"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "HACCP 计划（HACCP 计划）", "k2": "GMP 良好生产规范（GMP 良好生产规范）", "k3": "ISO 22000（ISO 22000）"},
    conventions=("工艺参数（温度/时间/pH/压力）须完整记录且可复现", "批次编号与抽样方案须说明", "微生物指标报告 CFU/g 或 CFU/mL", "产品特性测试须注明仪器与标准方法", "讨论须区分工艺改进与设备改进"),
    key_venues=("Journal of Food Engineering", "LWT - Food Science and Technology", "Innovative Food Research", "Food and Bioproducts Processing", "Journal of Food Processing and Preservation"),
    units_and_formulas_notes=("水分活度 aw 无量纲（0-1）", "杀菌强度用 F 值（°C·s）", "能耗用 kWh/t 或 MJ/t", "产量与得率用 % 或 g/kg"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("食品质构仪（Texture Analyzer）", "HPLC 高效液相色谱仪", "气相色谱-质谱联用仪 GC-MS", "近红外光谱仪 NIR", "流变仪 Rheometer", "电子鼻 E-nose", "食品红外热成像仪", "HACCP 食品安全管理软件", "MES 制造执行系统", "食品工厂 PLC 控制系统", "X 射线食品检测系统", "金相显微镜", "食品离心脱水机", "真空包装测试机", "食品 X 射线荧光仪 XRF", "食品 pH/水分测定仪", "食品色度计", "食品冷冻隧道 -40°C 冷库", "食品蒸汽灭菌釜 Retort", "食品离心喷雾干燥机"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
