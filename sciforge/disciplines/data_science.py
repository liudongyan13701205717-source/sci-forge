"""数据科学论文支持：数据挖掘、统计学习、数据可视化、大数据系统、因果推断。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="data_science",
    aliases=("data_science", "data_analytics", "数据科学", "数据分析"),
    paper_types={
        "research": ("abstract", "introduction", "related work", "method", "experiments", "results", "discussion", "conclusions", "references"),
        "application": ("abstract", "introduction", "domain background", "data description", "methodology", "deployment", "results", "lessons learned", "conclusions", "references"),
        "benchmark": ("abstract", "introduction", "dataset", "baselines", "evaluation protocol", "results", "analysis", "conclusions", "references"),
    },
    citation_style="APA 7（括号），如 (Author, Year)；或 KDD/ICDE 风格",
    reporting_standards={
        "data_quality": "须报告数据来源、缺失值处理、异常值检测方法与数据清洗步骤",
        "reproducibility": "须提供代码仓库链接、随机种子、依赖版本与运行环境",
        "fairness": "公平性分析须报告人口统计分组指标（如 demographic parity）",
        "scalability": "可扩展性须报告数据规模（行×列）、运行时间与资源消耗",
        "causal": "因果推断须声明识别假设、混杂变量处理与敏感性分析",
    },
    conventions=(
        "数据集用正式名称（UCI/Kaggle/公开数据源）+ 版本与下载日期",
        "模型用标准缩写（RF/XGB/LGBM/DNN）+ 关键超参",
        "图：散点图/热力图/箱线图须含数据点数 N",
        "表格用标准三线表；数值报告均值±标准差",
        "代码可复现性声明放在方法部分",
    ),
    key_venues=(
        "KDD (ACM SIGKDD Conference on Knowledge Discovery and Data Mining)",
        "VLDB (International Conference on Very Large Data Bases)",
        "NeurIPS",
        "Journal of Machine Learning Research",
        "Data Mining and Knowledge Discovery",
    ),
    units_and_formulas_notes=(
        "数据规模用 rows × columns；内存用 GB/TB",
        "训练时间用 GPU-hours 或 CPU-hours",
        "AUC/ROC 无量纲；准确率用 % 或小数",
        "F1-score/Precision/Recall 用小数（三位有效数字）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码", "数据集"),
    tools=("Python (NumPy/pandas)", "R", "SQL", "Git"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)
