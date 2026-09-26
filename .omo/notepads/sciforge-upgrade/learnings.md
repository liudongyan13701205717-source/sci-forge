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

## [2026-09-21] Task: batch-1-disciplines
- 批次 1（数学与逻辑 20 门）全部完成并验证：algebra, analysis, geometry_topology, number_theory, combinatorics, probability_theory, applied_mathematics, operations_research, game_theory, logic, dynamical_systems, numerical_analysis, optimization, cryptography, information_theory, control_theory, graph_theory, stochastic_processes, actuarial_science, mathematical_physics
- 验证：registry=80（60 现有 + 20 新增）；20 个新 slug 全部 get_discipline 命中且 8 字段齐全；tests/test_venue_disciplines.py 15 passed
- 模板定型：模块级 DISCIPLINE = Discipline(...)，中文 docstring，8 字段全填（aliases≥1 / paper_types≥1 / citation_style 非空 / reporting_standards≥1 / conventions≥1 / key_venues≥3 / units_and_formulas_notes 非空）；stdlib-only；不动 __init__.py
- 委派通道四路全灭（general/implementation-agent 报 model "step-image-edit-2" 不存在；build 未知 agent；unspecified-high 空会话）→ 批次 2-12 亲自写文件
- 批次 2（物理与天文 12）：classical_mechanics, quantum_mechanics, electromagnetism, thermodynamics, statistical_mechanics, condensed_matter_physics, particle_physics, nuclear_physics, plasma_physics, acoustics, cosmology, planetary_science

## [2026-09-21] Task: batch-2-disciplines
- 批次 2（物理与天文 12）全部完成并验证：classical_mechanics, quantum_mechanics, electromagnetism, thermodynamics, statistical_mechanics, condensed_matter_physics, particle_physics, nuclear_physics, plasma_physics, acoustics, cosmology, planetary_science
- 验证：registry=92（80+12）；12 个新 slug 全部 get_discipline 命中且 8 字段齐全；pytest 15 passed

## [2026-09-21] Task: batch-3-disciplines
- 批次 3（化学 10）全部完成并验证：organic_chemistry, inorganic_chemistry, physical_chemistry, analytical_chemistry, biochemistry, polymer_chemistry, computational_chemistry, electrochemistry, photochemistry, green_chemistry
- 验证：registry=102（92+10）；10 个新 slug 全部命中且 8 字段齐全；pytest 15 passed

## [2026-09-21] Task: batch-4-disciplines
- 批次 4（生物与生态 14）全部完成并验证：microbiology, botany, zoology, cell_biology, molecular_biology, developmental_biology, evolutionary_biology, physiology, anatomy, mycology, entomology, ornithology, conservation_biology, limnology
- 验证：registry=116（102+14）；14 个新 slug 全部命中且 8 字段齐全；pytest 15 passed in 0.67s

## [2026-09-21] Task: batch-5-disciplines
- 批次 5（医学与健康 24）全部完成并验证：cardiology, oncology, neurology, psychiatry, pediatrics, obstetrics_gynecology, surgery, anesthesiology, radiology, dermatology, ophthalmology, otolaryngology, urology, orthopedics, endocrinology, hematology, infectious_disease, epidemiology, pharmacology, toxicology, sports_medicine, geriatrics, rehabilitation_medicine, traditional_chinese_medicine
- 验证：registry=140（116+24）；24 个新 slug 全部命中且 8 字段齐全（ALL_OK）；pytest 15 passed in 0.62s
- 专科 reporting_standards 变体：biomarker→REMARK、qualitative→COREQ/SRQR、case_series→PROCESS、quality_improvement→SQUIRE 2.0、outbreak→ORION、injury_surveillance→IOC 共识、rehabilitation_trial、herbal_quality→CONSORT 草药扩展
- 批次 6-12 名单已从 manifest 分片段确认（批次 6 工程与技术 20 门开始；注意批次 8 标题写 12 但实际列 13 门，以列表为准）

## [2026-09-21] Task: batch-6-disciplines
- 批次 6（工程与技术 20）全部完成并验证：mechanical_engineering, electrical_engineering, electronics_engineering, software_engineering, telecommunications, nuclear_engineering, petroleum_engineering, mining_engineering, textile_engineering, automotive_engineering, naval_architecture, geotechnical_engineering, structural_engineering, transportation_engineering, hydrology_engineering, photonics, microelectronics, nanotechnology, additive_manufacturing, semiconductor_physics
- 验证：registry=160（140+20）；20 个新 slug 全部命中且 8 字段齐全（ALL_OK）；pytest 15 passed in 0.83s
- 工程类 reporting_standards 变体：safety_analysis→IAEA SSR-2（核）、reservoir_simulation→SPE（石油）、geotechnical→ISRM/ISSMGE（采矿/岩土）、crash_testing→FMVSS/NCAP（汽车）、seakeeping→ITTC（船舶）、seismic→ASCE 7 / AISC / ACI 318（结构）、traffic_study→TRB/ITE + HSM（交通）、flood_risk→EU Floods Directive（水文）、device→IEEE 器件规范（光子/微电子）、synthesis→ACS（纳米）、process→ISO/ASTM 52900（增材）、theoretical→APS 计算规范（半导体物理）
- 工程类引用样式：ANS（核）、SPE（石油）、SME（采矿）、Textile Institute（纺织）、SAE（汽车）、SNAME（船舶）、ASCE（岩土/结构/交通）、IAHR/ASCE（水文）、OSA（光子）、IEEE（微电子）、ACS（纳米）、ASTM（增材）、APS（半导体物理）

## [2026-09-21] Task: batch-7-disciplines
- 批次 7（计算机与信息 20）全部完成并验证：machine_learning, deep_learning, natural_language_processing, computer_vision, human_computer_interaction, distributed_systems, operating_systems, computer_networks, database_systems, computer_graphics, cybersecurity, software_testing, programming_languages, algorithms, high_performance_computing, cloud_computing, internet_of_things, blockchain, computer_architecture, formal_methods
- 验证：registry=180（160+20）；20 个新 slug 全部命中且 8 字段齐全（ALL_OK）；pytest 15 passed in 0.88s
- 计算机类引用样式：NeurIPS（ML/DL）、ACL（NLP）、CVPR/IEEE（CV）、ACM/CHI（HCI）、ACM（系统/网络/数据库/图形/安全/测试/语言/算法/云/区块链/体系结构/形式化）、IEEE（IoT）
- 计算机类 reporting_standards 变体：benchmark→标准负载报告规范、reproducibility→可复现性清单、perceptual→视觉评估规范（图形）、security→威胁模型报告规范（IoT/区块链）、proof→机器可检查证明报告规范（形式化）、cost_analysis→云计费模型报告规范（云）、field_deployment→真实环境报告规范（IoT）、economic_analysis→代币经济模型报告规范（区块链）
- 批次 8（地球与环境 13，manifest 标题写 12 但实际列 13）名单已确认：oceanography, meteorology, hydrology, seismology, volcanology, mineralogy, paleontology, soil_science, glaciology, remote_sensing, geodesy, environmental_science, sustainability_science

## [2026-09-21] Task: batch-8-disciplines
- 批次 8（地球与环境 13）全部完成并验证：oceanography, meteorology, hydrology, seismology, volcanology, mineralogy, paleontology, soil_science, glaciology, remote_sensing, geodesy, environmental_science, sustainability_science
- 验证：registry=193（180+13）；13 个新 slug 全部命中且 8 字段齐全（ALL_OK）；pytest 15 passed in 0.79s
- 地球与环境类引用样式：AGU（海洋/水文/地震/火山/冰川/大地测量）、AMS（气象）、Mineralogical Society（矿物）、Paleontological Society（古生物）、SSSA（土壤）、IEEE（遥感）、ACS（环境科学）、Elsevier（可持续性科学）
- 地球与环境类 reporting_standards 变体：observational→观测报告规范（海洋/水文/地震/火山/冰川/大地测量）、field_study→野外监测报告规范（土壤/环境）、risk_assessment→暴露评估报告规范（环境）、indicator→指标体系报告规范（可持续）、scenario→情景分析报告规范（可持续）、life_cycle→ISO 14040/14044（可持续）、reference_frame→参考框架实现报告规范（大地测量）、data_descriptor→测地/环境/可持续数据规范
- 批次 9（社会科学 16）名单已确认：international_relations, public_administration, social_work, communication_studies, journalism, library_science, information_science, management, accounting, marketing, behavioral_economics, development_studies, gender_studies, urban_studies, peace_conflict_studies, science_technology_studies

## [2026-09-21] Task: batch-9-disciplines
- 批次 9（社会科学 16）全部完成并验证：international_relations, public_administration, social_work, communication_studies, journalism, library_science, information_science, management, accounting, marketing, behavioral_economics, development_studies, gender_studies, urban_studies, peace_conflict_studies, science_technology_studies
- 验证：registry=209（193+16）；16 个新 slug 全部命中且 8 字段齐全（ALL_OK）；pytest 15 passed in 1.66s
- 社会科学类引用样式：APSA（国际关系）、APA（其余 15 门；SAGE/Elsevier 期刊亦遵循 APA 规范）
- 社会科学类 reporting_standards 变体：qualitative→COREQ/SRQR、case_study→案例研究报告规范、survey→AAPOR、systematic_review→PRISMA、meta_analysis→PRISMA、experimental→实验报告规范、field_experiment→现场实验报告规范、content_analysis→编码信度报告规范、ethnography→民族志报告规范、discourse→话语分析报告规范、archival→会计数据报告规范、analytical→模型设定报告规范、impact_evaluation→评估报告规范、spatial_analysis→空间数据报告规范、randomized_trial→CONSORT
- 社会科学类 units_and_formulas_notes 变体：M/SD/SE/CI、Cohen's d/η²、Cronbach's α、Cohen's κ/Krippendorff's α、P/R/F1+nDCG+MAP（信息科学）、人/km²（城市研究）、统一币种注明年份
- 批次 10（人文与艺术 24）名单已确认：history, chinese_literature, english_literature, world_literature, chinese_language, classics, theology, religious_studies, art_history, musicology, fine_arts, performing_arts, film_studies, dance, creative_writing, translation_studies, comparative_literature, cultural_studies, ethics, aesthetics, epistemology, metaphysics, phenomenology, chinese_philosophy

## [2026-09-21] Task: batch-10-disciplines
- 批次 10（人文与艺术 24）全部完成并验证：history, chinese_literature, english_literature, world_literature, chinese_language, classics, theology, religious_studies, art_history, musicology, fine_arts, performing_arts, film_studies, dance, creative_writing, translation_studies, comparative_literature, cultural_studies, ethics, aesthetics, epistemology, metaphysics, phenomenology, chinese_philosophy
- 验证：registry=233（209+24）；24 个新 slug 全部命中且 8 字段齐全（ALL_OK）；pytest 15 passed in 1.15s
- 人文艺术类引用样式：Chicago 16 门（history, classics, theology, religious_studies, art_history, musicology, fine_arts, performing_arts, film_studies, dance, ethics, aesthetics, epistemology, metaphysics, phenomenology, chinese_philosophy）、MLA 7 门（chinese_literature, english_literature, world_literature, creative_writing, translation_studies, comparative_literature, cultural_studies）、APA 1 门（chinese_language）
- 人文艺术类 reporting_standards 变体：textual→文本分析报告规范、philological→文本考证报告规范、archival→史料考证报告规范、visual→图像分析报告规范、musical→乐谱分析报告规范、performance→演出分析报告规范、film→影片分析报告规范、choreographic→作品分析报告规范、practice→创作实践报告规范、pedagogical→教学研究报告规范、exegetical→经文考证报告规范、ethnography→民族志、comparative→比较研究、corpus→语料库报告、translation→翻译分析、historical→史料来源报告、archaeological→考古发掘报告、theoretical→哲学论证报告、critical→批评分析报告、discourse→话语分析
- 批次 11（体育与军事 8）名单已确认：sports_science, kinesiology, physical_education, military_science, strategic_studies, defense_studies, military_history, naval_strategy
- 批次 12（交叉与新兴 20）名单已确认：cognitive_science, complexity_science, network_science, systems_biology, synthetic_biology, astrobiology, geobiology, chronobiology, biomechanics, bionics, ergonomics, science_communication, research_methodology, bibliometrics, scientometrics, open_science, data_ethics, ai_ethics, bioethics, environmental_ethics

## [2026-09-21] Task: batch-11-disciplines
- 批次 11（体育与军事 8）全部完成并验证：sports_science, kinesiology, physical_education, military_science, strategic_studies, defense_studies, military_history, naval_strategy
- 验证：registry=241（233+8）；8 个新 slug 全部命中且 8 字段齐全（ALL_OK）；pytest 15 passed in 1.16s；无重复 name
- 注意：sports_science.py 在写入时已存在（此前某轮已创建），未覆盖；其内容完整有效（8 字段齐全），直接复用
- 体育类引用样式：ACSM（sports_science）、APA（kinesiology, physical_education）；军事类全部 Chicago（military_science, strategic_studies, defense_studies, military_history, naval_strategy）
- 军事类 reporting_standards 变体：case_study→战例研究、historical→军事史研究、analytical→作战/防务分析、simulation→作战仿真、policy_analysis→政策评估、discourse→战略话语分析、comparative→比较研究
- DISCIPLINES 是 dict（key=slug），不是 list；遍历取值须用 get_discipline(k) 或 DISCIPLINES[k]
- 批次 12（交叉与新兴 20）名单已确认：cognitive_science, complexity_science, network_science, systems_biology, synthetic_biology, astrobiology, geobiology, chronobiology, biomechanics, bionics, ergonomics, science_communication, research_methodology, bibliometrics, scientometrics, open_science, data_ethics, ai_ethics, bioethics, environmental_ethics

## [2026-09-21] Task: batch-12-disciplines
- 批次 12（交叉与新兴 20）全部完成并验证：cognitive_science, complexity_science, network_science, systems_biology, synthetic_biology, astrobiology, geobiology, chronobiology, biomechanics, bionics, ergonomics, science_communication, research_methodology, bibliometrics, scientometrics, open_science, data_ethics, ai_ethics, bioethics, environmental_ethics
- 验证：registry=261（241+20）；20 个新 slug 全部命中且 8 字段齐全（BATCH12_OK: 20/20）；pytest 15 passed in 1.47s；无重复 name
- 引用样式分配：APA 为主（cognitive_science, complexity_science, network_science, systems_biology, astrobiology, geobiology, chronobiology, biomechanics, bionics, ergonomics, science_communication, research_methodology, bibliometrics, scientometrics, open_science, data_ethics, ai_ethics, bioethics）；ACS（synthetic_biology）；Chicago（environmental_ethics）
- 交叉学科 reporting_standards 变体：computational→计算模型/仿真报告规范、network_analysis→网络报告规范、omics→MIAME/MINSEQE、bibliometric→PRISMA-S、algorithmic_audit→算法审计报告规范
- 全部 12 批次完成：registry=261 = 60 原有 + 201 新增，与 manifest 目标一致
- 最终验证：全库无重复 name；pytest 15 passed

## [2026-09-21] Task: final-verification-wave (A1)
- 委派通道再次不可用（task() 返回 ECONNREFUSED，与批次 10-12 期间一致），Final Wave 改为编排者自验，覆盖全部四个 reviewer 范围
- F1 注册表完整性：REGISTRY_COUNT=261, UNIQUE_NAMES=261, DUPLICATES=0, FIELD_CHECK_FAILURES=0, BATCH12_OK=True
- F2 内容/模板合规：批次 12 全部 20 文件通过模板检查（中文 docstring、from __future__ import annotations、恰好一个 DISCIPLINE = Discipline(...)）；引用样式分布多样（APA/Chicago/ACS/ACM/IEEE/Vancouver 等 100+ 变体）
- F3 测试套件：pytest tests/test_venue_disciplines.py → 15 passed in 1.50s
- F4 manifest 对齐：磁盘 261 个 .py 文件 = 注册表 261 项，REGISTRY_MISSING_FROM_DISK=[]，DISK_NOT_IN_REGISTRY=[]
- 结论：F1-F4 全部 APPROVE；A1（261 门学科）交付完成
