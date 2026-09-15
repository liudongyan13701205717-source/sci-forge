# Learnings — sciforge 全方位升级

## 环境与仓库
- 仓库根目录（新）：F:/opencode工坊/sciforge（已从 clawsgo 复制改名；editable 安装已指向新路径）
- 远程：https://github.com/liudongyan13701205717-source/sci-forge.git，HEAD=3f73f09
- Python: >=3.10（C:/Python314/python.exe），stdlib-first，依赖仅 mcp>=1.29.0；避免新增依赖除非必要
- bash 终端中文乱码是显示问题（codepage），不影响实际文件内容

## 代码约定（必须遵守）
- server.py 模式：工具用 @mcp.tool() 注册，函数体内 lazy import（from sciforge.xxx import impl）
- MCP 工具 docstring：中文描述 + Args 文档（与现有 28 个工具一致）；当前 28 工具全部有 description
- 模块布局：sciforge/<module>/，实现放子模块，api.py 做门面
- 测试：tests/ 目录，pytest，当前 140/140 通过，全部离线（SCI_FORGE_OFFLINE=1 兼容）
- 全量测试命令：python -m pytest tests/ -q（约 55s）
- 离线优先：新功能计算必须不依赖网络；联网能力走 sciforge/science/ 连接器的离线降级模式

## 探索结论（librarian 报告要点）
- 规范仓库：Imbad0202/academic-research-skills（47.8k★：deep-research/academic-paper/academic-paper-reviewer/academic-pipeline）+ K-Dense-AI/scientific-agent-skills（44.7k★：165 skills）
- 最大差距：多视角评审面板（7人制+动态人格卡+Devil's Advocate+编辑综合+校准 FNR/FPR）、claim→source 核验（locator anchors+完整性门）、PRISMA 系统综述（流程计数）、venue 写作模板、风格校准
- sciforge 已领先：论文复现五步闭环（canonical 仓库无此能力）

## 批次：新增 4 学科模块（2026-09-15）
- 新增 sciforge/disciplines/：public_health.py（CDC MMWR/NEJM/Lancet Public Health）、nursing.py（International Journal of Nursing Studies）、dentistry.py（JDR）、veterinary_science.py（JAVMA/AJVR），registry 零注册自动发现
- 每模块：中文 docstring + 8 个 Discipline 字段全填（5 paper_types / 5 conventions / 5 key_venues / 5 units notes）；reporting_standards 均含 case_series/cohort/case_control/randomized_trial 设计类型（public_health 另含 outbreak(CDC)/surveillance/economic_evaluation(CHEERS 2022)；nursing 另含 qualitative(COREQ/SRQR)/instrument_validation(COSMIN)/quality_improvement(SQUIRE 2.0)；dentistry 另含 diagnostic_accuracy(STARD)/in_vitro(ISO 4049/14801)；veterinary 另含 diagnostic_accuracy(STARD)/animal_research(ARRIVE 2.0)，RCT 用 REFLECT/CONSORT）
- 测试强化：tests/test_venue_disciplines.py 的 test_disciplines_registry_count 阈值 12→16 并加入 4 个新学科名；`python -m pytest tests/test_venue_disciplines.py -q` 15 passed，registry=16
- 纯 LOC：80-82/文件；未改 server.py、未加依赖、未联网
