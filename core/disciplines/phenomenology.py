"""现象学学科论文支持：意识/意向性/生活世界体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="phenomenology",
    aliases=("phenomenology", "现象学", "现象学哲学", "意识哲学",
             "intentionality", "胡塞尔", "胡塞尔现象学", "梅洛-庞蒂",
             "生活世界", "lifeworld"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "argument（论证）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（发现）",
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
    citation_style="Chicago 样式（作者-年份或注-书目；Husserl Studies 遵循 Chicago 规范）",
    reporting_standards={
        "theoretical": "理论论证遵循哲学论证报告规范",
        "textual": "文本分析遵循文本分析报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "phenomenological": "现象学描述遵循 Husserl/Merleau-Ponty 传统",
    },
    conventions=(
        "核心概念须定义",
        "论证结构须清晰",
        "文本版本须注明",
        "引文给出页码",
        "术语用原文并注译",
        "区分本质描述与经验报告",
    ),
    key_venues=(
        "Husserl Studies",
        "Continental Philosophy Review",
        "Phenomenology and the Cognitive Sciences",
        "Journal of the British Society for Phenomenology",
        "Research in Phenomenology",
        "Philosophy Today",
    ),
    units_and_formulas_notes=(
        "引文给出页码",
        "版本与版次须注明",
        "译文给出原文页码",
        "时间用统一纪年格式",
        "术语用原文并注译",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("LaTeX 哲学排版", "Overleaf 在线 LaTeX", "Zotero 文献管理", "EndNote", "Mendeley", "NVivo 质性编码", "MAXQDA 质性分析", "ATLAS.ti 质性分析", "QCA 定性比较分析", "Word（Microsoft Office）", "Stanford Encyclopedia of Philosophy (SEP)", "PhilArchive 预印本平台", "现象学转录与编码工具", "Otter.ai 转录工具", "Rev.com 转录服务", "LogicGator 逻辑证明", "LogiQA 逻辑工具", "CSL 引用样式管理", "Tweagoo 逻辑工具", "Lean 4（形式化证明）"),
    category="哲学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref", "PhilPapers", "JSTOR", "JSTOR 数据库", "PhilPapers 哲学数据库"),
)
