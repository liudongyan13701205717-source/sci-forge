"""光子学学科论文支持：光学/激光/光纤体裁、OSA 引用样式与光子学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="photonics",
    aliases=("photonics", "光子学", "光子", "光学工程", "激光", "光纤光学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与光子学问题）",
            "methods（器件、实验与参数）",
            "results（光谱/效率数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "device_demonstration": (
            "abstract",
            "introduction",
            "device design（器件设计）",
            "fabrication（制备工艺）",
            "characterization（表征）",
            "performance（性能与讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "state of the art（现状分类）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="OSA 样式（作者-年份；Optica/OSA 期刊遵循 OSA 规范）",
    reporting_standards={
        "experimental": "光学实验遵循 OSA 实验报告规范",
        "device": "器件表征遵循 IEEE 光子器件报告规范",
        "simulation": "光学仿真遵循 SPIE 仿真报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "metrology": "计量遵循 NIST 光学计量规范",
    },
    conventions=(
        "波长/频率单位须规范（nm、THz）",
        "光源与探测器参数须完整报告",
        "功率/效率定义须明确（W、dBm、%）",
        "材料折射率与色散数据须注明来源",
        "仿真软件与网格/边界条件须说明",
    ),
    key_venues=(
        "Optica",
        "Optics Express",
        "Optics Letters",
        "Journal of Lightwave Technology",
        "Photonics Research",
        "Applied Optics",
    ),
    units_and_formulas_notes=(
        "波长用 nm；功率用 mW/dBm；效率用 %",
        "公式用 amsmath；耦合模与传输方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "dB 与线性单位换算须注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("Zemax", "COMSOL", "MATLAB", "Python（NumPy/SciPy）", "光谱仪"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI"),
)