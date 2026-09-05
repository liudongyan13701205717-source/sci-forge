"""阶段 0 冒烟测试：验证 5 个 MCP 工具注册并通过 stdio 调用成功。

运行：python -m pytest tests/ -v
"""

from __future__ import annotations

import asyncio
import os
import re
import sys

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXPECTED_TOOLS = {
    "reproduce_paper",
    "reproduce_status",
    "write_section",
    "export_document",
    "get_deliverables",
    "ideate_paper",
    "inject_results",
    "research_verdict",
}


def _clean(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


def _text_of(content) -> str:
    """从 MCP call_tool 结果中提取第一段文本内容。"""
    for block in content:
        text = getattr(block, "text", None)
        if text is not None:
            return _clean(text)
    return ""


def _new_params():
    env = dict(os.environ)
    env["PYTHONPATH"] = _PROJECT_ROOT + os.pathsep + env.get("PYTHONPATH", "")
    return StdioServerParameters(
        command=sys.executable,
        args=["-m", "sciforge.server"],
        cwd=_PROJECT_ROOT,
        env=env,
    )


def test_tools_registered_via_stdio():
    """MCP server 通过 stdio 启动，列出全部预期工具。"""

    async def _run():
        async with stdio_client(_new_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await session.list_tools()
                return {t.name for t in tools.tools}

    names = asyncio.run(_run())
    assert EXPECTED_TOOLS.issubset(names), f"缺少工具：{EXPECTED_TOOLS - names}"


def test_write_export_deliver_e2e():
    """写作 → 导出 → 交付端到端（真实实现，同一 stdio 会话）。"""
    import json

    async def _run():
        async with stdio_client(_new_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                # 1) 写两章
                r1 = await session.call_tool(
                    "write_section",
                    {"paper_id": "e2e", "section": "abstract",
                     "prompt": "研究大语言模型可解释性的高效方法", "format": "latex"},
                )
                d1 = json.loads(_text_of(r1.content))
                assert d1.get("ok") is True, f"写 abstract 失败：{d1}"
                r2 = await session.call_tool(
                    "write_section",
                    {"paper_id": "e2e", "section": "introduction",
                     "prompt": "背景与动机要点", "format": "latex"},
                )
                d2 = json.loads(_text_of(r2.content))
                assert d2.get("ok") is True, f"写 introduction 失败：{d2}"

                # 2) 导出 pdf
                r3 = await session.call_tool(
                    "export_document", {"paper_id": "e2e", "target": "pdf"}
                )
                d3 = json.loads(_text_of(r3.content))
                assert d3.get("ok") is True, f"导出失败：{d3}"
                assert d3.get("engine") in ("pymupdf", "xelatex", "pdflatex", "lualatex")
                assert any(p.endswith("doc.pdf") for p in d3.get("artefacts", []))

                # 3) 交付物清单（写作项目通过 task_id 承载 paper_id）
                r4 = await session.call_tool(
                    "get_deliverables", {"task_id": "e2e"}
                )
                d4 = json.loads(_text_of(r4.content))
                assert d4.get("ok") is True, f"交付物失败：{d4}"
                assert d4.get("count", 0) >= 3  # doc.md/tex/html/pdf 等
                return (d1, d3, d4)

    asyncio.run(_run())


def test_reproduce_real_via_stdio():
    """reproduce_paper / reproduce_status 已是 real 实现：能创建任务并查询状态。"""
    import os
    import json

    # 用一个不存在的 PDF 触发快速失败的背景任务（不提交、不跑子进程）
    pdf = os.path.abspath("smoke_bad_pdf.pdf")

    async def _run():
        async with stdio_client(_new_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                r1 = await session.call_tool(
                    "reproduce_paper", {"pdf_path": pdf, "framework": "pytorch"}
                )
                d1 = json.loads(_text_of(r1.content))
                assert d1.get("ok") is True, f"reproduce_paper 创建失败：{d1}"
                assert d1.get("task_id"), f"应返回 task_id：{d1}"
                assert d1.get("stub") is not True, "reproduce_paper 不应是 stub"

                r2 = await session.call_tool(
                    "reproduce_status", {"task_id": d1["task_id"]}
                )
                d2 = json.loads(_text_of(r2.content))
                assert d2.get("ok") is True, f"查询已创建任务应 ok=True：{d2}"
                assert d2.get("task_id") == d1["task_id"]
                return (d1, d2)

    asyncio.run(_run())


def test_write_section_rejects_unknown_section():
    """写作工具应拒绝未知章节。"""
    import json

    async def _run():
        async with stdio_client(_new_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                res = await session.call_tool(
                    "write_section",
                    {"paper_id": "p", "section": "bogus",
                     "prompt": "研究大语言模型可解释性", "format": "latex"},
                )
                return json.loads(_text_of(res.content))

    data = asyncio.run(_run())
    assert data.get("ok") is False
    assert any("未知章节" in m for m in data.get("notes", []))


def test_research_verdict_via_stdio():
    """research_verdict 可通过 stdio 调用，缺结果时返回 PIVOT。"""
    import json

    async def _run():
        async with stdio_client(_new_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                res = await session.call_tool(
                    "research_verdict", {"task_id": "no_such_task"}
                )
                return json.loads(_text_of(res.content))

    d = asyncio.run(_run())
    assert d.get("ok") is False
    assert d.get("verdict") == "PIVOT"


def test_ideate_via_stdio():
    """ideate_paper 离线可用：子进程设 OFFLINE 短路文献检索，仍返回 ok 与候选方向。"""
    import json

    def _params():
        base = _new_params()
        env = dict(base.env or {})
        env["CLAWSGO_SELF_OFFLINE"] = "1"
        return StdioServerParameters(
            command=base.command,
            args=base.args,
            cwd=base.cwd,
            env=env,
        )

    async def _run():
        async with stdio_client(_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                res = await session.call_tool(
                    "ideate_paper",
                    {"topic": "大语言模型的轻量化可解释方法", "paper_id": "smoke_idea"},
                )
                return json.loads(_text_of(res.content))

    d = asyncio.run(_run())
    assert d.get("ok") is True
    assert d.get("ideation", {}).get("candidates")
    assert d.get("plan_markdown")
    assert d.get("debate", {}).get("reviews")
