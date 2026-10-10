"""图书情报研究学科论文支持：信息检索、知识组织、数字信息与服务研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="library_and_information_studies",
    aliases=(
        "library_and_information_studies",
        "图书情报研究",
        "信息学",
        "information science",
        "library science",
        "knowledge organization",
        "知识组织",
        "information retrieval",
        "信息检索",
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
        "k1": "信息检索测试须报告召回率、精度与 F1",
        "k2": "用户研究须声明样本量、任务设计与伦理审批",
        "k3": "引文分析须报告时间窗口与来源库",
    },
    conventions=(
        "书目记录遵循 MARC 21 或 RDA",
        "主题标引遵循 LCSH 或汉语主题词表",
        "分类号遵循中图法或杜威十进分类",
        "引文网络图须标节点与边含义",
        "评估指标须报告置信区间",
    ),
    key_venues=(
        "Journal of the Association for Information Science and Technology",
        "Information Processing & Management",
        "Scientometrics",
        "Journal of Documentation",
        "图书情报工作",
    ),
    units_and_formulas_notes=(
        "召回率 Recall = TP / (TP + FN)",
        "精度 Precision = TP / (TP + FP)",
        "F1 = 2 × Precision × Recall / (Precision + Recall)",
        "影响因子 IF 保留两位小数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("万方数据", "VOSviewer", "CiteSpace", "Bibliometrix", "Python pandas", "R", "RStudio", "SPSS", "Stata", "NVivo", "ATLAS.ti", "Excel", "Tableau", "RefWorks", "Zotero", "EndNote", "Mendeley", "Jupyter Notebook", "Lucene", "OpenRefine"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "Web of Science", "Scopus", "Google Scholar", "Dimensions"),
)
