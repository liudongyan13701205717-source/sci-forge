"""机械工程学科论文支持：机械设计/制造/动力学体裁、ASME 引用样式与机械记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mechanical_engineering",
    aliases=("mechanical_engineering", "机械工程", "机械", "机械设计",
             "机械制造", "mechanical design"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与机械问题）",
            "methods（建模、实验与参数）",
            "results（性能与验证数据）",
            "discussion（机理与工程意义）",
            "references",
        ),
        "design": (
            "abstract",
            "introduction",
            "design requirements（需求与约束）",
            "conceptual design（方案与选型）",
            "detailed design（尺寸、公差与校核）",
            "validation（样机与试验）",
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
    citation_style="ASME 样式（作者-年份；ASME 期刊遵循 ASME 规范）",
    reporting_standards={
        "experimental": "台架/样机试验遵循 ASME PTC 性能试验规程",
        "finite_element": "有限元分析遵循 ASME V&V 10/20 验证与确认指南",
        "design": "工程制图与公差遵循 ASME Y14.5 几何公差标准",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "simulation": "数值仿真遵循 ASME V&V 验证与确认框架",
    },
    conventions=(
        "尺寸与公差（GD&T）须按 ASME Y14.5 标注",
        "单位制统一使用 SI；应力/应变符号须规范",
        "材料牌号与热处理状态须注明",
        "疲劳/强度校核给出安全系数与失效准则",
        "试验条件（载荷、转速、温度）须完整报告",
    ),
    key_venues=(
        "Journal of Mechanical Design",
        "Journal of Applied Mechanics",
        "International Journal of Mechanical Sciences",
        "Mechanism and Machine Theory",
        "Journal of Manufacturing Science and Engineering",
        "Journal of Vibration and Acoustics",
    ),
    units_and_formulas_notes=(
        "应力用 MPa；力用 N；扭矩用 N·m",
        "公式用 amsmath；运动学/动力学方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± 不确定度与样本量",
        "模态/振动分析给出频率与阻尼比",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("SolidWorks", "ANSYS", "MATLAB", "Abaqus"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)