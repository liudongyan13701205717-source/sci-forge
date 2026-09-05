"""命令行入口（`sci-forge` 脚本）：启动 MCP server。"""

from __future__ import annotations

import sys


def main() -> int:
    from sciforge.server import run

    run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
