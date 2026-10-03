"""Ngā Mātauranga Taiao O Te Māori (Māori Environmental Knowledges) 学科论文支持。""" 

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ng_mtauranga_taiao_o_te_mori",
    aliases=("Ngā Mātauranga Taiao O Te Māori (Māori Environmental Knowledges)",),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA",
    reporting_standards={},
    conventions=(),
    key_venues=(),
    units_and_formulas_notes=(),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=(),
    category="交叉学科",
    databases=("OpenAlex",),
)
