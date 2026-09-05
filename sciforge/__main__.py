"""CLI 入口：`python -m sciforge` 等价于启动 MCP stdio server。"""

import sys


def main() -> None:
    from sciforge.server import mcp

    # mcp.run() 通过 stdio 与 opencode 通信；主循环在 stdin 上运行，不阻塞交互。
    mcp.run()


if __name__ == "__main__":
    sys.exit(main())