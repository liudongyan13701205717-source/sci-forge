"""图书情报与档案研究学科论文支持：档案理论、信息管理研究方法与数字化研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="library_information_and_archival_studies",
    aliases=(
        "library_information_and_archival_studies",
        "图书情报与档案研究",
        "档案研究",
        "archival research",
        "information and records studies",
        "档案管理研究",
        "records management research",
        "library information science",
        "档案学理论",
    ),
    paper_types={
        "research": (
            "abstract（摘要）",
            "introduction（引言）",
            "literature review（文献综述）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references（参考文献）",
        ),
        "case_study": (
            "abstract（摘要）",
            "introduction（引言）",
            "case description（案例背景）",
            "analysis（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references（参考文献）",
        ),
        "review": (
            "abstract（摘要）",
            "introduction（引言）",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（展望）",
            "references（参考文献）",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "引文分析须报告数据库、时间窗口与筛选条件",
        "k2": "档案研究须声明保管单位与开放范围",
        "k3": "用户研究须报告样本量、抽样方法与响应率",
    },
    conventions=(
        "档案保管期限以年为单位",
        "元数据遵循 EAD、PREMIS、Dublin Core",
        "引文网络图须标节点含义与阈值",
        "文件字号采用 (年) X 字第 X 号",
        "评估指标须报告置信区间",
    ),
    key_venues=(
        "Archival Science",
        "Journal of Documentation",
        "Archives and Manuscripts",
        "档案学通讯",
        "中国档案",
    ),
    units_and_formulas_notes=(
        "影响因子 IF 保留两位小数",
        "召回率 Recall = TP / (TP + FN)",
        "档案数字化率 = 已数字化件数 / 总件数 × 100%",
        "评估置信水平以 % 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("万方数据", "VOSviewer", "CiteSpace", "Bibliometrix", "Python pandas", "R", "RStudio", "SPSS", "Stata", "NVivo", "ATLAS.ti", "Excel", "Tableau", "RefWorks", "Zotero", "EndNote", "Mendeley", "Jupyter Notebook", "Lucene", "OpenRefine"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Web of Science", "Scopus", "Google Scholar", "Dimensions"),
)
