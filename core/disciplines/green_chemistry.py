"""绿色化学学科论文支持：可持续化学/绿色合成体裁、ACS 引用样式与绿色化学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="green_chemistry",
    aliases=("green chemistry", "绿色化学", "可持续化学", "sustainable chemistry",
             "绿色合成", "green synthesis", "原子经济性", "atom economy",
             "可再生资源", "renewable feedstocks"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与可持续性目标）",
            "results and discussion（绿色方法、条件与产物）",
            "conclusion",
            "experimental section（实验细节）",
            "references",
        ),
        "sustainability_assessment": (
            "abstract",
            "introduction",
            "methodology（绿色指标与评估方法）",
            "results（E 因子、原子经济性、溶剂评估）",
            "discussion（与常规方法对比）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "principles（绿色化学 12 原则）",
            "main developments（按策略/应用综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份；Green Chem. 遵循 RSC 样式）",
    reporting_standards={
        "green_metrics": "绿色指标（E 因子、原子经济性、PMI）须计算并说明方法",
        "solvent_selection": "溶剂选择须说明（水、生物基溶剂或溶剂-free）",
        "energy_conditions": "反应能量输入（温度、微波、光）须报告",
        "waste_management": "废弃物与催化剂回收须说明",
        "comparison": "与常规方法的对比须给出量化数据",
    },
    conventions=(
        "绿色化学 12 原则在引言处引用（Anastas & Warner）",
        "E 因子（kg 废物/kg 产物）与原子经济性（%）定义须给出",
        "溶剂按绿色等级分类（推荐/可用/不推荐）",
        "催化剂负载与回收次数报告",
        "可再生原料来源须注明",
    ),
    key_venues=(
        "Green Chemistry",
        "ACS Sustainable Chemistry & Engineering",
        "ChemSusChem",
        "Green Synthesis and Catalysis",
        "Journal of Cleaner Production",
        "Sustainable Chemistry and Pharmacy",
    ),
    units_and_formulas_notes=(
        "产率用 %；E 因子无量纲；PMI 无量纲",
        "温度用 °C；压力用 bar",
        "公式用 amsmath；反应式与物料平衡排版统一",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出量化指标（如 E 因子 = 3.2）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("Python (NumPy/SciPy)", "Origin", "SPSS", "CHEM21", "LaTeX"),
    category="理学",
    databases=("Crossref", "OpenAlex", "PubChem", "CNKI", "万方"),
)