"""软件本地化学科论文支持：本地化工程/语言资源管理/国际化工具体裁、IEEE 样式与本地化记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="software_localisation",
    aliases=(
        "software_localisation",
        "软件本地化",
        "本地化工程",
        "软件翻译",
        "国际化",
        "i18n",
        "software localization",
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
        "empirical_study": (
            "abstract",
            "introduction",
            "research questions（研究问题）",
            "study design（研究设计）",
            "results（结果）",
            "threats to validity（有效性威胁）",
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
    citation_style="IEEE 样式（作者-编号）",
    reporting_standards={
        "experimental": "实验遵循本地化实验报告规范",
        "empirical": "实证研究遵循软件工程实证报告规范",
        "benchmark": "基准测试遵循翻译质量基准报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "目标语言与区域设置须报告",
        "翻译记忆库与术语库须说明",
        "本地化工作流与工具链须报告",
        "机器翻译与人工翻译比例须说明",
        "质量评估方法须注明",
    ),
    key_venues=(
        "Journal of Computer-Mediated Communication",
        "Language Resources and Evaluation",
        "Empirical Software Engineering",
        "Computational Linguistics",
        "International Journal of Machine Translation",
    ),
    units_and_formulas_notes=(
        "字数/字符数用 n",
        "时间用 s/min",
        "公式用 amsmath；翻译指标须编号",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Transifex", "Lokalise", "Phrase", "Crowdin", "memoQ", "Trados Studio", "SDL WorldServer", "SmartCAT", "GlobalSource", "Acrolinx", "Microsoft Translator", "Google Cloud Translation", "AWS Translate", "Babel", "i18next", "ICU MessageFormat", "Localize", "Translated", "POEditor", "Wordbee"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)
