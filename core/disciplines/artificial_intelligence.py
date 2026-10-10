"""人工智能论文支持：机器学习、深度学习、NLP、计算机视觉、强化学习。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="artificial_intelligence",
    aliases=(
        "artificial_intelligence",
        "AI",
        "machine_learning",
        "人工智能",
        "机器学习",
        "深度学习",
        "deep learning",
        "computational intelligence",
        "pattern recognition",
    ),
    paper_types={
        "research": ("abstract", "introduction", "related work", "method", "experiments", "results", "discussion", "conclusions", "references"),
        "survey": ("abstract", "introduction", "taxonomy", "methods", "benchmarks", "open challenges", "conclusions", "references"),
        "system": ("abstract", "introduction", "system overview", "implementation", "evaluation", "deployment", "conclusions", "references"),
    },
    citation_style="IEEE（编号），如 [1]；或 ACL/NeurIPS 风格 (Author et al. Year)",
    reporting_standards={
        "reproducibility": "须报告随机种子、硬件环境（GPU 型号/显存）、训练时间、代码/数据链接",
        "ablation": "消融实验须逐项报告各模块贡献，含置信区间",
        "benchmark": "基准对比须用标准数据集（ImageNet / SQUAD / GLUE 等），报告与 SOTA 差距",
        "hyperparameter": "超参搜索须报告搜索空间、策略（grid / random / Bayesian）与最终取值",
        "bias": "须讨论数据集偏差、模型公平性与伦理影响",
    },
    conventions=(
        "模型名用正式全称首次出现，后可用缩写；数据集用标准名称",
        "损失函数用数学符号（LCEL / NLL / CE）；优化器写全称（Adam / SGD）",
        "图：训练曲线用线图+阴影带（多次运行）；混淆矩阵用热力图",
        "表格须含数据集名、指标、基线、本文方法、提升百分比",
        "可复现性声明放在实验部分开头或附录",
        "所有数据集用官方切分；训练/验证/测试划分比例须报告",
    ),
    key_venues=(
        "NeurIPS (Conference on Neural Information Processing Systems)",
        "ICML (International Conference on Machine Learning)",
        "ICLR (International Conference on Learning Representations)",
        "AAAI (Association for the Advancement of Artificial Intelligence)",
        "ACM SIGGRAPH / SIGGRAPH Asia",
        "CVPR / ICCV / ECCV",
        "ACL / EMNLP / NAACL",
        "IEEE Transactions on Pattern Analysis and Machine Intelligence",
        "Journal of Machine Learning Research",
    ),
    units_and_formulas_notes=(
        "精度/召回率/F1 用小数或百分比（须统一）",
        "参数量用 M / B（百万/十亿）；FLOPs 用 GFLOPs / TFLOPs",
        "推理延迟用 ms；吞吐量用 samples/sec 或 tokens/sec",
        "GPU 时用 GPU-hours；显存用 GB",
        r"损失函数用 L(\theta) 记法；梯度记 \nabla_\theta L",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("PyTorch", "TensorFlow", "Keras", "scikit-learn", "JAX / Flax", "Hugging Face Transformers", "Hugging Face Datasets", "LangChain", "OpenCV", "Detectron2", "PyTorch Lightning", "XGBoost", "LightGBM", "Optuna", "MLflow", "Weights & Biases", "Ray", "Dask", "Airflow", "ONNX Runtime", "Triton Inference Server", "vLLM", "CUDA", "cuDNN", "NumPy", "SciPy", "Jupyter", "DVC", "Docker"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar", "Hugging Face Datasets"),
)
