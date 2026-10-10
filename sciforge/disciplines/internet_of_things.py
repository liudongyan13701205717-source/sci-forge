"""物联网（IoT）学科论文支持：感知、网络、平台与嵌入式研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="internet_of_things",
    aliases=("internet of things", "IoT", "物联网", "传感器网络", "嵌入式系统", "边缘计算", "M2M", "万物互联"),
    paper_types={
        "research": ("abstract", "introduction（背景、问题与贡献）", "methodology（系统设计、实现与实验）", "results（性能评估与对比）", "discussion（局限与展望）", "references"),
        "case_study": ("abstract", "introduction", "case description（部署场景与架构）", "analysis（性能、安全与能耗分析）", "results（实测数据）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（IoT 体系结构演进）", "evidence synthesis（协议、平台、场景证据）", "future directions", "references"),
    },
    citation_style="IEEE 会议与期刊样式（编号引用）",
    reporting_standards={
        "k1": "系统架构给分层图与关键模块",
        "k2": "实验环境给硬件、协议、拓扑与规模",
        "k3": "性能指标给吞吐、延迟、能耗与覆盖率",
    },
    conventions=(
        "节点、网关、平台、应用分层图示",
        "协议栈分层图示（物理层到应用层）",
        "能量模型与数据速率公式给出符号定义",
        "实验与仿真分别给出配置",
        "开源资源与代码链接给出"
    ),
    key_venues=(
        "IEEE Internet of Things Journal",
        "IEEE Transactions on Industrial Informatics",
        "ACM Transactions on Sensor Networks",
        "IEEE Internet of Computing",
        "IEEE Transactions on Cybernetics"
    ),
    units_and_formulas_notes=(
        "延迟单位 ms 或 μs，吞吐 kbps 或 Mbps，能耗 mJ/bit 或 mW",
        "电池容量 mAh 与循环次数",
        "覆盖率用 % 或 m² 明确",
        "无线信道给 dBm、dB、Hz"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Arduino", "Raspberry Pi", "ESP32", "STM32", "NodeMCU", "FreeRTOS", "Zephyr RTOS", "Node-RED", "ThingsBoard", "Azure IoT Hub", "AWS IoT Core", "Google Cloud IoT Core", "Eclipse Mosquitto", "libcoap", "The Things Stack", "Zigbee", "Home Assistant", "OpenHAB", "TensorFlow Lite", "NS-3"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
