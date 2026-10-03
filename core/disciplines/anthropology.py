"""人类学论文支持：民族志方法、田野调查、物质文化分析。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="anthropology",
    aliases=("anthropology", "ethnography", "人类学", "民族志", "田野"),
    paper_types={
        "ethnography": ("abstract", "introduction", "field site and methods", "ethnographic present",
                        "analysis", "reflexivity", "conclusion", "references"),
        "research": ("abstract", "introduction", "theory", "methods", "findings", "discussion", "references"),
        "review": ("abstract", "introduction", "genealogy of concepts", "debates", "directions", "references"),
    },
    citation_style="Chicago Author-Date 或 AAA style",
    reporting_standards={
        "fieldwork": "田野时长、地点、语言能力与关系建立过程须披露",
        "ethics": "知情同意与匿名化处理（IRB/伦理审查）须说明",
        "positionality": "研究者立场（reflexivity）须声明",
        "data": "引文须给访谈编号或田野笔记日期；人物化名统一",
        "translation": "翻译策略（直译/意译）与本地语言术语保留说明",
    },
    conventions=(
        "民族志现在时叙述与引语穿插； thick description 示范",
        "本地术语用斜体并附注释；系谱图/地图给来源",
        "理论对话明确（如实体论/本体论转向）",
        "避免东方主义式概括；内部差异呈现",
    ),
    key_venues=(
        "American Anthropologist",
        "Current Anthropology",
        "American Ethnologist",
        "Journal of the Royal Anthropological Institute",
        "Cultural Anthropology",
    ),
    units_and_formulas_notes=(
        "无统计要求时以质性论证为主",
        "如含量化内容给样本与描述统计；网络分析给指标定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=("NVivo", "QDA Miner", "MAXQDA", "Python", "R"),
    category="法学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
