"""国际关系学科论文支持：权力、外交、安全与地区研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="international_relations",
    aliases=("international relations", "国际关系", "政治学", "外交学", "国家安全", "战略研究", "国际政治", "地缘政治"),
    paper_types={
        "research": ("abstract", "introduction（问题提出与理论定位）", "methodology（案例或量化设计与因果识别）", "results（发现与讨论）", "discussion（机制与政策含义）", "references"),
        "case_study": ("abstract", "introduction", "case description（国家、危机或政策背景）", "analysis（决策过程与制度逻辑）", "results（过程追踪或量化发现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（现实主义、自由主义、建构主义）", "evidence synthesis（案例与数据综合）", "future directions", "references"),
    },
    citation_style="ASA 样式或 Chicago 17（脚注）",
    reporting_standards={
        "k1": "案例选择理由须说明（most 或 least likely design）",
        "k2": "过程追踪给事件序列与证据权重",
        "k3": "量化研究给样本框、年份、模型与标准误类型",
    },
    conventions=(
        "理论与机制区分，机制用中介或调节变量明确标注",
        "历史事实与当代评价区分",
        "概念（权力、安全、主权）在引言定义",
        "案例与文献综述按主题而非时间",
        "政策建议与学术主张分开"
    ),
    key_venues=(
        "International Organization",
        "Journal of Conflict Resolution",
        "American Political Science Review",
        "World Politics",
        "International Security"
    ),
    units_and_formulas_notes=(
        "冲突强度按 COW 分类（0-4 级）",
        "政权类型用 Polity 或 V-dem 数值化",
        "经济指标注明 GDP、人均与年度口径",
        "案例年份与数据年份对齐"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Polity V", "Correlates of War", "ACLED", "World Polity Project", "Global Terrorism Database", "Uppsala Conflict Data Program", "International Country Risk Guide", "IMF WEO", "SIPRI Yearbook", "Pew Research Center", "World Values Survey", "Varieties of Democracy", "Freedom House", "World Bank Governance Indicators", "International Crisis Group", "R", "STATA", "Python", "Tableau", "NVivo（质性文本分析）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Google Scholar"),
)
