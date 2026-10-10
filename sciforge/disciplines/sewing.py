"""缝纫学科论文支持：服装工艺/家用缝纫技能/服装设计与材料体裁、Chicago 引用样式与工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sewing",
    aliases=("sewing", "缝纫", "家用缝纫", "服装缝制", "sewing skills",
             "garment construction", "domestic sewing", "服装工艺"),
    paper_types={
        "research": (
            "abstract",
            "introduction（缝纫工艺与设计问题）",
            "methods（材料、工艺与施测流程）",
            "results（缝制质量、耐久与人体工学结果）",
            "discussion（工艺改进与教学启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（家用缝纫/服装工艺个案）",
            "analysis（工艺步骤与问题）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（缝制与服装工艺谱系）",
            "evidence synthesis（跨研究证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago Notes and Bibliography 样式（17th，服装与设计学主流）",
    reporting_standards={
        "materials": "材料研究遵循 ASTM D 系列（织物性能）与 ISO 13938 缝线强度",
        "ergonomics": "家用缝纫的人体工学评估遵循 ISO 8559 系列",
        "pattern": "纸样设计须报告尺寸体系、放量规则与版型验证（试制数据）",
    },
    conventions=(
        "缝纫工艺术语（明线、包缝、锁边、暗缝）须按行业惯例使用并首次出现中英对照",
        "线迹规格须用针距（mm）、线迹密度（针/cm）与缝纫速度（RPM）报告",
        "面料按成分（棉/涤/混纺）与克重（g/m²）标注；缝线按股数与色号报告",
        "工艺步骤按操作顺序编号；工序图与爆炸图辅助说明",
        "教学/技能研究须报告被试前经验、练习时长与技能评分（Rubric）",
    ),
    key_venues=(
        "Fashion Theory",
        "Textile Research Journal",
        "International Journal of Clothing Science and Technology",
        "Fashion and Textiles",
        "Clothing and Textiles Research Journal",
    ),
    units_and_formulas_notes=(
        "线距用 mm；线迹密度用针/cm；缝纫速度用 RPM 与 m/min",
        "面料克重用 g/m²；拉伸用 N、伸长率用 %",
        "纸样标注尺寸用 cm；放量规则（ease allowance）须显式列出",
        "样本量 n ≥ 30；技能评分用 1-5 或 1-10 分制报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Singer HD60 Heavy Duty", "Brother CS7000X", "Juki DDL-8100", "Bernina B790", "Pfaff Passport 2.0", "Janome MC6600", "Cricut Maker 3", "Silhouette Cameo 4", "CLO 3D", "Marvelous Designer", "Adobe Illustrator", "Adobe Photoshop", "AutoCAD", "Gerber Accumark", "Lectra Modaris", "TrueGRID", "Inkscape", "Tailor's Dummy/Form", "Tailor's Chalk", "PatternLab"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
