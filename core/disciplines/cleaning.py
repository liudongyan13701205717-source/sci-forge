"""Cleaning 学科论文支持：清洁科学/清洁技术/表面清洁/水与空气净化。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cleaning",
    aliases=(
        "Cleaning", "Cleaning Science", "清洁科学", "清洁工程",
        "Cleaning Technology", "清洁技术", "Cleaning Engineering",
        "Surface Cleaning", "清洁工程与技术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="Elsevier Journal Style",
    reporting_standards={
        "efficiency": "清洗效率须报告去除率（%）与清洁度（NTU/浊度值）",
        "conditions": "实验条件（温度、压力、流速、清洗剂浓度）须完整列出",
        "uncertainty": "数据须附不确定度（相对扩展不确定度 k=2）与重复实验次数",
        "surfaces": "表面表征须附 SEM 影像（标尺）与 AFM 粗糙度参数（Ra/Rq）",
        "environmental": "清洗液排放须报告 COD/BOD 与 pH；环保指标符合 GB/T 31962",
    },
    conventions=(
        "使用国际单位制（SI），质量/浓度单位统一为 mg/L、g/m² 等",
        "清洗效率用统一指标（去除率、清洁度、pH、浊度）",
        "实验条件（温度、压力、流速、清洗剂浓度）须显式记录",
        "数据须附不确定度与重复实验信息",
        "表面清洁实验须附 SEM/AFM 影像与能谱分析",
    ),
    key_venues=(
        "Journal of Cleaner Production",
        "Water Research",
        "Environmental Science & Technology",
        "Clean Technologies and Environmental Policy",
        "Chemosphere",
        "Environmental Pollution",
        "Science of the Total Environment",
        "Journal of Membrane Science",
    ),
    units_and_formulas_notes=(
        "浓度用 mg/L 或 g/m³；去除率用 %；浊度用 NTU 或 SFU",
        "清洗效率公式：η = (M₀ - M)/M₀ × 100%，M 为干基质量",
        "pH 无量纲；COD 用 mg O₂/L；电导率用 μS/cm",
        "表面粗糙度用 Ra/Rq（μm）；附着力用 ISO 2409 划格法等级",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Surface Force Apparatus", "Scanning Electron Microscope (SEM)", "Transmission Electron Microscope (TEM)", "Atomic Force Microscope (AFM)", "Spectrophotometer", "pH meter", "COD meter", "BOD meter", "Turbidity meter", "Laser Diffraction Particle Size Analyzer", "X-Ray Diffraction (XRD)", "FTIR spectrometer", "GC-MS", "HPLC", "MATLAB", "COMSOL Multiphysics", "ANSYS Fluent", "ChemDraw", "超声波清洗机", "高压水射流清洗设备"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Scopus"),
)
