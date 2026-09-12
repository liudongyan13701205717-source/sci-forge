"""标准 MCP 自检：以客户端的启动方式（command=sci-forge）spawn server，
自动 initialize + list_tools，证明「装完即可通过 MCP 工具调用」。

用法：python scripts/verify_mcp_auto.py
"""

from __future__ import annotations

import asyncio
import shutil
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


def _command() -> list[str]:
    cmd = shutil.which("sci-forge")
    if cmd:
        return [cmd]
    # 源码运行兜底：python -m sciforge.cli
    return [sys.executable, "-m", "sciforge.cli"]


async def main() -> None:
    params = StdioServerParameters(command=_command()[0], args=_command()[1:])
    async with stdio_client(params) as (r, w):
        async with ClientSession(r, w) as s:
            await s.initialize()
            tools = await s.list_tools()
            names = sorted(t.name for t in tools.tools)
            print(f"auto_started via {(_command()[0] if len(_command()) == 1 else 'python -m sciforge.cli')}, tools = {len(names)}")
            print("\n".join(f"  - {n}" for n in names))


if __name__ == "__main__":
    asyncio.run(main())
