"""命令行入口（`sci-forge` 脚本）：启动 MCP server。

无参数时以 stdio transport 启动（MCP 标准形态，供 opencode/Claude Code
等客户端按 `"command": ["sci-forge"]` 直接拉起）。
`--version` / `--help` 用于安装自检。
"""

from __future__ import annotations

import sys


def _usage() -> str:
    return (
        "sci-forge — MCP server（论文复现/写作/科研/交付 + 科学数据查询）\n\n"
        "用法：\n"
        "  sci-forge           以 stdio 启动 MCP server（客户端标准调用方式）\n"
        "  sci-forge --version 打印版本\n"
        "  sci-forge --help    显示本帮助\n"
    )


def main() -> int:
    argv = sys.argv[1:]
    if "--version" in argv or "-V" in argv:
        from sciforge import __version__

        print(f"sci-forge {__version__}")
        return 0
    if "--help" in argv or "-h" in argv:
        print(_usage())
        return 0
    if argv:
        print(f"未知参数：{argv[0]}\n\n{_usage()}", file=sys.stderr)
        return 2

    from sciforge.server import run

    run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
