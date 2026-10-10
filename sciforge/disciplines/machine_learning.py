"""机器学习学科论文支持：算法、模型架构与实证评估研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="machine_learning",
    aliases=(
        "machine_learning",
        "机器学习",
        "deep learning",
        "深度学习",
        "artificial intelligence",
        "AI",
        "supervised learning",
        "reinforcement learning",
        "model training",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景）",
            "methodology（方法）",
            "results（实验结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（文献综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "k1": "实证实验须报告数据集、种子与算力",
        "k2": "消融实验按组件报告精度与效率",
        "k3": "评估指标按任务选择并给出置信区间",
    },
    conventions=(
        "数据集划分遵循标准基准",
        "超参数须给出网格或搜索范围",
        "训练细节记录优化器、学习率与调度",
        "评估报告指标与基线对比",
        "开源代码附复现说明",
    ),
    key_venues=(
        "NeurIPS",
        "ICML",
        "ICLR",
        "AAAI",
        "JMLR",
    ),
    units_and_formulas_notes=(
        "损失函数以交叉熵或 MSE 报告",
        "精度以 accuracy/F1/ROC-AUC 报告",
        "训练步数以 iterations 或 epochs 计",
        "模型参数量以 M 或 B 计",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("PyTorch", "TensorFlow", "JAX", "Keras", "scikit-learn", "XGBoost", "LightGBM", "Hugging Face Transformers", "Diffusers", "Weights & Biases", "MLflow", "DVC", "Kubeflow", "Slurm", "Colab", "Hugging Face Datasets", "OpenML", "MLOps (Ray)", "vLLM", "LangChain"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
