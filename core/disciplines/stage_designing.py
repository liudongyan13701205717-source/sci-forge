"""舞台设计学科论文支持：舞台美术/戏剧照明/场景建构体裁、APA 引用样式与舞台设计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="stage_designing",
    aliases=("stage_designing", "舞台设计", "舞台美术设计", "戏剧舞台设计",
             "stage design", "theatrical design"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7th（艺术学主流；Theatre Journal 等遵循戏剧学期刊规范）",
    reporting_standards={
        "design_documentation": "舞台设计文档须包含平面图、立面图、剖面图与效果图（三视图齐备）",
        "lighting_design": "照明设计报告遵循 ESTA E1.11 与 ANSI E1.21 安全规程",
        "set_construction": "场景建构材料与技术须报告尺寸、荷载与防火等级",
    },
    conventions=(
        "设计图纸须标注比例（1:50 或 1:100）与图例",
        "灯具型号、光束角、色温须明确标注",
        "颜色规格以 Pantone 或 sRGB 报告",
        "三维模型须给出视点、比例与渲染条件",
        "术语首次出现给出中文全称与英文对照（如 fly system = 升降系统）",
    ),
    key_venues=(
        "Theatre Journal",
        "Theatre Design & Technology",
        "Scenic Art (American Scenic Artists Association)",
        "Design and Drama",
        "Journal of Design History",
    ),
    units_and_formulas_notes=(
        "尺寸以 mm 报告（工程图）；图纸比例须标注",
        "光束角、色温以 °、K 报告；照度以 lx 报告",
        "舞台荷载以 kN 或 kg 报告",
        "公式用 amsmath；光照衰减与色温换算须明确",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Vectorworks Architect", "Vectorworks Spotlight", "Capture Lighting", "Capture Lighting Pro", "ETC Design-Lite", "WYSIWYG 灯光模拟", "MA Lighting grandMA", "QLab 音视频控制", "ProPresenter", "Rhino 建模", "SketchUp 建筑建模", "Autodesk AutoCAD", "Autodesk Revit", "3ds Max 三维", "Blender 三维", "Maya 三维动画", "Unreal Engine 实时渲染", "Unity 实时引擎", "Adobe Photoshop", "Adobe Illustrator"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
