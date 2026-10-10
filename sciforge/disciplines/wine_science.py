"""葡萄酒科学学科论文支持：葡萄酒化学与感官分析体裁、ACS 引用样式与分析化学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wine_science",
    aliases=("wine science", "葡萄酒科学", "葡萄酒化学", "葡萄与葡萄酒学", "酿酒科学",
             "oenology", "viticulture and enology", "wine chemistry"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与科学问题）",
            "materials and methods（样品、分析与统计）",
            "results（成分、风味与感官数据）",
            "discussion（化学机理与品质意义）",
            "references",
        ),
        "analytical": (
            "abstract",
            "introduction",
            "materials and methods（方法、仪器与验证）",
            "results（分析结果与质量控制）",
            "discussion（方法学意义）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份或编号；J. Agric. Food Chem. 遵循 ACS 规范）",
    reporting_standards={
        "analytical": "分析化学须报告方法、仪器、标准品与验证参数（LOD/LOQ/回收率）",
        "sensory": "感官评价须报告评价员、标度与统计方法",
        "metabolomics": "代谢组学须报告样品制备、平台与数据处理流程",
        "statistical": "须报告重复数、统计方法与多重比较校正",
    },
    conventions=(
        "化合物须给出 IUPAC 名与 CAS 号（首次出现）",
        "浓度用 mg/L 或 μg/L 并注明当量基准",
        "葡萄品种与产地年份须交代",
        "感官描述须使用标准风味术语",
        "分析方法与仪器条件须完整报告",
    ),
    key_venues=(
        "Journal of Agricultural and Food Chemistry",
        "Food Chemistry",
        "American Journal of Enology and Viticulture",
        "Analytica Chimica Acta",
        "Molecules",
        "Food Research International",
    ),
    units_and_formulas_notes=(
        "浓度用 mg/L、μg/L；多酚用 mg/L（没食子酸当量）",
        "香气化合物用 μg/L；阈值用 μg/L 或 ng/L",
        "色度用吸光度 (A420/A520/A620)；色差用 ΔE",
        "统计用 PCA/PLS-DA 须报告解释方差与验证参数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("气相色谱-质谱联用仪 (GC-MS)", "高效液相色谱 (HPLC)", "液相色谱-质谱联用仪 (LC-MS)", "紫外-可见分光光度计", "FTIR 葡萄酒分析仪", "核磁共振波谱仪 (NMR)", "质谱仪 (MS)", "电子鼻 (e-nose)", "电子舌 (e-tongue)", "原子吸收光谱仪 (AAS)", "自动滴定仪", "pH 计", "酶标仪 (microplate reader)", "实时荧光定量 PCR", "扫描电镜 (SEM)", "R", "Python (scikit-learn)", "SAS", "SIMCA (multivariate analysis)", "XCMS"),
    category="农学",
    databases=("AGRIS", "OpenAlex", "Crossref", "FSTA"),
)
