"""蚀刻学科论文支持：蚀刻工艺、微纳加工与表面工程研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="etching",
    aliases=(
        "etching", "蚀刻", "蚀刻工艺",
        "etching process", "蚀刻工艺",
        "microfabrication", "微纳加工",
        "surface engineering", "表面工程",
        "etching technology", "蚀刻技术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（蚀刻问题与背景）",
            "methodology（蚀刻方法、实验条件、效果评估）",
            "results（蚀刻效果与表面评估）",
            "discussion（蚀刻优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "etching process（蚀刻过程）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（技术综述）",
            "comparison（方法对比）",
            "future trends",
            "references",
        ),
    },
    citation_style="ACS",
    reporting_standards={
        "experiment": "实验条件须完整（气体、功率、时间）",
        "analysis": "分析方法须注明（SEM、AFM 等）",
        "safety": "危险气体操作须声明安全规程",
    },
    conventions=(
        "蚀刻速率用 nm/min 表示",
        "选择比用 比值 表示",
        "表面粗糙度用 nm 表示",
        "温度用 °C 表示",
        "压力用 mTorr 表示",
    ),
    key_venues=(
        "Journal of Vacuum Science & Technology",
        "Journal of Micromechanics and Microengineering",
        "Microelectronic Engineering",
        "Journal of The Electrochemical Society",
        "Plasma Processes and Polymers",
        "Journal of Applied Physics",
    ),
    units_and_formulas_notes=(
        "蚀刻速率用 nm/min 表示",
        "选择比用 比值 表示",
        "表面粗糙度用 nm 表示",
        "温度用 °C 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Excel", "SPSS", "Origin", "SEM", "AFM", "Ellipsometer", "Profilometer", "Plasma Etcher", "RIE System", "ICP Etcher", "Wet Etching Station", "XPS", "XRD", "FTIR", "Contact Angle Goniometer", "TEM", "Lithography System"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "ACS Publications"),
)
