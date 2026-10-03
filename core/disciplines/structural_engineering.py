"""结构工程学科论文支持：结构分析/抗震/设计体裁、ASCE 引用样式与结构记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="structural_engineering",
    aliases=("structural_engineering", "结构工程", "结构", "结构设计",
             "抗震工程", "钢结构"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与结构问题）",
            "methods（试验、建模与参数）",
            "results（承载力/变形数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "structural_design": (
            "abstract",
            "introduction",
            "design criteria（设计准则与规范）",
            "loads（荷载与组合）",
            "analysis（结构分析）",
            "design（构件与节点设计）",
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
    citation_style="ASCE 样式（作者-年份；ASCE 期刊遵循 ASCE 规范）",
    reporting_standards={
        "experimental": "结构试验遵循 ASTM E 系列标准",
        "seismic": "抗震设计遵循 ASCE 7 荷载规范",
        "design": "钢结构遵循 AISC 规范；混凝土遵循 ACI 318",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "finite_element": "有限元分析遵循 NAFEMS 验证与确认指南",
    },
    conventions=(
        "荷载组合与分项系数须按规范说明",
        "材料强度（混凝土、钢材）等级须注明",
        "构件截面与配筋/连接细节须完整",
        "抗震设防烈度/类别须明确",
        "试验加载制度与量测方案须报告",
    ),
    key_venues=(
        "Journal of Structural Engineering",
        "Engineering Structures",
        "Earthquake Engineering & Structural Dynamics",
        "Journal of Constructional Steel Research",
        "Journal of Structural Engineering (ASCE)",
        "Structural Safety",
    ),
    units_and_formulas_notes=(
        "应力用 MPa；力用 kN；弯矩用 kN·m",
        "公式用 amsmath；刚度/稳定方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "位移用 mm；频率用 Hz",
    ),
    paper_capable=True,
    contribution_forms=("论文", "数据集"),
    tools=("SAP2000", "ETABS", "ANSYS", "MATLAB"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Zenodo", "CNKI"),
)