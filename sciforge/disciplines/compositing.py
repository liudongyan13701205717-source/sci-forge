"""数字合成学科论文支持：视频合成/视觉特效/后期合成体裁、APA 引用样式与合成研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="compositing",
    aliases=(
        "compositing", "合成", "compositing", "visual effects compositing",
        "视觉特效合成", "digital compositing", "数字合成", "visual effects",
        "视觉特效", "digital post-production", "数字后期",
        "compositing", "compositing", "visual effects art",
        "compositing", "digital matte painting", "数字概念画",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与合成问题）",
            "methods（合成方法与技术）",
            "results（合成结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "technique": (
            "abstract",
            "introduction",
            "technique description（技术描述）",
            "workflow（工作流程）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction（案例背景）",
            "shot description（镜头描述）",
            "workflow（合成流程）",
            "results（结果）",
            "analysis（分析）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；SIGGRAPH 遵循 ACM 规范）",
    reporting_standards={
        "technique": "合成技术报告须遵循技术报告规范",
        "empirical": "合成质量评估须遵循评估报告规范",
        "case_study": "案例研究须遵循案例研究规范",
    },
    conventions=(
        "合成过程须记录合成节点图与关键参数",
        "涉及实拍素材的研究须注明素材来源与版权信息",
        "合成质量评估须给出主观评分或客观指标（PSNR、SSIM）",
        "多层合成须按图层顺序说明合成逻辑",
        "涉及 3D 渲染的合成须注明渲染引擎与关键参数",
    ),
    key_venues=(
        "ACM SIGGRAPH",
        "ACM Transactions on Graphics",
        "IEEE Transactions on Visualization and Computer Graphics",
        "CGF (Computer Graphics Forum)",
        "Proc. Pacific Graphics",
        "IEEE Transactions on Circuits and Systems for Video Technology",
    ),
    units_and_formulas_notes=(
        "分辨率用像素（px）；帧率用 fps",
        "合成质量指标：PSNR（dB）、SSIM（无量纲）",
        "渲染时间给出硬件配置与渲染引擎版本",
        "涉及色彩空间时注明（sRGB、Rec.709、ACES）",
        "涉及运动跟踪时给出跟踪误差与关键帧数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Nuke", "After Effects", "DaVinci Resolve Fusion", "Photoshop", "Premiere Pro", "Houdini", "Blender", "Flame", "Touch", "Cinema 4D", "Maya", "3ds Max", "Unreal Engine", "Unity", "Matte Painting", "LaTeX", "Trucker", "Nuke Studio", "DaVinci Resolve", "Mocha"),
    category="艺术学",
    databases=("OpenAlex", "CNKI", "万方", "Crossref", "DOI"),
)
