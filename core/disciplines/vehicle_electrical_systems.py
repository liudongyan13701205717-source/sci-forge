"""车辆电气系统学科论文支持：整车 E/E 架构、高压系统与网络通信的体裁、IEEE 引用样式与电路记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vehicle_electrical_systems",
    aliases=(
        "vehicle_electrical_systems",
        "车辆电气系统",
        "汽车电气与电子",
        "整车电子电气架构",
        "vehicle e/e architecture",
        "EV power electronics",
        "车载网络",
        "CAN bus"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（系统瓶颈与需求）",
            "methods（电路/控制/协议设计与验证方案）",
            "results（试验波形、效率与实测数据）",
            "discussion（机理、失效模式与对比）",
            "conclusion",
            "references",
        ),
        "system_design": (
            "abstract",
            "introduction",
            "requirements（功能与电气需求分解）",
            "architecture（架构与接口定义）",
            "implementation（电路实现与验证）",
            "verification results（EMC、热、功能安全验证）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（E/E 架构与标准体系综述）",
            "evidence synthesis（方案与标准证据归纳）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（数字编号 [1]，IEEE Trans. / Proc. 缩写）",
    reporting_standards={
        "电气性能": "功率与效率须注明测量工况、仪表精度与温度；损耗与温升给出持续工作稳态值",
        "EMC 与绝缘": "报告所依据的标准（如 CISPR 25、ISO 11452/11454、IEC 60068）与试验等级，给出通过/偏离判定",
        "功能安全": "按 ISO 26262 说明安全目标与 ASIL 分解，报告危害分析与残余风险",
        "通信与协议": "CAN/LIN/以太网报文须给出信号定义、周期、刷新率与容错策略，实测波形与规范对比"
    },
    conventions=(
        "全文采用 SI 单位：电压 V/kV、电流 A、功率 kW、频率 Hz、能量 kWh",
        "高压系统统一标注额定电压与工作电压，绝缘试验按 kV 给出等级",
        "控制算法给出输入输出定义与时间步长，离散实现说明采样率与滤波",
        "电路与框图按同一编号体系，信号线用统一线型与网络标号",
        "标准引用写明标准号、版本与年份（如 ISO 26262:2018）"
    ),
    key_venues=(
        "IEEE Transactions on Industrial Electronics",
        "IEEE Transactions on Transportation Electrification",
        "SAE International Journal of Transportation",
        "Electric Power Components and Systems",
        "汽车技术"
    ),
    units_and_formulas_notes=(
        "电气功率 P = √3·U·I·cos φ（三相）与 P = U·I·cos φ（单相）须标明相数与功率因数",
        "电池容量以 Ah 与 kWh 同时给出，SOC 定义注明是否含可用容量区间与截止电压",
        "绝缘电阻按 MΩ 报告并注明施加电压与保持时间（如 500 V / 60 s）",
        "效率以百分比报告并给出不确定度；功率器件报告导通损耗与开关损耗分项"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("NI Multisim", "PSIM", "PLECS", "LTspice", "MATLAB/Simulink", "AutoCAD Electrical", "EPLAN P8", "Altium Designer", "Vector CANoe", "Vector CANalyzer", "Tektronix 示波器", "Keysight 示波器", "Fluke 435 功率分析仪", "Megger MIT250 绝缘测试仪", "Fluke 87V 万用表", "电池内阻测试仪", "高压耐压测试台", "Saber", "Simetrix", "Python (NumPy)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
