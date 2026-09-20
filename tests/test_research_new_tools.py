"""研究线新工具 MCP 协议级测试：真实 spawn MCP server，经 stdio 调用 12 个新工具。

覆盖：verify / papers / scout / rag / code_link 五模块全部公开函数。
离线确定性验证（SCI_FORGE_OFFLINE=1）：验证协议级可发现 + 可调用 + 优雅降级。

运行：python -m pytest tests/test_research_new_tools.py -v
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

NEW_TOOLS = {
    "verify_citation",
    "verify_claim",
    "verify_reference_list",
    "paper_metadata",
    "citation_graph",
    "download_paper_pdf",
    "scout_topic",
    "scout_compare",
    "rag_answer",
    "rag_sources",
    "find_code_for_paper",
    "link_papers_to_code",
}


def _clean(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


def _text_of(content) -> str:
    for block in content:
        text = getattr(block, "text", None)
        if text is not None:
            return _clean(text)
    return ""


def _params(offline: bool = True):
    env = dict(os.environ)
    env["PYTHONPATH"] = _PROJECT_ROOT + os.pathsep + env.get("PYTHONPATH", "")
    if offline:
        env["SCI_FORGE_OFFLINE"] = "1"
    return StdioServerParameters(
        command=sys.executable,
        args=["-m", "sciforge.server"],
        cwd=_PROJECT_ROOT,
        env=env,
    )


def test_new_tools_registered_via_stdio():
    """MCP server 经 stdio 启动，12 个新工具全部可发现。"""

    async def _run():
        async with stdio_client(_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                tools = await session.list_tools()
                return {t.name for t in tools.tools}

    names = asyncio.run(_run())
    assert NEW_TOOLS.issubset(names), f"缺少工具：{NEW_TOOLS - names}"


def test_verify_tools_via_stdio():
    """verify 三工具协议级调用（离线降级路径）。"""

    async def _run():
        async with stdio_client(_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                r1 = await session.call_tool(
                    "verify_citation", {"doi": "10.1038/s41586-020-2649-2"}
                )
                d1 = _text_of(r1.content)
                assert '"ok": false' in d1 and "离线模式" in d1

                r2 = await session.call_tool(
                    "verify_claim", {"claim": "深度学习提升图像识别准确率"}
                )
                d2 = _text_of(r2.content)
                assert '"ok": true' in d2 and "NO_EVIDENCE" in d2

                r3 = await session.call_tool(
                    "verify_reference_list",
                    {"refs": ["10.1038/s41586-020-2649-2", "10.9999/fake-doi"]},
                )
                d3 = _text_of(r3.content)
                assert '"ok": true' in d3 and '"total": 2' in d3

    asyncio.run(_run())


def test_papers_tools_via_stdio():
    """papers 三工具协议级调用（离线降级路径）。"""

    async def _run():
        async with stdio_client(_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                r1 = await session.call_tool(
                    "paper_metadata", {"doi": "10.1038/s41586-020-2649-2"}
                )
                d1 = _text_of(r1.content)
                assert '"ok": false' in d1 and "离线模式" in d1

                r2 = await session.call_tool(
                    "citation_graph", {"doi": "10.1038/s41586-020-2649-2"}
                )
                d2 = _text_of(r2.content)
                assert '"ok": false' in d2 and "离线模式" in d2

                r3 = await session.call_tool(
                    "download_paper_pdf", {"doi": "10.1038/s41586-020-2649-2"}
                )
                d3 = _text_of(r3.content)
                assert '"ok": false' in d3 and "离线模式" in d3

    asyncio.run(_run())


def test_scout_tools_via_stdio():
    """scout 两工具协议级调用（离线降级路径）。"""

    async def _run():
        async with stdio_client(_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                r1 = await session.call_tool(
                    "scout_topic", {"topic": "graph neural network"}
                )
                d1 = _text_of(r1.content)
                assert '"ok": true' in d1 and '"total": 0' in d1

                r2 = await session.call_tool(
                    "scout_compare", {"topics": ["gnn", "transformer"]}
                )
                d2 = _text_of(r2.content)
                assert '"ok": true' in d2 and '"comparison"' in d2

    asyncio.run(_run())


def test_rag_tools_via_stdio():
    """rag 两工具协议级调用（离线降级路径）。"""

    async def _run():
        async with stdio_client(_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                r1 = await session.call_tool(
                    "rag_answer", {"question": "什么是图神经网络？"}
                )
                d1 = _text_of(r1.content)
                assert '"ok": true' in d1 and "离线模式" in d1

                r2 = await session.call_tool(
                    "rag_sources", {"question": "transformer"}
                )
                d2 = _text_of(r2.content)
                assert '"ok": true' in d2 and '"sources"' in d2

    asyncio.run(_run())


def test_code_link_tools_via_stdio():
    """code_link 两工具协议级调用（离线降级路径）。"""

    async def _run():
        async with stdio_client(_params()) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                r1 = await session.call_tool(
                    "find_code_for_paper", {"title": "Attention is all you need"}
                )
                d1 = _text_of(r1.content)
                assert '"ok": true' in d1 and '"code_links"' in d1

                r2 = await session.call_tool(
                    "link_papers_to_code", {"topic": "diffusion model"}
                )
                d2 = _text_of(r2.content)
                assert '"ok": true' in d2 and '"links"' in d2

    asyncio.run(_run())


def test_new_tools_online_path_via_stdio():
    """在线路径冒烟：不设离线变量，工具应可调用且不抛异常（网络不可用时自动降级）。"""

    async def _run():
        async with stdio_client(_params(offline=False)) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                r = await session.call_tool(
                    "scout_topic", {"topic": "graph neural network", "limit": 3}
                )
                d = _text_of(r.content)
                assert '"ok": true' in d  # 在线成功或网络失败降级均返回 ok

    asyncio.run(_run())
