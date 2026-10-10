"""Aboriginal And Torres Strait Islander Environmental Knowledges And Management 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aboriginal_and_torres_strait_islander_environmental_knowledges_and_management",
    aliases=(
        "Aboriginal And Torres Strait Islander Environmental Knowledges And Management",
        "原住民环境知识与管理",
        "ATSI Environmental Management",
        "Indigenous Environmental Management",
        "First Nations Land Management",
        "Aboriginal Environmental Knowledge",
        "Country-based Land Management",
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
    citation_style="APA",
    reporting_standards={
        "ocap": "原住民环境数据须遵循 OCAP 原则",
        "tekm": "传统生态知识与现代科学知识须明确区分来源与归属",
        "field_data": "野外调查须记录季节性、地理位置与文化安全限制",
        "co_management": "联合管理研究须反映原住民社区决策过程与治理结构",
    },
    conventions=(
        "环境知识须区分科学数据与原住民传统知识（TEK），不可混用",
        "涉及土地、水域与生态系统的研究须获得原住民土地管理局授权",
        "野外调查须记录季节性与地理位置信息，尊重文化安全限制",
        "联合管理案例须反映原住民社区决策过程与治理结构",
    ),
    key_venues=(
        "Indigenous Resource Management",
        "Journal of Applied Ecology",
        "Environmental Management",
        "Ecological Applications",
        "Conservation Biology",
        "Journal of Cultural & Environmental Change",
    ),
    units_and_formulas_notes=(
        "物种丰度以每样带个体数（ind/strip）或每样方面积（ind/m²）计量，须注明采样方法",
        "生物量以 g/m² 或 t/ha 计量，覆盖度以百分比（%）报告",
        "传统生态知识（TEK）须注明知识持有者社区与季节背景，不可与定量科学数据混用",
        "空间数据须注明投影坐标系与精度（如 1:10000 地形图基准），文化敏感区域须标注访问限制",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("QGIS", "ArcGIS", "Google Earth Pro", "Mapbox", "NVivo", "SPSS", "R", "iNaturalist", "eBird", "EndNote", "Microsoft OneNote", "Adobe Lightroom", "Canva", "FieldMapper", "MapIT", "ArcPad", "Lantype", "Survey123", "MAGIS（Mobile ArcGIS）", "Rapid Shapefile Tools"),
    category="工学",
    databases=("OpenAlex",),
)
