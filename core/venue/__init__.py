"""venue 包：期刊写作模板 + journal-fit 评分。"""
from __future__ import annotations

from sciforge.venue.templates import (
    VENUE_TEMPLATES,
    get_template,
    list_venues,
)
from sciforge.venue.fit import journal_fit

__all__ = [
    "VENUE_TEMPLATES",
    "get_template",
    "list_venues",
    "journal_fit",
]