"""医学影像技术学科论文支持：成像操作/影像质量/辐射防护体裁、ACR 引用样式与影像参数记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="radiology_technology",
    aliases=(
        "radiology_technology",
        "医学影像技术",
        "影像技术",
        "放射技术",
        "Radiology Technology",
        "Medical Imaging Technology",
        "影像设备操作",
        "辐射防护",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与影像问题）", "methodology（成像方案与人群）", "results（影像质量与诊断数据）", "discussion（技术要点与临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（技术分析与影像评估）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ACR/Radiology 样式（作者-年份；遵循 ACR 影像报告规范）",
    reporting_standards={
        "k1": "影像质量研究须遵循 ACR 成像质量指南",
        "k2": "剂量学数据须遵循 ICRP 与 ICRU 剂量报告规范",
        "k3": "系统综述须遵循 PRISMA 声明",
    },
    conventions=(
        "成像参数（序列、层厚、kV、mAs、磁场强度）须完整报告",
        "辐射剂量用 mGy（CTDIvol）与 mGy·cm（DLP）",
        "阅片者一致性与 κ 值须报告",
        "设备型号、软件版本与成像协议须标注",
        "患者定位与体位描述须完整",
    ),
    key_venues=(
        "Radiology",
        "European Journal of Radiology",
        "Journal of Nuclear Medicine Technology",
        "Investigative Radiology",
        "Journal of Imaging Science and Technology",
    ),
    units_and_formulas_notes=(
        "剂量单位用 mGy 与 mGy·cm",
        "图像质量用 SNR/CNR 与主观评分",
        "统计量给出 M/SD 与 95% CI",
        "样本量与阅片者数量须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("GE Syngo.via", "Siemens Syngo.via", "Philips IntelliSpace", "Agfa Impax", "TeraRecon", "OsiriX MD", "Radiant DICOM Viewer", "Carestream eFilm", "Horos", "3D Slicer", "ITK-SNAP", "QIBA", "DICOM", "ACR Imaging Guidelines", "Radimetrics", "Medimorph", "ImageJ", "GE ADWS", "GE PACS", "GE CareStream"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
