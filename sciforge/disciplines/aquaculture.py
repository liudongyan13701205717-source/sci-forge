"""水产养殖学科论文支持：鱼类/贝类/藻类养殖、水质、病害、遗传育种、生态调控。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aquaculture",
    aliases=(
        "aquaculture",
        "Aquaculture",
        "水产养殖",
        "水产养殖学",
        "fisheries science",
        "渔业科学",
        "海洋养殖",
        "marine aquaculture",
        "淡水养殖",
        "养殖遗传学",
        "水产营养",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（物种、品种、饲养系统、实验设计）",
            "results（生长、存活、水质、饲料效率、疾病）",
            "discussion（机制与生产意义）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "species/system overview",
            "current evidence",
            "challenges and perspectives",
            "references",
        ),
        "technical_report": (
            "abstract",
            "site and system description",
            "methods and protocols",
            "results and comparison",
            "recommendations",
            "references",
        ),
    },
    citation_style="APA 7 或 Vancouver（水产类期刊多用数字编号）",
    reporting_standards={
        "animals": "物种（拉丁学名）、品种、体长/体重、来源、密度须报告",
        "system": "养殖系统类型（网箱/循环水/半集约化）、水体体积、温度、溶氧须说明",
        "feed": "饲料成分、投喂率、更换频率须明确",
        "water_quality": "温度、pH、溶氧、氨氮、亚硝酸盐、盐度须定期记录",
        "ethics": "涉及动物实验须说明伦理审查与福利措施",
        "statistics": "样本量、方差齐性检验、事后检验与效应量须报告",
    },
    conventions=(
        "物种用拉丁学名首次出现标注；中文名括注学名（如草鱼 Ctenopharyngodon idella）",
        "生长指标以体长 SL（斜长）、体高 BH、体重 BW 报告，含均值±标准差",
        "水质参数统一缩写：DO 溶氧、NH3-N 氨氮、NO2-N 亚硝酸盐、TAN 总氨",
        "饲料效率 FCR = 饲料消耗量/体重增量；料重比 SR = 1/FCR",
        "统计：M±SD；组间比较用 ANOVA/Tukey；效应量报告",
    ),
    key_venues=(
        "Aquaculture",
        "Aquaculture International",
        "Reviews in Aquaculture",
        "Aquaculture Research",
        "Journal of Applied Ichthyology",
        "水产学报",
    ),
    units_and_formulas_notes=(
        "长度 cm、mm；重量 g、kg；密度 尾/m³ 或 尾/m²",
        "温度 ℃；pH 无量纲；溶氧 mg/L；盐度 PSU",
        "投喂率 % BW/day；FCR 无量纲",
        "遗传：育种值 BLUP 单位 kg 或 %",
        "统计软件：R/SPSS/SAS/Excel 版本须注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("YSI 水质分析仪", "HACH 水质分析仪", "溶氧仪 DO（Optode/Polarographic）", "pH 计", "温度计（数字/铂电阻）", "盐度计（电导/阿贝）", "氨氮光度计（Salifert/Seachem）", "亚硝酸盐检测", "显微镜（Olympus/Nikon）", "电子天平", "孵化器（卵孵化桶）", "循环水养殖系统 RAS", "增氧机（罗茨风机）", "自动投饵机", "网箱管理平台", "分子遗传检测（PCR/qPCR）", "Sanger 测序仪", "Illumina 高通量测序", "流式细胞仪（性别鉴定）", "水质在线监测系统", "Python", "R", "RStudio", "Excel", "AquaSoft", "SAS", "SPSS"),
    category="农学",
    databases=("PubMed", "Web of Science", "CNKI", "万方", "OpenAlex", "Crossref"),
)
