"""乐器制作与维修学科论文支持：乐器制作工艺与声学分析体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="musical_instruments_making_repairing",
    aliases=(
        "musical_instruments_making_repairing", "乐器制作与维修",
        "Musical instruments (making, repairing)", "乐器制作",
        "乐器维修", "piano tuning", "钢琴调律",
        "luthier", "提琴制作",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（制作工艺/测试方法）",
            "results（声学/工艺结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（乐器背景）",
            "analysis（工艺/维修分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（制作综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE（声学测量论文用 IEEE）",
    reporting_standards={
        "k1": "声学测试须报告测试条件（温度、湿度、环境噪声）",
        "k2": "制作工艺研究须报告木材/材料与工艺步骤",
        "k3": "维修案例须报告损坏原因、修复过程与评估",
    },
    conventions=(
        "乐器术语首次出现须给出英文全称",
        "木材学名遵循国际木材标准（如 IAWA）",
        "引用制作谱例须给出页码与出处",
        "声学测量须给出频段与测试距离",
        "调律数据须给出参考音高（如 A4=440Hz）",
    ),
    key_venues=(
        "Journal of the Acoustical Society of America",
        "Journal of Vibration and Sound",
        "Journal of Musical Instruments",
        "Acustica",
        "《乐器》",
    ),
    units_and_formulas_notes=(
        "木材含水率用 %；密度用 kg/m³",
        "调律偏差用 cent；频率用 Hz",
        "音高用 A4=440Hz 为基准",
        "声压级用 dB(A)",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe Audition", "Reaper", "Pro Tools", "Audacity", "Sonic Visualiser", "Spectral Analysis Suite", "MATLAB", "LabVIEW", "SpectraPlus", "Sound Spectrograph", "Tunelab", "Piano Tuner (App)", "Korg Chromatic Tuner", "Severn Software", "Spectral Analyzer (Kleinschmidt)", "SolidWorks", "Autodesk Inventor", "Fusion 360", "EndNote", "Python (SciPy)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
