# sci-forge 文档

本目录是 **sci-forge** 面向用户的文档。内容以中文为主；仓库根目录另有完整对应的英文 README（[README_EN.md](../README_EN.md)）。

---

## 从这里开始

| 你现在的处境 | 读这一篇 |
| --- | --- |
| 第一次接触，想知道它能做什么 | [README.md](../README.md)，然后看 [快速开始](quickstart.md) |
| 准备安装 / 装不上 | [安装](installation.md) |
| 想跑通一次完整流程 | [快速开始](quickstart.md) |
| 想知道有哪些工具、参数怎么填 | [MCP 工具清单](mcp-tools.md) |
| 想知道支持哪些学科、字段含义 | [学科体系](disciplines.md) |
| 想知道能查哪些科学数据库 | [科学数据连接器](connectors.md) |
| 想提交代码 | [CONTRIBUTING.md](../CONTRIBUTING.md) |
| 发现了安全问题 | [SECURITY.md](../SECURITY.md) |
| 想知道某个版本改了什么 | [CHANGELOG.md](../CHANGELOG.md) |

---

## 文档地图

```
docs/
├── index.md         ← 你在这里：文档入口与导航
├── installation.md  ← 安装、extras、MCP 客户端注册、安装故障排查
├── quickstart.md    ← 从零到产出一篇文档的端到端流程
├── mcp-tools.md     ← 65 个 MCP 工具 + 2 个资源，按线分组，含参数与行为
├── disciplines.md   ← 学科 registry：字段体系、查询 API、统计口径、扩编指引
└── connectors.md    ← 46 个科学数据连接器 / 7 领域，逐库说明
```

> `docs/superpowers/` 是历史保留目录，不属于本套用户文档。

---

## 六条能力线

sci-forge 的 65 个工具按职责分成六条线。完整参数见 [MCP 工具清单](mcp-tools.md)。

| 线 | 工具数 | 入口工具 | 解决的问题 |
| --- | --- | --- | --- |
| 复现 | 2 | `reproduce_paper` | 从一篇 PDF 到可运行的复现结果与交付物 |
| 写作 | 2 | `write_section` | 按学科规范生成章节，并导出为 PDF / DOCX（LaTeX 源始终生成） |
| 研究 | 3 | `ideate_paper` | 从选题到研究缺口、假设与实验计划 |
| 科研 / 论文 | 35 | `research_plan` | 计划、综述、润色、引文、统计、代码关联 |
| 评审核验 | 10（含 3 个别名） | `run_panel` | 模拟评审、主张核验、完整性门、Material Passport（fail-closed） |
| 交付 | 2 | `package_submission` | 投稿材料打包与清单 |
| 科学数据 | 5 | `science_search` | 46 个公开科学数据库的检索与跨库联查 |
| 期刊匹配与学科 | 3 | `journal_fit` / `list_disciplines` | 期刊匹配度评分与学科 registry 查询 |
| **合计** | **65** | | |

---

## 三个贯穿全局的概念

理解这三个概念，就能理解整个工具面为什么这样设计。

### 1. 免 API key 可用，LLM 是可选增强

核心链路（文献检索、DOI 核验、元数据、引文图谱）走 OpenAlex / Crossref 的公开接口，不需要任何 key。

文本生成类工具（`ideate_paper`、`write_section`、`peer_review`、`venue_suggest` 等）在**未配置** LLM 端点时自动回退到本地模板与规则引擎，功能保持可用，只是文本自然度下降。配置方式见 [快速开始 · 可选增强](quickstart.md#可选增强llm)。

### 2. fail-closed

评审准入门（`validate_review_intake`）、完整性门（`gate_2_5` / `gate_4_5`）与豁免审批（`request_bypass`）遵循同一原则：**证据不足即拒绝**，而不是「尽量放行」。

这意味着你会看到工具返回 `gate_refuse` 类的拒绝结果——那是设计行为，不是故障。

### 3. 声明式学科知识

`sciforge/disciplines/` 里的 261 门学科是**数据**不是逻辑。新增一门学科 = 新增一个模块文件，发现机制自动收录，无需改动 registry 代码。详见 [学科体系](disciplines.md)。

---

## 存储位置

所有运行产物落在工作区根目录的 `.sci-forge/` 下（已 gitignore）：

```
.sci-forge/
├── env                     # 可选 LLM 端点配置，不提交
├── projects/{paper_id}/    # doc.md / doc.tex / doc.html / doc.pdf、sections/、research/
└── tasks/{task_id}/        # parse/、code/、runs/、deliverables/
```

---

## 与桌面版的关系

本仓库是 **MCP 版**（核心库 + server），与并列的 `sciforge-desktop`（PySide6 客户端）构成双仓。

**MCP 版与桌面版共享核心、默认一起改。** 凡涉及工具签名、工具语义、返回结构、学科字段或存储布局的改动，默认需在两个仓库一起落地。详见 [README.md · 与桌面版的关系](../README.md#与桌面版的关系双仓) 与 [CONTRIBUTING.md · 双仓同步约定](../CONTRIBUTING.md#双仓同步约定)。

---

## 约定说明

- 涉及会随时间变化的观测（网络可达性、接口字段、版本兼容性）时，本套文档均标注**观测日期**并用条件式表达。
- 本项目为独立开发的教育 / 研究工作，与 SciForge 官方站点、API、商标无关联；仅通过公开接口访问外部数据。

---

## 许可

文档与代码同受 [Apache License 2.0](../LICENSE) 约束 — Copyright 2026 liudongyan13701205717。
