"""铁道车辆检修与运维学科论文支持：故障诊断/无损检测/可靠性体裁、ANSI/ASME 引用与检测参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="train_repair_and_maintenance",
    aliases=("train_repair_and_maintenance", "铁道车辆检修与运维", "铁路检修",
             "列车维修", "轨道工程运维",
             "railway maintenance", "train repair", "track maintenance",
             "rolling stock maintenance", "predictive maintenance"),
    paper_types={
        "research": (
            "abstract",
            "introduction（故障现象与维修问题）",
            "methods（检测方案、试验台架与数据分析）",
            "results（缺陷检出率与损伤量化）",
            "discussion（与既有方法的比较及工程意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "operating conditions and failure history",
            "inspection and diagnosis",
            "repair scheme and verification",
            "lessons learned",
            "references",
        ),
        "reliability_analysis": (
            "abstract",
            "introduction",
            "failure data collection and preprocessing",
            "modeling and parameter estimation",
            "results（寿命分布与可靠度）",
            "maintenance strategy implications",
            "references",
        ),
    },
    citation_style="IEEE 或 ASME 样式",
    reporting_standards={
        "ndt": "无损检测须报告设备型号、耦合剂与灵敏度（参考 GB/T 或 ISO 标准）",
        "fatigue": "疲劳试验须报告应力比 R、频率与终止准则",
        "reliability": "可靠性分析须报告样本量、审查等级与置信度",
        "repair": "修复方案须给出工艺参数与验收标准",
        "data": "振动/温度等数据须报告采样率与工况",
    },
    conventions=(
        "缺陷描述须标注位置（车轮/轴颈/轨面）、类型与尺寸",
        "检测参数须注明来源标准（如 GB/T 21947 探伤灵敏度）",
        "可靠性指标须给出置信度与样本量",
        "维修方案须说明工艺参数与验收判据",
        "图像须附比例尺与检测方向标注",
    ),
    key_venues=(
        "Journal of Railway and Track Science",
        "Reliability Engineering & System Safety",
        "Mechanical Systems and Signal Processing",
        "International Journal of Fatigue",
        "Journal of Rail Transport Planning and Technologies",
        "铁道学报",
    ),
    units_and_formulas_notes=(
        "疲劳应力用 MPa，寿命用循环次数（cycles）",
        "振动加速度用 m/s²，频谱分析须注明采样率与窗函数",
        "探伤灵敏度以 dB 或反射波幅百分比报告",
        "可靠度 R(t) 与失效率 λ(t) 须明确定义",
        "MTBF 与 MTTR 须注明统计口径",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("轮对探伤仪", "超声波探伤仪", "磁粉探伤机", "涡流检测系统", "红外热像仪", "振动分析仪", "轴承温升检测仪", "轨道几何状态测量仪", "钢轨探伤车", "接触网检测车", "轨距尺", "车轮测量仪", "ANSYS", "ABAQUS", "SolidWorks", "CATIA", "NASTRAN", "MATLAB/Simulink", "Weibull++", "Minitab"),
    category="工学",
    databases=("IEEE Xplore", "ScienceDirect", "CNKI", "万方", "OpenAlex"),
)
