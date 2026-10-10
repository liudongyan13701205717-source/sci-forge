"""运动场草坪维护学科论文支持：草坪建植、养护、灌溉与检测技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="maintaining_sports_turf",
    aliases=(
        "maintaining_sports_turf",
        "运动场草坪维护",
        "运动草坪",
        "球场养护",
        "草坪管理",
        "Sports Turf",
        "Field Maintenance",
        "运动场地管理",
        "草坪养护",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
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
    citation_style="APA 7 样式（园艺与草坪研究通用）",
    reporting_standards={
        "field_trial": "田间试验遵循 CONSORT/STrengthening 规范",
        "remote_sensing": "遥感研究遵循 RECOMAND 建议",
        "meta_analysis": "元分析遵循 PRISMA 声明",
    },
    conventions=(
        "草坪质量指标须使用标准仪器（如 Clegg Impact Value、Ball Rebound）",
        "土壤取样须按剖面深度分层",
        "灌溉量须报告 mm/d 并标注水分亏缺阈值",
        "修剪高度以 mm 为单位并附标准",
        "病原/虫害识别须附显微镜或分子检测证据",
    ),
    key_venues=(
        "Crop Science",
        "Horticultural Science",
        "Journal of Turfgrass and Ornamental Plant Research",
        "Sports Turf Manager",
        "Applied Turfgrass Science",
        "Crop Production and Agriculture",
    ),
    units_and_formulas_notes=(
        "长度以 m/mm 为单位并标注 SI",
        "土壤水分以体积含水量 θ（%）报告",
        "灌溉量以 mm/d 或 L/m² 报告",
        "养分浓度以 mg/L 或 mg/kg 报告",
        "CIV/BRV 以标准方法测量并附样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Peren GRD2300A", "Peren GRD100A", "Peren T300T", "Peren T600TR", "Peren MGT", "Veris 3D", "Trimble T3", "Trimble T7", "Trimble AgriGPS 4400", "Trimble TSC3", "DJI Phantom 4 RTK", "DJI Mavic 2 Enterprise", "MicaSense RedEdge", "DroneDeploy", "Greensmaster 2700", "John Deere ZTR", "Toro Compressor", "SCS Turf Trax", "Peren GRD55", "Trifecta Soil Core Sampler"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
