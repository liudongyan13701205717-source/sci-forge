"""桥梁工程学科论文支持：桥梁结构/施工体裁、ASCE 引用样式与桥梁记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bridge_construction",
    aliases=(
        "bridge_construction",
        "Bridge construction",
        "桥梁工程",
        "桥梁建造",
        "桥梁设计",
        "桥梁结构",
        "桥梁施工",
        "bridge engineering",
        "bridge design",
        "bridge construction",
        "桥梁结构工程",
        "桥梁建造",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（试件、材料、试验）",
            "results（强度、变形、耐久性）",
            "discussion",
            "conclusion",
            "references",
        ),
        "design": (
            "abstract",
            "design brief",
            "structural analysis",
            "materials and construction",
            "results",
            "conclusion",
            "references",
        ),
    },
    citation_style="ASCE 样式（作者-年份）",
    reporting_standards={
        "geometry": "桥长、桥宽、跨径须明确",
        "materials": "混凝土等级、钢筋规格、钢材牌号须完整",
        "analysis": "承载能力极限状态（ULS）与正常使用极限状态（SLS）须按规范分析",
        "testing": "承载能力试验、荷载试验须按规范测试",
    },
    conventions=(
        "桥梁类型符号用中文术语（梁桥、拱桥、斜拉桥、悬索桥）",
        "桥面荷载符号用 Q（车辆）、P（人群）标记",
        "混凝土强度等级用 C30、C40 等标记",
        "钢筋用 HRB400、HRB500 等标记",
        "分析须符合 GB 50011 或 Eurocode",
    ),
    key_venues=(
        "International Journal of Bridge Engineering",
        "Engineering Structures",
        "Journal of Performance of Constructed Facilities",
        "Journal of Structural Engineering",
        "International Journal of Impact Engineering",
        "Construction and Building Materials",
        "Journal of Bridge Engineering",
    ),
    units_and_formulas_notes=(
        "跨度用 m 报告",
        "荷载用 kN 或 kN/m 报告",
        "混凝土强度用 C30、C40 等标记",
        "钢筋用 HRB400、HRB500 等标记",
        "分析须符合 GB 50011 或 Eurocode",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD Civil 3D", "Bentley OpenBridge", "Bentley MicroStation", "Bentley STAAD", "SAP2000", "ETABS", "MIDAS Civil", "Genie Civil", "LUSAS", "RISA-3D", "LiDAR Scanner", "Total Station", "Trimble GPS", "GNSS", "Drone Survey", "Agisoft Metashape", "CloudCompare", "LEAP Bridge", "STRUSAFE", "Microsoft Project"),
    category="工学",
    databases=("OpenAlex", "Google Scholar", "ScienceDirect", "Elsevier"),
)
