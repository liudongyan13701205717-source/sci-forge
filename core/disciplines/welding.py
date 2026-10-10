"""焊接学科论文支持：焊接冶金学、连接工艺评价与力学性能测试的专业写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="welding",
    aliases=("welding", "焊接", "焊接工程", "连接技术", "金属熔接", "welding engineering", "joining technology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与现状）",
            "materials and methods（材料与方法）",
            "experimental procedure（工艺参数与试样制备）",
            "results（宏观/微观组织与力学性能）",
            "discussion（机理分析与对比）",
            "conclusion（结论与展望）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工件与工况描述）",
            "process description（焊接工艺描述）",
            "inspection and testing（检测与试验）",
            "analysis（结果分析与问题诊断）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "welding methods overview（焊接方法综述）",
            "process-parameter–property relationships（工艺-性能关系）",
            "defect classification and prevention（缺陷分类与防控）",
            "future directions（前沿方向）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "process parameters": "所有工艺参数（电流、电压、速度、温度）须完整报告并标注单位",
        "specimen preparation": "试样制备过程须详细描述，包括坡口形式、装配间隙与热输入",
        "inspection methods": "无损检测方法须标注依据标准（如 ASTM E、ISO 17635）与操作条件",
        "statistical treatment": "多试样测试须报告样本量、均值、标准差与置信区间",
    },
    conventions=(
        "热输入计算公式明确写出：q = η·V·I/v（η 效率，V 电压，I 电流，v 速度）",
        "焊接方法缩写首次出现时给出全称（如 GMAW、GTAW、SAW、FCAW）",
        "显微组织图须标注放大倍数、腐蚀剂与方向（焊接方向/熔深方向）",
        "力学性能数据须区分焊缝金属（WM）、热影响区（HAZ）与母材（BM）",
        "缺陷分级引用 ISO 5817 或 AWS D1.1 标准等级",
    ),
    key_venues=(
        "Welding in the World",
        "International Journal of Advanced Manufacturing Technology",
        "Journal of Materials Processing Technology",
        "Welding Journal",
        "Science and Technology of Welding and Joining",
    ),
    units_and_formulas_notes=(
        "热输入单位 J/mm；焊接电流单位 A；焊接速度单位 mm/min",
        "硬度用 HV（维氏）或 HRC（洛氏 C 标尺）；抗拉强度用 MPa",
        "熔宽/熔深/余高单位 mm；未熔合/气孔尺寸单位 mm 或 μm",
        "热循环峰值温度单位 ℃；冷却时间 t8/5 单位 s",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("TIG 焊机（GTAW 电源）", "MIG/MAG 焊机（GMAW 电源）", "手工电弧焊焊机（SMAW 电源）", "激光焊接系统（如 IPG Photonics）", "电子束焊接机（EBW 加速器）", "等离子弧焊机", "摩擦焊设备（Friction Welding Machine）", "超声波焊接机（Ultrasonic Welder）", "光学显微镜（OM，含金相显微镜）", "扫描电子显微镜（SEM，如 TESCAN）", "电子探针显微分析仪（EPMA）", "透射电子显微镜（TEM）", "X 射线衍射仪（XRD，如 Bruker D8）", "维氏硬度计（Vickers Hardness Tester）", "洛氏硬度计（Rockwell Hardness Tester）", "万能试验机（UTM，如 Instron）", "疲劳试验机（Fatigue Testing Machine）", "数字图像处理软件（ImageJ / Avizo）", "有限元分析软件（ANSYS / ABAQUS）", "焊接过程模拟软件（SYSWELD / ProCAST）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
