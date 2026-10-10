"""木材加工技术学科论文支持：木材科学与加工体裁、Wood Science and Technology 引用样式与木材记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="timber_technology",
    aliases=("timber_technology", "木材加工技术", "木材科学", "木制品加工", "林业工程",
             "wood science", "wood technology", "木材保护", "胶合工程"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与木材科学问题）",
            "materials and methods（试样与测试方法）",
            "results（力学性能与表征结果）",
            "discussion（机理与工程应用）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工程/加工案例）",
            "analysis（性能分析与优化）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "sample_specification": "试样树种、含水率、尺寸与取材方向须明确",
        "testing_standard": "力学测试遵循 ISO 3831 / GB/T 1936 等标准",
        "moisture_content": "含水率报告至小数点后一位",
        "statistical_analysis": "样本量≥3，数据以均值±标准差报告",
    },
    conventions=(
        "树种用拉丁学名斜体表示，中文俗名括注",
        "含水率（%）定义须明确（绝干重/湿重）",
        "力学性能单位统一用 MPa 或 GPa",
        "密度用 kg/m³ 表示，注明基准温度",
        "实验条件（温度、湿度）须记录",
    ),
    key_venues=(
        "Wood Science and Technology",
        "Holzforschung",
        "Wood Science and Engineering",
        "Construction and Building Materials",
        "Bioresource Technology",
    ),
    units_and_formulas_notes=(
        "力学性能单位：抗压/抗弯强度用 MPa，弹性模量用 GPa",
        "密度单位 kg/m³；含水率单位 %",
        "胶合强度单位 MPa，断裂韧性单位 MPa·m^1/2",
        "公式用 amsmath 排版；木材干缩系数定义须明确",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("万能材料试验机", "电木压刨床", "木材含水率测定仪", "红外光谱仪（FTIR）", "扫描电子显微镜（SEM）", "X 射线衍射仪（XRD）", "热重分析仪（TGA）", "动态力学分析仪（DMA）", "木材硬度计", "数显电子天平", "高温高压蒸煮锅", "真空干燥箱", "砂带机", "木工开榫机", "胶合压机", "木材密度计", "色差仪", "高倍光学显微镜", "Origin Pro", "MATLAB"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
