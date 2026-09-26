"""计算机视觉学科论文支持：图像/视频理解体裁、CVPR 引用样式与视觉记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_vision",
    aliases=("computer_vision", "计算机视觉", "CV", "图像理解", "视觉计算"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "method（方法）",
            "experiments（实验）",
            "conclusion（结论）",
            "references",
        ),
        "benchmark_paper": (
            "abstract",
            "introduction",
            "dataset（数据集构建）",
            "metrics（评估指标）",
            "baselines（基线）",
            "results（结果）",
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
    citation_style="CVPR 样式（作者-年份；CVPR/ICCV 遵循其规范）",
    reporting_standards={
        "experimental": "实验遵循 CVPR 论文检查清单",
        "benchmark": "基准测试遵循数据集报告规范",
        "human_eval": "人工评估遵循视觉评估规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "可复现性遵循 CVPR 可复现性清单",
    },
    conventions=(
        "数据集与划分须明确",
        "图像分辨率与预处理须说明",
        "评估指标（mAP、IoU、PSNR 等）定义须一致",
        "模型规模与训练配置须报告",
        "可视化结果须与定量结果对应",
    ),
    key_venues=(
        "CVPR",
        "ICCV",
        "ECCV",
        "IEEE Transactions on Pattern Analysis and Machine Intelligence",
        "International Journal of Computer Vision",
        "IEEE Transactions on Image Processing",
    ),
    units_and_formulas_notes=(
        "损失用 L；学习率用 η；IoU 阈值用 τ",
        "公式用 amsmath；检测/分割方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "分辨率用像素（px）；FLOPs 用 G",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码", "数据集"),
    tools=("OpenCV", "PyTorch", "YOLO", "Python"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "HuggingFace", "Zenodo"),
)