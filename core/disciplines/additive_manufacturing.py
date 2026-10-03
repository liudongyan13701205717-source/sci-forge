"""增材制造学科论文支持：3D 打印/工艺/材料体裁、ASTM 引用样式与增材制造记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="additive_manufacturing",
    aliases=("additive_manufacturing", "增材制造", "3D打印", "3D 打印",
             "快速成型", "增材"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与增材制造问题）",
            "methods（工艺、材料与参数）",
            "results（力学/微观组织数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "process_optimization": (
            "abstract",
            "introduction",
            "materials（材料与粉末）",
            "process parameters（工艺参数）",
            "experimental design（试验设计）",
            "results（优化结果）",
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
    citation_style="ASTM 样式（作者-年份；Additive Manufacturing 遵循其规范）",
    reporting_standards={
        "experimental": "增材制造试验遵循 ASTM F42 标准",
        "mechanical_testing": "力学测试遵循 ASTM E8/ISO 6892",
        "process": "工艺报告遵循 ISO/ASTM 52900 术语标准",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "quality": "质量保证遵循 ISO/ASTM 52920 规范",
    },
    conventions=(
        "工艺类别（SLM、EBM、FDM 等）须注明",
        "设备型号与工艺参数须完整报告",
        "粉末/丝材规格与批次须说明",
        "后处理（热处理、去应力）须描述",
        "缺陷（孔隙率、裂纹）表征须报告",
    ),
    key_venues=(
        "Additive Manufacturing",
        "Journal of Manufacturing Processes",
        "International Journal of Advanced Manufacturing Technology",
        "Rapid Prototyping Journal",
        "Virtual and Physical Prototyping",
        "Journal of Materials Processing Technology",
    ),
    units_and_formulas_notes=(
        "层厚用 μm；扫描速度用 mm/s；能量密度用 J/mm³",
        "公式用 amsmath；能量密度与热模型方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "孔隙率用 %；粗糙度用 Ra（μm）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("3D 打印机", "材料试验机", "SolidWorks", "ANSYS", "MATLAB"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)