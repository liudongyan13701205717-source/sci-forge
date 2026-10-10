"""水产养殖学科论文支持：苗种培育/水质调控/病害防控/工厂化养殖体裁、水产养殖报告规范与养殖度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sea_food_breeding",
    aliases=("sea_food_breeding", "水产养殖", "海水养殖", "水产育苗", "marine aquaculture", "mariculture"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究意义）",
            "materials and methods（材料与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "trial_report": (
            "abstract",
            "introduction",
            "trial design（试验设计）",
            "materials and methods（材料与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据综合）",
            "future directions（展望）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "experimental": "试验研究遵循实验报告规范，须报告试验设计、样本量、对照设置",
        "data": "水质与生长数据须报告采样频率、检测方法与误差范围",
        "disease": "病害防控报告须说明病原体鉴定、感染率统计与治疗方案",
        "environmental": "环境影响评估遵循环境影响评价报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "养殖对象须注明物种学名（双名法）与养殖规格",
        "水质参数须注明检测方法与仪器型号",
        "生长指标须统一口径：体长用 cm、体重用 g、日增长率用 %/d",
        "成活率须报告初始与最终数量及计算公式",
        "图表须标注数据来源与采集时间",
    ),
    key_venues=(
        "Aquaculture Engineering",
        "Aquaculture Research",
        "Reviews in Aquaculture",
        "Aquaculture International",
        "Aquaculture Journal",
    ),
    units_and_formulas_notes=(
        "水温用 ℃；盐度用 ‰（ppt）；pH 无量纲；溶解氧用 mg/L",
        "面积用 m²；水体体积用 m³ 或 L；密度用 ind/m² 或 ind/L",
        "公式用 amsmath；生长方程（Logistic/BG 方程）须编号",
        "统计结果给出均值 ± 标准差与样本量；显著性用 p 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AquariumView", "NRS-3D 孵化系统", "Ocean Insight 光谱仪", "Hach 水质分析仪", "YSI 多参数水质探头", "Hamilton 自动生化分析仪", "Zebra 斑马鱼成像系统", "Fishtech 鱼类生长测量仪", "Marine Harvest 养殖管理系统", "StemCell 干细胞培养平台", "Olympus 显微镜", "Fluorescent Microscope 荧光显微镜", "PCR 实时荧光定量仪", "Matlab 数据分析", "R 统计建模", "LaTeX 排版", "Origin 绘图", "SPSS 统计软件", "GIS 养殖规划系统", "Python 数据分析"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)