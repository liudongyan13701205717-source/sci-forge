# 使用指南 (USAGE)

> 本文件说明如何让 `clawsgo-self` MCP 在 opencode / Claude Code 中**自动启动并自然调用**，
> 以及如何验证 server 自启正常。

---

## 1. 快速验证：server 能否自动启动

`clawsgo-self` 是 `type: local` 的 stdio MCP。只要配置正确，客户端会**自动 spawn** 一个
子进程并连接，无需任何手动操作。

### 命令行自检（30 秒）

```bash
C:\Python314\python.exe -c "import clawsgo_self.server; print('import ok')"
```

能打印 `import ok` 即说明包、依赖、路径都正常。

### 模拟客户端自动连接（推荐，彻底验证）

用与 `opencode.json` 完全一致的参数 spawn 子进程并自动调用工具，全程无手动：

```python
# scripts/verify_mcp_auto.py
import asyncio, os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = r"F:\opencode工坊"

async def main():
    env = dict(os.environ); env["PYTHONPATH"] = ROOT
    params = StdioServerParameters(
        command=r"C:\Python314\python.exe",
        args=["-m", "clawsgo_self.server"],
        cwd=ROOT, env=env,
    )
    async with stdio_client(params) as (r, w):
        async with ClientSession(r, w) as s:
            await s.initialize()
            tools = await s.list_tools()
            print("auto_started, tools =", sorted(t.name for t in tools.tools))

asyncio.run(main())
```

输出能看到 8 个工具即证明 server 自启 + 协议正常（日志走 stderr，不污染 stdout 的 JSON-RPC 流）。

---

## 2. 让 opencode 自动连接并自然调用

### 配置前提（已写入 `~/.config/opencode/opencode.json`）

```jsonc
{
  "mcp": {
    "clawsgo-self": {
      "type": "local",
      "command": ["C:\\Python314\\python.exe", "-m", "clawsgo_self.server"],
      "cwd": "F:\\opencode工坊",
      "enabled": true,
      "environment": {
        "CLAWSGO_SELF_ENV": "dev",
        "PYTHONPATH": "F:\\opencode工坊"
      }
    }
  }
}
```

关键点：
- **用绝对路径**指向解释器与工作区（不要用裸 `python`，避免命中系统 Store 占位符）。
- `cwd` 与 `PYTHONPATH` 都指向项目根，保证能 import 到 `clawsgo_self` 包。

### 让会话内看见工具

1. **完全退出 opencode 进程**（关掉整个终端/窗口，不是只关标签页），再重新打开。
   → 否则旧进程仍持有修改前的 MCP 配置。
2. 重启后，8 个工具应出现在可用工具列表：
   `reproduce_paper / reproduce_status / write_section / export_document /
    ideate_paper / inject_results / research_verdict / get_deliverables`
3. 若左侧工具列表没出现，输入 `/mcp` 打开面板，对 `clawsgo-self` 点 **connect**（一次性）。
   首次 spawn 会有 ~1–2s 冷启动。

> opencode 对 `type: local` MCP 是**懒加载**：首次真正调用工具时才拉起进程，之后本会话内自动复用。

### 对话中自然调用（与调用 GitHub MCP 一致）

直接在对话里描述意图，工具会被自动选中执行，例如：

```text
「构思一个大语言模型可解释性的研究课题」
→ 自动调用 ideate_paper(topic, paper_id)

「给我写一篇关于边缘推理优化的论文」
→ 自动调用 write_section(...) 各章节 + export_document(paper_id, "pdf")
```

调用过程会在对话流中显示（工具名 + 入参 + 结果），与其它 MCP 完全一致。

---

## 3. 端到端示例：对话式生成一篇论文

```text
# 1) 构思选题（研究线）
ideate_paper("大语言模型的可解释性", "explain_llm")

# 2) 逐章撰写（写作线）
write_section("explain_llm", "abstract",   "为《LLM 可解释性》写摘要", "markdown")
write_section("explain_llm", "problem",    "问题定义：黑箱与大模型归因", "markdown")
write_section("explain_llm", "modeling",   "建模：注意力归因与概念探测", "markdown")
write_section("explain_llm", "solution",   "求解：集成探针与忠实度评估", "markdown")
write_section("explain_llm", "results",    "实验设置与评估指标", "markdown")
write_section("explain_llm", "references", "参考文献", "markdown")

# 3) 导出成果（导出线）
export_document("explain_llm", "pdf")   # 产物 projects/explain_llm/doc.pdf + doc.tex + doc.html

# 4) 查看交付物（交付线）
get_deliverables(paper_id="explain_llm")
```

---

## 4. 常见问题

| 现象 | 原因 | 处理 |
| --- | --- | --- |
| 工具列表里没有 `clawsgo-self` | opencode 未重启 / 未 connect | 完全退出重启；或 `/mcp` → connect |
| 启动报错 `ModuleNotFoundError` | `PYTHONPATH` 或 `cwd` 未指向项目根 | 核对配置中的绝对路径 |
| 调用超时 / 卡住 | 首次冷启动 | 稍等 1–2s 重试 |
| 无法 git push | 本机 `github.com` 被网络环境阻断 | 用 GitHub API / MCP，或等网络恢复 |

---

## 5. 测试

```bash
python -m pytest tests/ -q   # 40 项，全离线可跑
```
