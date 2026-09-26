"""热力学学科论文支持：热力学/工程热力学体裁、AIP 引用样式与热力学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="thermodynamics",
    aliases=("thermodynamics", "热力学", "工程热力学", "engineering thermodynamics",
             "热力学第二定律", "second law of thermodynamics", "传热学", "heat transfer"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与系统描述）",
            "system definition（系统边界、状态变量与过程）",
            "analysis（第一/第二定律分析与方程）",
            "results（效率、性能系数或状态变化）",
            "discussion（与实验/文献对比）",
            "conclusion",
            "references",
        ),
        "experimental": (
            "abstract",
            "introduction",
            "experimental setup（装置、仪器与测量方法）",
            "procedure（实验步骤与数据采集）",
            "results（数据表、曲线与不确定度）",
            "discussion（误差分析与物理解释）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "thermodynamic framework",
            "main developments（按主题综述）",
            "open problems",
            "references",
        ),
    },
    citation_style="AIP 样式（作者-年份；工程期刊亦可遵循 ASME 样式）",
    reporting_standards={
        "system_boundary": "系统边界、控制体积与控制面须明确定义",
        "state_properties": "状态参数（T、P、V、熵、焓）须定义并注明参考态",
        "laws_statement": "第一/第二定律方程须完整写出，注明符号约定（功/热正负号）",
        "property_data": "物性数据须注明来源（NIST、标准表）与温度/压力范围",
        "uncertainty": "实验测量须报告不确定度与误差传播",
    },
    conventions=(
        "功 W 与热 Q 的符号约定（系统对外做功为正或负）须在开头声明",
        "状态函数（U、H、S、G）与过程量（W、Q）的区分须明确",
        "循环过程用 T-s 图或 P-v 图说明，标注各状态点",
        "效率 \\eta 与性能系数 COP 的定义须给出",
        "理想气体假设与真实气体修正须显式说明",
    ),
    key_venues=(
        "Physical Review E",
        "Journal of Chemical Thermodynamics",
        "International Journal of Heat and Mass Transfer",
        "Journal of Heat Transfer (ASME)",
        "Thermochimica Acta",
        "Applied Thermal Engineering",
    ),
    units_and_formulas_notes=(
        "默认 SI 单位：温度 K，压力 Pa，能量 J，比热 J/(kg·K)",
        "摄氏温度与开尔文换算（T[K] = T[°C] + 273.15）须注明",
        "公式用 amsmath；偏导数（\\partial）与全微分（d）记号区分清楚",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出有效数字与单位，避免混用 kcal/kJ",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("MATLAB", "Python (Cantera)", "Python (NumPy, SciPy)"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)