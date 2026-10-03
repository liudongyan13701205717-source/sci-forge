"""矿物学学科论文支持：矿物晶体/成因/应用体裁、Mineralogical Society 引用样式与晶体学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mineralogy",
    aliases=("mineralogy", "矿物学", "晶体学", "矿物成因"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "samples and methods（样品与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "new_mineral_report": (
            "abstract",
            "introduction",
            "occurrence（产状）",
            "physical and optical properties（物理与光学性质）",
            "crystallography（晶体学）",
            "chemical composition（化学成分）",
            "references",
        ),
        "experimental_study": (
            "abstract",
            "introduction",
            "experimental methods（实验方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="Mineralogical Society 样式（作者-年份；Am Min 遵循矿物学会规范）",
    reporting_standards={
        "experimental": "实验遵循矿物合成与表征报告规范",
        "new_mineral": "新矿物报告遵循 IMA 批准规范",
        "observational": "观察研究遵循矿物描述报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "data_descriptor": "数据论文遵循晶体学数据规范",
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
        "Journal of Applied Crystallography",
    ),
    units_and_formulas_notes=(
        "晶胞参数用 Å；角度用 °",
        "成分用 wt% 或 apfu",
        "公式用 amsmath；晶体化学式须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "XRD 数据注明辐射源与波长",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("X 射线衍射仪 (XRD)", "扫描电镜 (SEM)", "偏光显微镜"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)