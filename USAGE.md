# 使用指南 (USAGE)

> 本文件说明如何让 `sci-forge` MCP 在 opencode / Claude Code 中**自动启动并自然调用**，
> 以及如何验证 server 自启正常。

---

## 1. 快速验证：server 能否自动启动

`sci-forge` 是 `type: local` 的 stdio MCP。只要配置正确，客户端会**自动 spawn** 一个
子进程并连接，无需任何手动操作。

### 命令行自检（30 秒）

```bash
C:\Python314\python.exe -c "import sciforge.server; print('import ok')"
```

能打印 `import ok` 即说明包、依赖、路径都正常。

### 模拟客户端自动连接（推荐，彻底验证）

用与 `opencode.json` 完全一致的参数 spawn 子进程并自动调用工具，全程无手动：

```python
# scripts/verify_mcp_auto.py
import asyncio, os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = r"F:\opencode工坊\sciforge"

async def main():
    env = dict(os.environ); env["PYTHONPATH"] = ROOT
    params = StdioServerParameters(
        command=r"C:\Python314\python.exe",
        args=["-m", "sciforge.server"],
        cwd=ROOT, env=env,
    )
    async with stdio_client(params) as (r, w):
        async with ClientSession(r, w) as s:
            await s.initialize()
            tools = await s.list_tools()
            print("auto_started, tools =", sorted(t.name for t in tools.tools))

asyncio.run(main())
```

输出能看到 24 个工具即证明 server 自启 + 协议正常（日志走 stderr，不污染 stdout 的 JSON-RPC 流）。

---

## 2. 让 opencode 自动连接并自然调用

### 配置前提（已写入 `~/.config/opencode/opencode.json`）

```jsonc
{
  "mcp": {
    "sci-forge": {
      "type": "local",
      "command": ["C:\\Python314\\python.exe", "-m", "sciforge.server"],
      "cwd": "F:\\opencode工坊\\sciforge",
      "enabled": true,
      "timeout": 120000,
      "environment": {
        "SCIFORGE_ENV": "dev",
        "PYTHONPATH": "F:\\opencode工坊\\sciforge"
      }
    }
  }
}
```

关键点：
- **用绝对路径**指向解释器与工作区（不要用裸 `python`，避免命中系统 Store 占位符）。
- `cwd` 与 `PYTHONPATH` 都指向项目根，保证能 import 到 `sciforge` 包。
- `timeout` 设为 `120000`（毫秒）：opencode 默认首次连接超时只有几秒，冷启动 / 工具
  列表初始化较慢时会被误判为"掉线"（表现为需要手动 connect）。显式加大超时即可保证
  **自动拉起**。

### 让会话内看见工具

1. **完全退出 opencode 进程**（关掉整个终端/窗口，不是只关标签页），再重新打开。
   → 否则旧进程仍持有修改前的 MCP 配置。
2. 重启后，24 个工具应出现在可用工具列表
   （复现 2 + 写作 2 + 研究/科研 16 + 科学数据 4）：
   `reproduce_paper / reproduce_status / write_section / export_document /
    ideate_paper / inject_results / research_verdict / get_deliverables /
    research_plan / literature_review / auto_title_abstract / peer_review /
    venue_suggest / paper_polish /
    compare_metrics / check_novelty / package_submission /
    citation_landscape / project_memory / review_code /
    science_list_dbs / science_search / science_fetch / science_cross_lookup`
3. 若左侧工具列表没出现，输入 `/mcp` 打开面板，对 `sci-forge` 点 **connect**（一次性）。
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

## 4. 无 Key 成文（方案 A：agent 直接成文）——科研/论文推荐工作流

本复刻**不配置任何 LLM API key**，论文正文由 **agent（opencode 等）直接用当前对话模型
写出完整章节**，再由本地工具导出。这与"对话中自然调用 write_section"等价，区别在于：
每个章节都写成完整正文（不依赖 server 端模板占位），从而导出内容是真实论文而非骨架。

### 初始化脚手架（生成章节占位 + 成文协议）

```bash
# 在项目根，cwd 指向 sciforge
python scripts/agent_write_paper.py <paper_id> --topic "研究方向"
```

脚本会创建 `projects/<paper_id>/sections/*.md` 空章节占位 + 重建 `doc.md`，
并输出一份 10 章节的**成文清单**，同时写入 `WRITING_PROTOCOL.md` 记录无 key 契约。

### 科研/论文新增六工具（聚焦"全部科研、论文"）

| 工具 | 作用 | 落盘 |
| --- | --- | --- |
| `research_plan(topic, paper_id)` | 完整研究计划书（RQ/假设/目标/贡献/方法/数据/基线/里程碑/风险） | `research/research_plan.{json,md}` |
| `literature_review(topic, paper_id)` | 文献综述（OpenAlex 免 key 检索：代表文献/聚类/缺口/结构） | `research/literature_review.{json,md}` |
| `auto_title_abstract(paper_id)` | 从正文提炼标题/摘要/关键词；无一级标题时以摘要首句生成候选标题，无关键词行时走中文 n-gram 主题词回退 | `research/metadata.{json,md}` |
| `peer_review(paper_id)` | 模拟同行评审（4 维评分 + 推荐 + 优缺点/修改建议） | `research/peer_review.{json,md}` |
| `venue_suggest(topic, paper_id)` | 投稿/期刊匹配（内置映射库 + 可选 LLM） | `research/venue_suggest.{json,md}` |
| `paper_polish(paper_id, mode)` | 润色/一致性/完整性检查（mode: completeness/consistency/grammar） | `research/polish_{mode}.{json,md}` |

这些工具无 LLM 时**全部走确定性模板/映射/规则**，可独立产出有价值结果；配置了
`SCIFORGE_LLM_*` 环境变量后会自动升级为模型增强。

### 成果分析与交付六工具（科研进阶）

| 工具 | 作用 | 落盘 |
| --- | --- | --- |
| `compare_metrics(paper_id, tasks, baseline, metric)` | 汇总多个复现任务的指标序列，输出均值±std 对比表，并对对照组做 Welch t / Mann-Whitney U 显著性检验（纯标准库，无需 numpy/scipy） | `research/benchmark_compare.{json,md}` |
| `check_novelty(paper_id, max_papers)` | 从标题/摘要抽关键词检索 OpenAlex 相似工作，给出重叠度与候选差异点 | `research/novelty.{json,md}` |
| `citation_landscape(paper_id, doi_or_topic)` | 围绕 DOI 或主题分析引文热度：年度分布 / 高被引代表 / 主要载体 | `research/citation_landscape.{json,md}` |
| `package_submission(paper_id, task_id)` | 把论文导出物 + 研究产物 +（可选）复现代码打成投稿 zip，内置 Cover Letter 与投稿前 Checklist | `projects/{id}/submission_*.zip` |
| `project_memory(paper_id, action, note, milestone, status)` | 项目进度记账（read/note/milestone/status），形成可回溯研究日志 | `projects/{id}/memory.json` |
| `review_code(task_id)` | 复现代码静态点评：行数/函数/导入、随机种子、硬编码超参、裸 except、TODO 等，并给出 100 分制可信度分 | `tasks/{id}/code_review.{json,md}` |

这些工具同样遵循**离线优先**：网络检索失败时自动回退启发式模板，不抛错。

### 端到端科研-论文链路建议

```text
ideate_paper(topic, paper_id)          # 选题与缺口
research_plan(topic, paper_id)         # 研究计划书
literature_review(topic, paper_id)     # 文献综述（related work 素材）
# agent 依 WRITING_PROTOCOL 用 write_section 写满各章完整正文
auto_title_abstract(paper_id)          # 提炼标题/摘要/关键词
peer_review(paper_id)                  # 模拟审稿，据意见修订
paper_polish(paper_id, "completeness") # 检查完整性
paper_polish(paper_id, "grammar")      # 语言润色
venue_suggest(topic, paper_id)         # 投稿建议
export_document(paper_id, "pdf")       # 终版导出
```

---

## 5. 常见问题

| 现象 | 原因 | 处理 |
| --- | --- | --- |
| 工具列表里没有 `sci-forge` | opencode 未重启 / 未 connect | 完全退出重启；或 `/mcp` → connect |
| 启动报错 `ModuleNotFoundError` | `PYTHONPATH` 或 `cwd` 未指向项目根 | 核对配置中的绝对路径 |
| 首次打开出现"需要手动 connect" | 默认连接/枚举超时太短，冷启动被误判掉线 | 配置 `"timeout": 120000` 后完全重启 opencode |
| 调用超时 / 卡住 | 首次冷启动 | 稍等 1–2s 重试 |
| `check_novelty` / `citation_landscape` 返回"离线模板" | 网络不可达（本机 github/OpenAlex 被阻断） | 属预期回退，仍产出启发式结论 |
| 无法 git push | 本机 `github.com` 被网络环境阻断 | 用 GitHub API / MCP，或等网络恢复 |

---

## 6. 测试

```bash
python -m pytest tests/ -q   # 全量测试，全离线可跑
```

---

## 7. 科学数据查询

通过 41 个连接器覆盖 7 大领域（literature / proteins / chemistry / genomics / pathways / omics / datasets），提供 4 个 MCP 工具：

### 列出可用数据库

```text
science_list_dbs()                          # 列出全部 41 个数据库
science_list_dbs("literature")              # 仅列出 literature 领域的数据库
```

### 单库搜索

```text
science_search("openalex", "transformer attention", limit=5)   # 搜索 OpenAlex
science_search("uniprot", "BRCA1", limit=3)                   # 搜索 UniProt
science_search("chembl", "aspirin", limit=5)                  # 搜索 ChEMBL
```

### 按 ID 获取记录

```text
science_fetch("openalex", "W123456789")            # 获取 OpenAlex 记录
science_fetch("uniprot", "P53_HUMAN")              # 获取 UniProt 记录
science_fetch("rcsb-pdb", "1ABC")                  # 获取 PDB 结构
```

### 多库联合查询

```text
science_cross_lookup("BRCA1", databases=["uniprot", "mygene"], limit=3)   # 多库查 BRCA1
science_cross_lookup("aspirin")                                             # 全库搜索
```
