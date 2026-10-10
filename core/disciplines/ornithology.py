"""鸟类学学科论文支持：形态学/分类/行为/分布与保护研究规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ornithology",
    aliases=(
        "ornithology",
        "鸟类学",
        "Ornithology",
        "鸟类分类学",
        "Bird Biology",
        "鸟类生态学",
        "Avian Ecology",
        "鸟类保护",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methodology（观察与采样方法）",
            "results（记录与分析结果）",
            "discussion（生态与演化讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例与样点描述）",
            "analysis（行为或生态分析）",
            "results（观测结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与系统综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（国际）/ GB/T 7714（中文）",
    reporting_standards={
        "empirical": "生态与鸟类观察研究报告规范",
        "taxonomic": "ITIS / ZoonBank 命名规范",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "物种拉丁学名双名法标注并给出版本",
        "采样地点用 WGS84 经纬度或 UTM 报告",
        "时间精确到分钟，气候要素齐全",
        "种群数据按 BBS / eBird 格式整理",
        "伦理许可（IACUC / Bird Banding Lab）须引用编号",
    ),
    key_venues=(
        "Auk: Ornithological Advances",
        "The Auk",
        "Journal of Avian Biology",
        "Ornithology",
        "Ibis",
    ),
    units_and_formulas_notes=(
        "体长/翼展以 mm 报告",
        "体重精度 0.1 g",
        "鸣声分析给出频谱范围 kHz 与音节时长 s",
        "统计模型用 GLM/GLMM 并报告 β 与置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("eBird（观鸟记录）", "Merlin ID（AI 识别）", "Sondelux（声学监测）", "AviSound（鸣声分析）", "Bandit（GPS 追踪）", "R 4（ecological stats）", "QGIS（分布制图）", "MapView（分布可视化）", "Photoshop（标本/照片处理）", "Excel（观测数据）", "EndNote（文献）", "LaTeX（排版）", "Beech-Museum Banding Tool", "Spectrogram Analysis Raven Pro", "CamTraps（红外相机）", "DawnChorus（鸣声鉴定）", "Hawkwatch / BirdWeather 迁飞数据", "Rapid-Response BioAcoustic (RRBAC) 软件", "Avian Pathogen RT-PCR 试剂平台", "Microscope OLYMPUS BX53（形态学）"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
