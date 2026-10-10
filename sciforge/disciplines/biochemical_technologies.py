"""生化技术（Biochemical Technologies）学科论文支持：生物反应器、分离纯化、发酵工程与工艺开发。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biochemical_technologies",
    aliases=(
        "biochemical technologies", "生物化工技术", "bioprocess engineering",
        "生物过程工程", "发酵工程", "fermentation technology", "生物反应器",
        "bioreactor", "生物制药工艺", "biosynthesis", "合成生物学工艺",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、工艺需求与瓶颈）",
            "materials and methods（菌种/培养基/工艺参数/分析）",
            "results（菌体生长、产量、纯度、转化率）",
            "discussion（机理、放大可行性与工艺改进）",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "背景",
            "工艺类型综述（分批发酵/连续发酵/补料分批发酵）",
            "设备与放大",
            "outlook",
            "references",
        ),
        "process_development": (
            "abstract",
            "背景",
            "工艺开发路线（菌种→种子→发酵→下游）",
            "工艺参数与放大",
            "质量控制",
            "references",
        ),
    },
    citation_style="ACS 或 Nature 系列；中文类遵循 GB/T 7714",
    reporting_standards={
        "strain": "菌种鉴定（16S rRNA、基因组）与传代次数须交代",
        "medium": "培养基配方、pH、温度、DO、搅拌、通气须完整",
        "bioreactor": "反应器型号、体积、工作体积、灭菌参数须报告",
        "analysis": "HPLC/GC-MS/qPCR/流式等分析方法须报告参数与检出限",
        "scaleup": "中试与放大须遵循相似准则（如 kLa、P/V 恒定）",
        "gmp": "若涉及药物生产须遵循 GMP 或 ISO 14644 洁净度",
    },
    conventions=(
        "菌种名用斜体，学名与保藏编号（如 CGMCC、ATCC）齐备",
        "工艺参数按温度/DO/pH/搅拌/通气的顺序报告",
        "产物质量用 mg/L 或 g/L 报告；转化率 g/g 或 %",
        "动力学模型（Monod、Luedeking-Piret）须给出拟合参数",
        "误差棒定义（SD/SEM）与生物学重复数须报告",
    ),
    key_venues=(
        "Biochemical Engineering Journal",
        "Biotechnology and Bioengineering",
        "Biotechnology Progress",
        "Journal of Biotechnology",
        "Applied Microbiology and Biotechnology",
        "Metabolic Engineering",
    ),
    units_and_formulas_notes=(
        "浓度 mg/L、g/L、mmol/L；温度 °C；pH 无量纲",
        "生物量 g/L 或 OD600（注明比色波长与菌种）",
        "产物得率 Yp/s、Yp/x；比生长速率 μ (h^-1)",
        "公式用 amsmath；动力学方程须给出参数含义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Cytiva Biostat B 系列生物反应器", "Sartorius BioCout/STF 生物反应器", "Bello Life Sci. 发酵罐", "BioLector（高通量发酵）", "Thermo Fisher FBM 520（发酵罐）", "Thermo Q Exactive (LC-MS)", "Thermo Orbitrap Exploris (LC-MS)", "Agilent 6550 Q-TOF (GC-MS)", "Waters ACQUITY UPLC (HPLC)", "Shimadzu HPLC（LC-20A）", "ÄKTA Pure/Explorer（层析系统）", "Cytiva AKTA Go（层析）", "Beckman Coulter Avanti（超速离心机）", "Thermo Sorvall（离心机）", "Eppendorf 5424R（台式离心机）", "Thermo Scientific QuantStudio qPCR", "Bio-Rad CFX Opus qPCR", "Bio-Rad Gel Doc（凝胶成像）", "Bio-Rad ChemiDoc（Western blot 成像）", "BD FACSCanto 流式细胞仪", "BD FACSMelody 流式分选", "CellaVision 自动细胞计数", "Hamilton Microlab STAR（自动化液体处理）", "Tecan Freedom EVO（液体处理工作站）", "Sartorius BabyMixer 3D（摇床）", "Shakers（New Brunswick 摇床）", "Biomation 自动化", "Cytomat（细胞培养自动化）", "Cytomat Bioreactor（自动化培养）", "Cytomat（自动化细胞处理）", "CO2 培养箱（Thermo、Eppendorf）", "恒温培养箱（Incubator）", "冻干机（Labconco FreeZone）", "超滤/切向流过滤系统", "亲和层析磁珠", "Protein A/G 亲和层析", "离子交换层析（IEC）", "反相层析（RPC）", "体积排阻层析（SEC）", "透析袋（Spectra/Pierce）", "PCR 仪（Thermo GeneAmp）", "热循环仪（Eppendorf Mastercycler）", "NanoDrop（核酸定量）", "Qubit 荧光定量仪（Thermo）", "Benchtop UV-Vis（Shimadzu UV-1800）", "酶标仪（BioTek Synergy、Tecan Infinite）", "Thermo Scientific NanoDrop（UV-Vis）", "Shimadzu UV-Vis（分光光度计）", "ImageJ / Fiji", "GraphPad Prism", "R", "Python (Biopython, NumPy, SciPy)", "LaTeX"),
    category="工学",
    databases=("PubMed", "Europe PMC", "OpenAlex", "Scopus", "BMC", "CNKI"),
)
