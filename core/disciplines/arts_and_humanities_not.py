"""Arts and humanities (not elsewhere classified) 学科论文支持：人文学科与艺术研究综合，偏数字人文、资料组织与跨学科分析。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="arts_and_humanities_not",
    aliases=(
        "arts_and_humanities_not",
        "arts and humanities not elsewhere classified",
        "艺术与人文学科（未分类）",
        "艺术与人文学科综合",
        "digital humanities",
        "数字人文",
        "humanities computing",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "conceptual framework",
            "materials and methods（语料/档案/影像来源与处理流程）",
            "findings（分析、图示与解读）",
            "discussion",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical and methodological overview",
            "state of the art",
            "open questions",
            "references",
        ),
    },
    citation_style="APA 7th 或 MLA 9th（依期刊）；引用一手文献与数字数据集版本时须标注",
    reporting_standards={
        "source": "语料/档案/影像来源须逐条标注（馆藏、目录号、检索日期、许可）",
        "method": "定性编码方案须报告编码者数量、信度（Cohen's κ）与迭代过程",
        "corpus": "语料库规模、语种、切分与预处理方式须完整报告",
        "digital_methods": "数字人文工具与参数（分词、去停用词、相似度阈值）须报告",
        "ethics": "涉及个人或敏感档案须报告伦理审查与知情同意",
    },
    conventions=(
        "直接引文用引号，超过 40 词的块引文缩进；译文与原文对照处标明译者",
        "一手文献与二手研究须区分标注；档案条目按「馆藏+目录号+页码」引用",
        "定性研究须给出编码表（codebook）摘要或附录；数字人文工具报告版本号",
        "图表首次出现处编号并按正文引用顺序排号",
        "术语首次出现给出中英文名称；专有名词保持原文大小写",
        "统计结果报告 n、P 值与效应量；P 值报告格式统一",
    ),
    key_venues=(
        "Digital Humanities Quarterly (DHQ)",
        "Literary and Linguistic Computing",
        "Journal of Cultural Analytics",
        "New Media & Society",
        "Journal of the History of Ideas",
        "Critical Inquiry",
        "Public Culture",
    ),
    units_and_formulas_notes=(
        "语料规模用词数（words）或 token 数；语速/节奏用 beat per minute 或 s/phrase",
        "相似度与距离用 cosine similarity 或 TF-IDF；模型指标用 P/R/F1 或 accuracy",
        "定性强度的频率报告次数/占比并附样本量 n",
        "图表数据以数值表并列，不依赖图形阅读得出数值结论",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Zotero", "EndNote", "Mendeley Reference Manager", "RefWorks", "NVivo", "MAXQDA", "ATLAS.ti", "QDA Miner", "AntConc", "Sketch Engine", "Voyant Tools", "Gephi", "NetworkX", "Tropy", "Omeka S", "Scalar", "ELAN", "PRAAT", "LaTeX", "Jupyter Notebook", "Python (pandas, spaCy)", "IIIF viewers", "Cuneiform Digital Library Initiative"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "JSTOR", "ERIC", "PhilPapers", "OpenEdition"),
)
