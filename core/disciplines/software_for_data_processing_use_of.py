"""数据处理软件使用学科论文支持：流水线/清洗转换/批量作业体裁、IEEE 引用样式与数据血缘注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="software_for_data_processing_use_of",
    aliases=("software_for_data_processing_use_of", "数据处理软件", "数据处理", "数据清洗", "ETL", "数据管线"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="IEEE 样式（数字编号制，如 [1]）",
    reporting_standards={
        "reproducibility": "流水线须附配置文件、版本号与调度参数以支持复现",
        "lineage": "数据血缘须覆盖来源-转换-落地各节点，中间产物须可追溯",
        "validation": "数据质量校验规则（空值率、唯一性、范围）须声明并通过",
    },
    conventions=(
        "数据质量指标给空值率、重复率与行数前后对比",
        "批处理须报告任务时长、重试次数与失败率",
        "样本量与分区数须报告，避免以抽样代替全量结论",
        "工具版本与运行环境（内存/并行度）须声明",
        "结果给均值 ± 标准差与样本量",
    ),
    key_venues=(
        "ACM SIGMOD Record",
        "Proceedings of the VLDB Endowment",
        "IEEE Transactions on Knowledge and Data Engineering",
        "Journal of Open Source Software",
        "Big Data Research",
    ),
    units_and_formulas_notes=(
        "处理吞吐用 行/秒 或 MB/s；批处理时长用 s/min",
        "并行度（task/executor 数）与内存配置须给出具体数值",
        "百分比给出基数；比率注明分子分母定义",
        "公式用 amsmath；算法伪代码用 algorithm 环境",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Python", "R", "Jupyter Notebook", "Apache Spark", "Hadoop", "IBM DataStage", "Talend", "Informatica PowerCenter", "SSIS", "Alteryx", "KNIME", "RapidMiner", "Tableau Prep Builder", "Power BI Desktop", "Dask", "Prefect", "Dataiku", "Weka", "OpenRefine", "dbt"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)
