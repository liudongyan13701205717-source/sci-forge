"""矿物学学科论文支持：矿物晶体/成因/应用体裁、Mineralogical Society 引用样式与晶体学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mineralogy",
    aliases=(
        "mineralogy", "矿物学", "晶体学", "矿物成因", "crystallography",
        "petrology", "矿物地球化学", "mineral earth chemistry", "结构矿物学"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "samples and methods（样品与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（矿物产地与产状）",
            "analysis（晶体结构与成分）",
            "results（光学与化学性质）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（晶体学与成因理论）",
            "evidence synthesis（矿物分类综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="Mineralogical Society 样式（作者-年份；Am Min 遵循矿物学会规范）",
    reporting_standards={
        "experimental": "实验遵循矿物合成与表征报告规范",
        "new_mineral": "新矿物报告遵循 IMA 批准规范",
        "observational": "观察研究遵循矿物描述报告规范",
    },
    conventions=(
        "样品产地与产状须报告",
        "晶体结构数据（空间群/晶胞参数）须给出",
        "化学成分须附分析方法",
        "新矿物须经 IMA 批准",
        "XRD/EPMA 等分析条件须说明",
    ),
    key_venues=(
        "American Mineralogist",
        "Mineralogical Magazine",
        "European Journal of Mineralogy",
        "The Canadian Mineralogist",
        "Physics and Chemistry of Minerals",
    ),
    units_and_formulas_notes=(
        "晶胞参数用 Å；角度用 °",
        "成分用 wt% 或 apfu",
        "公式用 amsmath；晶体化学式须编号",
        "数值结果给出均值 ± 标准差与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("X 射线衍射仪 (XRD)", "扫描电镜 (SEM)", "偏光显微镜", "电子探针 (EPMA)", "透射电镜 (TEM)", "红外光谱仪", "拉曼光谱仪", "单晶衍射仪", "高温高压合成装置", "原子力显微镜 (AFM)", "热分析仪器 (TGA/DSC)", "Python (NumPy)", "FullProf", "TOPAS", "Mercury", "Materials Studio", "WIReMAT", "IMA-Database", "MacCrystallize", "Rietveld 分析软件"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
