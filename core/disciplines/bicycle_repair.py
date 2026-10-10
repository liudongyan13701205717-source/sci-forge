"""自行车维修（Bicycle Repair）学科论文支持：故障诊断、维修工艺、材料与备件技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bicycle_repair",
    aliases=(
        "bicycle repair", "bicycle maintenance", "自行车维修", "自行车保养",
        "bike servicing", "cycle servicing", "故障诊断", "bicycle troubleshooting",
        "自行车修理", "two-wheeler service",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与诊断需求）",
            "materials and methods（诊断流程、试验设计）",
            "results（故障模式与数据）",
            "discussion（机理与工艺改进）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "故障现象",
            "诊断过程与工具",
            "维修方案与结果",
            "references",
        ),
        "review": (
            "abstract",
            "背景",
            "故障模式分类",
            "诊断技术综述",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 7；工程类亦可遵循 GB/T 7714",
    reporting_standards={
        "diagnostic_flow": "诊断流程须画出决策树或流程图（工具-测量-判定）",
        "failures": "故障模式（磨损、裂纹、疲劳、松动）须按 FMEA 或 Weibull 分布分类",
        "torque_specs": "关键扭矩值（碗组、把立、五通、轮组）须按厂商规格给出",
        "tools": "诊断工具型号、精度、校准日期须报告",
        "reproducibility": "样本量、车型谱系与维修历史须交代",
    },
    conventions=(
        "扭矩单位统一 N·m，精度按厂商规格",
        "故障模式用故障树（FTA）或鱼骨图（Ishikawa）表达",
        "维修前后性能指标对比（如踏板效率、轮组真圆度）须成对报告",
        "维修工具与备件须列出品牌与型号",
        "维修工时与安全规程须遵循 ISO 11946 类规范",
    ),
    key_venues=(
        "Journal of Bicycling Research",
        "Applied Engineering in Agriculture（车辆诊断相关）",
        "Journal of Mechanical Design",
        "中国机械工程",
        "Manufacturing Engineering Journal",
        "Bicycle News Technical",
    ),
    units_and_formulas_notes=(
        "扭矩 N·m；力 N；位移 mm；角度 °",
        "故障率用 λ(t) 或 Weibull 参数（β、η）表达",
        "MTBF/MTTR 单位小时或骑行公里",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Park Tool 扭力扳手（TP-2 / HG-0.3 / FC-3）", "Shimano 官方工具（TL-FH99 扭力计等）", "Lezyne 工具套装", "Continental 电子扭力计", "Savik 扭力扳手", "Cotter 扭力计", "千分表（Mitutoyo / Fowler）", "游标卡尺（Mitutoyo / Starrett）", "超声波探伤仪（EPOCH 650 / Omniscope）", "工业内窥镜（Delsigma / Veeco）", "光学显微镜（Nikon / Olympus）", "激光测距仪（Leica DISTO）", "电子充气泵（Minnick / Continental）", "骑行台（Wahoo Kickr / Rolando R7）", "功率计（Stages / SRM / Power2max）", "轴承压装机（Bench vise / Shimano FC-17）", "中轴取出器（Park Tool FR-5 / Shimano TL-FC31）", "3D 打印机（Prusa MK4 / Ultimaker S5）", "3D 打印耗材（PLA / PETG / ASA / Nylon）", "Fusion 360", "SolidWorks", "Fusion 360 Simulation", "Ansys Mechanical", "LabVIEW（试验台控制）", "MATLAB（数据处理）", "Minitab（可靠性统计）", "SPSS", "SolidCAM / Mastercam", "LaTeX"),
    category="工学",
    databases=("OpenAlex", "Scopus", "CNKI", "IEEE Xplore"),
)
