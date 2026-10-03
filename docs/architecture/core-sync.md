# 核心同步约定（源仓视角）

> 适用范围：本文件描述 `sciforge`（源仓）如何把核心库单向投影到 `sciforge-desktop`（消费方）。
> 桌面端的镜像说明见 `sciforge-desktop/docs/architecture/core-sync.md`；逐目录映射见
> [`core-sync-mapping.md`](./core-sync-mapping.md)。

本文档中的所有数量与状态均标注观测日期 **2026-09-26**，为当次实测值，会随上游演进变化。

---

## 1. 为什么需要这份约定

两仓面向同一套领域模型（学科 registry、连接器目录、工具语义、`.sci-forge` 存储布局），
但形态不同：

| 维度 | `sciforge`（本仓，源） | `sciforge-desktop`（消费方） |
| --- | --- | --- |
| 形态 | MCP stdio server | PySide6 桌面客户端 |
| 核心代码位置 | `sciforge/` 包内 | `core/`（投影所得） |
| 独有部分 | `server.py` / `cli.py` / `__main__.py` / 包 `__init__.py` | `agent/` `api/` `cli/` `gui/` `sessions/` |

**2026-09-26 当次实测**：两仓之间**零共享代码、零同步机制**。桌面端 `core/` 仅有一个
3 行 docstring 的空占位 `__init__.py`，且其 `pyproject.toml` 未声明对本仓的依赖。
本文件与随附的 `scripts/sync_core.py` 就是补齐这一缺口的机制。

---

## 2. 同步边界

### 2.1 纳入范围

同步以**目录**为单位，源仓包目录 `sciforge/` 下共 **12 个**真实目录，全部纳入：

```
core/  claims/  deliver/  disciplines/  export/  parse/
reproduce/  research/  review/  science/  venue/  write/
```

### 2.2 排除范围

源包**根层散文件**不在同步范围内（**2026-09-26 实测共 4 个**）：

| 文件 | 排除理由 |
| --- | --- |
| `sciforge/server.py` | MCP server 传输层入口（FastMCP、65 个 `@mcp.tool`），仅源仓有意义 |
| `sciforge/cli.py` | `sci-forge` 命令入口（stdio / `--version` / `--help`），仅源仓有意义 |
| `sciforge/__main__.py` | `python -m sciforge` 入口，仅源仓有意义 |
| `sciforge/__init__.py` | 包级导出面，其绝对导入路径在桌面端不成立 |

排除是**结构性的**：脚本清单只登记目录，因此根层散文件天然不在范围内，无需额外排除规则。
若将来 `sciforge/` 根层新增 `.py` 文件，它同样不会进入投影；若某文件应当共享，
需先把它移入 12 个目录之一，再更新本文件与映射表。

### 2.3 内容级排除

脚本在遍历时跳过以下路径（不进入投影、不参与漂移判定）：

- 目录名 `__pycache__`
- 隐藏文件/目录（名字以 `.` 开头）
- 后缀 `.pyc` / `.pyo` / `.orig` / `.rej`

### 2.4 不在范围内

- 桌面端 `core/` **之外**的任何文件：桌面端自有代码，不受本机制影响。
- 本仓 `tests/`、`docs/`、`scripts/` 其余脚本：不属于核心库。
- 依赖声明（`pyproject.toml`）：**不在**同步范围，两仓依赖不同（`mcp>=1.29.0` vs `PySide6>=6.6`）。

---

## 3. 方向：单向

```
sciforge/sciforge/<12 个目录>   ──(只写、不删)──▶   sciforge-desktop/core/
        源（唯一真值）                                          投影（只读消费）
```

- 脚本**只实现** `源 → 消费方` 一个方向，没有任何反向路径。
- 桌面端**不得**直接编辑 `core/` 内的文件：下次同步会被源文件逐字节覆盖。
- 桌面端若需要本地特化，应在 `core/` **之外**新增适配层（例如 `api/` 或新建模块），
  而不是在投影内打补丁 —— 后者必然在下次同步时丢失。

---

## 4. 冲突优先级

当同一相对路径在两侧都存在且内容不同时，规则如下：

| 优先级 | 规则 | 理由 |
| --- | --- | --- |
| 1 | **源仓为唯一真值源** | 领域模型、工具语义、学科数据只在源仓维护 |
| 2 | **同名文件一律由源覆盖**（`content-differs` → 复制） | 避免两处实现漂移；桌面端无法审查源变更 |
| 3 | **目标侧独有文件一律保留**（`target-only` → 仅报告） | 脚本不含任何删除操作，永不丢用户数据 |
| 4 | **禁止反向同步** | 桌面端改动必须先回源仓提交，再单向投影 |
| 5 | **桌面端特化只允许在 `core/` 之外** | 保证投影可被安全覆盖 |

第 3 条是刻意的不对称：覆盖有明确真值来源，删除没有。因此**删除源文件不会自动传播到桌面端**，
桌面端会残留一个 `target-only` 文件并在校验报告中列出，需人工确认后处置。

---

## 5. 一致性判定

- 判定方式：逐文件 **SHA-256** 摘要比对，不依赖 mtime、不依赖文本比较。
- 复制方式：`shutil.copy2`，保留 mtime，因此重复同步不会产生无谓差异。
- 状态枚举：

| 状态 | 含义 | `--apply` 行为 | `--check` 是否算漂移 |
| --- | --- | --- | --- |
| `identical` | 两侧 SHA-256 相同 | 不动 | 否 |
| `missing-in-target` | 目标侧没有该文件 | 复制 | **是** |
| `content-differs` | 两侧都有但摘要不同 | 覆盖复制 | **是** |
| `target-only` | 仅目标侧存在 | **不动**（只报告） | 否 |

「一致」的判定等价于：`missing-in-target` 与 `content-differs` 均为 0。
`target-only` 存在**不**破坏一致性判定 —— 它是设计允许的状态，不是漂移。

---

## 6. 脚本用法

脚本在两仓各存一份，**内容必须逐字节一致**，由 `scripts/sync_core.py` 承载。

```bash
# 预览差异（默认模式，不写任何文件）
python scripts/sync_core.py --dry-run

# 落盘同步
python scripts/sync_core.py --apply

# 只校验；发现漂移以退出码 1 结束（供 CI 判定）
python scripts/sync_core.py --check

# 机器可读输出
python scripts/sync_core.py --check --json

# 打印同步清单
python scripts/sync_core.py --list-manifest
```

显式指定路径（CI 与非标准布局用）：

```bash
python scripts/sync_core.py --check \
  --source   F:/opencode工坊/sciforge/sciforge \
  --target   F:/opencode工坊/sciforge-desktop/core
```

### 退出码

| 码 | 含义 |
| --- | --- |
| `0` | 正常结束；`--check` 下表示两侧一致 |
| `1` | `--check` 检出漂移 |
| `2` | 用法或环境错误（源根不存在、源与目标同路径、目标位于源内部等） |

### 安全护栏

- 默认 `--dry-run`：**不加参数绝不写盘**。
- 拒绝 `--source == --target`。
- 拒绝目标根位于源根内部（会把投影写回源仓）。
- 脚本不含 `subprocess` / `os.system` / `shutil.rmtree`，无任何删除路径。
- 仅使用 Python 标准库，Python 3.11+（实测本机为 3.14.6）。

---

## 7. 已知适配问题：绝对导入

**这是当前最大的落地障碍，必须在真正执行同步前处理。**

**2026-09-26 当次实测**：以文本匹配方式统计，源仓有 **482 处** `sciforge.` 绝对导入，
分布于 **320 个**文件（口径为 grep 文本匹配，含注释与字符串字面量，为上界估计）。

投影是**逐字节**复制，因此投影后的文件仍写着 `from sciforge.disciplines import ...`。
在桌面端的包布局（6 个平铺顶层包 `agent`/`api`/`cli`/`core`/`gui`/`sessions`）下，
这些导入**不会自动成立**。可选应对（按侵入性从低到高）：

| 方案 | 做法 | 代价 |
| --- | --- | --- |
| A. 桌面侧提供 `sciforge` 兼容包 | 在 `core/` 之外建 `sciforge` 包，转调 `core.*` | 需维护一层薄映射，但投影保持逐字节 |
| B. 桌面侧把 `core/` 放进 `sciforge` 命名空间 | 调整桌面包布局为 `sciforge_desktop.core` | 动桌面既有包名，破坏性最大 |
| C. 投影后批量改写导入 | 同步后跑一次导入重写 | 破坏「逐字节」前提，需引入改写步骤与校验 |

**本机制不做决定**：A/B/C 属架构选型，超出本文件范围。无论选哪个，
`sync_core.py` 的行为都不变 —— 它保证的是**字节一致**，导入可解析性由适配层负责。

---

## 8. 现状快照（2026-09-26 实测）

| 项 | 观测值 |
| --- | --- |
| 源包核心目录数 | 12 |
| 源包根层散文件（排除） | 4 |
| `disciplines/` 学科注册表 | 261 门 |
| `disciplines/` 目录下 `.py` 文件 | 264 个（多出的 3 个为 `__init__.py` 等包结构文件，非学科条目） |
| `science/` 连接器 | 46 个 / 7 个领域 |
| `research/` 目录下 `.py` 文件 | 29 个 |
| 桌面端 `core/` 内容 | 仅 1 个 `__init__.py`，3 行 docstring |
| 桌面端 `core/` 是否有可执行代码 | 无 |

`disciplines/` 的 264 与 261 是**两个不同口径**：前者是文件数，后者是 registry 条目数。
本仓 README 记载 `list_by_category()` 使用子串匹配，`"理学"` 会连带命中 `"管理学"`，
因此按门类统计时须用精确相等。本文件不对门类数量作断言。

### 文档漂移（与本机制无关，但已发现）

以下引用在 2026-09-26 的工作树中**不存在**，属既有 README 漂移，非本任务引入：

- 本仓 README 引用 `.github/workflows/ci.yml`，但本仓工作树**无 `.github/` 目录**。
- 本仓 README 引用 `docs/mcp-tools.md`、`docs/disciplines.md`、`docs/connectors.md` 等，
  但本仓 `docs/` 下当时**只有** `superpowers/`。
- 桌面端 README 引用 `docs/index.md`、`docs/desktop-core-relationship.md`、`.github/SUPPORT.md`，
  但桌面端工作树**无 `docs/` 目录**，`.github/` 下只有 `ISSUE_TEMPLATE/` 与 `pull_request_template.md`。

本任务新增的两份源仓文档与本文件，会使 `docs/architecture/` 成为本仓首个真实文档目录。

---

## 9. CI

工作流：`.github/workflows/core-consistency.yml`（本仓）。

它做两件事：

1. 校验本仓 `scripts/sync_core.py` 与桌面端同名文件是否**逐字节一致**（防两份副本漂移）。
2. 克隆桌面端到相邻目录，跑 `--check`，把漂移作为失败。

### 触发覆盖的实际限制（必须知情）

一个 GitHub Actions 工作流**只能响应本仓的事件**，无法订阅另一仓库的 push/PR。
因此在「只在源仓新建这一个工作流」的前提下：

| 仓库 | push / PR | 手动触发 |
| --- | --- | --- |
| `sciforge`（本仓） | ✅ 自动 | ✅ `workflow_dispatch` |
| `sciforge-desktop` | ❌ **不触发** | 需在本仓手动 `workflow_dispatch` |

桌面端事件要获得自动校验，必须在桌面端也放一份工作流；那超出本任务的文件范围，
因此此处**如实标注为已知缺口**而非假装覆盖。若将来允许扩展，桌面端工作流只需
`--check --source ../sciforge/sciforge --target core`，逻辑与本仓一致。

### 首次落地的预期结果

在真正执行 `--apply` 之前，桌面端 `core/` 仅有 1 个 stub 文件，
因此 CI 的 `--check` **必然报漂移并失败**：12 个目录下的源文件几乎全部为 `missing-in-target`，
`core/__init__.py` 为一条 `content-differs`。总量为数百个文件量级
（其中 `disciplines/` 单独贡献 264 个 `.py`；确切总数以脚本实际运行输出为准，本文不断言精确值）。
这是机制的**预期初始状态**，不是配置错误：CI 的作用正是让「桌面端还没投影」这件事可见。
完成首次 `--apply` 后 CI 转绿。

---

## 10. 明确不做

- 不做反向同步（桌面 → 源）。
- 不删除目标侧任何文件。
- 不同步依赖声明、不同步测试、不同步 `pyproject.toml`。
- 不改写投影内容的导入路径（见第 7 节，属架构选型）。
- 不提供 Git hooks、不自动提交、不自动推送。
- 不在文档中作永久性断言：一切数量与状态均带观测日期。
