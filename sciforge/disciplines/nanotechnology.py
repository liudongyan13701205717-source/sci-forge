"""纳米技术学科论文支持：纳米材料/纳米器件/纳米表征体裁、ACS 引用样式与纳米记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="nanotechnology",
    aliases=("nanotechnology", "纳米技术", "纳米", "纳米材料", "纳米器件",
             "纳米科学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与纳米问题）",
            "methods（合成、表征与参数）",
            "results（形貌/性能数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "synthesis_study": (
            "abstract",
            "introduction",
            "synthesis（合成方法）",
            "characterization（表征）",
            "properties（性能测试）",
            "discussion（机理讨论）",
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
    citation_style="ACS 样式（作者-年份；ACS Nano 遵循 ACS 规范）",
    reporting_standards={
        "experimental": "纳米材料表征遵循 ACS 表征报告规范",
        "synthesis": "合成方法遵循 ACS 实验方法报告规范",
        "safety": "纳米安全遵循 ISO/TR 12885 指南",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "characterization": "显微表征遵循 ASTM E 系列标准",
    },
    conventions=(
        "粒径/尺寸分布须报告统计方法与样本量",
        "表征手段（TEM、SEM、XRD、XPS）须注明条件",
        "合成前驱体与浓度须完整报告",
        "性能指标（比表面积、带隙）定义须一致",
        "批次间重复性与误差须说明",
    ),
    key_venues=(
        "ACS Nano",
        "Nano Letters",
        "Nature Nanotechnology",
        "Advanced Materials",
        "Nanoscale",
        "Small",
    ),
    units_and_formulas_notes=(
        "尺寸用 nm；比表面积用 m²/g；浓度用 mg/mL",
        "公式用 amsmath；量子尺寸效应等方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "带隙用 eV；粒径分布用 PDI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利", "数据集"),
    tools=("透射电镜（TEM）", "扫描电镜（SEM）", "原子力显微镜（AFM）",
           "X 射线衍射仪（XRD）", "Python（NumPy/SciPy）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv", "CNKI", "万方"),
)