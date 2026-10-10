"""动画学科论文支持：三维动画、二维动画、计算机图形学、动画叙事与制作。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="animation",
    aliases=(
        "animation",
        "Animation",
        "动画",
        "动画学",
        "computer animation",
        "三维动画",
        "二维动画",
        "CG",
        "computer graphics",
        "动画制作",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "related work",
            "method（模型、渲染管线、算法、创作流程）",
            "experiments or production（技术验证或作品产出）",
            "discussion",
            "conclusions",
            "references",
        ),
        "artwork": (
            "artist statement",
            "concept and reference",
            "production process（故事板、资产、镜头、渲染）",
            "final artwork",
            "reflective commentary",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical overview",
            "current trends",
            "future directions",
            "references",
        ),
    },
    citation_style="ACM SIGGRAPH 样式（图形学主流）或 Chicago Author-Date（艺术创作类）",
    reporting_standards={
        "method": "渲染算法/模型须说明输入、参数、复杂度与对照实验",
        "artwork": "作品须附制作流程文档（timeline/storyboard）与创作说明",
        "hardware": "渲染硬件（GPU/CPU）与渲染时间须报告以便复现",
        "software": "使用软件版本（Blender/Maya/Houdini/Unreal Engine）须注明",
        "ethics": "AI 生成素材（Midjourney/Stable Diffusion）须明确披露使用范围",
    },
    conventions=(
        "镜头编号用 SHOT-xx；资产命名用 assetType_subject_LOD.suffix",
        "关键帧与动捕数据单位统一（秒/帧）；帧率（fps）在片头声明",
        "色彩空间（sRGB/ACES/Linear）在渲染设置与输出格式中一致",
        "代码示例用 Python（Houdini/Blender Python API）或 HDA/VEX",
        "作品类论文附创作过程截图、时间轴与渲染统计",
    ),
    key_venues=(
        "ACM Transactions on Graphics (TOG)",
        "SIGGRAPH / SIGGRAPH Asia Technical Papers",
        "IEEE Transactions on Visualization and Computer Graphics (TVCG)",
        "Computer Graphics Forum (CGF)",
        "Pacific Graphics",
        "Animation Journal",
    ),
    units_and_formulas_notes=(
        "长度用 cm 或虚拟单位（Blender 1 单位 = 1 米默认）",
        "帧率 fps；时间 s 或 ms；帧数 frames",
        "颜色：sRGB、ACEScg/ACEScct、Linear；色深 8/16/32bit",
        "渲染：光线数 rays/samples、降噪 iterations",
        "存储：GB；纹理分辨率（2K/4K/8K）；面数（tris/polygons）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Blender", "Autodesk Maya", "SideFX Houdini", "Maxon Cinema 4D", "Toon Boom Harmony", "Adobe Animate", "Adobe After Effects", "Nuke (The Foundry)", "Substance Painter/Designer", "Pixar Marvelous Designer", "Autodesk Mudbox", "Pixar RenderMan", "Unreal Engine 5", "Unity", "TouchDesigner", "Grasshopper (Rhinoceros)", "Adobe Photoshop", "Adobe Premiere Pro", "DaVinci Resolve", "Procreate", "Clip Studio Paint", "Autodesk 3ds Max", "Marmoset Toolbag", "ZBrush"),
    category="艺术学",
    databases=("ACM Digital Library", "OpenAlex", "Crossref", "DBLP", "arXiv"),
)
