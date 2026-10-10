"""博物馆学学科论文支持：博物馆理论与实践研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="museology",
    aliases=(
        "museology", "博物馆学", "Museum science", "museum management",
        "博物馆管理", "博物馆研究", "展陈设计",
        "exhibition studies", "展陈研究",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（研究设计）",
            "results（发现）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（博物馆背景）",
            "analysis（运营/展陈分析）",
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
    citation_style="Chicago 样式",
    reporting_standards={
        "k1": "观众研究须报告样本量、抽样方法与问卷信效度",
        "k2": "展陈评估须报告参观时长与互动行为数据",
        "k3": "机构研究须报告运营指标与治理结构",
    },
    conventions=(
        "博物馆名称首次出现须给出全称与所在地",
        "藏品描述须遵循 ICOM 藏品分类",
        "展陈分析须交代空间布局与灯光参数",
        "参观者访谈须说明知情同意与伦理审查",
        "引用博物馆政策须给出发布机构与年份",
    ),
    key_venues=(
        "Museum Management and Curatorship",
        "International Journal of Museum Management and Curatorship",
        "Museum International",
        "Curator: The Museum Journal",
        "《中国博物馆》",
    ),
    units_and_formulas_notes=(
        "藏品数量给出件/套口径",
        "展陈面积用 m²；参观人数按日/月/年分组",
        "参观时长用分钟；停留时长用秒",
        "预算与收入数据须说明统计口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "SPSS", "RStudio", "SAS", "Tableau", "Power BI", "SketchUp", "Autodesk Revit", "Enscape", "Rhino", "3ds Max", "Adobe InDesign", "ICOM CMS", "Cohesion", "Cultural Heritage Management Systems", "EndNote", "Zotero", "Google Analytics", "KoboToolbox"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
