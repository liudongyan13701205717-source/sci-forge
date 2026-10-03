"""岩土工程学科论文支持：土力学/基础/边坡体裁、ASCE 引用样式与岩土记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geotechnical_engineering",
    aliases=("geotechnical_engineering", "岩土工程", "岩土", "土力学",
             "基础工程", "边坡工程"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与岩土问题）",
            "methods（试验、建模与参数）",
            "results（土性/变形数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "site_characterization": (
            "abstract",
            "introduction",
            "site conditions（场地条件）",
            "investigation program（勘察方案）",
            "laboratory/field tests（室内/现场试验）",
            "geotechnical model（岩土模型）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "project background（工程背景）",
            "design（设计）",
            "construction and monitoring（施工与监测）",
            "performance（性能评价）",
            "references",
        ),
    },
    citation_style="ASCE 样式（作者-年份；ASCE 期刊遵循 ASCE 规范）",
    reporting_standards={
        "experimental": "土工试验遵循 ASTM D 系列标准",
        "site_characterization": "场地勘察遵循 ISSMGE 建议方法",
        "numerical": "数值分析遵循 ISSMGE 数值方法规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "case_study": "案例研究遵循 ISSMGE 案例报告规范",
    },
    conventions=(
        "土体分类（USCS）与物理指标须报告",
        "强度/变形参数须注明试验方法",
        "地下水位与孔压条件须说明",
        "安全系数与设计准则须明确",
        "监测项目与仪器须报告",
    ),
    key_venues=(
        "Journal of Geotechnical and Geoenvironmental Engineering",
        "Géotechnique",
        "Canadian Geotechnical Journal",
        "Soils and Foundations",
        "Géotechnique Letters",
        "Computers and Geotechnics",
    ),
    units_and_formulas_notes=(
        "应力用 kPa/MPa；含水量用 %；重度用 kN/m³",
        "公式用 amsmath；有效应力与固结方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "渗透系数用 m/s 或 cm/s",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("PLAXIS", "GEOSTUDIO", "MATLAB", "FLAC3D"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Zenodo", "CNKI"),
)