"""信息学学科论文支持：信息系统、信息管理与信息技术的理论与应用研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="informatics",
    aliases=(
        "informatics",
        "信息学",
        "信息科学",
        "信息系统",
        "计算机信息学",
        "informatic sciences",
        "information technology studies",
        "computational informatics",
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
    citation_style="IEEE 样式（工程类）或 APA 7 样式（信息系统研究）",
    reporting_standards={
        "system_evaluation": "系统评估须报告功能完整性、性能指标与用户满意度",
        "survey_study": "调查研究须报告样本量、信度系数与偏差控制",
        "design_science": "设计科学须遵循 Hevner 等（2004）构建物报告框架",
        "clinical_informatics": "临床信息学须遵循 STARD 或 CONSORT-ICT 报告",
    },
    conventions=(
        "信息检索指标须注明 P/R/F1、nDCG、MAP 及其计算口径",
        "系统架构须用标准图（UML/BPMN）描述",
        "数据集须说明规模、划分与预处理方法",
        "基线对比须注明版本与参数",
        "可复现性配置须附代码与参数清单",
    ),
    key_venues=(
        "Journal of Management Information Systems",
        "MIS Quarterly",
        "Information Systems Research",
        "Journal of the Association for Information Science and Technology",
        "信息学报",
    ),
    units_and_formulas_notes=(
        "性能指标（响应时间、吞吐量）须注明测试环境与基准",
        "统计量给出 M/SD/95% CI",
        "显著性检验须说明方法（t 检验/卡方/非参数检验）",
        "数据分割须注明 train/val/test 比例",
        "指标对比须用配对检验避免选择偏差",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Elasticsearch（信息检索系统）", "Python（scikit-learn）", "R（文本挖掘）", "SPSS", "NVivo（质性分析）", "Hadoop/Spark（大数据处理）", "MATLAB", "Apache Kafka（流数据处理）", "Jupyter Notebook（可复现性）", "Docker（容器化部署）", "Kubernetes（编排）", "PostgreSQL", "Redis（缓存）", "Grafana（监控）", "ELK 栈", "Tableau（可视化）", "Python（pandas/numpy）", "UML 建模工具（Enterprise Architect）", "Git（版本控制）", "Postman（API 测试）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "SQL（关系数据库）", "Neo4j（图数据库）"),
)
