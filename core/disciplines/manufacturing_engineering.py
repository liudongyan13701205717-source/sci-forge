"""制造工程学科论文支持：工艺、装配、生产系统与增材制造体裁、SI 单位与工艺参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="manufacturing_engineering",
    aliases=("manufacturing_engineering", "制造工程", "制造业工程", "制造学", "生产制造",
             "Manufacturing Engineering", "Production Engineering", "Process Engineering",
             "智能制造", "先进制造"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题陈述与工业需求）",
            "methodology（工艺建模、仿真、实验台架与数据采集）",
            "results（结果与统计分析）",
            "discussion（讨论与工艺优化空间）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（车间/产线描述）",
            "analysis（工艺瓶颈与改进方案）",
            "results（改进前后对比）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（工艺与系统集成综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="ANSI/BibTeX 样式（工程编号制；IEEE 亦可）",
    reporting_standards={
        "repeatability": "实验须报告重复样本数与工艺稳定性（Cpk/Ppk）",
        "tool_wear": "涉及刀具/模具须报告磨损量与寿命曲线",
        "dimensional_accuracy": "几何量测须遵循 ISO 1101 GD&T 与 ISO 2768 公差",
        "energy_consumption": "涉能耗须报告单位产品能耗（J/piece 或 kWh/kg）",
        "safety": "涉及高压/高温/切削须报告 EHS 与安全护栏",
    },
    conventions=(
        "采用 SI 单位，转速用 r/min 或 rad/s 并统一",
        "工艺参数须明示范围与名义值，误差用 ± 或 3σ",
        "CAD/CAE/CAM 数据链须注明模型版本与公差传递",
        "生产数据须注明采集节拍、传感器与信号处理",
        "对比实验须控制变量并报告统计显著性",
    ),
    key_venues=(
        "International Journal of Production Research",
        "CIRP Annals - Manufacturing Technology",
        "International Journal of Advanced Manufacturing Technology",
        "Journal of Manufacturing Systems",
        "Manufacturing & Production Operations Management",
        "Computer-Aided Design",
    ),
    units_and_formulas_notes=(
        "长度单位：毫米（mm）；速度单位：米每分钟（m/min）",
        "功率单位：千瓦（kW）；能量单位：千焦（kJ）或千瓦时（kWh）",
        "切削参数：f（进给 mm/rev）、v_c（切削速度 m/min）、a_p（背吃刀量 mm）",
        "效率 η = P_输出 / P_输入；良率 Y = N_good / N_total",
        "节拍时间 CT = T_batch / N_items（秒/件）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Siemens NX", "PDM/PLM（Teamcenter）", "MES（制造执行系统）", "MATLAB", "Python（pandas/NumPy）", "Ansys Mechanical", "Abaqus", "COMSOL Multiphysics", "UGNX CAM", "Mastercam", "SolidWorks", "CNC 加工中心（Fanuc/ Siemens SINUMERIK）", "工业机器人与示教器（KUKA/ABB）", "3D 打印（SLM/SLS 设备）", "三坐标测量机（CMM，Zeiss）", "激光测头（Keyence）", "数字孪生平台（NVIDIA Omniverse）", "数据采集与 SCADA（Rockwell FactoryTalk）", "公差分析仪（GD&T，PC-DMIS）", "工艺仿真（Adams/Process）"),
    category="工学",
    databases=("OpenAlex", "Crossref", "ScienceDirect", "IEEE Xplore", "CNKI"),
)
