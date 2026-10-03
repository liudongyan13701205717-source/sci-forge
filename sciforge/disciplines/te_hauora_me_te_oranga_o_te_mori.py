"""Te Hauora Me Te Oranga O Te Māori (Māori Health And Wellbeing) 学科论文支持。""" 

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="te_hauora_me_te_oranga_o_te_mori",
    aliases=("Te Hauora Me Te Oranga O Te Māori (Māori Health And Wellbeing)",),
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
