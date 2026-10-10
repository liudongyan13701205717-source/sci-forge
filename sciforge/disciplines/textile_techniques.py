"""纺织工艺学科论文支持：纺纱/织造/染整等纺织加工工艺与工艺优化研究体裁、IEEE 引用样式与工艺参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="textile_techniques",
    aliases=(
        "textile_techniques",
        "Textile techniques",
        "纺织工艺",
        "纺织工程技术",
        "纺纱工艺",
        "织造工艺",
        "染整工艺",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究动机）",
            "materials and methods（材料与工艺参数）",
            "results（工艺输出与测试数据）",
            "discussion（机理分析与参数影响）",
            "conclusions",
            "references",
        ),
        "process_development": (
            "abstract",
            "introduction",
            "baseline process（基线工艺）",
            "optimization study（参数优化与试验设计）",
            "results（工艺性能与成本对比）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technique overview（工艺分类与原理综述）",
            "comparative analysis（工艺间对比）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号引用 [1]）",
    reporting_standards={
        "process_parameters": "工艺参数（锭速、牵伸倍数、纱线捻度、织机转速、染色温度/时间）须完整列出并注明单位",
        "testing_protocol": "物理性能测试须注明标准（ASTM、ISO、GB）与仪器型号、试样数量",
        "sampling": "试样制备与取样方案须可复现（随机化、样本量、重复次数）",
        "statistical": "参数优化研究须报告统计检验与置信区间",
    },
    conventions=(
        "纤维类型与规格须显式标注（细度旦尼尔/微米、长度、公转）",
        "工艺参数用 SI 单位（捻度用捻/m、密度用 g/m²）",
        "试样数量与重复次数须注明",
        "图片须标注放大倍数与拍摄角度",
        "结论须明确适用边界（纤维/机型/工艺范围）",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of the Textile Institute",
        "Journal of Industrial Textile & Home Economics Education",
        "纤维制品",
        "纺织学报",
    ),
    units_and_formulas_notes=(
        "纱线细度用旦尼尔（den）或特克斯（tex），1 tex = 9.000 den",
        "捻度用捻数/米（tpm）并标明方向（Z 或 S）",
        "织物密度用根/英寸或根/cm，克重用 g/m²",
        "染色温度用 °C 与 K 二选一并全文统一",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Texcel CAD", "Loomworks", "Hertz", "MTEX", "ImageJ", "MATLAB", "Python (NumPy, SciPy)", "R", "Minitab", "JMP", "MATLAB Statistics Toolbox", "Shirley 摩擦测试仪", "Martindale 耐磨试验机", "Bierengraber 单纱强力测试仪", "Sartorius 电子天平", "Instron 万能试验机", "XRD（X 射线衍射仪）", "SEM（扫描电子显微镜）", "NIR 近红外光谱仪", "Zotero"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
