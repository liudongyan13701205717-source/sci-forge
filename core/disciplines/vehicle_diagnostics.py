"""车辆故障诊断学科论文支持：状态监测、信号特征提取与故障机理判别的体裁、IEEE 引用样式与信号处理记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vehicle_diagnostics",
    aliases=(
        "vehicle_diagnostics",
        "车辆故障诊断",
        "汽车故障诊断",
        "车载诊断系统",
        "故障检测",
        "vehicle fault diagnosis",
        "OBD",
        "condition monitoring"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（故障机理与诊断难点）",
            "methods（数据采集、特征提取与算法）",
            "results（识别精度与对照试验）",
            "discussion（机理解释与失效模式）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（车辆、故障现象与维修史）",
            "analysis（信号分析与定位过程）",
            "results（确诊结论与修复验证）",
            "discussion（经验与推广）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（诊断方法体系综述）",
            "evidence synthesis（数据集与算法对比证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（数字编号 [1]，IEEE Access / Trans. 缩写规范）",
    reporting_standards={
        "数据集": "须公开样本量、故障类型分布、工况覆盖与划分方式；划分须按对象（车/台架）而非按样本，避免数据泄漏",
        "指标定义": "识别结果报告准确率、精确率、召回率与 F1，多分类须给出混淆矩阵；不得只报总体准确率",
        "工况说明": "信号采集须记录转速、负载、温度与激励条件，明确是否含噪声/缺失/漂移",
        "可复现性": "随机种子、超参数与训练/验证集比例须列出，代码与预处理脚本随文归档"
    },
    conventions=(
        "信号统一标注采样率、通道、量程与滤波设置；波形图横轴为时间 s 或转速 r/min",
        "故障类型用标准命名（如 bearing outer-race fault、ignition coil fault），同一术语全文一致",
        "算法对比在同一数据集与同一划分下进行，报告参数量、推理时间与精度",
        "结论须区分“统计显著”与“工程可用”，给出误判代价说明",
        "CAN/OBD 故障码用标准格式（如 P0301、U0100），并标注协议版本"
    ),
    key_venues=(
        "Mechanical Systems and Signal Processing",
        "IEEE Transactions on Industrial Electronics",
        "SAE International Journal of Transportation",
        "International Journal of Automotive Technology",
        "振动与冲击"
    ),
    units_and_formulas_notes=(
        "时域特征报告 RMS、峰值因子 (peak/RMS)、峭度与包络谱主频，单位与量纲随参数标注",
        "频谱分析给出窗函数、重叠率与分辨率 Δf = fs/N，阶次分析以 rpm 为基准并标注阶次带宽",
        "分类指标 F1 = 2·P·R/(P+R)，多类采用宏平均并报告各类别样本量",
        "CAN 报文以 ID、周期 ms、字节载荷描述；时序异常报告为周期抖动（μs 级）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Autel MaxiSys", "Launch X431", "Snap-on Verus", "Bosch ECU Test", "Delphi DOS-4S", "NI CAN Interface", "Tektronix 示波器", "Rigol 示波器", "Fluke 万用表", "SKF CMS 振动分析仪", "FLIR 红外热像仪", "Bosch KTS", "Foxwell NT690", "ELM327 接口", "Oscilloscope 数据采集卡", "Python (SciPy/PyWavelets)", "MATLAB", "Weibull++ Reliability", "Isograph FaultTree+", "Origin"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
