"""观赏植物生产学科论文支持：栽培/生理/采后加工/种质资源评价体系。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ornamental_plant_production",
    aliases=(
        "ornamental_plant_production",
        "观赏植物生产",
        "花卉生产",
        "Ornamental Horticulture",
        "Floriculture",
        "Ornamental Plant Science",
        "盆栽花卉",
        "盆花栽培",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "methodology（材料与栽培方法）",
            "results（生长与品质结果）",
            "discussion（机理与应用讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（栽培案例描述）",
            "analysis（生产要素分析）",
            "results（产量与品质结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（国际期刊）/ GB/T 7714（中文期刊）",
    reporting_standards={
        "experimental": "MIAME 园艺实验报告规范",
        "survey": "APAS 社会调查规范",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "栽培试验须说明重复数与随机化设计",
        "环境因子（温光水肥）须完整记录",
        "性状测定方法须给出并引用标准",
        "图表须含误差棒与显著性标记",
        "拉丁学名与俗名并列使用",
    ),
    key_venues=(
        "Scientia Horticulturae",
        "Horticulturae",
        "Acta Horticulturae",
        "Journal of the American Society for Horticultural Science",
        "Chinese Journal of Ornamental Horticulture",
    ),
    units_and_formulas_notes=(
        "温度单位用 ℃，光强用 μmol·m⁻²·s⁻¹",
        "施肥浓度给出 N/P/K 摩尔比与质量浓度",
        "株高/冠幅精度到 mm，产量以 kg·m⁻² 报告",
        "统计方法给出检验类型与 α=0.05",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ImageJ（株高与叶片面积测量）", "WinRHSScan（叶面积扫描）", "LI-COR LI-6400（光合测定）", "SPSS（方差分析）", "R（植物生长分析）", "Photoshop（图表制作）", "Origin（数据绘图）", "EndNote（文献管理）", "LaTeX（论文排版）", "Excel（栽培数据台账）", "MarsHydro（水肥一体化控制）", "Horticultural Supplies - 气候箱", "Quantum Yield - 光合光响应", "Chlorophyll Fluorometer - PAM200", "Soil EC/P/H Meter", "Photoperiod Timer - 光周期调控", "Huntingdon H13 温室内传感器", "Spectrophotometer UV-Vis（色素测定）", "HPLC（花色苷分析）", "QCA（根系扫描）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
