"""职业健康人机工程学科论文支持：职业医学、工作环境与健康促进研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="ergonomics_occupational_health_and",
    aliases=(
        "ergonomics_occupational_health_and", "职业健康人机工程",
        "ergonomics occupational health and safety", "职业健康人机工程",
        "occupational health", "职业健康",
        "workplace safety", "工作场所安全",
        "occupational medicine", "职业医学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（职业健康问题与背景）",
            "methodology（实验设计、人体测量、评估方法）",
            "results（职业健康效果与评估）",
            "discussion（职业健康优化建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "occupational analysis（职业分析）",
            "results（效果评估）",
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
    citation_style="APA 7",
    reporting_standards={
        "experiment": "实验条件须完整（受试者、任务、环境）",
        "measurement": "人体测量须注明测量方法与工具",
        "statistics": "统计检验须注明方法与显著性水平",
    },
    conventions=(
        "人体尺寸用 cm 表示",
        "力量用 N 表示",
        "角度用 ° 表示",
        "时间用 ms 表示",
        "统计检验注明方法、p 值与效应量",
    ),
    key_venues=(
        "Ergonomics",
        "Applied Ergonomics",
        "Human Factors",
        "International Journal of Industrial Ergonomics",
        "Journal of Biomechanics",
        "Ergonomics in Design",
    ),
    units_and_formulas_notes=(
        "人体尺寸用 cm 表示",
        "力量用 N 表示",
        "角度用 ° 表示",
        "时间用 ms 表示",
        "统计检验注明 t/F/χ² 值、p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (numpy, scipy)", "R (RStudio)", "Excel", "SPSS", "Origin", "Motion Capture System", "Force Plate", "EMG System", "Eye Tracker", "Pressure Mat", "Goniometer", "Dynamometer", "Anthropometer", "3D Body Scanner", "CAD Software", "Ergonomic Assessment Software", "RULA Software", "REBA Software", "NIOSH Lifting Equation Software"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "IEEE Xplore"),
)
