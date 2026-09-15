"""生物学科论文支持：实验设计/对照规范、GO 词条与资源可追溯。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="biology",
    aliases=("biology", "生物", "细胞", "cell biology", "遗传", "genetics",
             "生态", "ecology", "演化", "evolution", "分子生物学", "molecular"),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "results（结果先行，按逻辑递进组织图版）",
            "discussion（解释、局限与模型）",
            "materials and methods（材料与方法，可入文末）",
            "acknowledgments（致谢与资助）",
            "references",
        ),
        "resource": (
            "abstract",
            "introduction（资源动机与适用范围）",
            "results（资源构建与验证）",
            "discussion（使用建议与局限）",
            "materials and methods",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按机制/问题组织的进展）",
            "outstanding questions（未解问题）",
            "references",
        ),
    },
    citation_style="作者-年份或编号（视期刊：Cell 编号 / eLife 作者-年份）",
    reporting_standards={
        "experimental_design": "随机化、盲法与生物学重复数须显式声明；动物实验按 ARRIVE 2.0 报告",
        "controls": "须含阳性/阴性对照与无关对照，并说明对照的生物学合理性",
        "resources": "抗体、细胞系、模式生物须给出来源与目录号（RRID），并说明验证方式",
        "data": "组学/测序数据存档（GEO/SRA/ArrayExpress）并给出登录号；图像原始数据可用",
        "statistics": "统计检验给出 n、检验类型、p 值与效应量；多重比较须校正并注明方法",
    },
    conventions=(
        "基因符号斜体、蛋白符号正体（如 SHH 基因 / SHH 蛋白），物种规范随数据库（如 MGI/HGNC）",
        "物种首次出现给拉丁学名（斜体）与品系名",
        "图版多面板以 a/b/c 标注，每个面板可独立阅读",
        "缩写首次出现给出全称并收入缩写表",
        "结果小节标题使用陈述句（如 X activates Y），不使用方法式标题",
    ),
    key_venues=(
        "Cell",
        "Nature",
        "eLife",
        "PNAS",
        "Nature Methods",
    ),
    units_and_formulas_notes=(
        "浓度 µM/mg·mL⁻¹；分子量 kDa；离心力以 ×g 表示而非 rpm",
        "统计图给出独立重复数（n）与误差棒含义（SD/SEM/95% CI）",
        "剂量-时间曲线注明给药途径与频次",
        "基因型命名按标准记法（如 c.123A>G, p.R45H）",
        "图像定量注明采集参数（曝光、显微镜型号）保持组间一致",
    ),
)
