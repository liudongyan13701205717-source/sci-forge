# 贡献指南

感谢你考虑为 **sci-forge** 贡献代码、文档、学科数据或连接器。

本文档说明如何参与。**提 issue 不需要遵守任何流程**；只有提交代码或文档改动时才需要。

---

## 目录

- [我能帮上什么忙](#我能帮上什么忙)
- [贡献方式对照](#贡献方式对照)
- [开发环境](#开发环境)
- [分支与提交规范](#分支与提交规范)
- [测试要求](#测试要求)
- [代码规范](#代码规范)
- [文档规范](#文档规范)
- [新增一门学科](#新增一门学科)
- [新增一个科学数据库连接器](#新增一个科学数据库连接器)
- [双仓同步约定](#双仓同步约定)
- [PR 流程](#pr-流程)
- [评审标准](#评审标准)
- [行为准则与安全](#行为准则与安全)

---

## 我能帮上什么忙

按大致优先级（这是**建议**而非承诺的排期）：

| 类别 | 具体机会 |
| --- | --- |
| 学科数据 | 校对已有 261 门学科的 `paper_types` / `key_venues` / `conventions`；补齐明显缺失的学科；统一 `tools` 命名 |
| 文档 | 翻译、术语统一、示例补充、链接修复 |
| 连接器 | 补齐 `science_fetch`（当前仅 `uniprot` 实现）；新增公开数据库连接器 |
| 功能 | 补 `list_disciplines` 的 `domain` 过滤、`citation_graph` 的多层展开 |
| 工程 | 覆盖率与静态类型门禁、`ruff` / `mypy` / `coverage` 配置 |
| 报告 | 复现失败案例、连接器返回字段与文档不符的 bug |

> 观测记录（盘点日期 2026-09-26）：学科 `tools` 字段当前有 597 个不同字符串，其中 504 个只出现 1 次，属于明显的命名碎片化；统一命名是欢迎的第一类贡献。

---

## 贡献方式对照

| 你想做的事 | 怎么做 |
| --- | --- |
| 报告 bug | [新建 issue](https://github.com/liudongyan13701205717-source/sci-forge/issues/new/choose)，选 Bug 报告模板 |
| 提功能需求 | 同上，选 Feature 请求模板 |
| 提问 / 讨论 | [Discussions](https://github.com/liudongyan13701205717-source/sci-forge/discussions)；**不要**用 issue 提问 |
| 报告安全漏洞 | **不要**开 issue，见 [SECURITY.md](./SECURITY.md) |
| 改代码 / 文档 | Fork → 分支 → PR，见下文 |
| 贡献学科数据 | 见 [新增一门学科](#新增一门学科) |
| 贡献连接器 | 见 [新增一个科学数据库连接器](#新增一个科学数据库连接器) |

---

## 开发环境

```bash
git clone https://github.com/liudongyan13701205717-source/sci-forge.git
cd sci-forge

# 建议用虚拟环境
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 完整开发依赖（含复现线数值依赖）
pip install -e ".[reproduce,dev]"

# 安装 ruff（CI 会用；当前不在 dev extras 内）
pip install ruff
```

要求 Python **≥ 3.10**；CI 覆盖 3.11 / 3.12 / 3.13。

---

## 分支与提交规范

### 分支命名

| 类型 | 格式 | 示例 |
| --- | --- | --- |
| 功能 | `feat/<简述>` | `feat/domain-filter` |
| 修复 | `fix/<简述>` | `fix/offline-connect-retry` |
| 文档 | `docs/<简述>` | `docs/translation-glossary` |
| 学科数据 | `discipline/<学科名>` | `discipline/hydrology` |
| 连接器 | `connector/<库名>` | `connector/fastpass` |
| 杂项 | `chore/<简述>` | `chore/ruff-config` |

分支名用小写与连字符，不要用中文。

### 提交信息

采用 [Conventional Commits](https://www.conventionalcommits.org/)：

```
<type>(<scope>): <简短说明>

<可选正文>

<可选脚注>
```

| type | 用途 |
| --- | --- |
| `feat` | 新功能 / 新工具 / 新连接器 / 新学科 |
| `fix` | 缺陷修复 |
| `docs` | 文档变更 |
| `test` | 测试 |
| `refactor` | 不改变行为的重构 |
| `perf` | 性能 |
| `chore` | 构建、依赖、配置 |
| `ci` | 工作流 |
| `build` | 构建配置 |

示例：

```
feat(discipline): add hydrology discipline

新增水文学科，含 3 种体裁结构、 reporting standards 路由
与 5 个优先数据库绑定。

fix(science): return empty result instead of raising in cnki connector

未配置 CNKI_API_URL 时抛异常会打断跨库联查，改为返回空结果。
```

---

## 测试要求

**所有 PR 都必须保持测试全绿。** 提交前本地跑一遍：

```bash
SCI_FORGE_OFFLINE=1 python -m pytest tests/ -q
```

要点：

- **必须设置 `SCI_FORGE_OFFLINE=1`。** 未设置时测试会尝试访问外部网络；CI 中该变量已在工作流级别导出。
- **不要让测试依赖真实网络。** 需要外部数据时用桩（stub）或 monkeypatch。
- **新增功能必须带测试。** 测试放在 `tests/`，命名 `test_<主题>.py`。
- **修 bug 必须先写会失败的测试。** 该测试在修复前失败、修复后通过，才算有效。
- **只收集不执行**（确认用例数量）：

  ```bash
  SCI_FORGE_OFFLINE=1 python -m pytest tests/ -q --collect-only
  ```

当前基线：26 个测试文件、268 个被收集的用例。

CI（`.github/workflows/ci.yml`）在 3.11 / 3.12 / 3.13 三个版本上跑 `ruff check` 与上述 pytest 命令。

---

## 代码规范

- 遵循现有文件风格，保持一致；不要在同一 PR 里做无关的重排或重命名。
- **注释写「为什么」，不写「是什么」**；代码本身已经说明的事情不要再注释一遍。
- 不要引入新的运行时依赖而不先开 issue 讨论。复现线额外依赖只放在 `reproduce` extra，不要放到基础依赖。
- 不要修改 `sciiforge/disciplines/contribution_forms.py` 里的 10 个固定产出形式取值——那是跨学科的稳定契约。
- 公开函数的 docstring 用英文（与代码库一致），用户文档用中文。

> 说明：本仓库的导入包名为 `sciforge`（不含连字符），发行包名为 `sci-forge`。

---

## 文档规范

- 用户文档放在 `docs/`，**以中文为主**。
- `README.md` 与 `README_EN.md` 必须**结构一一对应**：改动一侧时同步另一侧，包括标题层级与表格列数。
- 涉及会随时间变化的观测（网络可达性、服务可用性、版本兼容性、接口字段）时，**必须标注观测日期**，并用条件式表达，不要写永久性断言。
- 不要在文档里写「以后一直……」「总是……」「始终……」这类断言。

---

## 新增一门学科

学科 registry 是**声明式数据**，新增学科不需要改动发现机制。

1. 在 `sciforge/disciplines/` 下新增一个模块文件，例如 `hydrology.py`。
2. 在该文件中声明一个模块级 `Discipline` 实例：

   ```python
   from sciforge.disciplines.base import Discipline

   discipline = Discipline(
       name="hydrology",
       aliases=("水文科学", "水文学", "hydrological science", "hydrology"),
       paper_types={
           "research_article": ("abstract", "introduction", "methods",
                                "results", "discussion", "conclusions"),
           "review": ("abstract", "introduction", "literature_review",
                      "synthesis", "conclusions"),
       },
       citation_style="apa",
       reporting_standards={"quantitative": "other:xxxx"},
       conventions=(
           "以 SI 单位报告流量与水位",
           "水文站编号需在方法中完整给出",
       ),
       key_venues=("Water Resources Research", "Journal of Hydrology"),
       units_and_formulas_notes=("流量单位区分 m3/s 与 m3/d",),
       paper_capable=True,
       contribution_forms=("论文", "数据集"),
       tools=("R", "HydroRadar", "HEC-RAS"),
       category="工学",
       databases=("OpenAlex", "Crossref", "万方"),
   )
   ```

3. **在 PR 描述中给出计数增量**：`len(DISCIPLINES)` 从 N 变为 N+1，并说明依据。
4. `contribution_forms` 的取值必须来自固定的 10 个：论文、数据集、软件与代码、学术专著、专利、报告、艺术作品、文学作品、译文、教案与教材。
5. `category` 用中国学科门类命名：理学、工学、医学、交叉学科、法学、文学、哲学、管理学、艺术学、军事学、农学、历史学、教育学、经济学。
6. 提交前跑测试与 lint，并确认新学科可被检索到：

   ```bash
   python -c "from sciforge.disciplines import get_discipline; print(get_discipline('hydrology'))"
   ```

字段含义详见 [docs/disciplines.md](./docs/disciplines.md)。

---

## 新增一个科学数据库连接器

1. 在 `sciforge/science/sources/` 下新增模块，实现对应领域的连接器，声明其 id 与检索端点。
2. 在该领域包的注册入口（如 `literature/__init__.py`）里导入并登记。
3. 遵循既有约定：
   - **默认免 API key。** 需要鉴权时，把 key 做成可选环境变量，未配置时返回空结果而不是抛异常。
   - 保持返回字段结构与同领域其他连接器一致，否则跨库联查的聚合会失真。
   - 尊重上游服务的限流与使用条款。
4. 同步更新 [docs/connectors.md](./docs/connectors.md) 的领域表与计数。
5. 为新连接器补测试（至少覆盖「正常返回」与「未配置可选环境变量时返回空」两条路径）。

连接器详见 [docs/connectors.md](./docs/connectors.md)。

---

## 双仓同步约定

本仓库是 **MCP 版**（核心库 + server），与 `sciforge-desktop`（桌面版）构成双仓。

- **共享核心。** 学科 registry、连接器目录、工具语义、`.sci-forge` 存储布局由本仓定义，桌面版通过 MCP 消费，不复制实现。
- **默认一起改。** 凡是会改变**工具签名、工具语义、返回结构、学科字段、存储布局**的改动，**默认同时在两个仓库落地**。

PR 描述中请勾选对应项：

- [ ] 本改动不涉及 MCP 契约（可单仓合并）
- [ ] 本改动涉及 MCP 契约，已在 `sciforge-desktop` 同步（PR 链接：______）
- [ ] 本改动涉及 MCP 契约，待同步（阻塞合并，请勿勾选「可单仓合并」）

> 观测记录（盘点日期 2026-09-26）：两仓尚未建立代码级同步机制——桌面版 `pyproject.toml` 未声明对本仓的依赖，其 `core/` 目录为空占位。因此在机制落地前，「默认一起改」靠 PR 描述中的勾选与人工核对来保证。

---

## PR 流程

1. **先开 issue**（较大的改动）：说明意图与方案，避免白做。
2. **Fork 并建分支**，命名见[上文](#分支与提交规范)。
3. **改动 + 补测试 + 补文档**（含 README 双语同步）。
4. **本地自检**：

   ```bash
   ruff check .
   SCI_FORGE_OFFLINE=1 python -m pytest tests/ -q
   ```

5. **开 PR**，填写 [PR 模板](./.github/pull_request_template.md)。
6. **响应评审**：评审意见按技术判断处理；有异议时说明理由而不是直接照改。
7. 涉及 MCP 契约时，按[双仓约定](#双仓同步约定)同步桌面版。

---

## 评审标准

评审关注这几件事，按重要性排序：

1. **正确性**：逻辑对不对？边界条件处理了吗？
2. **测试**：有没有能真正抓住这个 bug 的测试？
3. **契约一致**：返回结构与既有工具是否兼容？破坏性变更需要在 PR 中显式声明。
4. **可维护性**：命名、注释、复杂度是否与代码库现状相当？
5. **文档**：README 双语是否同步？用户文档是否补齐？

不要求：个人偏好的写法、纯风格重排、大规模的无关重构。

---

## 行为准则与安全

- 参与讨论即表示同意 [行为准则（Contributor Covenant v2.1）](./CODE_OF_CONDUCT.md)。
- 发现安全漏洞请按 [安全策略](./SECURITY.md) 私下报告，**不要**开公开 issue。

---

## 许可

你的贡献将以 [Apache License 2.0](./LICENSE) 授权，与本项目保持一致。
