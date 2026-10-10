"""直升机工程学科论文支持：航空与结构工程体裁、AIAA 样式与结构记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="helicopter_construction",
    aliases=("helicopter_construction", "直升机工程", "直升机设计", "直升机制造", "旋翼工程", "航空工程", "旋翼系统", "航空构造", "直升机开发"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="AIAA 样式",
    reporting_standards={
        "experimental": "实验研究规范",
        "simulation": "模拟研究规范",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "长度用 m/mm；力用 N/kN",
        "材料性能须报告",
        "结构强度须报告",
        "疲劳分析须报告",
        "单位换算须一致",
    ),
    key_venues=(
        "Aerospace Science and Technology",
        "Journal of Sound and Vibration",
        "Structural Safety",
        "Composite Structures",
        "Engineering Structures",
    ),
    units_and_formulas_notes=(
        "长度用 m/mm；力用 N/kN",
        "公式用 amsmath；结构公式须编号",
        "行内公式避免复杂分式",
        "数值结果给出均值±SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (NumPy/SciPy)", "ANSYS", "SolidWorks", "CATIA V5", "NX", "Creo", "Solid Edge", "Teamcenter", "Simcenter", "Nastran", "Abaqus", "Fluent", "STAR-CCM+", "OpenFOAM", "Blender", "Inventor", "CATIA V6", "CATIA Digital Twin", "Siemens PLM"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
