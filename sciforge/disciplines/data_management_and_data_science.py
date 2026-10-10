"""Data Management And Data Science 学科论文支持：数据管理/数据科学/FAIR 数据体裁、ACM/APA 样式与数据管理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="data_management_and_data_science",
    aliases=(
        "data_management_and_data_science", "数据管理与数据科学",
        "research data management", "研究数据管理", "FAIR data",
        "数据管理", "data governance", "数据治理", "data stewardship",
        "data science management",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与数据管理问题）",
            "methodology（数据管理方案与分析方法）",
            "results（评估数据）",
            "discussion（管理与科学意义）",
            "conclusions（结论与建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（案例背景）",
            "analysis（数据治理与科学问题分析）",
            "conclusions（结论与启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（综述主体）",
            "outlook",
            "references",
        ),
    },
    citation_style="ACM/APA 混合样式（作者-年份；FAIR 数据遵循 DataCite/APA 引用）",
    reporting_standards={
        "data_management": "数据管理遵循 FAIR 与 CARE 原则",
        "reproducibility": "可复现性遵循 20.6 标准与可复现清单",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_study": "案例研究遵循案例研究报告规范",
    },
    conventions=(
        "数据集须使用正式标识符（DOI/URN/PID）并公开访问级别",
        "元数据须遵循领域标准（如 EML/METADATA/DATASEARCH/SKOS）",
        "数据来源、许可（CC/BY/ODbL）与保留期限须明确",
        "所有分析在方法部分给出代码链接与运行环境",
        "涉及人类数据须报告伦理审查与伦理编号",
    ),
    key_venues=(
        "Journal of Data Science",
        "Journal of Data Management and Software Engineering",
        "Journal of the Association for Information Science and Technology",
        "Data as Evidence",
        "Data Science Journal",
        "Journal of Biomedical Informatics",
        "Digital Scholarship in the Humanities",
    ),
    units_and_formulas_notes=(
        "数据量用 GB/TB；条数用 rows 或 records",
        "时间用 分:秒 或 天",
        "公式用 amsmath；显示公式仅在被引用时编号",
        "所有变量首次出现时给出符号与单位",
        "时间用统一纪年格式；货币用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("DataCite", "Zenodo", "Figshare", "Dryad", "Dataverse", "IRIS (Innovative Reference Integration System)", "Pure", "Q4Press", "Galaxy", "KNIME", "Apache NiFi", "Apache Kafka", "Apache Spark", "Airflow", "dbt", "Snowflake", "Databricks", "Alteryx", "Fivetran", "Looker", "Tableau", "Power BI", "Hex", "Observable", "Streamlit", "Dask", "R (tidyverse)", "Python (pandas)", "Git", "Docker", "Kubernetes", "DataLad", "OpenRefine"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "DataCite"),
)
