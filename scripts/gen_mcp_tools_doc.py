"""从 `sciforge/server.py` 重新生成 `docs/mcp-tools.md`。

先写死一个错误计数会漂移，所以文档必须由 live server 生成：
  - 静态扫描 `@mcp.tool()` 定义，读函数签名与 docstring；
  - 运行时用 `mcp.list_tools()` 复核，两侧不一致即报错退出。
用法：
    python scripts/gen_mcp_tools_doc.py            # 打印差异，不写盘
    python scripts/gen_mcp_tools_doc.py --write    # 写回 docs/mcp-tools.md
"""

from __future__ import annotations

import ast
import asyncio
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("SCI_FORGE_OFFLINE", "1")

SERVER = ROOT / "sciforge" / "server.py"
DOC = ROOT / "docs" / "mcp-tools.md"

GROUPS = [
    ("复现闭环", ("reproduce_",)),
    ("论文写作", ("write_section", "export_document", "auto_title_abstract",
                 "paper_polish", "revision_coach", "rebuttal_audit",
                 "detect_style", "calibrate_style", "score_style_text",
                 "claim_strength", "paper_metadata", "package_submission")),
    ("研究线与选题", ("ideate_paper", "research_plan", "literature_review",
                    "research_verdict", "inject_results", "check_novelty",
                    "citation_landscape", "project_memory", "scout_",
                    "recommend_papers", "find_code_for_paper",
                    "link_papers_to_code", "rag_answer", "rag_sources")),
    ("评审与质量门", ("peer_review", "review_code", "run_panel",
                    "validate_review_intake", "review_panel_intake",
                    "validate_claims_evidence", "claims_evidence_matrix",
                    "verify", "gate_2_5", "gate_4_5", "run_gates",
                    "request_bypass", "build_passport", "blinded_screening",
                    "screening_audit", "screening_triage")),
    ("引用与文献", ("ref_to_bibtex", "batch_ref_export", "convert_citation",
                   "verify_citation", "verify_claim", "verify_reference_list",
                   "citation_graph", "download_paper_pdf", "journal_fit",
                   "select_reporting_guidelines", "select_guidelines")),
    ("科研数据连接器", ("science_",)),
    ("学科 registry", ("list_disciplines", "get_discipline")),
    ("系统综述", ("prisma_review",)),
    ("证据权重与源约束", ("evidence_grade", "grounded_compose")),
    ("监测与分流", ("retraction_watch", "citation_context", "evidence_alert",
                   "discovery_curve", "credibility_score")),
]


def static_tools() -> list[dict]:
    tree = ast.parse(SERVER.read_text(encoding="utf-8"))
    out: list[dict] = []
    for node in tree.body:
        if not isinstance(node, ast.FunctionDef) or not node.decorator_list:
            continue
        if not any(isinstance(d, ast.Call) and getattr(d.func, "attr", None) == "tool"
                   for d in node.decorator_list):
            continue
        doc = ast.get_docstring(node) or ""
        summary = doc.strip().splitlines()[0].strip() if doc.strip() else ""
        args = []
        for a in node.args.args:
            if a.arg in ("self", "cls"):
                continue
            ann = ast.unparse(a.annotation) if a.annotation else "Any"
            default = None
            if len(node.args.defaults) >= len(node.args.args) - len(node.args.defaults):
                pass
            args.append((a.arg, ann))
        ndef = len(node.args.defaults)
        for i, (name, ann) in enumerate(args):
            args[i] = (name, ann, i >= len(args) - ndef)
        out.append({
            "name": node.name,
            "summary": summary,
            "args": args,
            "returns": ast.unparse(node.returns) if node.returns else "dict",
            "doc": doc,
        })
    return out


def runtime_names() -> list[str]:
    from sciforge.server import mcp

    async def _run():
        return [t.name for t in await mcp.list_tools()]

    return sorted(asyncio.run(_run()))


def sig(t: dict) -> str:
    parts = []
    for name, ann, has_default in t["args"]:
        s = f"{name}: {ann}"
        if has_default:
            s += " = ..."
        parts.append(s or name)
    return ", ".join(parts)


def render(tools: list[dict]) -> str:
    names = [t["name"] for t in tools]
    total = len(tools)
    lines: list[str] = []
    lines.append(f"# MCP 工具清单（{total} 个）")
    lines.append("")
    lines.append("> 本文档由 `scripts/gen_mcp_tools_doc.py` 从 `sciforge/server.py` 生成。")
    lines.append(f"> 静态扫描 `@mcp.tool()` 计 {total} 个，运行时 `mcp.list_tools()` "
                 f"计 {total} 个，两侧一致；不一致时脚本报错退出。")
    lines.append("> 重新生成：`python scripts/gen_mcp_tools_doc.py --write`")
    lines.append("")
    lines.append("## 工具总表")
    lines.append("")
    lines.append("| # | 工具名 | 功能简述 | 参数 | 返回值 |")
    lines.append("| --- | --- | --- | --- | --- |")
    for i, t in enumerate(tools, 1):
        params = ", ".join(n for n, _a, _d in t["args"]) or "（无）"
        lines.append(f"| {i} | `{t['name']}` | {t['summary']} | {params} | dict |")
    lines.append("")

    assigned = set()
    for title, prefixes in GROUPS:
        members = [t for t in tools
                   if any(t["name"].startswith(p) or t["name"] == p for p in prefixes)
                   and t["name"] not in assigned]
        if not members:
            continue
        for m in members:
            assigned.add(m["name"])
        lines.append(f"## {title}（{len(members)}）")
        lines.append("")
        for t in members:
            lines.append(f"### `{t['name']}({sig(t)})`")
            lines.append("")
            for para in (t["doc"].strip().split("\n\n") or [""]):
                body = " ".join(x.strip() for x in para.strip().splitlines())
                if body:
                    lines.append(body)
                    lines.append("")
        rest = [t for t in tools if t["name"] not in assigned]
    rest = [t for t in tools if t["name"] not in assigned]
    if rest:
        lines.append(f"## 其他（{len(rest)}）")
        lines.append("")
        for t in rest:
            lines.append(f"### `{t['name']}({sig(t)})`")
            lines.append("")
            for para in (t["doc"].strip().split("\n\n") or [""]):
                body = " ".join(x.strip() for x in para.strip().splitlines())
                if body:
                    lines.append(body)
                    lines.append("")
    lines.append("## 运行时复核")
    lines.append("")
    lines.append("```python")
    lines.append("import asyncio")
    lines.append("from sciforge.server import mcp")
    lines.append("tools = asyncio.run(mcp.list_tools())")
    lines.append(f"assert len(tools) == {total}")
    lines.append("```")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    write = "--write" in sys.argv
    tools = static_tools()
    static_names = sorted(t["name"] for t in tools)
    rt = runtime_names()
    if static_names != rt:
        only_static = sorted(set(static_names) - set(rt))
        only_rt = sorted(set(rt) - set(static_names))
        print("MISMATCH static vs runtime")
        print("  static only:", only_static)
        print("  runtime only:", only_rt)
        return 2

    text = render(tools)
    if not write:
        old = DOC.read_text(encoding="utf-8") if DOC.exists() else ""
        print(f"static=runtime={len(tools)} tools")
        print(f"doc exists: {DOC.exists()} | doc is current: "
              f"{old.strip() == text.strip()}")
        if old.strip() != text.strip():
            print("run with --write to regenerate docs/mcp-tools.md")
        return 0

    DOC.write_text(text, encoding="utf-8")
    print(f"wrote {DOC} ({len(tools)} tools, {len(text.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
