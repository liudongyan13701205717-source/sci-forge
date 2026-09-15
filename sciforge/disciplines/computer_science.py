"""计算机科学学科论文支持：benchmark 规范、复杂度标注与可复现性清单。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_science",
    aliases=("computer science", "计算机", "机器学习", "machine learning", "深度学习",
             "deep learning", "nlp", "自然语言处理", "系统", "systems", "算法", "algorithm",
             "人工智能", "ai"),
    paper_types={
        "conference": (
            "abstract",
            "introduction（问题、挑战与贡献列表）",
            "related work",
            "method（方法/模型/算法）",
            "experiments（数据集、基线、评测协议与消融）",
            "discussion/limitations",
            "conclusion",
            "references",
            "appendix（超参、证明、补充实验）",
        ),
        "systems": (
            "abstract",
            "introduction",
            "background and motivation",
            "design（设计目标与架构）",
            "implementation（实现要点与工程细节）",
            "evaluation（工作负载、端到端与微基准）",
            "related work",
            "conclusion",
            "references",
        ),
        "theory": (
            "abstract",
            "introduction",
            "preliminaries（模型、记号与问题定义）",
            "main results（定理/复杂度界陈述）",
            "proofs",
            "conclusion",
            "references",
        ),
    },
    citation_style="ACM/IEEE 编号或 alpha（按会议模板，如 [1] / [ZLP+22]）",
    reporting_standards={
        "benchmark": "基准评测须公开：数据集与划分、评测协议、提示/超参与代码；SOTA 对比注明引用年份",
        "reproducibility": "可复现性清单（NeurIPS checklist / artifact evaluation / ACM badging）逐项核对",
        "complexity": "复杂度以 O()/Θ()/Ω() 标注，并说明输入规模 n 的度量与常数因子适用范围",
        "ethics": "更广泛影响（broader impact）、伦理声明与许可（数据/模型 license）须给出",
        "compute": "算力预算（GPU 型号/数量/时长）与随机种子须报告",
    },
    conventions=(
        "算法用 algorithm 环境写伪代码，输入/输出与不变式显式给出",
        "图表矢量导出；坐标轴带单位与刻度；对比表加粗最优并标注显著性",
        "脚注或正文给出代码仓库链接（匿名期用匿名仓库）",
        "缩写首次出现给出全称；术语与已有工作保持一致",
        "贡献以编号列表在引言末尾显式陈述",
    ),
    key_venues=(
        "NeurIPS",
        "ICML",
        "ICLR",
        "ACL",
        "SOSP",
        "OSDI",
    ),
    units_and_formulas_notes=(
        "时间/空间复杂度按位/字长/样本量说明度量口径（FLOPs、BOPs、token 数）",
        "精度/召回/F1 等指标给定义与聚合方式（micro/macro）",
        "统计显著性用配对检验（如 paired bootstrap/t-test）并注明次数",
        "延迟/吞吐给硬件环境与百分位（p50/p99）",
        "公式仅对被引用者编号；复杂度推导可在附录展开",
    ),
)
