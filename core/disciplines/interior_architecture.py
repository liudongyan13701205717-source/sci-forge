"""室内建筑学学科论文支持：空间设计、结构与可持续研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="interior_architecture",
    aliases=(
        "interior_architecture",
        "室内建筑学",
        "Interior Architecture",
        "Interior Architecture Design",
        "Interieur Architecture",
        "Architektur im Innern",
        "空间设计",
        "室内空间规划",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、场地与问题）",
            "methodology（研究方法）",
            "results（结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（案例分析）",
            "results（发现）",
            "discussion（启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="APA 7（艺术/建筑类可用 Chicago 作者-年份）",
    reporting_standards={
        "k1": "ASHRAE（暖通与建筑性能）",
        "k2": "LEED 报告规范（可持续认证）",
        "k3": "WELL Building Standard",
    },
    conventions=(
        "平面图、剖面与轴测图须符合制图标准",
        "材料表须完整列出规格与供应商",
        "人体尺度与无障碍规范须符合 GB 55019",
        "光环境与声环境须给出量化指标",
        "结构荷载须通过计算校核",
    ),
    key_venues=(
        "Architectural Design",
        "Domus",
        "AZ Architectuur en Wonen",
        "Interior Design International",
        "Journal of Interior Design",
    ),
    units_and_formulas_notes=(
        "长度单位用 mm 或 m，面积用 ㎡",
        "照度用 lux（lx），色温用 K",
        "噪声用 dB(A) 与声压级区分",
        "材料导热系数与吸声系数须注明测试方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SketchUp", "Rhino", "Revit", "ArchiCAD", "Vectorworks", "V-Ray", "Enscape", "Lumion", "D5 Render", "3ds Max", "Corona", "Sketchfab", "SolidWorks", "Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "Chief Architect", "Chief Architect 3D", "Planner 5D"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
