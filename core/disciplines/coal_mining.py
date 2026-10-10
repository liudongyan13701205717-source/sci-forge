"""煤矿开采学科论文支持：采矿工程/煤矿开采体裁、GB/T 引用样式与采矿参数记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="coal_mining",
    aliases=("coal_mining", "煤矿开采", "采矿工程", "井工煤矿",
             "露天采矿", "煤矿安全", "矿山工程",
             "coal mining engineering", "mining engineering",
             "underground coal mining", "surface mining"),
    paper_types={
        "research": (
            "abstract",
            "introduction（采矿条件与工程问题）",
            "mining conditions（地质条件、煤层赋存、开采方法）",
            "design and process（采掘工艺与支护方案）",
            "monitoring and analysis（监测数据与数值分析）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "mine background（矿井简介与开采条件）",
            "mining method and layout",
            "monitoring and analysis",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "state of the art",
            "future directions",
            "references",
        ),
    },
    citation_style="GB/T 7714 样式（中国文献规范）与英文文献采用数字编号",
    reporting_standards={
        "safety": "煤矿安全遵循 GB 50215《煤矿井下安全规程》与 AQ 1082《煤矿安全监控系统及检测仪器使用管理规范》",
        "ventilation": "通风设计遵循 GB 50215、AQ 1029 与《煤矿安全规程》",
        "seam_pressure": "煤与瓦斯突出防范遵循 AQ 1026、AQ 1027",
        "monitoring": "矿压与瓦斯监测遵循 GB/T 25571、AQ 6207",
        "reproducibility": "煤层参数、开采方法与监测设备须给出标准编号与版本年份",
    },
    conventions=(
        "煤层参数（厚度、倾角、瓦斯含量、埋深）须给出具体数值与来源",
        "采矿方法须按《煤矿开采》分类体系标注（长壁/房柱/充填/房柱+充填）",
        "支护方案须给出支架类型、初/末阻、工作/支撑阻力",
        "监测数据须注明采样频率、设备型号与时间窗口",
        "结论须给出煤层条件、开采方法与适用边界",
    ),
    key_venues=(
        "煤炭学报 (Journal of the China Coal Society)",
        "中国矿业大学学报 (Journal of China University of Mining and Technology)",
        "煤炭科学技术 (Coal Science and Technology)",
        "采矿与安全工程学报 (Journal of Mining and Safety Engineering)",
        "International Journal of Mining Science and Technology",
        "Mining Science and Technology",
        "International Journal of Rock Mechanics and Mining Sciences",
    ),
    units_and_formulas_notes=(
        "煤厚、倾角、埋深用 m 与 °",
        "瓦斯含量用 m³/t，瓦斯涌出量用 m³/min",
        "支架阻力用 MN，矿压用 MPa",
        "围岩变形用 mm；位移速率用 mm/d",
        "公式用 amsmath；岩体力学参数（E、σc、μ、φ）须定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("UG/NX (Siemens)", "CATIA", "SolidWorks", "AUTODYN", "3DEC", "FLAC3D", "UDEC", "LS-DYNA", "ANSYS", "Abaqus", "COMSOL Multiphysics", "VentSim", "RoofPro", "Minetec", "DrillCut", "Sightline", "Python (PyGithub, PyTMRaster)", "MATLAB", "Surpac", "Dakota", "Karamba", "GeoStudio"),
    category="工学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)
