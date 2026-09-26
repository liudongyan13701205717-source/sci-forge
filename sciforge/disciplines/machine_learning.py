"""机器学习学科论文支持：监督/无监督/强化学习体裁、NeurIPS 引用样式与机器学习记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="machine_learning",
    aliases=("machine_learning", "机器学习", "ML", "统计学习", "模式识别"),
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
        "benchmark_study": (
            "abstract",
            "introduction",
            "setup（基准与设置）",
            "baselines（基线）",
            "results（结果）",
            "analysis（分析）",
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
    citation_style="NeurIPS 样式（作者-年份；NeurIPS/ICML 遵循其规范）",
    reporting_standards={
        "experimental": "实验遵循 NeurIPS 论文检查清单",
        "benchmark": "基准测试遵循 MLPerf 报告规范",
        "reproducibility": "可复现性遵循 NeurIPS 可复现性清单",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "human_subjects": "人类受试者研究遵循 IRB 规范",
    },
    conventions=(
        "数据集划分（train/val/test）须明确",
        "随机种子与初始化须报告",
        "超参数与调参过程须说明",
        "评估指标定义须一致（准确率、F1、AUC 等）",
        "与基线对比须统计检验",
    ),
    key_venues=(
        "NeurIPS",
        "ICML",
        "ICLR",
        "Journal of Machine Learning Research",
        "Machine Learning",
        "IEEE Transactions on Pattern Analysis and Machine Intelligence",
    ),
    units_and_formulas_notes=(
        "损失函数用 L；学习率用 η；正则化用 λ",
        "公式用 amsmath；模型方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "复杂度用 O(·) 记法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码", "数据集"),
    tools=("Python", "PyTorch", "scikit-learn", "Jupyter"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "HuggingFace", "Zenodo"),
)