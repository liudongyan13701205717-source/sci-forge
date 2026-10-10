"""蒸馏学科论文支持：蒸馏技术、精馏工艺与分离工程体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="distilling",
    aliases=(
        "distilling", "蒸馏", "蒸馏技术",
        "distillation", "蒸馏",
        "rectification", "精馏",
        "separation technology", "分离技术",
        "fractional distillation", "分馏",
        "vacuum distillation", "真空蒸馏",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（分离问题与背景）",
            "methodology（蒸馏方案设计、实验条件、分析）",
            "results（分离效率与产品纯度）",
            "discussion（工艺优化建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology overview（蒸馏技术综述）",
            "comparison（各技术对比）",
            "future trends",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "process analysis（工艺分析）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
    },
    citation_style="ACS",
    reporting_standards={
        "experiment": "实验条件须完整（温度、压力、流量、回流比）",
        "analysis": "分析方法须注明（GC、HPLC等）",
        "safety": "危险物质操作须声明安全规程",
    },
    conventions=(
        "温度用 °C 表示并注明测点位置",
        "压力用 kPa 表示",
        "回流比用 N/R 表示",
        "产品纯度用 % (w/w 或 mol%) 表示",
        "收率用 % 表示",
    ),
    key_venues=(
        "Industrial & Engineering Chemistry Research",
        "Journal of Chemical Engineering Data",
        "Chemical Engineering Science",
        "Separation and Purification Technology",
        "Distillation Design and Operation",
    ),
    units_and_formulas_notes=(
        "温度用 °C 表示",
        "压力用 kPa 表示",
        "流量用 L/min 或 kg/h 表示",
        "回流比用 N/R 表示",
        "理论板数用 N 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (SciPy, NumPy)", "HYSYS", "Aspen Plus", "ChemCAD", "PRO/II", "COMSOL Multiphysics", "OpenFOAM", "Process Simulation Software", "LabVIEW", "SPSS", "Origin", "Excel", "GC", "HPLC", "Density Meter", "Refractometer", "Theoretical Plate Calculator", "Column Simulation Software", "Thermodynamic Database"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "ACS Publications"),
)
