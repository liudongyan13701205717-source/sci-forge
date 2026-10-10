"""印刷术（Lithography）学科论文支持：胶版印刷工艺与印前印后技术。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="lithography",
    aliases=(
        "lithography",
        "印刷术",
        "胶版印刷",
        "litho printing",
        "平版印刷",
        "offset printing",
        "prepress",
        "print media",
        "CMYK",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工艺背景）",
            "methodology（实验方法）",
            "results（实验结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（工艺分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（文献综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="ISO 690",
    reporting_standards={
        "k1": "色彩还原报告使用 ΔE 与仪器型号",
        "k2": "胶版印刷参数须记录压力、温湿度",
        "k3": "印刷油墨测试按 ISO 284 系列执行",
    },
    conventions=(
        "色彩数据标注测量仪器与色域",
        "印刷工艺参数给出单位与重复次数",
        "油墨配方以体积比与质量比明确区分",
        "印张测试使用 ISO 12647 标准条",
        "环保指标注明 VOC 与溶剂限量",
    ),
    key_venues=(
        "Journal of Printing Science and Technology",
        "Applied Spectroscopy",
        "Polymer Degradation and Stability",
        "Color Research and Application",
        "Print Week",
    ),
    units_and_formulas_notes=(
        "色差 ΔE 采用 CIE 1976 或 CIE 2000",
        "网点扩大率以 % 记录",
        "密度测量使用 D 值并标注几何",
        "油墨粒径以 nm 报告并给出 D50",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("X-Rite eXact", "X-Rite DTP9430", "GretagMacbeth Eye-One i2 Display", "Konica Minolta CM-3600d", "Bauert GMS 330", "Pantum Graphix", "Heidelberg Prinect", "KBA Rapida", "KBA Speedmaster", "Comexi Digital", "Ridder Printers", "GMG FineTones", "Ergo Soft RIP", "Adobe Photoshop", "Adobe InDesign", "Adobe Illustrator", "CorelDRAW", "Tiffen Digital Duet", "Agfa Onyx RIP", "EFI Fiery Color Server"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
