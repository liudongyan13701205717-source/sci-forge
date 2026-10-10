"""文化研究学科论文支持：媒介/身份/消费体裁、MLA 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cultural_studies",
    aliases=(
        "cultural_studies",
        "文化研究",
        "文化批评",
        "大众文化研究",
        "媒介文化研究",
        "cultural studies",
        "media studies",
        "popular culture studies",
        "cultural criticism",
        "critical cultural studies",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "analysis（分析）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "discourse_analysis": (
            "abstract",
            "introduction",
            "corpus（语料）",
            "analytical framework（分析框架）",
            "findings（发现）",
            "discussion（讨论）",
            "references",
        ),
        "ethnographic_study": (
            "abstract",
            "introduction",
            "fieldwork（田野）",
            "data（数据）",
            "analysis（分析）",
            "findings（发现）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="MLA 样式（作者-页码；Cultural Studies 遵循 MLA 规范）",
    reporting_standards={
        "discourse": "话语分析遵循话语分析报告规范",
        "ethnography": "民族志研究遵循民族志报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "理论框架与立场须明确，注明所依理论家（如 Hall/Burke/Giroux）与所属传统",
        "语料与样本须说明来源、采集时间、规模与选择规则",
        "质性编码须报告编码框架、编码者与信度（编码者间一致性）",
        "媒介分析须同时给出文本内部特征与生产/流通/接收的外部语境",
        "伦理与知情同意须报告；涉及弱势群体与未成年人需额外说明保护措施",
        "引文给出页码；反思性（positionality/reflexivity）须在方法部分讨论",
    ),
    key_venues=(
        "Cultural Studies",
        "International Journal of Cultural Studies",
        "European Journal of Cultural Studies",
        "New Formations",
        "Theory, Culture & Society",
        "Journal of Cultural Analysis and Social Change",
        "文化研究",
    ),
    units_and_formulas_notes=(
        "引文给出页码",
        "频数与百分比给出基数",
        "样本量须报告",
        "时间用统一格式",
        "译文给出原文页码",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo", "MAXQDA", "ATLAS.ti", "WebQDA", "Dedoose", "CoderTaal", "AntConc", "LancsBox (Lancaster University Corpus Tools)", "Sketch Engine", "LArc", "FREQ (Lancaster University)", "Voyant Tools", "Gephi", "NetworkX", "spaCy", "NLTK", "Stanza", "LDAvis", "RStudio", "LaTeX", "Overleaf", "Open Refine"),
    category="文学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "Web of Science"),
)
