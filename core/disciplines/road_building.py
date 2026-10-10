"""道路建设学科论文支持：路基路面工程与养护技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="road_building",
    aliases=(
        "road_building",
        "道路建设",
        "道路工程",
        "road engineering",
        "公路",
        "路面工程",
        "路基",
        "pavement",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程背景）",
            "methodology（试验/仿真方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工程项目）",
            "analysis（设计与施工分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与规范综述）",
            "evidence synthesis（工程证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="GB/T 7714 或 APA 7",
    reporting_standards={
        "materials_test": "ASTM、EN 12697 或 GB/T 50001 系列方法须注明",
        "pavement_design": "MEPDG 或 JTG D50 方法学步骤须完整",
        "construction_control": "压实度、厚度、平整度检测频率须符合规范",
    },
    conventions=(
        "材料密度 g/cm³；回弹模量 MPa；强度 MPa 或 kN",
        "路面结构分层给出厚度与级配曲线",
        "温度/湿度条件（如压实含水率）须报告",
        "荷载模型采用标准轴载 BZZ-100/130",
        "施工与养护照片/原始记录附于补充材料",
    ),
    key_venues=(
        "Construction and Building Materials",
        "Transportation Research Record",
        "Journal of Materials in Civil Engineering",
        "公路交通科技",
        "中国公路学报",
    ),
    units_and_formulas_notes=(
        "沥青混合料压实度 %；空隙率 %；稳定度 kg",
        "平整度 IR/IRI 单位 mm/km 或 mm",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MARVAL Compactometer", "Bennett Falling Weight Deflectometer", "Laser Profiler", "GPR Ground Penetrating Radar", "Nuclear Density Gauge", "Asphalt Binder Analyzer", "Marshall Tester", "Superpave Gyratory Compactor", "Autoclave Oven", "SEM-EDS", "XRD", "Finite Element ABAQUS", "MEPDG Software", "Civil 3D", "Civil3D AutoCAD", "Global Positioning System RTK", "Photogrammetry Station", "Soil Hygrometer", "Penetration Tester", "Ravelmeter"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
