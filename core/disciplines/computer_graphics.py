"""计算机图形学学科论文支持：渲染/几何处理体裁、ACM 引用样式与图形记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_graphics",
    aliases=("computer graphics", "计算机图形学", "图形学",
             "渲染", "计算机视觉与图形", "3D 建模", "3D modeling",
             "real-time rendering", "实时渲染", "visualization", "数据可视化"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work",
            "method",
            "implementation",
            "results",
            "references",
        ),
        "rendering": (
            "abstract",
            "introduction",
            "background",
            "method（渲染方法）",
            "implementation",
            "results（含 PSNR/SSIM 对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method",
            "taxonomy",
            "gaps and outlook",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份；SIGGRAPH 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "评估须给出硬件/驱动/GPU 型号",
        "benchmark": "渲染/几何指标须同场景同分辨率对比",
        "reproducibility": "场景、光照设置、随机种子须公开",
        "perceptual": "感知评估须报告评估人数量与协议",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "渲染场景与硬件须报告",
        "误差度量（PSNR、SSIM 等）定义须一致",
        "对比方法须公平（同输入）",
        "性能测量方法须说明",
        "视觉结果须与定量结果对应",
    ),
    key_venues=(
        "SIGGRAPH",
        "SIGGRAPH Asia",
        "ACM Transactions on Graphics",
        "IEEE Transactions on Visualization and Computer Graphics",
        "Computer Graphics Forum",
        "Eurographics",
        "IEEE Pacific Visualization Symposium (PacificVis)",
        "IEEE Visualization Conference (VIS)",
    ),
    units_and_formulas_notes=(
        "分辨率用 px；帧率用 fps；误差用 RMSE",
        "公式用 amsmath；渲染方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "颜色用 RGB/线性空间注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Blender", "Maya", "Houdini", "3ds Max", "ZBrush", "Substance Painter", "Substance Designer", "Open3D", "Python", "OpenCV", "PyTorch3D", "Nanite", "Lumen", "Embree", "OptiX", "Cycles", "Mitsuba 3", "pbrt", "OpenVDB", "OpenMesh", "MeshLab", "Blender Python API", "CUDA", "VisIt", "ParaView"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)
