"""广义/综合学科论文支持：通用体裁、通用引用样式与学术记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="broad_generic",
    aliases=(
        "broad_generic",
        "Broad generic (non-specialised)",
        "广义学科",
        "综合学科",
        "交叉学科",
        "跨学科",
        "通用",
        "broad-based",
        "interdisciplinary",
        "cross-disciplinary",
        "generic",
        "unclassified",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical background",
            "main developments",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 7（通用引用样式）",
    reporting_standards={
        "data": "数据来源、样本、方法须明确",
        "statistics": "统计检验与显著性水平须报告",
        "replication": "可复现性要求（代码、数据、环境）",
    },
    conventions=(
        "章节结构清晰，每节开头给出该节目的",
        "统计结果用均值±SD 或 中位数[IQR] 报告",
        "样本量与显著性水平（p<0.05）须明确",
        "图表编号与正文引用一致",
        "参考文献按字母顺序或引用顺序排列",
    ),
    key_venues=(
        "Nature",
        "Science",
        "Cell",
        "Nature Reviews",
        "Science Advances",
        "PNAS",
        "Nature Communications",
        "Scientific Reports",
    ),
    units_and_formulas_notes=(
        "使用 SI 单位",
        "统计结果用均值±SD 或 中位数[IQR]",
        "显著性水平 p<0.05",
        "样本量 n 须明确",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("LaTeX", "Microsoft Word", "Google Docs", "Overleaf", "Microsoft Excel", "LibreOffice Calc", "Google Sheets", "Python", "R", "MATLAB", "SPSS", "Stata", "Jupyter Notebook", "JupyterLab", "RStudio", "Anaconda", "GitHub", "Mendeley", "Zotero", "EndNote"),
    category="教育学",
    databases=("OpenAlex", "Google Scholar", "PubMed", "arXiv", "CNKI"),
)
