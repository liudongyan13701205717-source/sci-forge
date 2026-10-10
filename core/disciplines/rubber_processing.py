"""橡胶加工学科论文支持：胶料配方、硫化工艺与性能测试。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="rubber_processing",
    aliases=(
        "rubber_processing",
        "橡胶加工",
        "rubber",
        "橡胶",
        "硫化",
        "vulcanization",
        "聚合物加工",
        "胶料",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（材料背景）",
            "methodology（配方与试验方法）",
            "results（性能结果）",
            "discussion（结构与性能讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（产品/工艺案例）",
            "analysis（配方与工艺分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（结构与加工综述）",
            "evidence synthesis（性能证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="ACS 或 APA 7",
    reporting_standards={
        "rubber_test": "ASTM D、ISO 2230 或 GB/T 528 系列方法须注明",
        "compounding": "配方质量分数、混炼工艺与温度须完整",
        "curing": "硫化曲线条件与时间点须报告",
    },
    conventions=(
        "配方以 phr（每百份生胶）表示；填料与助剂列全",
        "硫化条件以温度 °C 与时间 min 报告；交联度以 μ 表示",
        "力学性能拉伸强度 MPa；伸长率 %",
        "热性能以 DSC、TGA 曲线附于原图",
        "老化试验温度与时长须给出",
    ),
    key_venues=(
        "Rubber Chemistry and Technology",
        "Polymer Testing",
        "Journal of Applied Polymer Science",
        "Industrial and Engineering Chemistry Research",
        "橡胶工业",
    ),
    units_and_formulas_notes=(
        "硬度 Shore A；回弹率 %；耐磨体积损失 cm³",
        "粘度以 Pa·s 或 ml/min（ASTM D1230）报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Mixer Lab Ram Platen", "Banbury Mixer", "Press Tester", "Cureometer", "Rheometer", "Universal Tensile Tester", "Hardness Tester", "Abrasion Tester", "DSC Differential Scanning Calorimeter", "TGA Thermogravimetric Analyzer", "FTIR Spectrometer", "Raman Spectrometer", "SEM Scanning Electron Microscope", "GPR Rubber Tester", "Thermal Imager", "Chromatography HPLC", "NMR Nuclear Magnetic Resonance", "Swelling Tester", "Permeability Tester", "Fatigue Testing Machine"),
    category="工学",
    databases=("OpenAlex", "Crossref", "ScienceDirect"),
)
