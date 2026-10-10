"""传统医学学科论文支持：民族医药/草药民族药理学体裁、PRISMA 与成分分析注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="traditional_medicine",
    aliases=("traditional_medicine", "传统医学", "民族医学", "民族医药",
             "草药民族药理学", "传统疗法",
             "ethnobotany", "ethnopharmacology", "traditional healing"),
    paper_types={
        "research": (
            "abstract",
            "introduction（传统知识背景与研究目的）",
            "materials and methods（标本采集、鉴定、提取与测定）",
            "results（成分谱、活性与含量）",
            "discussion（与传统用途的关联及机理）",
            "references",
        ),
        "ethnobotanical_survey": (
            "abstract",
            "introduction",
            "study area and interview protocol",
            "results（药用植物名录与使用频率指数）",
            "discussion（传统知识传承与保护建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "search strategy and inclusion criteria",
            "results（证据综合）",
            "discussion（证据质量与转化前景）",
            "references",
        ),
    },
    citation_style="GB/T 7714（中文）或 Vancouver（英文）",
    reporting_standards={
        "specimen": "标本须采集模式标本并留存于标本馆，注明采集地与采集人",
        "extraction": "提取方法须报告溶剂、体积比、温度与时间",
        "identification": "植物鉴定须引用权威检索表并附标本照片",
        "safety": "毒性试验须报告剂量分级与观察指标",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "植物名用中文名并附拉丁学名（首次出现），俗名单独标注",
        "传统用途须注明来源（文献/访谈）与受访者背景",
        "成分鉴定须报告质谱/核磁数据与对照品信息",
        "使用频率指数（FID）须给出计算公式",
        "统计结果给出均值 ± SD 与样本量",
    ),
    key_venues=(
        "Journal of Ethnopharmacology",
        "Journal of Ethnobiology and Ethnomedicine",
        "Phytomedicine",
        "Evidence-Based Complementary and Alternative Medicine",
        "中国民族药志",
        "植物学报",
    ),
    units_and_formulas_notes=(
        "含量以 mg/g（干重）或 %（w/w）表示，须注明干燥条件",
        "提取率 = 提取物质量/原料质量 × 100%",
        "质谱数据以 m/z 与相对丰度报告",
        "IC50 以 μmol/L 报告并给出 95% CI",
        "FID = 引用次数/受访人数 × 100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("植物标本压制设备", "气相色谱仪", "高效液相色谱仪", "液相色谱-质谱联用仪", "红外分光光度计", "紫外分光光度计", "薄层色谱仪", "原子吸收分光光度计", "电子天平", "干燥箱", "回流提取装置", "超声提取仪", "AutoDock Vina", "SWISS-MODEL", "Schrödinger", "Cytoscape", "R", "SPSS", "RevMan（Cochrane）", "PRISMA 筛选工具"),
    category="医学",
    databases=("PubMed", "CNKI", "万方", "OpenAlex", "民族药志"),
)
