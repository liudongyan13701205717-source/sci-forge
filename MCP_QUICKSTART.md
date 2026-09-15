# sci-forge — MCP 标准安装与调用（3 分钟上手）

> 目标是：**装好后，你只需要像用其它 MCP 一样在对话里自然描述任务**，
> `sci-forge_*` 工具就会自动被 agent 选中并执行——**不需要写命令、不需要碰文件**。

---

## 1. 一次安装

要求：Python ≥ 3.10。

```bash
# 方式 A：从 GitHub 安装（推荐，总是最新）
pip install "git+https://github.com/liudongyan13701205717-source/sci-forge.git"

# 方式 B：先克隆、再本地安装（可同时拿到源码与示例）
git clone https://github.com/liudongyan13701205717-source/sci-forge.git
cd sci-forge
pip install .

# （可选）复现线依赖：解析 PDF / 沙箱跑代码 / 画收敛图
pip install ".[reproduce]"
```

`pip install` 会自动把 `sci-forge` 命令放进 PATH（Windows 在
`<Python>\Scripts`，macOS/Linux 在 `<venv>/bin`）。

**自检：新开一个终端，下面两条必须正常。**

```bash
sci-forge --version      # 打印 sci-forge 0.1.0
sci-forge --help         # 打印用法帮助
```

> 若提示 `sci-forge` 找不到：确认该 Python 环境的 `Scripts`/`bin` 目录在 PATH 里。
> Windows 下可 `where sci-forge` 查看。

---

## 2. 注册为 MCP server（配置一次，永续生效）

### opencode（`~/.config/opencode/opencode.json`）

```jsonc
{
  "mcp": {
    "sci-forge": {
      "type": "local",
      "command": ["sci-forge"],
      "enabled": true,
      "timeout": 120000,
      "environment": {
        "SCI_FORGE_OFFLINE": "0",
        // 可选：接入 OpenAI 兼容 LLM，让章节生成/评审更自然
        "SCI_FORGE_LLM_BASE": "https://api.example.com/v1",
        "SCI_FORGE_LLM_KEY": "sk-...",
        "SCI_FORGE_LLM_MODEL": "your-model"
      }
    }
  }
}
```

> 关键点：`command` 只写 `sci-forge` 这个名字，**不要**写绝对路径解释器 / `PYTHONPATH`
> / `cwd` —— 安装后它就在 PATH 上，这才是一份能在任何机器原样生效的标准配置。

### Claude Code（`~/.claude.json` / claude mcp add）

```bash
claude mcp add sci-forge -- python -m sciforge.cli
```

### Cursor / 其它 MCP 客户端

新增一条 `local` / `stdio` MCP：

- 命令：`sci-forge`
- 参数：无
- 启用后重启客户端

---

## 3. 验证：工具被正常加载

重启你的 MCP 客户端（**完全退出再打开**，让新 PATH / 新配置生效），然后：

- opencode：应能在工具列表看到 `sci-forge_*` 前缀的约 44 个工具；
- 其它客户端：进入 MCP 面板确认 `sci-forge` 状态为 connected。

需要 research/写作/复现都正常的话，快速冒烟：

```
science_list_dbs()            → 返回 41 个数据库（跨 7 个领域）
list_disciplines()            → 返回 44 门学科（自动发现）
get_deliverables("demo")      → 若无项目会报“不存在”，属正常
```

---

## 4. 用起来：标准 MCP 调用（不是命令，不是文件）

装好之后，**一切通过对话触发**。以下都是自然语言，agent 会自动映射到工具：

| 你说 | agent 实际调用 | 结果落盘 |
| --- | --- | --- |
| “构思一个大语言模型可解释性的课题” | `ideate_paper(topic, paper_id)` | 缺口/假设/辩论/实验计划 |
| “写一篇边缘推理优化的论文” | `write_section(...)`×6 → `export_document(...)` | `doc.md / doc.pdf / doc.tex / doc.docx` |
| “把我的项目打包成投稿 zip” | `package_submission(paper_id)` | `submission_*.zip`（含 cover letter） |
| “传说中用 OpenAlex 查一下 transformer 论文” | `science_search("openalex", ...)` | 返回结构化结果 |
| “复现这份 PDF 并跑实验” | `reproduce_paper(pdf_path)` → `reproduce_status(...)` | tasks/…/results.json + 图 |

工作区约定：所有产物写入**运行客户端的当前目录**下的 `.sci-forge/`（projects 与 tasks 子目录），
已 gitignore，不入库。

---

## 5. 离线模式（可选）

有网时全部工具自动联网。若在无外网环境使用，设 `SCI_FORGE_OFFLINE=1`，
联网类工具会**优雅降级**（返回占位模板/启发式结果），本地写作/导出/交付不受影响。

---

## 6. 故障排查

| 现象 | 原因 | 处理 |
| --- | --- | --- |
| 工具列表里没有 sci-forge | 配置未生效 / 未重启 | 完全退出客户端重启；opencode 用 `/mcp` → connect |
| 报 `ModuleNotFoundError` | `PYTHONPATH` 指到了别的工程目录 | 不要设置 PYTHONPATH；除非你是源码运行 |
| 启动即退出 | PATH 里没有 `sci-forge` | `pip install` 后重开终端；`where sci-forge` 验证 |
| 工具返回“离线模板/无结果” | `SCI_FORGE_OFFLINE=1` 或网络不可达 | 改 `"0"` 或检查网络 |
| 调用超时 | 首次冷启动 | 等 1–2s 重试 |

---

**一切就绪后，剩下的就是对话。** 详细功能清单与端到端示例见 [README.md](./README.md) 与 [USAGE.md](./USAGE.md)。
