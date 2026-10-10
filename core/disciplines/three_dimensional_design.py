"""三维设计学科论文支持：三维造型/数字雕刻/渲染管线体裁、SIGGRAPH 样式与三维设计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="three_dimensional_design",
    aliases=("three_dimensional_design", "三维设计", "3D设计", "数字雕刻", "三维造型",
             "3D modeling", "3D sculpting", "CG 造型", "三维动画"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与三维设计问题）",
            "methods（建模/雕刻/渲染方法）",
            "results（案例作品与评估）",
            "discussion（美学与工程权衡）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景与需求）",
            "process（制作流程与工具链）",
            "results（最终作品与分析）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical overview",
            "main developments",
            "future directions",
            "references",
        ),
    },
    citation_style="SIGGRAPH 样式（作者-年份，ACM 参考格式）",
    reporting_standards={
        "software_artifact": "附源码或工具链清单（含版本号）",
        "visual_quality": "提供高分辨率渲染截图（≥300 DPI）",
        "reproducibility": "声明硬件配置与软件版本，确保可复现",
        "ethics_review": "涉及真实人物形象时声明肖像授权",
    },
    conventions=(
        "模型顶点/面数在附录列出，精度与面数权衡说明",
        "渲染参数（光照、采样数、色调映射）统一报告",
        "坐标系统与单位（米/厘米）全文一致",
        "着色器或材质参数以代码片段给出",
        "术语首次出现给出中英文对照",
    ),
    key_venues=(
        "ACM Transactions on Graphics (TOG)",
        "Computer Graphics Forum (CGF)",
        "SIGGRAPH Conference Proceedings",
        "International Conference on Computational Aesthetics",
        "IEEE Transactions on Visualization and Computer Graphics",
    ),
    units_and_formulas_notes=(
        "几何精度用三角面片数（triangles）或顶点数衡量",
        "渲染时间以秒为单位，注明 GPU 型号与驱动版本",
        "纹理分辨率用像素数表示（如 2048×2048）",
        "公式用 amsmath 排版；渲染方程引用时注明原始文献",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Blender", "Autodesk Maya", "3ds Max", "ZBrush", "Autodesk Mudbox", "Houdini", "Cinema 4D", "Substance Painter", "Substance Designer", "Unreal Engine", "Unity", "Autodesk Fusion 360", "Rhino 3D", "Grasshopper", "Mari", "Marmoset Toolbag", "Octane Render", "Redshift", "Nuke", "Adobe Photoshop"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
