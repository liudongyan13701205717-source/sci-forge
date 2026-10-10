"""外语学科论文支持：外语教育、语言学与跨文化研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="exogenous_languages",
    aliases=(
        "exogenous_languages", "外语", "外语教育",
        "exogenous languages", "外语",
        "foreign language education", "外语教育",
        "linguistics", "语言学",
        "cross-cultural studies", "跨文化研究",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（语言问题与背景）",
            "methodology（语言分析、教学实验、跨文化比较）",
            "results（语言教学与跨文化评估）",
            "discussion（语言教学优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "language analysis（语言分析）",
            "results（效果评估）",
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
    citation_style="APA 7",
    reporting_standards={
        "analysis": "语言分析须注明理论框架",
        "teaching": "教学方案须完整描述",
        "comparison": "比较研究须注明国家与时间",
    },
    conventions=(
        "语言名称须使用标准名称",
        "语言学术语须使用行业标准",
        "教学方案须完整描述",
        "比较研究须注明国家与时间",
    ),
    key_venues=(
        "Modern Language Journal",
        "TESOL Quarterly",
        "Language Learning",
        "Applied Linguistics",
        "Journal of Multilingual and Multicultural Development",
        "International Journal of Bilingual Education and Bilingualism",
    ),
    units_and_formulas_notes=(
        "语言名称须使用标准名称",
        "语言学术语须使用行业标准",
        "教学方案须完整描述",
        "比较研究须注明国家与时间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Praat", "ELAN", "Transana", "FLEx", "AntConc", "Wmatrix", "Sketch Engine", "SRILM", "Audacity", "Toolbox", "SayMore", "LINGO", "R", "Python", "NLTK", "CMUdict", "panphon", "OT Editor", "Zotero", "LaTeX"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR", "Google Scholar", "PubMed"),
)
