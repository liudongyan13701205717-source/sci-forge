"""物联网学科论文支持：感知/通信/应用体裁、IEEE 引用样式与能耗度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="internet_of_things",
    aliases=("internet_of_things", "物联网", "IoT", "边缘感知"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work（相关工作）",
            "system design（系统设计）",
            "implementation（实现）",
            "evaluation（评估）",
            "references",
        ),
        "application_paper": (
            "abstract",
            "introduction",
            "background（背景：应用场景）",
            "system architecture（系统架构）",
            "deployment（部署）",
            "evaluation（评估与现场数据）",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "taxonomy（分类体系）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号制；IoT-J/INFOCOM 遵循 IEEE 规范）",
    reporting_standards={
        "experimental": "实验遵循物联网系统评估规范",
        "field_deployment": "现场部署遵循真实环境报告规范",
        "benchmark": "基准测试遵循标准协议报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "security": "安全评估遵循威胁模型报告规范",
    },
    conventions=(
        "协议栈（感知/网络/应用层）须明确",
        "硬件平台与传感器型号须报告",
        "能耗与电池寿命须报告",
        "通信协议（LoRa/NB-IoT/ZigBee 等）须说明",
        "现场数据与仿真数据须区分",
    ),
    key_venues=(
        "IEEE Internet of Things Journal",
        "ACM/IEEE International Conference on Internet of Things Design and Implementation (IoTDI)",
        "IEEE International Conference on Communications (ICC)",
        "IEEE INFOCOM",
        "ACM Transactions on Sensor Networks",
        "IEEE Sensors Journal",
    ),
    units_and_formulas_notes=(
        "能耗用 mJ 或 mAh；功率用 mW；传输距离用 m",
        "数据率用 kbps/Mbps；采样率用 Hz",
        "公式用 amsmath；能耗模型公式须编号",
        "数值结果给出均值 ± 标准差与样本量",
        "电池寿命用天（d）或月（mo）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "软件与代码", "专利"),
    tools=("Arduino", "STM32", "Python", "MATLAB"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)