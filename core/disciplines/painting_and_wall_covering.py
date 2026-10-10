"""油漆与壁纸施工学科论文支持：建筑装饰表面涂装、涂层材料性能与施工工艺研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="painting_and_wall_covering",
    aliases=(
        "painting_and_wall_covering",
        "油漆与壁纸施工",
        "Painting and Wall Covering",
        "建筑涂装",
        "涂层施工",
        "Wall Covering",
        "涂装与饰面",
        "Paint Application",
        "decorative coating"
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
            "case description（工程案例描述）",
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
        "k1": "材料性能测试遵循 ISO 与 GB 系列标准",
        "k2": "施工工艺研究须报告环境与温湿度条件",
        "k3": "耐久性试验须报告加速老化条件与判定阈值"
    },
    conventions=(
        "材料须报告产品型号、批号、施工条件与干膜厚度",
        "测试条件须注明温度、湿度与养护龄期",
        "数据报告须给出均值、标准差与样本量",
        "施工工艺描述须给出工序、层数与工具规格",
        "耐久性结论须区分实验室数据与现场验证"
    ),
    key_venues=(
        "Progress in Organic Coatings",
        "Construction and Building Materials",
        "Surface and Coatings Technology",
        "Coatings",
        "涂料工业"
    ),
    units_and_formulas_notes=(
        "涂层厚度以 μm 报告（湿膜与干膜须区分）",
        "固含量以质量百分比报告并注明溶剂类型",
        "附着力与硬度按标准方法报告并注明测试参数",
        "施工环境与养护条件须以 °C、%RH 记录"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Elcometer 涂层测厚仪", "超声波涂层测厚仪", "划格法附着力测试仪", "拉开法附着力测试仪", "60° 光泽仪", "色差仪", "盐雾试验箱", "氙灯老化试验箱", "温湿度记录仪", "表面粗糙度测试仪", "拉伸强度测试仪", "无气喷涂机", "静电喷涂机器人", "湿膜厚度梳", "涂-4 粘度杯", "电子分析天平", "恒温恒湿箱", "金相显微镜", "OriginPro", "Microsoft Excel"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
