"""Care (non-medical) of disabled adults 学科论文支持。""" 

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="care_of_disabled_adults",
    aliases=("Care (non-medical) of disabled adults",),
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
