"""社区规划学科论文支持：社区规划/城市社区体裁、APA 引用样式与规划研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="community_planning",
    aliases=(
        "community_planning", "社区规划", "community planning and development",
        "urban community planning", "城市社区规划", "urban design",
        "城市设计", "residential community planning", "居住区规划",
        "neighborhood planning", "邻里规划", "spatial planning",
        "社区营造", "community design",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与规划问题）",
            "literature review（文献综述）",
            "methods（方法与数据采集）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction（案例背景）",
            "site analysis（场地分析）",
            "method（研究方法）",
            "findings（发现）",
            "analysis（分析）",
            "recommendations（建议）",
            "references",
        ),
        "evaluation": (
            "abstract",
            "introduction",
            "program description（规划方案描述）",
            "evaluation design（评估设计）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Journal of the American Planning Association 遵循 APA 规范）",
    reporting_standards={
        "quantitative": "定量研究遵循 CONSORT 或 PRISMA 声明",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "participatory": "参与式研究遵循 CARE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "规划方案须说明适用对象（居住/商业/工业）与人口规模假设",
        "规划评估须报告满意度与可达性指标",
        "涉及公众参与的研究须声明参与方式与伦理审查",
        "规划指标须注明来源与统计口径",
        "空间分析结果须给出比例尺与地理投影",
    ),
    key_venues=(
        "Journal of the American Planning Association",
        "Planning Perspectives",
        "Urban Studies",
        "Housing Studies",
        "Planning, Practice & Research",
        "Regional Science & Urban Economics",
    ),
    units_and_formulas_notes=(
        "面积单位用 m² 或 km²；距离用 m 或 km",
        "容积率、建筑密度等指标须注明计算口径",
        "人口密度以人/km² 报告",
        "时间用统一纪年格式；货币用统一币种并注明年份",
        "涉及空间统计时给出效应量与置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("ArcGIS", "ArcGIS Pro", "QGIS", "AutoCAD", "AutoCAD Civil 3D", "SketchUp", "Rhino 3D", "Grasshopper", "Revit", "Vectorworks", "CityGML", "UrbanFootprint", "Caliper", "Global Mapper", "Google Earth Pro", "Lumion", "SPSS", "Stata", "R (RStudio)", "Python (Jupyter)", "Tableau", "Microsoft Power BI", "NVivo", "SurveyMonkey", "Qualtrics", "KoboToolbox", "OpenStreetMap", "PostGIS", "Miro", "Google Sheets"),
    category="管理学",
    databases=("OpenAlex", "CNKI", "万方", "Crossref", "JSTOR", "DOAJ"),
)
