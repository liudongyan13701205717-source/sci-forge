"""深度学习学科论文支持：神经网络/表示学习体裁、NeurIPS 引用样式与深度学习记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="deep_learning",
    aliases=("deep_learning", "深度学习", "神经网络", "深度神经网络", "DNN"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "method（网络架构与方法）",
            "experiments（实验）",
            "conclusion（结论）",
            "references",
        ),
        "architecture_proposal": (
            "abstract",
            "introduction",
            "architecture（架构设计）",
            "training（训练细节）",
            "evaluation（评估）",
            "ablation（消融研究）",
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
    citation_style="NeurIPS 样式（作者-年份；NeurIPS/ICLR 遵循其规范）",
    reporting_standards={
        "experimental": "实验遵循 NeurIPS 论文检查清单",
        "reproducibility": "可复现性遵循 NeurIPS 可复现性清单",
        "benchmark": "基准测试遵循 MLPerf 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "model_card": "模型发布遵循 Model Card 规范",
    },
    conventions=(
        "网络结构（层数、宽度、激活）须完整描述",
        "训练配置（优化器、批次、epoch）须报告",
        "数据增强与预处理须说明",
        "参数量与计算量（FLOPs）须报告",
        "消融实验须覆盖关键设计选择",
    ),
    key_venues=(
        "NeurIPS",
        "ICLR",
        "ICML",
        "IEEE Transactions on Pattern Analysis and Machine Intelligence",
        "International Journal of Computer Vision",
        "Journal of Machine Learning Research",
    ),
    units_and_formulas_notes=(
        "损失用 L；学习率用 η；批次用 B；epoch 用 E",
        "公式用 amsmath；网络层方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "参数量用 M（百万）；FLOPs 用 G",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码", "数据集"),
    tools=("PyTorch", "TensorFlow", "JAX", "Python"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "HuggingFace", "Zenodo"),
)