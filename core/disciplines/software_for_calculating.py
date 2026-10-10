"""计算软件（电子表格）学科论文支持：表结构建模/公式推导/自动化体裁、IEEE 引用样式与数值精度注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="software_for_calculating",
    aliases=("software_for_calculating", "计算软件", "电子表格", "表格软件", "电子制表", "办公计算"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="IEEE 样式（数字编号制，如 [1]）",
    reporting_standards={
        "reproducibility": "表格文件须给出公式清单与依赖外部数据源版本",
        "accuracy": "数值结果须注明精度与舍入规则，避免浮点误差累积",
        "automation": "宏/VBA/脚本自动化流程须附源码与运行环境说明",
    },
    conventions=(
        "单元格引用写绝对/相对形式（如 $B$2 与 B2），并注明范围语义",
        "财务模型年份轴横向排列，输入区/计算区/输出区分色标注",
        "公式首次出现给出文字释义与量纲检查",
        "百分比、货币、日期单元格格式统一声明",
        "假设参数集中放置于独立输入表并标注取值依据",
    ),
    key_venues=(
        "Journal of Spreadsheet Practice",
        "Engineering Management",
        "Operations Research",
        "Journal of Financial Data Science",
        "Spreadsheet Magazine",
    ),
    units_and_formulas_notes=(
        "数值精度给出有效位数与舍入方向（四舍五入/截断）",
        "货币单位（万元/亿元）与汇率基准日须标注",
        "增长率用几何平均而非算术平均，须说明",
        "公式用 amsmath；单元格公式与数学公式须一一对应",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Microsoft Excel", "LibreOffice Calc", "Google Sheets", "Apple Numbers", "WPS 表格", "OnlyOffice Spreadsheet", "Setasign Calc", "Calligara Sheets", "SoftMaker Office", "Mathcad", "Maple", "Mathematica", "MATLAB", "GeoGebra", "Microsoft Power Query", "Microsoft Power Pivot", "Excel Solver", "Python", "R", "Octave"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
