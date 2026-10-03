"""计算机图形学学科论文支持：渲染/几何处理体裁、ACM 引用样式与图形记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_graphics",
    aliases=("computer_graphics", "计算机图形学", "图形学", "渲染"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "method（方法）",
            "implementation（实现）",
            "results（结果）",
            "references",
        ),
        "rendering_paper": (
            "abstract",
            "introduction",
            "background（背景）",
            "method（渲染方法）",
            "implementation（实现）",
            "results（结果与比较）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份；SIGGRAPH 遵循 ACM 规范）",
    reporting_standards={
        "experimental": "实验遵循图形学论文评估规范",
        "benchmark": "基准测试遵循标准场景报告规范",
        "reproducibility": "可复现性遵循图形学可复现性清单",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "perceptual": "感知评估遵循视觉评估规范",
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
    ),
    units_and_formulas_notes=(
        "分辨率用像素（px）；帧率用 fps；误差用 RMSE",
        "公式用 amsmath；渲染方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "颜色用 RGB/线性空间注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码"),
    tools=("Blender", "Maya", "Open3D", "Python"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar"),
)