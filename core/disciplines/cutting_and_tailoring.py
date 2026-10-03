"""Cutting and tailoring 学科论文支持。""" 

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cutting_and_tailoring",
    aliases=("Cutting and tailoring",),
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
