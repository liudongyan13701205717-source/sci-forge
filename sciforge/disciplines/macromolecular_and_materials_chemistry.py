"""高分子与材料化学学科论文支持：聚合物合成、结构与性能研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="macromolecular_and_materials_chemistry",
    aliases=(
        "macromolecular_and_materials_chemistry",
        "高分子与材料化学",
        "polymers",
        "高分子",
        "materials chemistry",
        "聚合物",
        "polymer science",
        "nanomaterials",
        "soft matter",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景）",
            "methodology（合成与表征方法）",
            "results（结果与表征）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（材料体系描述）",
            "analysis（结构与性能分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="ACS",
    reporting_standards={
        "k1": "合成实验报告试剂、溶剂与催化剂用量",
        "k2": "表征数据报告仪器型号与测试条件",
        "k3": "性能数据须报告重复次数与置信区间",
    },
    conventions=(
        "聚合物命名遵循 IUPAC 命名规则",
        "分子量报告 M_n、M_w 与 PDI",
        "结构表征附核磁、红外与质谱图",
        "性能测试标注温度、湿度与试样尺寸",
        "化学结构使用 ChemDraw 绘制",
    ),
    key_venues=(
        "Macromolecules",
        "Polymer",
        "Journal of Polymer Science",
        "Chemical Reviews",
        "Advanced Materials",
    ),
    units_and_formulas_notes=(
        "分子量以 g/mol 报告",
        "反应温度以 °C 报告并给出区间",
        "力学性能以 MPa 或 GPa 报告",
        "溶液浓度以 mol/L 或 wt% 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("NMR (Bruker)", "GPC (Waters)", "FTIR (Thermo Fisher)", "XRD (Bruker D8)", "SEM (Zeiss)", "TEM (JEOL)", "DSC (TA Instruments)", "TGA (TA Instruments)", "UV-Vis (Shimadzu)", "Rheometer (Anton Paar)", "Universal Testing Machine (Instron)", "XPS (Thermo Fisher)", "AFM (Bruker)", "ChemDraw", "Materials Studio", "Gaussian", "VASP", "Origin", "MATLAB", "Avizo"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
