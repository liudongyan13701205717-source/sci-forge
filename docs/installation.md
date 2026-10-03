# 安装

本页覆盖：环境要求、几种安装方式、extras 的区别、MCP 客户端注册、验证安装、常见安装故障。

---

## 环境要求

| 项目 | 要求 |
| --- | --- |
| Python | **>= 3.10**（CI 覆盖 3.11 / 3.12 / 3.13） |
| 基础依赖 | 仅 `mcp>=1.29.0` |
| 操作系统 | Linux / macOS / Windows 均可；复现线在 Linux / macOS 上验证更充分 |
| 网络 | 检索类工具需能访问 OpenAlex / Crossref 等公开接口；其余功能可完全离线 |

无需数据库、无需 Docker、无需 GPU。

---

## 安装方式

### 方式 A：直接装（推荐普通用户）

```bash
pip install "git+https://github.com/liudongyan13701205717-source/sci-forge.git"
```

### 方式 B：可编辑安装 + 全部可选能力（推荐开发者）

```bash
git clone https://github.com/liudongyan13701205717-source/sci-forge.git
cd sci-forge
pip install -e ".[reproduce,dev]"
```

可编辑安装的好处：改动源码立即生效，且能直接跑本仓库的测试。

### 方式 C：开发模式（可编辑 + 测试工具）

```bash
pip install -e ".[dev]"
```

---

## extras 说明

基础安装只装核心 MCP server。三个 extras 按需叠加：

| extra | 引入的依赖 | 装它之后能做什么 |
| --- | --- | --- |
| `reproduce` | `pymupdf`、`numpy`、`matplotlib` | **复现线**：`reproduce_paper` 解析 PDF、生成并执行复现代码、产出图表与数值 |
| `export` | **无硬依赖**（当前为空占位） | 仅作语义标记。PDF 导出走的是**本机 LaTeX 引擎**（`xelatex` / `pdflatex`）；没有引擎时自动回退到内置 PyMuPDF 渲染，因此不装也能导出 |
| `dev` | `pytest`（及开发用工具） | 跑测试、提交贡献 |

组合写法（可叠加多个）：

```bash
pip install -e ".[reproduce,export,dev]"
```

> **注意**：不装 `reproduce` 时，复现线工具仍可被列出，但执行会因缺少 `pymupdf` 报错。要用复现线就必须装这个 extra。

---

## 验证安装

```bash
sci-forge --version      # 应输出：sci-forge 0.1.0
sci-forge --help         # 查看可用子命令
```

也可以用模块入口（等价）：

```bash
python -m sciforge --help
```

再确认包能被导入：

```bash
python -c "import sciforge; print(sciforge.__version__)"
```

---

## 注册到 MCP 客户端

sci-forge 是一个标准 MCP server（`FastMCP("sci-forge")`），以 stdio 方式启动。把启动命令写进你的 MCP 客户端配置即可。

通用配置形态：

```json
{
  "mcpServers": {
    "sci-forge": {
      "command": "sci-forge",
      "args": []
    }
  }
}
```

如果 `sci-forge` 不在 PATH 中（常见于 pipx / 虚拟环境未激活），用绝对路径或 `python -m`：

```json
{
  "mcpServers": {
    "sci-forge": {
      "command": "python",
      "args": ["-m", "sciforge"]
    }
  }
}
```

注册后，客户端里应能看到 **65 个工具**与 **2 个资源**。可用的资源：

- `science://databases` — 静态列表：全部 46 个连接器及其领域
- `science://databases/{domain}` — 按领域读取，如 `science://databases/genomics`

> 各客户端的配置位置与格式略有差异，请以你所用客户端的文档为准。核心是 `command` 指向 `sci-forge`（或 `python -m sciforge`）。

---

## 可选增强：接入 LLM 端点

核心功能**不需要** LLM 也能用（走本地模板 / 规则引擎）。若想获得更自然的生成文本，可在工作区根目录创建 `.sci-forge/env`：

```bash
BASE_URL=https://your-endpoint/v1
API_KEY=sk-...
MODEL=your-model
```

- 该目录已被 `.gitignore` 忽略，但仍要确认不会被 `package_submission` 打进投稿包。
- 未配置时所有文本类工具自动回退，不报错。
- 数据会转发到你指定的 OpenAI 兼容服务；数据流向由该端点决定。

详见 [快速开始 · 可选增强](quickstart.md)。

---

## 离线模式（测试 / 无网环境）

设置环境变量可强制离线，检索类工具不会发起外部请求：

```bash
# Linux / macOS
export SCI_FORGE_OFFLINE=1

# Windows PowerShell
$env:SCI_FORGE_OFFLINE = "1"
```

CI 与本地测试都用这个变量：

```bash
SCI_FORGE_OFFLINE=1 python -m pytest tests/ -q
```

---

## 常见安装故障

| 现象 | 原因 | 处理 |
| --- | --- | --- |
| `pip install` 报 Python 版本错误 | 本机 Python < 3.10 | 升级 Python，或用 pyenv / conda 切到 3.10+ |
| 客户端里看不到 sci-forge 工具 | server 没起来或 `command` 路径错 | 先在终端手动跑 `sci-forge --help` 确认可执行；再把 `command` 改成绝对路径或 `python -m sciforge` |
| `reproduce_paper` 报缺 `pymupdf` | 没装 `reproduce` extra | `pip install -e ".[reproduce]"` |
| 复现线跑一半卡在图表 | 缺 `matplotlib` | 同上，`reproduce` extra 已含 |
| `export_document` 导 PDF 失败 | 本机既无 LaTeX 引擎，内置渲染也出错 | 装 LaTeX（`xelatex` 或 `pdflatex`）可提升质量；注意装 `export` extra **不会**带来 LaTeX，它本身没有依赖 |
| 检索类工具无结果 | 本机无法访问外部接口 | 检查网络 / 代理；或设 `SCI_FORGE_OFFLINE=1` 走离线 |
| 部分连接器返回空 | 未配置可选 key（`CORE_API_KEY` 等） | 空结果是预期行为，不报错；见 [连接器 · 可选凭据](connectors.md#可选凭据) |
| 导入报错 `No module named sciforge` | 安装到了别的环境 | 确认 `pip` 与 `python` 指向同一环境；必要时用 `python -m pip install` |

---

## 下一步

- 想跑通一次完整流程 → [快速开始](quickstart.md)
- 想知道有哪些工具 → [MCP 工具清单](mcp-tools.md)
- 装好了、想直接看学科与数据库 → [学科体系](disciplines.md) / [连接器](connectors.md)

---

## 许可

本文档随仓库同受 [Apache License 2.0](../LICENSE) 约束 — Copyright 2026 liudongyan13701205717。
