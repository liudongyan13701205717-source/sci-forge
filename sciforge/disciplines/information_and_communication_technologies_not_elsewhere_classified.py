"""信息通信技术（未另分类）学科论文支持：信息通信技术跨领域应用与未细分方向研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="information_and_communication_technologies_not_elsewhere_classified",
    aliases=(
        "information_and_communication_technologies_not_elsewhere_classified",
        "信息通信技术（未另分类）",
        "ICT 未另分类",
        "信息通信技术",
        "通信技术与信息科学",
        "ICT (not elsewhere classified)",
        "information and communication technologies",
        "IC technologies general",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式（工程技术）或 APA 7 样式（应用研究）",
    reporting_standards={
        "system_design": "系统设计须报告架构、性能指标与可复现性",
        "field_trial": "现场试验须注明样本量、地理分布与测试时长",
        "simulation": "仿真须注明工具版本与参数",
        "survey": "调查须报告响应率与抽样方法",
    },
    conventions=(
        "ICT 术语须注明 3GPP 版本与频段",
        "性能指标须注明测试条件（信道、负载、硬件）",
        "引用标准须注明 ISO/IEC 编号与版本",
        "统计量须给 95% CI",
        "可复现性须附代码与配置",
    ),
    key_venues=(
        "IEEE Transactions on Information Technology in Biomedicine",
        "IEEE Communications Magazine",
        "Information Systems Journal",
        "International Journal of Communication Systems",
        "计算机工程与应用",
    ),
    units_and_formulas_notes=(
        "带宽/速率单位用 bps/Mbps/Gbps，须注明",
        "延迟用 ms，须注明单向/往返",
        "吞吐量须注明并发数与测试方法",
        "统计量须给 M/SD/95% CI",
        "显著性检验须说明方法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python（numpy/scipy/pandas）", "GNU Radio", "NS-3（网络仿真）", "OPNET", "CST（电磁仿真）", "ANSYS HFSS", "Wireshark", "Xilinx FPGA", "National Instruments 数据采集", "Keysight 网络分析仪", "Rohde & Schwarz 频谱分析", "Docker", "R", "SPSS", "Jupyter Notebook", "PostgreSQL", "Kafka（流数据）", "Grafana（监控）", "Elasticsearch"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
