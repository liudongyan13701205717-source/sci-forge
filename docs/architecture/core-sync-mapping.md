# 核心目录映射表（源 → 桌面）

> 配套文档：[`core-sync.md`](./core-sync.md)。
> 事实来源：`scripts/sync_core.py` 中的 `MANIFEST` 常量，二者必须一致。
> 所有数量与状态观测日期：**2026-09-26**，为当次实测值，会随上游演进变化。

---

## 1. 映射规则

源根 = `sciforge/sciforge/`，目标根 = `sciforge-desktop/core/`。

```
<源根>/<源子目录>/<目录内相对路径>   ──▶   <目标根>/<目标子目录>/<目录内相对路径>
```

两条规则决定了绝大多数映射：

1. **目录内相对路径原样保留。** 只换顶层目录名，目录内部的子目录结构与文件名一字不改。
2. **`core/` 是锚点目录，映射到目标根本身。** 其余 11 个目录保持原名，作为目标根下的子目录。

因此 `sciforge/core/project_memory.py` → `sciforge-desktop/core/project_memory.py`（落在根），
而 `sciforge/venue/journal_fit.py` → `sciforge-desktop/core/venue/journal_fit.py`（落在子目录）。

---

## 2. 映射总表

| # | 源目录 | 目标路径 | 内容 | 适配注意 |
| --- | --- | --- | --- | --- |
| 1 | `core/` | `core/`（根，**锚点**） | `workspace_root()`、`.sci-forge` 布局 `Layout`、项目记忆、可选 LLM 连接层 | 投影后会**覆盖**桌面端现有的 `core/__init__.py` stub；该 stub 是桌面端 `core/` 目前**唯一**的文件 |
| 2 | `claims/` | `core/claims/` | claim→source 核验、Stage 2.5 / 4.5 完整性门、Material Passport、bypass 审批 | 依赖源仓 `sciforge.*` 绝对导入；门控逻辑为 fail-closed |
| 3 | `deliver/` | `core/deliver/` | 交付物清单、投稿材料打包（zip + cover letter + checklist） | 打包路径约定指向 `.sci-forge/tasks/`，桌面端需保证同名工作区存在 |
| 4 | `disciplines/` | `core/disciplines/` | 学科 registry，**1538 门**，14 个门类，零注册自动发现 | 目录下实测 **1541 个 `.py`**（多出 3 个为 `__init__.py` 等包结构文件，非学科条目）；`list_by_category()` 用子串匹配，`"理学"` 会连带命中 `"管理学"` |
| 5 | `export/` | `core/export/` | Markdown / LaTeX / HTML / DOCX 导出、PDF 渲染 | PDF 导出在无 LaTeX 引擎时回退内置 PyMuPDF；渲染属重 I/O，桌面端调用宜放线程 |
| 6 | `parse/` | `core/parse/` | 论文 PDF 解析（PyMuPDF） | 依赖 `pymupdf>=1.24`，属 `reproduce` extra，桌面端默认不装 —— 投影后**导入即失败**，需按需安装 |
| 7 | `reproduce/` | `core/reproduce/` | 五步复现闭环：任务、代码生成、沙箱、编排、静态点评 | 依赖 `numpy>=1.26`、`matplotlib>=3.8`（同属 `reproduce` extra）；含子进程调用 —— 与「同步脚本禁 subprocess」的约束无关，该约束只针对 `sync_core.py` |
| 8 | `research/` | `core/research/` | 研究线与科研/论文工具集，实测 **29 个 `.py`** | 文件数最多、单文件跨度最大；含大量 Crossref / OpenAlex 免 key 调用 |
| 9 | `review/` | `core/review/` | 7 席多视角评审面板、评审准入门、报告指南 | 准入门为 fail-closed，证据不足即拒绝 |
| 10 | `science/` | `core/science/` | 科学数据连接器框架，**46 个连接器 / 7 个领域**，含 `science/sources/` | 连接器源码在 `science/sources/` 子目录，随目录整体投影；**已知缺口：`science_fetch` 仅 `uniprot` 实现回调，其余 45 个仅 `science_search` 可用**；3 个连接器读 `CORE_API_KEY` / `CNKI_API_URL` / `WANFANG_API_URL` |
| 11 | `venue/` | `core/venue/` | 期刊/会议模板、journal-fit 匹配度评分 | 模板为数据驱动，改动频繁，漂移概率最高 |
| 12 | `write/` | `core/write/` | 论文文档存储（DocStore）、章节模板、章节校验 | 写入目标为 `.sci-forge/projects/{paper_id}/`，与桌面端 `sessions/` 是两套独立存储，不可混用 |

---

## 3. 排除项

| 项 | 位置 | 排除理由 |
| --- | --- | --- |
| `server.py` | 源包根层 | MCP server 传输层入口（FastMCP、75 个 `@mcp.tool`、2 个 `@mcp.resource`），仅源仓有意义 |
| `cli.py` | 源包根层 | `sci-forge` 命令入口（stdio / `--version` / `--help`），仅源仓有意义 |
| `__main__.py` | 源包根层 | `python -m sciforge` 入口，仅源仓有意义 |
| `__init__.py` | 源包根层 | 包级导出面；其绝对导入路径在桌面端包布局下不成立 |
| `__pycache__/` | 任意层级 | 编译缓存 |
| `.*` 隐藏文件 | 任意层级 | 本地配置 |
| `.pyc` / `.pyo` / `.orig` / `.rej` | 任意层级 | 编译产物与补丁残留 |

根层 4 个散文件的排除是**结构性**的：脚本清单只登记目录，根层散文件天然不在范围内。
数量依据：2026-09-26 实测源包根层 `.py` 恰为 4 个。

---

## 4. 规模与漂移预期

| 指标 | 2026-09-26 实测 |
| --- | --- |
| 纳入同步的目录数 | 12 |
| 排除的源包根层散文件 | 4 |
| 桌面端 `core/` 现有文件 | 1（`__init__.py` stub，3 行 docstring） |
| 首次 `--apply` 预期写入 | 12 个目录下的全部 `.py`；`disciplines/` 单独贡献 1541 个文件，故总量为**数百个文件** |
| 首次 `--check`（apply 前）预期结果 | 必然失败：桌面端几乎全部文件为 `missing-in-target`，`core/__init__.py` 为 `content-differs` |
| 桌面端是否已有可执行核心代码 | 无 |

首次落地的预期失败是**机制正常工作的证明**，不是配置错误：CI 的作用正是让
「桌面端还没投影」这件事可见。完成首次 `--apply` 后 CI 转绿。

---

## 5. 漂移高发区

按「改动频率 × 文件数」判断，以下目录最需要频繁跑 `--check`：

| 优先级 | 目录 | 原因 |
| --- | --- | --- |
| 高 | `disciplines/` | 文件基数最大（1541 个 `.py`），学科条目按数据新增，漂移面积最大 |
| 高 | `venue/` | 期刊模板与匹配规则为数据表，更新频繁 |
| 中 | `science/sources/` | 46 个连接器各自演化，含 API 端点与字段变动 |
| 中 | `research/` | 29 个 `.py`，工具集持续扩充 |
| 低 | `parse/`、`reproduce/` | 依赖外部二进制与数值库，变更节奏较慢 |

---

## 6. 已知阻塞项

**绝对导入不随投影解决。** 2026-09-26 实测：源仓有 **482 处** `sciforge.` 绝对导入，
分布于 **320 个**文件（grep 文本匹配口径，含注释与字符串字面量，为上界估计）。
投影是逐字节复制，投影后这些导入在桌面端包布局下不成立。

映射表**只登记事实，不做架构选型**。三种应对方案（桌面侧兼容包 / 调整命名空间 / 同步后改写导入）
及其代价见 [`core-sync.md` 第 7 节](./core-sync.md)。无论选哪个，`sync_core.py` 的行为不变 ——
它保证字节一致，导入可解析性由适配层负责。

---

## 7. 清单一致性维护

映射表与脚本的 `MANIFEST` 是同一份事实的两个视图：

- 改目录名 / 增删目录 → 必须同时改 `MANIFEST` 与本表。
- 只改说明文字 → 两处都改，避免注释与实现分家。
- 脚本在发现清单中某源目录不存在时，会在报告的「说明」段落列出并提示
  「若目录被重命名，请同步更新本脚本的 MANIFEST」，不会静默跳过。
- 脚本提供 `--list-manifest` 打印当前清单，可与本表逐行对照。
