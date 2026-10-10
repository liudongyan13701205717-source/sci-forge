"""其他信息与计算科学学科论文支持：未被细类归入的信息管理、数据科学与计算建模研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_information_and_computing_sciences",
    aliases=(
        "other_information_and_computing_sciences", "其他信息与计算科学",
        "other information and computing sciences", "其他信息与计算科学",
        "information sciences", "信息科学",
        "data science", "数据科学",
        "computational science", "计算科学",
        "bibliometrics and scientometrics", "文献计量与科学计量",
        "information systems", "信息系统",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与相关研究）",
            "methodology（数据、方法与评估方案）",
            "results（模型表现与消融分析）",
            "discussion（可复现性与局限）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（系统与场景）",
            "analysis（设计与实现分析）",
            "results（实测与对比）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（方法与模型综述）",
            "evidence synthesis（实证证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "k1": "算法与数据集须发布可复现代码与固定随机种子",
        "k2": "模型评估须报告标准划分、指标定义与置信区间",
        "k3": "数据集论文须遵循数据描述模板并说明许可与偏见审计",
    },
    conventions=(
        "数据集须报告规模、划分、缺失处理与采集时间窗口",
        "指标须给出定义式并区分 precision/recall/F1 与 AUC/ROC",
        "复杂度须给出时间/空间复杂度与实测开销",
        "统计检验注明方法、p 值与效应量",
        "符号首次出现须定义全称与量纲",
    ),
    key_venues=(
        "Journal of the Association for Information Science and Technology",
        "Information Processing & Management",
        "Journal of Informetrics",
        "Data & Knowledge Engineering",
        "IEEE Transactions on Knowledge and Data Engineering",
        "《情报学报》",
    ),
    units_and_formulas_notes=(
        "准确率类指标用 % 或小数表示并注明阈值",
        "计算开销注明硬件平台与运行时长",
        "数据规模用样本数与字段数报告",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Python", "R (RStudio)", "MATLAB", "Julia", "Octave", "Stata", "SPSS", "SAS", "Apache Spark", "Hadoop", "TensorFlow", "PyTorch", "scikit-learn", "KNIME", "RapidMiner", "Weka", "Orange", "Apache Flink", "EndNote", "LaTeX"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
