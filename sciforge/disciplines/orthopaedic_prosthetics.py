"""矫形假肢学科论文支持：假肢设计、康复评估与临床效果评价。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="orthopaedic_prosthetics",
    aliases=(
        "orthopaedic_prosthetics",
        "矫形假肢学",
        "Prosthetics and Orthotics",
        "假肢矫形器",
        "康复工程",
        "Rehabilitation Engineering",
        "Bionics",
        "智能假肢",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与临床问题）",
            "methodology（设计与评估方法）",
            "results（生物力学/临床结果）",
            "discussion（设计与应用讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（病例与假肢配置）",
            "analysis（功能分析）",
            "results（康复效果）",
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
    citation_style="Vancouver（康复/生物医学期刊）/ GB/T 7714（中文）",
    reporting_standards={
        "clinical_trial": "CONSORT 声明",
        "device_study": "ISO 10993 生物相容性",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "ISO 编码（如 A1C1L5）须报告",
        "步态参数用国际术语（步长/步幅/支撑相）",
        "肌电数据须去基线与带通滤波记录",
        "评估量表使用 ISAK/SS-Q/COMPASS-Q",
        "临床试验须注册并报告伦理编号",
    ),
    key_venues=(
        "Journal of Rehabilitation Research and Development",
        "Prosthetics and Orthotics International",
        "Journal of Applied Biomechanics",
        "Restorative Neurology and Neuroscience",
        "Chinese Journal of Rehabilitation Medicine",
    ),
    units_and_formulas_notes=(
        "步频用 steps/min，步速用 m/s",
        "地面反作用力用 N 或 %BW",
        "关节力矩以 N·m 报告",
        "肌电归一化用 %MVC",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Vicon 光学运动捕捉", "BTS SMARTSuit DX", "Kistler Force Plates", "Delsys Trigno EMG", "MATLAB / Simulink（信号处理）", "R（统计）", "SPSS", "SolidWorks（建模）", "ANSYS（有限元）", "Fusion 360", "Photoshop", "Origin（绘图）", "EndNote", "LaTeX", "Excel", "Gait Pro / C3D 分析软件", "OpenSim（多体仿真）", "3D Scanner (Artec Eva)", "SLA Printer (Formlabs)", "MyoWare EMG 模块"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
