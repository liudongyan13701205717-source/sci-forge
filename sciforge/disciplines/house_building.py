"""房屋建筑学科论文支持：建筑结构/施工组织/施工管理研究体裁、IEEE/GB 引用样式与结构力学单位注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="house_building",
    aliases=(
        "house_building",
        "房屋建筑",
        "建筑工程",
        "House Building",
        "Building Construction",
        "建筑技术",
        "土木工程",
        "Civil Construction",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714 样式（作者-年份；工程类亦常用 IEEE 数字引用）",
    reporting_standards={"k1": "结构研究须报告荷载工况", "k2": "施工案例须说明施工周期", "k3": "材料试验须报告试件编号"},
    conventions=(
        "荷载/材料参数给出取值依据",
        "单位统一为 SI 制",
        "计算书须给出边界条件",
        "案例须注明地理位置与气候区",
        "图纸比例与编号须规范",
    ),
    key_venues=(
        "Building and Environment",
        "Construction and Building Materials",
        "Engineering Structures",
        "Journal of Constructional Steel Research",
        "Automation in Construction",
    ),
    units_and_formulas_notes=(
        "力/力矩单位统一为 kN/kN·m",
        "应力单位统一为 MPa",
        "温度/湿度给出单位",
        "误差与置信区间须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "Revit", "ArchiCAD", "PKPM", "YJK 盈建科", "MIDAS Civil", "SAP2000", "ETABS", "STAAD.Pro", "ANSYS", "ABAQUS", "3ds Max", "SketchUp", "Photoshop", "Excel", "SPSS", "MATLAB", "Python", "Matlab/Simulink", "Endnote"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
