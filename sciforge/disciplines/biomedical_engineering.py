"""生物医学工程论文支持：医疗器械、生物力学、生物材料、医学影像、组织工程。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biomedical_engineering",
    aliases=(
        "biomedical_engineering",
        "BME",
        "biomedical_device_engineering",
        "medical_device_engineering",
        "tissue_engineering",
        "bioinstrumentation",
        "生物医学工程",
        "医学工程",
        "生物医学器械",
        "医疗器械工程",
        "生物材料与组织工程",
        "医学影像工程",
    ),
    paper_types={
        "research": ("abstract", "introduction", "materials and methods", "results", "discussion", "conclusions", "references"),
        "review": ("abstract", "introduction", "classification", "state-of-the-art", "challenges", "future directions", "conclusions", "references"),
        "technical": ("abstract", "introduction", "design", "fabrication", "characterization", "application", "conclusions", "references"),
    },
    citation_style="Vancouver（编号），如 [1]",
    reporting_standards={
        "biocompatibility": "生物相容性须按 ISO 10993 系列标准报告",
        "mechanical_testing": "力学测试须报告试验标准（ASTM/ISO）、试样尺寸与加载速率",
        "clinical": "临床试验须注册（ClinicalTrials.gov），报告伦理批准与知情同意",
        "imaging": "医学影像须报告设备型号、序列参数（TR/TE/层厚）与重建算法",
    },
    conventions=(
        "器械用正式商品名（首次出现括注通用名/型号）",
        "生物材料用标准名称（如 PCL/PLGA/HA）+ 供应商与批号",
        "图：显微镜图须含比例尺；力学曲线须含误差棒（n≥3）",
        "统计须报告检验方法、p 值与效应量",
        "伦理声明放在方法部分开头或单独伦理声明段",
    ),
    key_venues=(
        "Biomaterials",
        "Medical Engineering & Physics",
        "IEEE Transactions on Biomedical Engineering",
        "Journal of Biomechanical Engineering",
        "Tissue Engineering Part A/B/C",
        "Acta Biomaterialia",
        "Medical Image Analysis",
        "Radiology",
        "Journal of the Mechanical Behavior of Biomedical Materials",
    ),
    units_and_formulas_notes=(
        "力学强度用 MPa/GPa；弹性模量用 MPa/GPa",
        "细胞密度用 cells/cm² 或 cells/mL",
        "降解速率用 %/day 或 mg/day",
        "影像分辨率用 mm 或 μm/pixel",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "ANSYS Mechanical", "ANSYS Fluent", "COMSOL Multiphysics", "Abaqus", "MSC Nastran", "Altair HyperWorks", "SolidWorks", "SolidWorks Simulation", "OpenFOAM", "Gmsh", "ParaView", "Mimics（Materialise）", "3-matic（Materialise）", "3D Slicer", "ITK-SNAP", "SimpleITK", "Fiji（ImageJ）", "OpenCV", "CELLINK BioPlotter", "Zeiss Xradia 610", "Instron 5969", "Zeiss LSM 800", "Zeiss Sigma 300VP", "Cytiva AKTA pure 25", "Thermo Nanoindent G200", "Thermo Zetasizer Nano"),
    category="工学",
    databases=("OpenAlex", "Crossref", "PubMed", "PATENTSCOPE", "IEEE Xplore", "CNKI"),
)
