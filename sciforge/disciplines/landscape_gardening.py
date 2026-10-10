"""景观园艺学科论文支持：园艺植物、栽培技术、植物景观与城市绿建。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="landscape_gardening",
    aliases=(
        "landscape_gardening",
        "景观园艺",
        "Landscape Gardening",
        "Horticulture",
        "Ornamental Horticulture",
        "Urban Horticulture",
        "Garden Design",
        "Plant Landscape",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（绪论）",
            "methodology（研究方法）",
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
    citation_style="APA",
    reporting_standards={
        "k1": "GB/T 26795 园林绿化植物材料质量等级",
        "k2": "BS 5837 城市树木与施工管理",
        "k3": "AHTA 植物栽培标准",
    },
    conventions=(
        "植物描述须使用拉丁学名（斜体）与中文名",
        "栽培试验须采用随机区组或拉丁方设计",
        "物候记录须注明观测时间与地点",
        "土壤数据须包括pH、有机质、养分与质地",
        "病虫害防治须优先推荐生物防治措施",
    ),
    key_venues=(
        "HortScience",
        "Acta Horticulturae",
        "Journal of Plant Growth Regulation",
        "Urban Forestry & Urban Greening",
        "中国园林",
    ),
    units_and_formulas_notes=(
        "pH以0~14无量纲值表示",
        "土壤有机质以%表示",
        "株距以m表示，冠幅以cm表示",
        "生长量以mm/年或cm/年表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "QGIS", "SketchUp", "AutoCAD", "Adobe Illustrator", "Adobe Photoshop", "Rhino", "Grasshopper", "Enscape", "Lumion", "V-Ray", "D5 Render", "Plant Designing", "MATLAB", "R", "OriginPro", "SPSS", "Google Earth", "PlantNET", "GB/T 26795"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
