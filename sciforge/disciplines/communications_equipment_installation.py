"""通信设备安装学科论文支持：网络部署/光纤施工/维护管理体裁、IEEE 引用样式与工程记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="communications_equipment_installation",
    aliases=("communications equipment installation", "通信设备安装",
             "网络施工", "光纤安装", "通信工程",
             "network installation", "fiber optic installation",
             "telecommunications construction", "cable installation"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与工程需求）",
            "methodology（施工方法与技术方案）",
            "results（实施结果与测试数据）",
            "discussion（分析与改进建议）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "site description（站点概况与条件）",
            "installation process（施工过程）",
            "acceptance testing（验收测试）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "state of the art（现状分类）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="IEEE 样式（编号制）",
    reporting_standards={
        "installation": "安装工程遵循 GB 51171 通信管道与通道工程设计规范",
        "fiber_splicing": "光纤接续遵循 GB/T 50886 通信线路工程设计规范",
        "acceptance": "验收测试遵循 GB/T 1236 光缆交接箱标准",
        "safety": "施工安全遵循 GB 26859 电力安全工作规程",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "安装方案须符合国家标准（GB）与运营商规范",
        "测试报告须给出验收标准与实测数据对照",
        "布线须符合规范并标注线序、色标与标签",
        "变更管理须走审批流程并记录变更日志",
        "工程文档须包含竣工图纸与测试报告",
    ),
    key_venues=(
        "IEEE Network",
        "IEEE Communications Surveys & Tutorials",
        "Computer Networks",
        "IEEE Transactions on Network and Service Management",
        "IEEE Systems Journal",
        "中国通信",
        "电信工程",
    ),
    units_and_formulas_notes=(
        "光纤衰减用 dB/km；带宽用 MHz/Gbps/Tbps",
        "距离用 m/km；温度用 ℃",
        "公式用 amsmath；链路预算方程须编号",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "测试结果给出均值 ± 标准差与测试次数",
        "回波损耗给出 dB 值与测试频率",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Cisco Packet Tracer", "GNS3", "EVE-NG", "Wireshark", "PuTTY", "TFTP Server", "NMAP", "SolarWinds", "Cisco NAC Manager", "Huawei U2000", "Huawei eSight", "OTDR (Optical Time Domain Reflectometer)", "Spectrum Analyzer", "Optical Power Meter", "Fusion Splicer", "Fiber Identifier", "LCR Meter", "Continuity Tester", "Insulation Tester", "VFL (Visual Fault Locator)", "Fiber End-face Inspector", "Light Source and Power Meter", "Cable Tracer", "Cable Punch-down Tool", "Cable Tester (Fluke)", "Microsoft Visio", "AutoCAD"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方"),
)
