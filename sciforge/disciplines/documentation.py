"""文献管理学科论文支持：文献组织、知识管理与信息检索体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="documentation",
    aliases=(
        "documentation", "文献管理", "文献管理",
        "archival science", "档案学",
        "knowledge management", "知识管理",
        "information science", "信息科学",
        "information retrieval", "信息检索",
        "records management", "档案管理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（信息问题与背景）",
            "methodology（方法设计、数据采集、分析）",
            "results（检索效果与管理评估）",
            "discussion（管理优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（管理实践分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（技术对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "experiment": "实验条件须完整（查询、语料、评价指标）",
        "analysis": "统计方法须注明",
        "ethics": "涉及用户数据须声明隐私保护",
    },
    conventions=(
        "检索效果用 查准率/查全率/F1 表示",
        "文献计量指标须定义",
        "分类法须注明版本与语言",
        "元数据标准须注明（如 Dublin Core）",
        "统计检验注明方法、p 值与置信区间",
    ),
    key_venues=(
        "Journal of the Association for Information Science and Technology",
        "Information Processing & Management",
        "Journal of Documentation",
        "Information Research",
        "Journal of the American Society for Information Science and Technology",
    ),
    units_and_formulas_notes=(
        "查准率/查全率用 % 表示",
        "F1 用 0-1 范围表示",
        "引用次数用 次 表示",
        "文献计量指标注明计算方法",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R (RStudio)", "Python (pandas, nltk)", "Java", "C++", "SQL", "Lucene", "Solr", "Elasticsearch", "OpenSearch", "EndNote", "Zotero", "Mendeley", "RefWorks", "CiteSeerX", "BibSonomy", "MARC 21", "Dublin Core", "ARKS", "LIDO"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore", "ACM Digital Library", "ProQuest"),
)
