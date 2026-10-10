"""地方公共行政学科论文支持：基层治理、地方政府决策与公共服务。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="local_public_administration",
    aliases=(
        "local_public_administration",
        "地方公共行政",
        "local government",
        "基层治理",
        "地方政府",
        "public administration",
        "local policy",
        "governance",
        "street-level bureaucracy",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题背景）",
            "methodology（研究方法）",
            "results（研究结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（政策分析）",
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
    citation_style="APA 7",
    reporting_standards={
        "k1": "定量研究须报告样本、置信区间与效应量",
        "k2": "政策评估采用 DID 或 RD 等识别策略",
        "k3": "地方治理案例标注辖区与时间段",
    },
    conventions=(
        "政策研究注明发文机关与文号",
        "财政数据使用统一口径并跨年可比",
        "问卷标注有效样本与缺失处理",
        "田野材料注明来源与知情同意",
        "制度比较研究明确比较维度",
    ),
    key_venues=(
        "Journal of Public Administration, Theory and Practice",
        "Public Administration Review",
        "Administration & Society",
        "Journal of Chinese Public Administration",
        "中国行政管理",
    ),
    units_and_formulas_notes=(
        "财政指标按万元人民币报告",
        "基尼系数区间 [0, 1]",
        "投票率以百分比计",
        "政策文本分析标注词频与主题数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("R", "Stata", "SPSS", "NVivo", "ATLAS.ti", "Python", "Tableau", "QGIS", "GIS (ArcGIS Pro)", "OpenRefine", "MaxQDA", "NVivo Coding", "WeLab Survey (问卷星)", "Weaver (WeChat Poll)", "Pew Research Center", "World Bank WDI", "OECD.Stat", "IMF Fiscal Data Explorer", "CEPII Geocodifier", "Google Public Datasets"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
