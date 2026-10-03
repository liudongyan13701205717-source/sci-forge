"""纺织工程学科论文支持：纺织材料/工艺/染整体裁、Textile Institute 引用样式与纺织记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="textile_engineering",
    aliases=("textile_engineering", "纺织工程", "纺织", "纺织材料", "染整",
             "纤维工程"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与纺织问题）",
            "methods（材料、工艺与测试）",
            "results（纤维/织物性能数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "process_study": (
            "abstract",
            "introduction",
            "materials（原料与规格）",
            "process design（工艺设计）",
            "experiments（试验与参数）",
            "results and analysis（结果与分析）",
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
    citation_style="Textile Institute 样式（作者-年份；Textile Research Journal 遵循其规范）",
    reporting_standards={
        "experimental": "纤维/织物测试遵循 Textile Institute 测试规范",
        "quality_control": "质量控制遵循 ISO 纺织品测试标准",
        "sustainability_assessment": "可持续性评价遵循 ISO 14040 LCA 框架",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "mechanical_testing": "力学测试遵循 ASTM D 纺织品标准",
    },
    conventions=(
        "纤维细度（dtex、denier）单位须规范",
        "织物结构参数（经纬密、组织）须报告",
        "测试条件（温湿度、标准）须注明",
        "染整工艺参数（温度、时间、浓度）须完整",
        "性能指标（强力、耐磨、透气）定义须一致",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of the Textile Institute",
        "Fibers and Polymers",
        "Journal of Engineered Fibers and Fabrics",
        "Cellulose",
        "Textile Research Journal (TRJ)",
    ),
    units_and_formulas_notes=(
        "细度用 dtex/denier；强力用 cN/dtex 或 N",
        "公式用 amsmath；织物几何与性能方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 标准差与样本量",
        "透气率用 mm/s；克重用 g/m²",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("SolidWorks", "Instron 万能材料试验机", "纺织品检测仪器（透气率/色牢度）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)