"""口腔颌面外科学科论文支持：手术技术、颌面创伤与正颌手术体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dental_surgery",
    aliases=(
        "dental_surgery", "口腔颌面外科", "口腔外科",
        "oral and maxillofacial surgery", "OMFS",
        "maxillofacial surgery", "颌面外科学",
        "oral surgery", "oral and maxillofacial pathology",
        "implant surgery", "种植外科",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（临床问题与手术背景）",
            "methods（手术方案、分组、术后评估）",
            "results（手术成功率与并发症）",
            "discussion（临床意义与改进建议）",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、盲法、手术步骤）",
            "results（疗效与安全性终点）",
            "discussion",
            "references",
        ),
        "case_series": (
            "abstract",
            "introduction",
            "case presentation（患者情况、手术过程、术后随访）",
            "discussion（鉴别诊断与手术策略）",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "RCT": "CONSORT 声明",
        "case_series": "CARE 指南",
        "surgical_technique": "手术步骤须完整描述（入路、切骨、缝合）",
        "complications": "并发症报告须分类（Clavien-Dindo 分级）",
    },
    conventions=(
        "手术入路与切口位置须明确标注",
        "影像评估注明设备（CBCT/CT/MRI）与扫描参数",
        "种植体尺寸/角度/深度须精确记录",
        "术后恢复评估给出时间窗（如 7 天、3 个月、6 个月）",
        "疼痛评估用 VAS 或 NRS 量表",
    ),
    key_venues=(
        "Journal of Oral and Maxillofacial Surgery",
        "Clinical Oral Investigations",
        "International Journal of Oral and Maxillofacial Implants",
        "Journal of Cranio-Maxillofacial Surgery",
        "Oral Surgery, Oral Medicine, and Oral Pathology",
    ),
    units_and_formulas_notes=(
        "切骨深度用 mm 表示",
        "种植体直径/长度用 mm 表示",
        "手术时间用 min 表示",
        "骨密度用 Hounsfield Units (HU) 表示",
        "VAS 疼痛评分用 0-10 分",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CBCT", "口内扫描仪", "CAD/CAM 义齿设计软件", "种植导板设计软件", "手术导航系统", "超声骨刀", "种植扭矩测试仪", "万能试验机", "锥形束 CT", "CBCT 分析软件", "SPSS", "R (RStudio)", "Microsoft Excel", "Power BI", "Surgical Planning Software", "Slicer", "3D 打印机", "种植手术套件", "超声骨刀系统", "显微外科设备"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Crossref"),
)
