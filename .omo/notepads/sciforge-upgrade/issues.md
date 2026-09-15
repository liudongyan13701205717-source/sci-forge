# Issues — sciforge 全方位升级

- 旧目录 F:/opencode工坊/clawsgo 被当前会话 MCP 进程占用，无法删除；重启 opencode 后可删
- 当前会话 opencode 仍是离线环境（旧 SCI_FORGE_OFFLINE=1），在线检索只能验证降级路径
- scripts/verify_mcp_auto.py 可能硬编码工具数 28，注册新工具后需同步更新
- tests/ 中可能有断言工具数量的测试，新增 server.py 工具后需 grep "28" 同步
