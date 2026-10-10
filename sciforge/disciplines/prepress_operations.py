"""印刷前作业学科论文支持：印前数据处理、色彩管理与印刷制版工艺研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="prepress_operations",
    aliases=(
        "prepress operations", "印刷前作业", "印前制作",
        "pre-press", "印前",
        "print production", "印刷制作",
        "color management", "色彩管理",
        "CTP", "计算机直接制版",
        "halftoning", "加网",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（印刷问题与工艺背景）",
            "methodology（色彩测量、样品设计与分析）",
            "results（色差、网点增大与再现性）",
            "discussion（工艺影响与改进建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（产品与工艺流程）",
            "analysis（印前环节与质量控制）",
            "results（成品质量与交付效果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（色彩理论与印前技术理论）",
            "evidence synthesis（工艺与标准证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "k1": "色差按 ISO 11664-6 的 CIE Delta E 报告",
        "k2": "网点增大率按 ISO 12647-2 报告并注明区域（阴影/中调/亮调）",
        "k3": "密度测量须注明光源、观察者与几何条件（如 D50/2°）",
    },
    conventions=(
        "色差以 Delta E 表示并注明测量仪器与照明条件",
        "网点增大率按面积百分比报告并注明印刷区域",
        "分辨率与加网线数须注明 lpi（lines per inch）与角度",
        "印刷样品须注明纸张类型、涂层与克重",
        "色彩转换须说明 ICC 配置文件版本与渲染意图",
    ),
    key_venues=(
        "Journal of Imaging Science",
        "Color Research & Application",
        "Journal of Applied Spectroscopy",
        "Applied Spectroscopy",
        "Journal of Printing Science and Technology",
    ),
    units_and_formulas_notes=(
        "Delta E 以无色数值表示，目视限度 ≤ 1.5（ISO 12647-2 优级）",
        "印刷密度以吸光度 log 值表示，K 密度通常 ≥ 1.4",
        "网点增大率以百分比表示，T10/T50/T85 分区报告",
        "加网线数以 lpi 表示，常用 150–200 lpi",
        "墨色密度须注明测量仪器型号与测量模式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe InDesign", "Adobe Photoshop", "Adobe Illustrator", "Adobe Acrobat Pro", "QuarkXPress", "CorelDRAW", "EFI Fiery 印前处理器", "Xerox iMF 印前系统", "Kodak Trendsetter 数字制版系统", "HP Indigo 数字印刷机", "Komori Lithrone 胶印机", "Heidelberg Speedmaster 胶印机", "X-Rite i1Profiler 色彩管理", "Datacolor SpectroColor 分光光度计", "X-Rite SpectroEye 测色仪", "Konica Minolta CM-2600d", "Zeiss 测量显微镜", "MATLAB 图像处理", "Python OpenCV", "Python Pillow"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
