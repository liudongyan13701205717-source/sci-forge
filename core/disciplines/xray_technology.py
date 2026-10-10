"""X 射线技术学科论文支持：医学影像与放射防护研究、Vancouver 引用样式与剂量学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="xray_technology",
    aliases=("xray_technology", "X 射线技术", "医学影像技术", "x-ray technology", "radiology technology", "放射技术"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与影像问题）",
            "materials and methods（影像采集与处理）",
            "results（影像与剂量数据）",
            "discussion（讨论与临床意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "patient/case information（病例信息）",
            "imaging protocol（影像方案）",
            "analysis（影像分析）",
            "discussion（讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and search（范围与检索）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="Vancouver 样式（数字编号，放射学专业期刊通用）",
    reporting_standards={
        "imaging_parameters": "影像采集参数（kVp、mAs、曝光时间）须报告",
        "dose_assessment": "剂量评估须遵循 ICRU/ICRP 标准",
        "image_quality": "影像质量须用客观指标评估（SNR、CNR、noise）",
        "ethics": "研究伦理审批与知情同意须给出",
        "statistics": "统计检验与样本量须报告",
    },
    conventions=(
        "影像术语遵循 DICOM/IAHR 等标准",
        "剂量单位用 mGy/mSv，剂量长度乘积用 mGy·cm",
        "影像采集参数须完整报告",
        "病例信息脱敏（去除 DICOM 标签中的 PII）",
        "Monte Carlo 模拟须报告物理模型与验证方法"
    ),
    key_venues=(
        "Radiology",
        "European Radiology",
        "Medical Physics",
        "Journal of Medical Imaging",
        "Radiation Protection Dosimetry"
    ),
    units_and_formulas_notes=(
        "剂量用 mGy（吸收剂量）与 mSv（当量剂量）",
        "曝光参数用 kVp（管电压）与 mAs（管电流-时间积）",
        "影像质量用 SNR/CNR 与 noise（HU 标准差）评估",
        "有效剂量用 DLP 与转换系数 k 计算"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("3D Slicer", "Osirix MD", "Orthanc (DICOM 存储与检索)", "dcm4che (DICOM 中间件)", "ITK-SNAP", "Geant4 (Monte Carlo 模拟)", "MCNP (Monte Carlo 模拟)", "GATE (Geant4 医学物理)", "CT-Analysis (CT 剂量分析)", "CT Dose Index 计算器", "电离室剂量仪", "数字减影血管造影 (DSA) 系统", "数字断层摄影系统 (DBT)", "数字乳腺摄影 (Mammo) 系统", "CT 扫描设备", "数字 X 射线摄影系统 (DR)", "Mimics (3D 重建)", "Mimvista (3D 可视化)", "MIM (治疗计划系统)", "DICOM OM"),
    category="医学",
    databases=("PubMed", "OpenAlex", "Crossref"),
)
