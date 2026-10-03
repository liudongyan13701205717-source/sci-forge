# 学科体系（261 门）

> 本文档记录  下所有 261 门学科的完整 v2 字段配置。
> 每门学科是一个 Python 模块，声明一个  数据类实例。

## 门类分布

| 门类 | 学科数 |
| --- | --- |
| 理学 | 87 |
| 工学 | 56 |
| 医学 | 30 |
| 交叉学科 | 23 |
| 法学 | 12 |
| 文学 | 11 |
| 哲学 | 9 |
| 管理学 | 7 |
| 艺术学 | 6 |
| 军事学 | 5 |
| 农学 | 4 |
| 历史学 | 4 |
| 教育学 | 4 |
| 经济学 | 3 |
| **合计** | **261** |

## 学科明细

| # | 学科名 | 别名（前5） | 门类 | 产出形式 | 工具数 | 数据库数 | 体裁数 | 论文主导 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | accounting | accounting, 会计学, 财务会计, 审计学 | 管理学 | 论文, 报告 | 5 | 5 | 3 | 是 |
| 2 | acoustics | acoustics, 声学, 声学工程, acoustical engineering, 超声 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 3 | actuarial_science | actuarial science, 精算, 精算学, 保险数学, actuarial | 理学 | 论文, 报告 | 4 | 4 | 3 | 是 |
| 4 | additive_manufacturing | additive_manufacturing, 增材制造, 3D打印, 3D 打印, 快速成型 | 工学 | 论文, 专利 | 5 | 4 | 3 | 是 |
| 5 | aerospace_engineering | aerospace, aeronautics, astronautics, 航空航天工程, 航空工程 | 工学 | 论文, 专利 | 4 | 3 | 3 | 是 |
| 6 | aesthetics | aesthetics, 美学, 审美学, 艺术哲学 | 哲学 | 论文, 学术专著 | 4 | 4 | 3 | 是 |
| 7 | agriculture | agriculture, agronomy, crop, soil, farming | 农学 | 论文 | 5 | 4 | 3 | 是 |
| 8 | ai_ethics | ai_ethics, 人工智能伦理, AI 伦理, 负责任 AI, AI ethics | 交叉学科 | 论文, 学术专著 | 3 | 5 | 3 | 是 |
| 9 | algebra | algebra, 代数, 群论, 环论, 域论 | 理学 | 论文 | 4 | 3 | 3 | 是 |
| 10 | algorithms | algorithms, 算法, 算法设计与分析, 计算复杂性 | 工学 | 论文, 软件与代码 | 4 | 4 | 3 | 是 |
| 11 | analysis | analysis, 分析, 实分析, 复分析, 泛函分析 | 理学 | 论文 | 4 | 3 | 3 | 是 |
| 12 | analytical_chemistry | analytical chemistry, 分析化学, 分离科学, separation science, 色谱 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 13 | anatomy | anatomy, 解剖学, 人体解剖学, human anatomy, 形态学 | 理学 | 论文 | 5 | 3 | 3 | 是 |
| 14 | anesthesiology | anesthesiology, 麻醉学, 麻醉, 围术期医学, perioperative medicine | 医学 | 论文 | 6 | 4 | 3 | 是 |
| 15 | anthropology | anthropology, ethnography, 人类学, 民族志, 田野 | 法学 | 论文, 学术专著 | 5 | 4 | 3 | 是 |
| 16 | applied_mathematics | applied mathematics, 应用数学, 应用分析, 数学建模, applied math | 理学 | 论文, 软件与代码 | 3 | 3 | 3 | 是 |
| 17 | archaeology | archaeology, archeology, 考古学, 考古 | 历史学 | 论文, 学术专著 | 5 | 4 | 3 | 是 |
| 18 | architecture | architecture, building, built environment, 建筑学, 建筑 | 工学 | 论文, 艺术作品 | 4 | 3 | 3 | 是 |
| 19 | art_history | art_history, 艺术史, 美术史, 艺术史学 | 艺术学 | 论文, 学术专著, 艺术作品 | 3 | 4 | 3 | 是 |
| 20 | artificial_intelligence | artificial_intelligence, AI, machine_learning, 深度学习, 人工智能 | 工学 | 论文, 软件与代码 | 4 | 3 | 3 | 是 |
| 21 | astrobiology | astrobiology, 天体生物学, 地外生命, 宜居性研究, astrobiology | 交叉学科 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 22 | astrophysics | astrophysics, astronomy, cosmology, astro, stars | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 23 | atmospheric_science | atmospheric_science, meteorology, climatology, 大气科学, 气象学 | 理学 | 论文 | 5 | 5 | 3 | 是 |
| 24 | automotive_engineering | automotive_engineering, 汽车工程, 汽车, 车辆工程, 整车开发 | 工学 | 论文, 专利 | 4 | 4 | 3 | 是 |
| 25 | behavioral_economics | behavioral_economics, 行为经济学, 行为金融, 实验经济学 | 经济学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 26 | bibliometrics | bibliometrics, 文献计量学, 引文分析, 文献计量, bibliometric analysis | 交叉学科 | 论文, 软件与代码, 数据集 | 3 | 4 | 3 | 是 |
| 27 | biochemistry | biochemistry, 生物化学, 酶学, enzymology, 蛋白质化学 | 理学 | 论文, 数据集, 专利 | 5 | 6 | 3 | 是 |
| 28 | bioethics | bioethics, 生命伦理, 医学伦理, 生物伦理, bioethics | 交叉学科 | 论文, 学术专著 | 3 | 4 | 3 | 是 |
| 29 | bioinformatics | bioinformatics, genomics, transcriptomics, omics, 生物信息 | 理学 | 论文, 软件与代码, 数据集 | 4 | 4 | 3 | 是 |
| 30 | biology | biology, 生物, 细胞, cell biology, 遗传 | 理学 | 论文 | 4 | 4 | 3 | 是 |
| 31 | biomechanics | biomechanics, 生物力学, 人体力学, 运动生物力学, biomechanics | 交叉学科 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 32 | biomedical_engineering | biomedical_engineering, BME, 生物医学工程, 生物工程 | 工学 | 论文, 专利 | 4 | 3 | 3 | 是 |
| 33 | bionics | bionics, 仿生学, 仿生设计, 生物启发工程, biomimetics | 交叉学科 | 论文, 专利 | 3 | 4 | 3 | 是 |
| 34 | biotechnology | biotechnology, biotech, 生物技术, 生物工程 | 理学 | 论文, 专利 | 4 | 4 | 3 | 是 |
| 35 | blockchain | blockchain, 区块链, 分布式账本, 智能合约 | 工学 | 论文, 软件与代码 | 4 | 3 | 3 | 是 |
| 36 | botany | botany, 植物学, 植物生理学, plant physiology, 植物分类学 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 37 | business | management, business, strategy, 管理学, 工商管理 | 管理学 | 论文, 报告 | 4 | 4 | 3 | 是 |
| 38 | cardiology | cardiology, 心脏病学, 心血管病学, 心血管内科, 心血管医学 | 医学 | 论文, 数据集 | 6 | 5 | 3 | 是 |
| 39 | cell_biology | cell biology, 细胞生物学, 细胞信号, cell signaling, 细胞周期 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 40 | chemical_engineering | chemical engineering, process, reactors, separation, catalysis | 工学 | 论文, 专利 | 4 | 3 | 3 | 是 |
| 41 | chemistry | chemistry, 化学, 有机, organic, 催化 | 理学 | 论文 | 5 | 5 | 3 | 是 |
| 42 | chinese_language | chinese_language, 中国语言学, 汉语语言学, 汉语言文字学 | 文学 | 论文, 学术专著 | 4 | 4 | 3 | 是 |
| 43 | chinese_literature | chinese_literature, 中国文学, 中国现当代文学, 中国古代文学 | 文学 | 论文, 学术专著, 文学作品 | 3 | 4 | 3 | 是 |
| 44 | chinese_philosophy | chinese_philosophy, 中国哲学, 中国思想史, 国学 | 哲学 | 论文, 学术专著, 译文 | 4 | 4 | 3 | 是 |
| 45 | chronobiology | chronobiology, 时间生物学, 生物节律, 昼夜节律, chronobiology | 交叉学科 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 46 | civil_engineering | civil, structural, bridge, geotechnical, construction | 工学 | 论文 | 4 | 3 | 3 | 是 |
| 47 | classical_mechanics | classical mechanics, 经典力学, 分析力学, analytical mechanics, 刚体动力学 | 理学 | 论文 | 3 | 3 | 3 | 是 |
| 48 | classics | classics, 古典学, 古典语文学, 古希腊罗马研究 | 历史学 | 论文, 学术专著, 译文 | 4 | 4 | 3 | 是 |
| 49 | climatology | climate, meteorology, oceanography, 气候, 大气科学 | 理学 | 论文 | 5 | 5 | 3 | 是 |
| 50 | cloud_computing | cloud_computing, 云计算, 云原生, serverless | 工学 | 论文, 软件与代码 | 3 | 3 | 3 | 是 |
| 51 | cognitive_science | cognitive_science, 认知科学, 认知研究, 心智科学, cognitive science | 交叉学科 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 52 | combinatorics | combinatorics, 组合, 组合数学, 极值组合, 代数组合 | 理学 | 论文 | 3 | 3 | 3 | 是 |
| 53 | communication_studies | communication_studies, 传播学, 传播研究, 媒介研究 | 文学 | 论文, 报告 | 5 | 5 | 3 | 是 |
| 54 | comparative_literature | comparative_literature, 比较文学, 跨文化文学研究, 影响研究 | 文学 | 论文, 学术专著, 文学作品 | 5 | 4 | 3 | 是 |
| 55 | complexity_science | complexity_science, 复杂性科学, 复杂系统, 复杂性研究, complex systems | 交叉学科 | 论文, 软件与代码 | 4 | 4 | 3 | 是 |
| 56 | computational_chemistry | computational chemistry, 计算化学, 分子模拟, molecular simulation, 电子结构计算 | 理学 | 论文, 软件与代码, 数据集 | 5 | 5 | 3 | 是 |
| 57 | computational_mathematics | numerical, scientific computing, 数值分析, 偏微分方程, pde | 理学 | 论文, 软件与代码 | 5 | 5 | 3 | 是 |
| 58 | computer_architecture | computer_architecture, 计算机体系结构, 微架构, 处理器设计 | 工学 | 论文, 软件与代码, 专利 | 4 | 3 | 3 | 是 |
| 59 | computer_graphics | computer_graphics, 计算机图形学, 图形学, 渲染 | 工学 | 论文, 软件与代码 | 4 | 4 | 3 | 是 |
| 60 | computer_networks | computer_networks, 计算机网络, 网络, 网络协议 | 工学 | 论文, 软件与代码, 专利 | 4 | 5 | 3 | 是 |
| 61 | computer_science | computer science, 计算机, 机器学习, machine learning, 深度学习 | 工学 | 论文, 软件与代码 | 5 | 3 | 3 | 是 |
| 62 | computer_vision | computer_vision, 计算机视觉, CV, 图像理解, 视觉计算 | 工学 | 论文, 软件与代码, 数据集 | 4 | 5 | 3 | 是 |
| 63 | condensed_matter_physics | condensed matter physics, 凝聚态物理, 固体物理, solid state physics, 材料物理 | 理学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 64 | conservation_biology | conservation biology, 保护生物学, 物种保护, species conservation, 保护规划 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 65 | control_theory | control theory, 控制理论, 控制, 自动控制, 系统与控制 | 理学 | 论文, 软件与代码 | 4 | 3 | 3 | 是 |
| 66 | cosmology | cosmology, 宇宙学, 物理宇宙学, physical cosmology, 宇宙微波背景 | 理学 | 论文, 数据集 | 4 | 5 | 3 | 是 |
| 67 | creative_writing | creative_writing, 创意写作, 创作学, 写作学 | 文学 | 论文, 文学作品 | 5 | 4 | 3 | 是 |
| 68 | criminology | criminology, criminal_justice, 犯罪学, 刑事司法 | 法学 | 论文, 报告 | 5 | 4 | 3 | 是 |
| 69 | cryptography | cryptography, 密码学, 密码, 密码分析, crypto | 理学 | 论文, 软件与代码 | 5 | 3 | 3 | 是 |
| 70 | cultural_studies | cultural_studies, 文化研究, 文化批评, 大众文化研究 | 文学 | 论文, 学术专著 | 5 | 4 | 3 | 是 |
| 71 | cybersecurity | cybersecurity, 网络安全, 信息安全, 安全, 密码学应用 | 工学 | 论文, 软件与代码 | 4 | 4 | 3 | 是 |
| 72 | dance | dance, 舞蹈学, 舞蹈研究, 编舞学 | 艺术学 | 论文, 艺术作品 | 3 | 4 | 3 | 是 |
| 73 | data_ethics | data_ethics, 数据伦理, 数据治理, 数据隐私, data ethics | 交叉学科 | 论文, 学术专著 | 3 | 4 | 3 | 是 |
| 74 | data_science | data_science, data_analytics, 数据科学, 数据分析 | 工学 | 论文, 软件与代码, 数据集 | 4 | 3 | 3 | 是 |
| 75 | database_systems | database_systems, 数据库系统, 数据库, 数据管理 | 工学 | 论文, 软件与代码 | 4 | 4 | 3 | 是 |
| 76 | deep_learning | deep_learning, 深度学习, 神经网络, 深度神经网络, DNN | 工学 | 论文, 软件与代码, 数据集 | 4 | 5 | 3 | 是 |
| 77 | defense_studies | defense_studies, 国防研究, 防务研究, 国防政策, defence studies | 军事学 | 论文, 学术专著, 报告 | 4 | 4 | 3 | 是 |
| 78 | demography | demography, demographics, 人口学, 人口统计学 | 法学 | 论文, 报告 | 5 | 4 | 3 | 是 |
| 79 | dentistry | dentistry, 口腔医学, 口腔, 牙科, dental | 医学 | 论文 | 5 | 3 | 5 | 是 |
| 80 | dermatology | dermatology, 皮肤病学, 皮肤科, 皮肤性病学, dermatology clinical | 医学 | 论文 | 4 | 4 | 3 | 是 |
| 81 | development_studies | development_studies, 发展研究, 发展经济学, 国际发展 | 法学 | 论文, 报告 | 5 | 5 | 3 | 是 |
| 82 | developmental_biology | developmental biology, 发育生物学, 胚胎学, embryology, 模式形成 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 83 | distributed_systems | distributed_systems, 分布式系统, 分布式计算, 分布式 | 工学 | 论文, 软件与代码 | 4 | 4 | 3 | 是 |
| 84 | dynamical_systems | dynamical systems, 动力系统, 遍历理论, 混沌, ergodic theory | 理学 | 论文, 软件与代码 | 4 | 3 | 3 | 是 |
| 85 | earth_science | earth_science, geosciences, 地球科学, 地学 | 理学 | 论文 | 5 | 5 | 3 | 是 |
| 86 | ecology | ecology, conservation, biodiversity, population, community | 理学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 87 | economics | economics, 经济学, 计量, econometrics, 金融 | 经济学 | 论文, 报告 | 4 | 3 | 3 | 是 |
| 88 | education | education, 教育学, 教学, learning, pedagogy | 教育学 | 论文, 报告, 教案与教材 | 5 | 4 | 3 | 是 |
| 89 | electrical_engineering | electrical_engineering, 电气工程, 电气, 电力系统, 电力电子 | 工学 | 论文, 专利 | 4 | 4 | 3 | 是 |
| 90 | electrochemistry | electrochemistry, 电化学, 电分析, electroanalysis, 电催化 | 理学 | 论文, 数据集, 专利 | 5 | 5 | 3 | 是 |
| 91 | electromagnetism | electromagnetism, 电磁学, 电动力学, electrodynamics, 电磁场理论 | 理学 | 论文 | 3 | 3 | 3 | 是 |
| 92 | electronics_engineering | electronics_engineering, 电子工程, 电子, 集成电路, 电路设计 | 工学 | 论文, 专利, 软件与代码 | 4 | 4 | 3 | 是 |
| 93 | endocrinology | endocrinology, 内分泌学, 内分泌科, 代谢病学, metabolism | 医学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 94 | energy_engineering | energy, power, renewable, solar, wind | 工学 | 论文, 专利 | 3 | 3 | 3 | 是 |
| 95 | engineering | engineering, 工程, 机械, mechanical, 控制 | 工学 | 论文 | 4 | 3 | 3 | 是 |
| 96 | english_literature | english_literature, 英语文学, 英国文学, 美国文学 | 文学 | 论文, 学术专著, 文学作品 | 4 | 4 | 3 | 是 |
| 97 | entomology | entomology, 昆虫学, 昆虫分类学, insect taxonomy, 昆虫生态学 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 98 | environmental_engineering | environmental, environmental engineering, 水处理, 给水排水, 污染控制 | 工学 | 论文, 专利 | 3 | 3 | 3 | 是 |
| 99 | environmental_ethics | environmental_ethics, 环境伦理, 生态伦理, 环境哲学, environmental ethics | 交叉学科 | 论文, 学术专著 | 3 | 5 | 3 | 是 |
| 100 | environmental_science | environmental_science, 环境科学, 环境工程, 污染控制 | 理学 | 论文, 数据集, 报告 | 6 | 5 | 3 | 是 |
| 101 | epidemiology | epidemiology, 流行病学, 疾病流行病学, 临床流行病学, clinical epidemiology | 医学 | 论文, 数据集, 报告 | 5 | 5 | 3 | 是 |
| 102 | epistemology | epistemology, 认识论, 知识论, 知识哲学 | 哲学 | 论文, 学术专著 | 4 | 4 | 3 | 是 |
| 103 | ergonomics | ergonomics, 人机工效学, 人因工程, 工效学, human factors | 交叉学科 | 论文, 数据集 | 3 | 4 | 3 | 是 |
| 104 | ethics | ethics, 伦理学, 道德哲学, 应用伦理学 | 哲学 | 论文, 学术专著 | 4 | 4 | 3 | 是 |
| 105 | evolutionary_biology | evolutionary biology, 进化生物学, 系统发育, phylogenetics, 群体遗传学 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 106 | film_studies | film_studies, 电影学, 电影研究, 影视研究 | 艺术学 | 论文, 艺术作品 | 2 | 4 | 3 | 是 |
| 107 | finance | finance, asset pricing, corporate finance, 金融学, 金融 | 经济学 | 论文, 报告 | 4 | 3 | 3 | 是 |
| 108 | fine_arts | fine_arts, 美术, 造型艺术, 视觉艺术 | 艺术学 | 论文, 艺术作品 | 2 | 4 | 3 | 是 |
| 109 | food_science | food_science, food_technology, 食品科学, 食品工程 | 工学 | 论文, 专利 | 4 | 4 | 3 | 是 |
| 110 | forestry | forestry, forest_science, 林学, 林业科学 | 农学 | 论文 | 5 | 4 | 3 | 是 |
| 111 | formal_methods | formal_methods, 形式化方法, 形式验证, 模型检测 | 工学 | 论文, 软件与代码 | 3 | 3 | 3 | 是 |
| 112 | game_theory | game theory, 博弈论, 博弈, 机制设计, mechanism design | 理学 | 论文 | 3 | 3 | 3 | 是 |
| 113 | gender_studies | gender_studies, 性别研究, 女性研究, 女性主义研究 | 法学 | 论文, 学术专著 | 5 | 5 | 3 | 是 |
| 114 | genetics | genetics, 遗传学, 基因组学, genomics | 理学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 115 | geobiology | geobiology, 地球生物学, 生物地球化学, 地质微生物学, geobiology | 交叉学科 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 116 | geodesy | geodesy, 大地测量学, GNSS, 测量学 | 理学 | 论文, 数据集 | 6 | 5 | 3 | 是 |
| 117 | geography | geography, geosciences, 地理学, 地理科学 | 理学 | 论文 | 4 | 4 | 3 | 是 |
| 118 | geology | geology, geophysics, petrology, geochemistry, tectonics | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 119 | geometry_topology | geometry, topology, 几何, 拓扑, 微分几何 | 理学 | 论文 | 3 | 3 | 3 | 是 |
| 120 | geotechnical_engineering | geotechnical_engineering, 岩土工程, 岩土, 土力学, 基础工程 | 工学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 121 | geriatrics | geriatrics, 老年医学, 老年科, 老年病学, geriatric medicine | 医学 | 论文, 数据集 | 3 | 4 | 3 | 是 |
| 122 | glaciology | glaciology, 冰川学, 冰川, 冰盖 | 理学 | 论文, 数据集 | 6 | 5 | 3 | 是 |
| 123 | graph_theory | graph theory, 图论, 图, 网络科学, graph | 理学 | 论文, 软件与代码 | 4 | 4 | 3 | 是 |
| 124 | green_chemistry | green chemistry, 绿色化学, 可持续化学, sustainable chemistry, 绿色合成 | 理学 | 论文, 专利 | 5 | 5 | 3 | 是 |
| 125 | hematology | hematology, 血液学, 血液科, 血液病学, haematology | 医学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 126 | high_performance_computing | high_performance_computing, 高性能计算, HPC, 并行计算, 超级计算 | 工学 | 论文, 软件与代码 | 4 | 3 | 3 | 是 |
| 127 | history | history, 历史学, 史学, 历史研究 | 历史学 | 论文, 学术专著 | 4 | 4 | 3 | 是 |
| 128 | human_computer_interaction | human_computer_interaction, 人机交互, HCI, 交互设计, 可用性 | 工学 | 论文, 软件与代码 | 4 | 4 | 3 | 是 |
| 129 | hydrology | hydrology, 水文学, 水文科学, 水资源 | 理学 | 论文, 数据集 | 4 | 3 | 3 | 是 |
| 130 | hydrology_engineering | hydrology_engineering, 水文工程, 水文学, 水文, 水资源 | 工学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 131 | immunology | immunology, 免疫学, immune_system, immunity | 理学 | 论文 | 4 | 4 | 3 | 是 |
| 132 | infectious_disease | infectious_disease, 感染病学, 感染科, 传染病学, infectious diseases | 医学 | 论文, 数据集 | 4 | 5 | 3 | 是 |
| 133 | information_science | information_science, 信息科学, 情报学, 信息管理 | 管理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 134 | information_theory | information theory, 信息论, 香农, 编码理论, Shannon | 理学 | 论文, 软件与代码 | 3 | 4 | 3 | 是 |
| 135 | inorganic_chemistry | inorganic chemistry, 无机化学, 配位化学, coordination chemistry, 金属有机 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 136 | international_relations | international_relations, 国际关系, 国际政治, 外交学 | 法学 | 论文, 学术专著 | 5 | 5 | 3 | 是 |
| 137 | internet_of_things | internet_of_things, 物联网, IoT, 边缘感知 | 工学 | 论文, 软件与代码, 专利 | 4 | 3 | 3 | 是 |
| 138 | journalism | journalism, 新闻学, 新闻研究, 新闻传播 | 文学 | 论文, 报告 | 5 | 5 | 3 | 是 |
| 139 | kinesiology | kinesiology, 运动机能学, 人体运动学, 动作科学, human movement science | 教育学 | 论文, 数据集 | 5 | 4 | 3 | 是 |
| 140 | law | law, legal, jurisprudence, 法学, 法律 | 法学 | 论文, 学术专著 | 5 | 4 | 3 | 是 |
| 141 | library_science | library_science, 图书馆学, 图书馆情报, 图书情报 | 管理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 142 | limnology | limnology, 湖沼学, 淡水生态学, freshwater ecology, 湖泊学 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 143 | linguistics | linguistics, 语言学, 语料, corpus, phonology | 文学 | 论文, 学术专著, 译文 | 5 | 4 | 3 | 是 |
| 144 | logic | logic, 逻辑, 数理逻辑, 集合论, 模型论 | 理学 | 论文 | 5 | 3 | 3 | 是 |
| 145 | machine_learning | machine_learning, 机器学习, ML, 统计学习, 模式识别 | 工学 | 论文, 软件与代码, 数据集 | 4 | 5 | 3 | 是 |
| 146 | management | management, 管理学, 组织管理, 战略管理 | 管理学 | 论文, 报告 | 5 | 5 | 3 | 是 |
| 147 | marine_biology | marine_biology, 海洋生物学, ocean_biology, marine_ecology | 理学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 148 | marketing | marketing, 市场营销, 营销学, 消费者行为 | 管理学 | 论文, 报告 | 5 | 5 | 3 | 是 |
| 149 | materials_science | materials science, 材料科学, 材料, materials, 纳米 | 工学 | 论文, 专利 | 4 | 3 | 3 | 是 |
| 150 | mathematical_physics | mathematical physics, 数学物理, 理论物理, 统计力学严格结果, mathematical physics | 理学 | 论文 | 3 | 3 | 3 | 是 |
| 151 | mathematics | math, 数学, 定理, 证明, 代数 | 理学 | 论文 | 5 | 5 | 3 | 是 |
| 152 | mechanical_engineering | mechanical_engineering, 机械工程, 机械, 机械设计, 机械制造 | 工学 | 论文, 专利 | 4 | 3 | 3 | 是 |
| 153 | medicine | medicine, medical, 医学, 临床, clinical | 医学 | 论文 | 4 | 3 | 5 | 是 |
| 154 | metaphysics | metaphysics, 形而上学, 本体论, 存在论 | 哲学 | 论文, 学术专著 | 4 | 4 | 3 | 是 |
| 155 | meteorology | meteorology, 气象学, 天气学, 大气科学 | 理学 | 论文, 数据集 | 4 | 3 | 3 | 是 |
| 156 | microbiology | microbiology, 微生物学, 细菌学, bacteriology, 微生物组 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 157 | microelectronics | microelectronics, 微电子学, 微电子, 集成电路, 半导体器件 | 工学 | 论文, 专利, 软件与代码 | 5 | 5 | 3 | 是 |
| 158 | military_history | military_history, 军事史, 战争史, 战史, war history | 军事学 | 论文, 学术专著 | 4 | 4 | 3 | 是 |
| 159 | military_science | military_science, 军事科学, 军事学, 作战研究, military studies | 军事学 | 论文, 学术专著 | 4 | 4 | 3 | 是 |
| 160 | mineralogy | mineralogy, 矿物学, 晶体学, 矿物成因 | 理学 | 论文, 数据集 | 3 | 3 | 3 | 是 |
| 161 | mining_engineering | mining_engineering, 采矿工程, 采矿, 选矿, 岩石力学 | 工学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 162 | molecular_biology | molecular biology, 分子生物学, 基因表达, gene expression, 分子克隆 | 理学 | 论文, 数据集 | 5 | 6 | 3 | 是 |
| 163 | musicology | musicology, 音乐学, 音乐研究, 民族音乐学 | 艺术学 | 论文, 学术专著, 艺术作品 | 4 | 4 | 3 | 是 |
| 164 | mycology | mycology, 真菌学, 真菌分类学, fungal taxonomy, 真菌生理学 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 165 | nanotechnology | nanotechnology, 纳米技术, 纳米, 纳米材料, 纳米器件 | 工学 | 论文, 专利, 数据集 | 5 | 5 | 3 | 是 |
| 166 | natural_language_processing | natural_language_processing, 自然语言处理, NLP, 计算语言学, 文本挖掘 | 工学 | 论文, 软件与代码, 数据集 | 4 | 5 | 3 | 是 |
| 167 | naval_architecture | naval_architecture, 船舶与海洋工程, 船舶工程, 船舶设计, 水动力 | 工学 | 论文, 专利 | 4 | 4 | 3 | 是 |
| 168 | naval_strategy | naval_strategy, 海军战略, 海权研究, 海上战略, naval warfare | 军事学 | 论文, 学术专著, 报告 | 4 | 4 | 3 | 是 |
| 169 | network_science | network_science, 网络科学, 复杂网络, 图网络分析, network analysis | 交叉学科 | 论文, 软件与代码, 数据集 | 4 | 4 | 3 | 是 |
| 170 | neurology | neurology, 神经病学, 神经内科, 临床神经科学, clinical neuroscience | 医学 | 论文, 数据集 | 6 | 5 | 3 | 是 |
| 171 | neuroscience | neuroscience, 神经科学, 脑科学, brain, fMRI | 理学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 172 | nuclear_engineering | nuclear_engineering, 核工程, 核能, 核反应堆, 核安全 | 工学 | 论文, 专利 | 4 | 4 | 3 | 是 |
| 173 | nuclear_physics | nuclear physics, 核物理, 原子核物理, nuclear structure, 核结构 | 理学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 174 | number_theory | number theory, 数论, 解析数论, 代数数论, 算术几何 | 理学 | 论文 | 4 | 3 | 3 | 是 |
| 175 | numerical_analysis | numerical analysis, 数值分析, 数值方法, 科学计算, numerical methods | 理学 | 论文, 软件与代码 | 3 | 3 | 3 | 是 |
| 176 | nursing | nursing, 护理, 护理学, nurse, 临床护理 | 医学 | 论文 | 3 | 3 | 5 | 是 |
| 177 | nutrition | nutrition, diet, dietetics, 营养学, 膳食 | 医学 | 论文 | 4 | 3 | 3 | 是 |
| 178 | obstetrics_gynecology | obstetrics_gynecology, 妇产科学, 妇产科, 产科, 妇科 | 医学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 179 | oceanography | oceanography, 海洋学, 物理海洋, 海洋科学 | 理学 | 论文, 数据集 | 4 | 3 | 3 | 是 |
| 180 | oncology | oncology, 肿瘤学, 癌症研究, 肿瘤内科, 肿瘤外科 | 医学 | 论文, 数据集 | 6 | 6 | 3 | 是 |
| 181 | open_science | open_science, 开放科学, 开放研究, 开放获取, open research | 交叉学科 | 论文, 报告 | 3 | 5 | 3 | 是 |
| 182 | operating_systems | operating_systems, 操作系统, OS, 内核 | 工学 | 论文, 软件与代码 | 3 | 4 | 3 | 是 |
| 183 | operations_research | operations research, 运筹学, OR, 管理科学, 数学规划 | 理学 | 论文, 软件与代码 | 4 | 3 | 3 | 是 |
| 184 | ophthalmology | ophthalmology, 眼科学, 眼科, 视觉科学, visual science | 医学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 185 | optics_photonics | optics, photonics, laser, 光学, 光子学 | 理学 | 论文, 专利 | 5 | 5 | 3 | 是 |
| 186 | optimization | optimization, 最优化, 优化, 数学规划, 凸优化 | 理学 | 论文, 软件与代码 | 5 | 3 | 3 | 是 |
| 187 | organic_chemistry | organic chemistry, 有机化学, 有机合成, organic synthesis, 有机方法学 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 188 | ornithology | ornithology, 鸟类学, 鸟类生态学, avian ecology, 鸟类行为学 | 理学 | 论文, 数据集 | 5 | 4 | 3 | 是 |
| 189 | orthopedics | orthopedics, 骨科学, 骨科, 矫形外科学, 运动骨科 | 医学 | 论文, 数据集 | 5 | 4 | 3 | 是 |
| 190 | otolaryngology | otolaryngology, 耳鼻咽喉科学, 耳鼻喉科, 头颈外科, otorhinolaryngology | 医学 | 论文 | 4 | 4 | 3 | 是 |
| 191 | paleontology | paleontology, 古生物学, 化石, 古生态 | 历史学 | 论文, 数据集 | 4 | 3 | 3 | 是 |
| 192 | particle_physics | particle physics, 粒子物理, 高能物理, high energy physics, 标准模型 | 理学 | 论文, 数据集 | 4 | 5 | 3 | 是 |
| 193 | peace_conflict_studies | peace_conflict_studies, 和平与冲突研究, 和平研究, 冲突研究 | 法学 | 论文, 学术专著 | 5 | 5 | 3 | 是 |
| 194 | pediatrics | pediatrics, 儿科学, 儿科, 儿童医学, 新生儿学 | 医学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 195 | performing_arts | performing_arts, 表演艺术, 戏剧学, 舞台艺术 | 艺术学 | 论文, 艺术作品 | 2 | 4 | 3 | 是 |
| 196 | petroleum_engineering | petroleum_engineering, 石油工程, 石油, 油气藏工程, 钻井工程 | 工学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 197 | pharmacology | pharmacology, 药理学, 基础药理学, 临床药理学, clinical pharmacology | 医学 | 论文, 专利 | 4 | 5 | 3 | 是 |
| 198 | pharmacy | pharmacy, pharmacology, pharmaceutics, drug, 药学 | 医学 | 论文, 专利 | 4 | 4 | 3 | 是 |
| 199 | phenomenology | phenomenology, 现象学, 现象学哲学, 意识哲学 | 哲学 | 论文, 学术专著 | 4 | 4 | 3 | 是 |
| 200 | philosophy | philosophy, ethics, epistemology, metaphysics, logic | 哲学 | 论文, 学术专著 | 2 | 3 | 3 | 是 |
| 201 | photochemistry | photochemistry, 光化学, 光物理, photophysics, 光催化 | 理学 | 论文, 数据集, 专利 | 5 | 5 | 3 | 是 |
| 202 | photonics | photonics, 光子学, 光子, 光学工程, 激光 | 工学 | 论文, 专利 | 5 | 4 | 3 | 是 |
| 203 | physical_chemistry | physical chemistry, 物理化学, 化学热力学, chemical thermodynamics, 化学动力学 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 204 | physical_education | physical_education, 体育教育, 学校体育, 体育教学, PE | 教育学 | 论文, 教案与教材 | 4 | 4 | 3 | 是 |
| 205 | physics | physics, 物理, 量子, quantum, 粒子 | 理学 | 论文 | 5 | 5 | 3 | 是 |
| 206 | physiology | physiology, 生理学, 人体生理学, human physiology, 器官生理 | 理学 | 论文, 数据集 | 5 | 4 | 3 | 是 |
| 207 | planetary_science | planetary science, 行星科学, 行星学, planetology, 行星地质 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 208 | plasma_physics | plasma physics, 等离子体物理, 等离子体科学, plasma science, 磁约束聚变 | 理学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 209 | political_science | political science, politics, govt, 政治学, 公共行政 | 法学 | 论文, 学术专著 | 5 | 4 | 3 | 是 |
| 210 | polymer_chemistry | polymer chemistry, 高分子化学, 聚合物科学, polymer science, 高分子物理 | 理学 | 论文, 专利 | 5 | 5 | 3 | 是 |
| 211 | probability_theory | probability, 概率论, 概率, 随机, probability theory | 理学 | 论文, 软件与代码 | 3 | 3 | 3 | 是 |
| 212 | programming_languages | programming_languages, 程序设计语言, 编程语言, PL, 类型系统 | 工学 | 论文, 软件与代码 | 5 | 4 | 3 | 是 |
| 213 | psychiatry | psychiatry, 精神病学, 精神医学, 临床心理学, clinical psychiatry | 医学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 214 | psychology | psychology, 心理学, 认知, cognitive, 行为 | 理学 | 论文, 学术专著 | 4 | 4 | 3 | 是 |
| 215 | public_administration | public_administration, 公共管理, 行政管理, 公共政策 | 管理学 | 论文, 报告 | 5 | 5 | 3 | 是 |
| 216 | public_health | public health, 公共卫生, 预防医学, preventive medicine, global health | 医学 | 论文, 报告 | 4 | 3 | 5 | 是 |
| 217 | quantum_computing | quantum computing, quantum, qubit, 量子计算, 量子信息 | 交叉学科 | 论文, 软件与代码 | 4 | 3 | 3 | 是 |
| 218 | quantum_mechanics | quantum mechanics, 量子力学, 量子理论, quantum theory, 量子信息 | 理学 | 论文 | 3 | 3 | 3 | 是 |
| 219 | radiology | radiology, 放射学, 医学影像学, 影像诊断, 介入放射学 | 医学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 220 | rehabilitation_medicine | rehabilitation_medicine, 康复医学, 康复科, 物理医学与康复, physical medicine and rehabilitation | 医学 | 论文 | 4 | 4 | 3 | 是 |
| 221 | religious_studies | religious_studies, 宗教学, 宗教研究, 比较宗教学 | 哲学 | 论文, 学术专著 | 3 | 4 | 3 | 是 |
| 222 | remote_sensing | remote_sensing, 遥感, 遥感科学, 对地观测 | 工学 | 论文, 数据集 | 5 | 5 | 3 | 是 |
| 223 | research_methodology | research_methodology, 科研方法论, 研究方法论, 研究设计, research methods | 交叉学科 | 论文, 学术专著 | 3 | 5 | 3 | 是 |
| 224 | robotics | robotics, robot, slam, manipulation, 机器人 | 工学 | 论文, 软件与代码, 专利 | 4 | 3 | 3 | 是 |
| 225 | science_communication | science_communication, 科学传播, 科技传播, 科学普及, science communication | 交叉学科 | 论文, 报告, 教案与教材 | 3 | 5 | 3 | 是 |
| 226 | science_technology_studies | science_technology_studies, 科学技术研究, STS, 科技与社会 | 交叉学科 | 论文, 学术专著 | 5 | 5 | 3 | 是 |
| 227 | scientometrics | scientometrics, 科学计量学, 科研评价, 科学指标, scientometrics | 交叉学科 | 论文, 软件与代码, 数据集 | 3 | 4 | 3 | 是 |
| 228 | seismology | seismology, 地震学, 震源机制, 地震波 | 理学 | 论文, 数据集 | 4 | 3 | 3 | 是 |
| 229 | semiconductor_physics | semiconductor_physics, 半导体物理, 半导体, 能带理论, 半导体材料 | 工学 | 论文, 专利, 数据集 | 4 | 5 | 3 | 是 |
| 230 | social_science | social science, 社会科学, 社会学, sociology, 政治学 | 法学 | 论文, 报告 | 5 | 4 | 3 | 是 |
| 231 | social_work | social_work, 社会工作, 社会福利, 社会服务 | 法学 | 论文, 报告 | 5 | 5 | 3 | 是 |
| 232 | sociology | sociology, social science, 社会学, 社会分层, 社会网络 | 法学 | 论文, 学术专著 | 5 | 4 | 3 | 是 |
| 233 | software_engineering | software_engineering, 软件工程, 软件, 软件方法, 软件测试 | 工学 | 论文, 软件与代码 | 4 | 5 | 3 | 是 |
| 234 | software_testing | software_testing, 软件测试, 测试, 软件质量保障 | 工学 | 论文, 软件与代码 | 4 | 4 | 3 | 是 |
| 235 | soil_science | soil_science, 土壤学, 土壤科学, 土壤肥力 | 农学 | 论文, 数据集 | 4 | 3 | 3 | 是 |
| 236 | sports_medicine | sports_medicine, 运动医学, 运动损伤, 运动康复, sports medicine | 医学 | 论文, 数据集 | 5 | 4 | 3 | 是 |
| 237 | sports_science | sports_science, 运动科学, 运动训练学, 运动表现, sport science | 教育学 | 论文, 数据集 | 5 | 4 | 3 | 是 |
| 238 | statistical_mechanics | statistical mechanics, 统计力学, 统计物理, statistical physics, 系综理论 | 理学 | 论文 | 3 | 3 | 3 | 是 |
| 239 | statistics | statistics, biostatistics, biometrika, 数理统计, 计量经济 | 理学 | 论文, 软件与代码 | 5 | 5 | 3 | 是 |
| 240 | stochastic_processes | stochastic processes, 随机过程, 随机分析, 鞅, 布朗运动 | 理学 | 论文, 软件与代码 | 4 | 3 | 3 | 是 |
| 241 | strategic_studies | strategic_studies, 战略研究, 安全研究, 战略学, strategic analysis | 军事学 | 论文, 学术专著, 报告 | 4 | 4 | 3 | 是 |
| 242 | structural_engineering | structural_engineering, 结构工程, 结构, 结构设计, 抗震工程 | 工学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 243 | surgery | surgery, 外科学, 外科, 普通外科, 手术学 | 医学 | 论文, 数据集 | 6 | 5 | 3 | 是 |
| 244 | sustainability_science | sustainability_science, 可持续性科学, 可持续发展, 可持续 | 交叉学科 | 论文, 报告, 数据集 | 6 | 5 | 3 | 是 |
| 245 | synthetic_biology | synthetic_biology, 合成生物学, 基因回路, 生物工程, synbio | 交叉学科 | 论文, 专利, 数据集 | 4 | 5 | 3 | 是 |
| 246 | systems_biology | systems_biology, 系统生物学, 组学整合, 生物网络建模, systems biology | 交叉学科 | 论文, 软件与代码, 数据集 | 4 | 5 | 3 | 是 |
| 247 | telecommunications | telecommunications, 电信, 通信工程, 通信, 无线通信 | 工学 | 论文, 专利 | 5 | 4 | 3 | 是 |
| 248 | textile_engineering | textile_engineering, 纺织工程, 纺织, 纺织材料, 染整 | 工学 | 论文, 专利 | 3 | 4 | 3 | 是 |
| 249 | theology | theology, 神学, 系统神学, 圣经研究 | 哲学 | 论文, 学术专著 | 3 | 4 | 3 | 是 |
| 250 | theoretical_computer_science | tcs, theoretical cs, 算法, complexity, proof theory | 理学 | 论文, 软件与代码 | 4 | 3 | 2 | 是 |
| 251 | thermodynamics | thermodynamics, 热力学, 工程热力学, engineering thermodynamics, 热力学第二定律 | 理学 | 论文 | 3 | 3 | 3 | 是 |
| 252 | toxicology | toxicology, 毒理学, 毒理, 毒物学, 风险评估 | 医学 | 论文, 报告 | 4 | 5 | 3 | 是 |
| 253 | traditional_chinese_medicine | traditional_chinese_medicine, 中医学, 中医, 中医药, TCM | 医学 | 论文 | 4 | 5 | 3 | 是 |
| 254 | translation_studies | translation_studies, 翻译学, 翻译研究, 口译研究 | 文学 | 论文, 学术专著, 译文 | 5 | 4 | 3 | 是 |
| 255 | transportation_engineering | transportation_engineering, 交通工程, 交通, 交通运输, 交通规划 | 工学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 256 | urban_studies | urban_studies, 城市研究, 城市规划, 城市科学 | 工学 | 论文, 数据集, 报告 | 5 | 5 | 3 | 是 |
| 257 | urology | urology, 泌尿外科学, 泌尿外科, 泌尿科, 男科学 | 医学 | 论文, 数据集 | 4 | 4 | 3 | 是 |
| 258 | veterinary_science | veterinary, veterinary science, 兽医学, 兽医, animal science | 农学 | 论文 | 5 | 3 | 5 | 是 |
| 259 | volcanology | volcanology, 火山学, 火山地质, 火山监测 | 理学 | 论文, 数据集 | 4 | 3 | 3 | 是 |
| 260 | world_literature | world_literature, 世界文学, 比较文学, 跨文化文学 | 文学 | 论文, 学术专著, 文学作品 | 3 | 4 | 3 | 是 |
| 261 | zoology | zoology, 动物学, 动物分类学, animal taxonomy, 动物行为学 | 理学 | 论文, 数据集 | 5 | 4 | 3 | 是 |

## 字段说明

| 字段 | 类型 | 说明 |
| --- | --- | --- |
|  |  | 学科主键，英文小写 snake_case |
|  |  | 别名与检索关键词（中英文） |
|  |  | 体裁 → 章节结构 |
|  |  | 主引用样式 |
|  |  | 报告规范路由 |
|  |  | 写作约定 |
|  |  | 代表性顶刊/顶会 |
|  |  | 单位与公式注记 |
|  |  | 是否以论文为主要产出 |
|  |  | 产出形式（可多值） |
|  |  | 该学科用到的软件/仪器/方法平台 |
|  |  | 学科门类 |
|  |  | 优先论文库/数据库 |

## Python API

```python
from sciforge.disciplines import (
    DISCIPLINES,                 # dict[str, Discipline]
    list_disciplines,            # 全部学科，按名排序
    get_discipline,              # 按名或别名查
    list_by_category,            # 按门类过滤
    list_by_contribution_form,   # 按产出形式过滤
    list_by_tool,                # 按工具过滤
    list_by_database,            # 按优先数据库过滤
)

len(DISCIPLINES)                    # 261
d = get_discipline("machine_learning")
d.contribution_forms               # ("论文", "软件与代码", "数据集")
list_by_contribution_form("专利")   # 可产出专利的学科
list_by_tool("PyTorch")            # 绑定 PyTorch 的学科
list_by_database("PubMed")         # 优先 PubMed 的学科
```