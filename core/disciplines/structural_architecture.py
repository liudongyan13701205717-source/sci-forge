"""Structural architecture 学科论文支持：结构表现主义/参数化设计/结构拓扑优化。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="structural_architecture",
    aliases=(
        "structural_architecture", "Structural architecture",
        "结构建筑", "结构表现主义", "参数化建筑设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与结构问题）",
            "methods（建模与优化方法）",
            "results（结构性能与设计方案）",
            "discussion（讨论与工程意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景）",
            "analysis（结构分析）",
            "results（设计成果）",
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
    citation_style="ASCE 样式（作者-年份）",
    reporting_standards={
        "structural_analysis": "结构分析须报告边界条件、荷载与材料参数",
        "optimization": "拓扑优化须报告目标函数、约束条件与优化算法",
        "bim_model": "BIM 模型须报告 LOD（模型精细度）与版本",
        "performance": "结构性能须报告安全系数、位移与变形",
    },
    conventions=(
        "材料强度（混凝土/钢材）等级须注明",
        "荷载组合与分项系数须按规范说明",
        "构件截面与配筋/连接细节须完整",
        "有限元网格独立性分析须报告",
        "BIM 模型须注明 LOD 与软件版本",
    ),
    key_venues=(
        "Journal of Architectural Engineering",
        "Automatika",
        "Architectural Research Quarterly",
        "Engineering Structures",
        "建筑结构学报",
    ),
    units_and_formulas_notes=(
        "应力用 MPa；力用 kN；位移用 mm",
        "结构安全系数 β 与目标失效概率须给出",
        "优化目标函数与约束条件须编号",
        "数值结果给出均值 ± 不确定度与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Rhino（Rhinoceros 3D 建模）", "Grasshopper（参数化设计）", "Karamba 3D（结构分析插件）", "Karamba（结构优化）", "Forma（3ds Max 参数化建模）", "3ds Max", "Revit（BIM 建模）", "Archicad（BIM 建模）", "Autodesk Robot Structural Analysis", "ANSYS（有限元分析）", "MIDAS Gen", "Dynamo（BIM 参数化设计）", "Navisworks（BIM 协调平台）", "SketchUp（三维建模）", "AutoCAD（制图）", "Lumion（建筑可视化渲染）", "Enscape（实时渲染）", "FormIt（建筑体块建模）", "V-Ray（渲染器）", "混凝土 3D 打印机（数字建造）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
