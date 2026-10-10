"""Civil security 学科论文支持：公共安全/犯罪学/应急/安防技术体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="civil_security",
    aliases=(
        "Civil security", "civil security", "public security",
        "security studies", "security management",
        "公共安全", "治安学", "安防", "公共安全管理", "社会治安",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（安全威胁/治理问题/理论框架）",
            "methodology（犯罪学统计/空间分析/技术评估/访谈）",
            "findings",
            "discussion（治理、伦理、政策建议）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case_description",
            "analysis",
            "prevention_implications",
            "references",
        ),
        "technology_review": (
            "abstract",
            "introduction",
            "system_overview",
            "performance_evaluation",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7 样式（法律类亦常见 Bluebook / GB/T 7714）",
    reporting_standards={
        "crime_statistics": "数据源（如公安部公报、CPS、犯罪档案）、统计口径与年份须明确",
        "spatial_analysis": "犯罪热点/空间模式分析遵循 Knox/Chavis/Getis-Ord G* 标准",
        "survey": "问卷遵循 IRB；受访者匿名化与隐私保护",
        "technology_evaluation": "安防设备/系统性能报告检测率、误报率、召回率与 F1",
        "intervention": "干预实验报告对照组、平行趋势、异质性",
    },
    conventions=(
        "案件类型/行为名称采用官方术语（如「电信诈骗」「校园欺凌」「群体性事件」）",
        "时间/地点/参与者引用官方口径；数据源标注年份与发布机构",
        "统计报告犯罪率（‰/‱）与人口基准",
        "技术系统性能报告 precision/recall/F1/ROC-AUC；标注数据集划分",
        "涉及隐私、未成年人、敏感信息的内容须匿名化并遵守伦理规范",
    ),
    key_venues=(
        "Journal of Criminal Justice",
        "Crime & Delinquency",
        "Journal of Quantitative Criminology",
        "Journal of Urban Affairs",
        "Studies in Crime & Offending",
        "中国公共安全",
        "公安学刊",
        "中国刑事警察杂志",
    ),
    units_and_formulas_notes=(
        "犯罪率（‰/‱）；发生数；立案数；破案率 %",
        "警务绩效报告警力配置（人/km²）、到岗率（%）",
        "技术系统性能报告 Precision/Recall/F1/AUC；时间延迟 ms/s",
        "调查/访谈报告参与者数、访谈时长、编码节点数",
        "统计报告 p 值、95% CI、效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("CrimeStat", "SPAG（Spatial Analysis for GIS）", "CrimeStat Analyzer", "CrimeAnalysis by CrimeStat", "i2 Analyst's Notebook", "Palantir Gotham", "ArcGIS Pro", "QGIS", "PostgreSQL + PostGIS", "Google Earth Pro", "OpenStreetMap", "CCTV 智能分析（海康威视 HikCentral / 大华 DSS）", "Cognex 视频分析", "BMC 视频分析", "VideoSifter", "FaceCheck ID", "MegaFace 人脸基准", "NIST FRVT", "NVivo", "Dedoose", "Atlas.ti", "SPSS Statistics", "Stata", "R 统计软件", "Python (pandas/scikit-learn)", "MATLAB", "SPSSAU", "NVivo Transcription", "Qualtrics", "OSF", "REDcap", "CrimeStat Analyst", "CrimeLab", "Gephi", "VosViewer"),
    category="法学",
    databases=("OpenAlex", "Crossref", "Scopus", "ERIC", "CNKI"),
)
