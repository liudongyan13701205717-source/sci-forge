"""时间生物学学科论文支持：时间生物学/生物节律体裁、APA 引用样式与时间生物学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chronobiology",
    aliases=("chronobiology", "时间生物学", "生物节律", "昼夜节律", "chronobiology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与节律问题）",
            "methods（实验设计与节律测量）",
            "results（节律参数数据）",
            "discussion（节律机理）",
            "references",
        ),
        "longitudinal_study": (
            "abstract",
            "introduction",
            "methods（纵向设计与测量）",
            "results（节律相位与振幅）",
            "discussion（与既往研究对比）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；J Biol Rhythms 遵循 APA 规范）",
    reporting_standards={
        "longitudinal": "纵向研究遵循节律测量报告规范",
        "experimental": "实验研究遵循 APA 报告规范",
        "observational": "观察性研究遵循 STROBE 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "preregistration": "预注册研究遵循预注册报告规范",
    },
    conventions=(
        "光照条件与时间表须报告",
        "节律测量方法（褪黑素、体温等）须注明",
        "节律参数（相位、振幅、周期）须定义",
        "时区与当地时间换算须明确",
        "统计方法（cosinor、FFT 等）须报告",
    ),
    key_venues=(
        "Journal of Biological Rhythms",
        "Chronobiology International",
        "Sleep",
        "Journal of Pineal Research",
        "Frontiers in Physiology",
        "Current Biology",
    ),
    units_and_formulas_notes=(
        "时间用 h/min；相位用 h 或角度（°）",
        "公式用 amsmath；cosinor 拟合与周期计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD/SEM 与样本量",
        "节律显著性给出 p 值与振幅置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("ClockLab 节律分析仪", "Actogram Analyst", "Lima Clock 生物钟可视化", "Chronoclock", "Chronoscope", "Actiware Activity/Rest Analysis", "Oral T (Oral T Sleep Monitor)", "Oral C (Oral T Corp)", "Ambulatory Blood Pressure Monitor (ABPM)", "Actigraphy 腕带式活动记录仪（ActiGraph GT9X）", "ActiGraph wGT9X Link", "Axivity AX3/AX6", "Bioniq iButton", "Luxmeter (照度计)", "Circadian Lighting System (Light Therapeutics)", "Sensotronics 2008", "Luminex 200/300 (褪黑素/皮质醇 ELISA)", "Bio-Techne Enzyme-Linked Immunosorbent Assay", "Enzyme Linked Immunosorbent Assay (ELISA)", "Real-time PCR (Bio-Rad CFX96)", "QuantStudio 5 (Applied Biosystems)", "Thermal Cycler (Mettler TOPTec)", "Western Blot (Bio-Rad ChemiDoc)", "Flow Cytometer (BD FACSCanto II)", "qPCR 引物设计", "R 时间序列分析", "Python (NumPy/SciPy/Chronobiology)", "Chronos (时间序列工具)", "cosinor R 包", "cosinor_4", "cosinor_5", "cosinor_6", "Rhythm", "JChrono", "ChronoS", "Chronos (Google Research)", "Chronos (ChronoStats)", "ChronoStats", "TimeGazer", "TimeGazer (Spectral Analysis)", "SpectrAnalysis Rhythm R 包", "Spectral Density (Welch's method)", "Fast Fourier Transform (FFT)", "Short-Time Fourier Transform", "MATLAB Signal Processing Toolbox", "OriginLab", "GraphPad Prism", "IBM SPSS Statistics", "SAS (SAS Institute)", "Statistica", "GEO (NCBI Gene Expression Omnibus)", "Metaboanalyst", "Molecular Modeler", "PyMOL", "UCSF ChimeraX", "ChimeraX Volume Analysis"),
    category="理学",
    databases=("PubMed", "OpenAlex", "Crossref", "GEO"),
)