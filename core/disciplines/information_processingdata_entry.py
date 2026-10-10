"""信息处理与数据录入学科论文支持：数据收集、录入、清洗与信息处理流程研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="information_processingdata_entry",
    aliases=(
        "information_processingdata_entry",
        "信息处理与数据录入",
        "数据录入",
        "信息处理",
        "数据处理",
        "information processing and data entry",
        "data entry and processing",
        "数据录入与处理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
            "results（结果）",
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
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（信息管理）或 GB 样式（数据处理报告）",
    reporting_standards={
        "data_quality": "数据质量评估须报告完整率、准确率与一致性",
        "process_design": "流程设计须注明工具版本与参数",
        "automation_study": "自动化研究须报告效率提升与错误率",
        "survey": "调查须报告样本量与响应率",
    },
    conventions=(
        "数据字段须注明数据类型、长度与编码",
        "错误率用百分比报告，须注明口径（录入错误/传输错误/逻辑错误）",
        "处理速度用 条/分钟或 条/小时，须注明",
        "数据清洗须注明规则与处理顺序",
        "统计量须给 M/SD/95% CI",
    ),
    key_venues=(
        "Data & Knowledge Engineering",
        "Journal of Data and Information Management",
        "International Journal of Data Science and Analytics",
        "Chinese Journal of Data and Information Management",
        "数据与计算发展前沿",
    ),
    units_and_formulas_notes=(
        "记录单位用 条/批次，须注明统计窗口",
        "准确率用 %，须注明分子/分母",
        "处理速度用 records/hour，须注明并行数",
        "存储容量用 GB/TB，须注明压缩比",
        "统计量须给 M/SD/95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Python（pandas 数据处理）", "Excel（数据清洗）", "PostgreSQL", "MySQL", "R（数据质量评估）", "OpenRefine（数据清洗）", "Talend（ETL）", "Apache NiFi（数据集成）", "Hadoop/Spark（大规模处理）", "Kafka（流式处理）", "Airflow（任务编排）", "Redcap（电子数据录入）", "EpiData（调查数据录入）", "SurveyMonkey", "Qualtrics", "Tableau（可视化）", "Jupyter Notebook", "MATLAB", "SPSS", "Microsoft Power Query（数据转换）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "SQL（数据库管理）"),
)
