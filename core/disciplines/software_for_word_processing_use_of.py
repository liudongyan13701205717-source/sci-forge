"""文字处理软件使用学科论文支持：文档管理/排版/协作编辑体裁、APA 7 样式与文档记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="software_for_word_processing_use_of",
    aliases=(
        "software_for_word_processing_use_of",
        "文字处理",
        "Word",
        "文档编辑",
        "办公自动化",
        "文档管理",
        "word processing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methods（方法）",
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
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份）",
    reporting_standards={
        "experimental": "实验遵循文档工程实验报告规范",
        "case_study": "案例研究遵循文档案例报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "可复现性遵循文档工程可复现性清单",
    },
    conventions=(
        "文档格式与模板须报告",
        "协作流程与权限须说明",
        "版本控制与修订记录须保留",
        "导出格式与兼容性须注明",
        "字体与样式须遵循标准规范",
    ),
    key_venues=(
        "Journal of Information Systems",
        "Computers & Education",
        "Journal of the Association for Information Science",
        "International Journal of Human-Computer Studies",
        "Information & Management",
    ),
    units_and_formulas_notes=(
        "页数/字数/字符数用 n",
        "时间用 s/min",
        "公式用 amsmath；流程参数须编号",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Word", "Google Docs", "LibreOffice Writer", "WPS Office", "Apple Pages", "OnlyOffice Writer", "Zoho Writer", "Apache OpenOffice Writer", "Microsoft OneNote", "Microsoft Teams", "Microsoft SharePoint", "Google Drive", "Dropbox Paper", "Grammarly", "Microsoft Editor", "Microsoft Publisher", "Microsoft Scribe", "WordWeb", "iA Writer", "Typora"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
