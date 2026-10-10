"""钣金修复（车身钣金）学科论文支持：汽车车身钣金修复、成型工艺与材料力学研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="panel_beating",
    aliases=(
        "panel_beating",
        "钣金修复",
        "Panel Beating",
        "车身钣金",
        "钣金成型",
        "金属钣金工艺",
        "汽车钣金修复",
        "Body Repair",
        "sheet metal forming"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references"
        ),
    },
    citation_style="GB/T 7714-2015",
    reporting_standards={
        "k1": "力学性能测试遵循 ISO 与 ASTM 标准",
        "k2": "工艺参数研究须报告材料与热处理状态",
        "k3": "有限元分析须报告网格、边界条件与实验验证方法"
    },
    conventions=(
        "材料须报告牌号、批号与力学性能测试状态",
        "工艺参数须给出区间与最优解判定依据",
        "有限元模型须报告网格密度、边界条件与实验验证结果",
        "修复变形量以位移量与曲率报告",
        "结果须区分模拟与实验并报告不确定度"
    ),
    key_venues=(
        "Journal of Materials Processing Technology",
        "International Journal of Crashworthiness",
        "SAE International Journal of Commercial Vehicles",
        "Welding Journal",
        "汽车工程"
    ),
    units_and_formulas_notes=(
        "应力与应变以 MPa 与 % 报告并注明测试标准",
        "变形量以 mm 与 mm/m 报告",
        "温度以 °C 报告并注明测温位置",
        "有限元网格尺寸须报告并做收敛性分析"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("大梁校正仪", "车身拉拔机", "三维车身测量系统", "Go!Set4 测量系统", "便携式 3D 车身扫描仪", "MIG/MAG 焊接机", "电阻点焊机", "拉钉枪", "热塑性塑料加热枪", "钣金剪", "钣金锤", "电烙铁", "拉伸试验机", "XRF 光谱分析仪", "金相显微镜", "ABAQUS", "ANSYS", "Autodesk Inventor", "OriginPro", "Microsoft Excel"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
