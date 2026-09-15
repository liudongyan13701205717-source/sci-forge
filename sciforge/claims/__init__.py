"""claims 包：claim→source 核验 + 完整性门 + Material Passport。"""
from __future__ import annotations

from sciforge.claims.verify import (
    verify,
    parse_claims,
    parse_citations,
    parse_constraints,
    classify_findings,
)
from sciforge.claims.gates import (
    gate_2_5,
    gate_4_5,
    run_gates,
    request_bypass,
    build_passport,
    BLOCK_PATTERNS,
)

__all__ = [
    "verify",
    "parse_claims",
    "parse_citations",
    "parse_constraints",
    "classify_findings",
    "gate_2_5",
    "gate_4_5",
    "run_gates",
    "request_bypass",
    "build_passport",
    "BLOCK_PATTERNS",
]