"""有机化学学科论文支持：有机合成/有机方法学体裁、ACS 引用样式与有机化学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="organic_chemistry",
    aliases=("organic chemistry", "有机化学", "有机合成", "organic synthesis",
             "有机方法学", "organic methodology", "天然产物", "natural products"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与目标分子/反应）",
            "results and discussion（反应条件筛选、底物范围与机理讨论）",
            "conclusion",
            "experimental section（实验细节与表征数据）",
            "references",
        ),
        "synthesis": (
            "abstract",
            "introduction（目标分子与逆合成分析）",
            "results（合成路线与关键步骤）",
            "discussion（选择性、产率与机理）",
            "conclusion",
            "experimental section（化合物数据）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按反应类型/策略综述）",
            "outlook（挑战与展望）",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份，如 (Smith, J. A. et al. J. Am. Chem. Soc. 2020, 142, 1234)）",
    reporting_standards={
        "characterization": "新化合物须提供 ^1H NMR、^13C NMR、HRMS 等表征数据",
        "purity": "纯度与分析方法（HPLC、元素分析）须报告",
        "yields": "产率须注明分离产率或粗产率，并给出反应规模",
        "reaction_conditions": "反应条件（溶剂、温度、时间、催化剂负载）须完整",
        "reproducibility": "关键实验须足以复现；新方法须给出底物范围",
    },
    conventions=(
        "化合物编号用加粗数字（1、2、3），全文引用一致",
        "结构式用 ChemDraw 风格；立体化学用楔形键/虚线键标注",
        "NMR 数据格式：δ (ppm), multiplicity, J (Hz), integration",
        "反应式标注条件（试剂、溶剂、温度、产率）",
        "机理用箭头推演（curly arrows），中间体/过渡态标注",
    ),
    key_venues=(
        "Journal of the American Chemical Society",
        "Angewandte Chemie International Edition",
        "Journal of Organic Chemistry",
        "Organic Letters",
        "Chemical Science",
        "Nature Chemistry",
    ),
    units_and_formulas_notes=(
        "浓度用 mol/L 或 M；产率用 %；温度用 °C",
        "NMR 化学位移用 ppm，耦合常数用 Hz",
        "公式用 amsmath；反应式用 chemfig 或等效工具排版",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "实验数据给出仪器型号与测量条件",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("ChemDraw", "Origin", "Python (NumPy/SciPy)", "MATLAB", "LaTeX"),
    category="理学",
    databases=("Crossref", "OpenAlex", "PubChem", "Semantic Scholar", "CNKI"),
)