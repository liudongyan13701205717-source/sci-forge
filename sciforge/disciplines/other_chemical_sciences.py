"""其他化学科学学科论文支持：跨方向化学合成/表征与数据分析规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_chemical_sciences",
    aliases=(
        "other_chemical_sciences",
        "其他化学科学",
        "Other Chemical Sciences",
        "化学交叉学科",
        "Green Chemistry",
        "Supramolecular Chemistry",
        "Chemical Biology",
        "催化交叉",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methodology（实验方法与表征）",
            "results（合成与表征结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
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
    citation_style="ACS（国际化学期刊）/ GB/T 7714（中文）",
    reporting_standards={
        "reaction_yields": "ACS 有机合成报告规范",
        "crystallography": "IUCr 晶体学数据规范",
        "spectroscopy": "IUPAC 光谱学规范",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "反应条件（温度/时间/溶剂/摩尔比）须完整报告",
        "产率以 % 报告并给出纯品/粗品",
        "表征数据给出 ¹H/¹³C NMR、MS、IR 关键峰",
        "晶体结构须提交至 CCDC",
        "统计方法给出重复次数与误差",
    ),
    key_venues=(
        "Journal of the American Chemical Society",
        "Chemical Reviews",
        "Angewandte Chemie",
        "Chemical Science",
        "Chemical Journal of Chinese Universities",
    ),
    units_and_formulas_notes=(
        "温度用 ℃ 或 K，压力用 MPa 或 atm",
        "浓度用 mol/L，产率用 %",
        "波长用 nm，波数用 cm⁻¹",
        "统计量给出平均值与标准差",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("NMR Spectrometer (Bruker 400 MHz)", "Mass Spectrometer (Q-TOF)", "GC-MS / HPLC", "UV-Vis Spectrophotometer", "FTIR Spectrometer", "XRD (Bruker D8)", "SEM / TEM (Zeiss)", "Thermal Analyzer (TGA/DSC)", "ChemDraw（结构绘制）", "Materials Studio / GaussView", "Gaussian（量子化学）", "Origin（绘图）", "Excel", "EndNote", "LaTeX", "Photoshop", "Schrödinger Suite（分子模拟）", "Cryo-EM (Thermo Fisher)", "Rotovap 旋转蒸发仪", "Schlenk Line 无水无氧操作"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
