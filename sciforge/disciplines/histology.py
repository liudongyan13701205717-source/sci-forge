"""组织学学科论文支持：形态学与显微解剖体裁、Vancouver 引用样式与组织学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="histology",
    aliases=("histology", "组织学", "组织解剖学", "组织病理学", "显微解剖学", "组织切片", "组织染色", "组织研究", "组织学技术"),
    paper_types={
        "research": ("abstract", "introduction（背景与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver（作者-序号）",
    reporting_standards={
        "morphological": "形态学研究规范",
        "experimental": "实验研究规范",
        "systematic_review": "PRISMA 声明",
    },
    conventions=(
        "组织学特征须描述",
        "染色方法须报告",
        "显微摄影须报告",
        "图像分析须报告",
        "单位换算须一致",
    ),
    key_venues=(
        "Journal of Histochemistry and Cytochemistry",
        "Histopathology",
        "Methods in Molecular Biology",
        "Journal of Investigative Dermatology",
        "Journal of Cell Science",
    ),
    units_and_formulas_notes=(
        "尺寸用 μm/mm",
        "公式用 amsmath",
        "行内公式避免复杂分式",
        "数值结果给出均值±SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("光学显微镜", "电子显微镜", "免疫组化", "荧光显微镜", "显微摄影", "冰冻切片", "石蜡切片", "HE 染色", "PAS 染色", "特殊染色", "荧光染色", "免疫荧光", "电镜制样", "图像分析软件", "ImageJ", "QuPath", "FIJI", "SPSS", "R", "Python (SciPy)"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
