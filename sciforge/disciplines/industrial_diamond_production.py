"""工业金刚石生产论文支持：HPHT/CVD 合成、磨料加工、半导体散热与培育钻。"""
from __future__ import annotations
from sciforge.disciplines.base import Discipline
DISCIPLINE = Discipline(
    name="industrial_diamond_production",
    aliases=("industrial_diamond_production", "工业金刚石生产", "HPHT_diamond", "CVD_diamond", "synthetic_diamond", "polycrystalline_diamond", "PDC_compact", "diamond_synthesis", "lab_grown_diamond"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法论）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 或 ACS（材料科学）",
    reporting_standards={"synthesis": "合成工艺须报告温压时间（HPHT）或工艺气体比例（CVD）、衬底、生长率", "pdc": "PDC 复合体须报告金刚石含量、基体成分、粒度、烧结温压", "characterization": "表征须报告方法（XRD/Raman/SEM/XPS）、不确定度与样品位置"},
    conventions=("金刚石类型按 IIa/IIb/IIc/I/IIIb 分级标注", "生长率以 μm/h 或 mm/h 表示", "合成条件以 MPa/GPa、°C/K 并列", "掺杂剂量以 ppm、at% 或 wt% 表示"),
    key_venues=("Diamond and Related Materials", "Carbon", "Journal of Crystal Growth", "MRS Bulletin", "Carbon Letters"),
    units_and_formulas_notes=("压力以 MPa/GPa，温度以 °C/K 表示", "生长率以 μm/h 或 mm/h 表示", "掺杂剂量以 ppm/at%/wt% 表示", "粒度以 μm、比表面积以 m²/g 表示"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("HPHT 压机（六面顶）", "冷床 HPHT 压机", "微波 CVD 反应器", "热丝 CVD（HFCVD）反应器", "直流等离子体 CVD（DCP-CVD）", "XRD", "Raman", "SEM", "TEM", "XPS", "NIR 光谱仪", "FTIR", "DLS", "N2 吸附仪", "热导率仪", "激光粒度仪", "ICP-MS", "MATLAB", "Python", "ANSYS"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
