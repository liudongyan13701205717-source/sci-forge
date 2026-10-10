"""糖果/糖果工艺学科论文支持：食品科学/工艺技术/质构与感官评价体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="confectionery",
    aliases=(
        "confectionery", "糖果", "糖果工艺", "confectionery science",
        "糖果食品科学", "sugar confectionery", "巧克力", "chocolate",
        "食品工艺", "food technology", "糖果技术",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "materials and methods（原料、配方与工艺）",
            "results（理化、质构与感官数据）",
            "discussion（机理分析与优化）",
            "conclusion",
            "references",
        ),
        "product_development": (
            "abstract",
            "background",
            "product specification",
            "formulation and process（配方与工艺）",
            "sensory evaluation",
            "shelf-life study",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method",
            "main developments",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 7 或 Springer 样式（食品科学常用）",
    reporting_standards={
        "sensory": "感官评价遵循 ISO 8586/ISO 13299（标准/描述性面板）",
        "shelf_life": "货架期研究须报告储存条件、时间序列与加速实验",
        "process": "工艺参数（温度、时间、湿度）须给出区间与重复次数",
        "statistics": "感官数据须给出重复次数、面板成员数与 ANOVA 结果",
    },
    conventions=(
        "配方须给出原料种类、质量分数与添加顺序",
        "工艺参数（结晶温度、退火温度、糖化时间）须用统一单位并给出控制范围",
        "感官描述用语须遵循 ISO 13299 描述性术语",
        "统计结果给出均值 ± 标准差与显著性（p 值）",
        "术语表首次出现即给出缩写与全称",
    ),
    key_venues=(
        "LWT - Food Science and Technology",
        "Food Research International",
        "Journal of Food Engineering",
        "International Journal of Food Science & Technology",
        "Food Chemistry",
        "Journal of Sensory Studies",
        "European Journal of Lipid Science and Technology",
    ),
    units_and_formulas_notes=(
        "温度用 ℃；时间用 min/h；水分活度用 a_w",
        "硬度和粘弹性用 MPa / Pa·s；色泽用 L*a*b* 或 CIELAB",
        "公式用 amsmath；感官评分用统一量表（1-5 或 1-9）",
        "数值结果给出均值 ± 标准差与 p 值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Texture Analyzer (TA.XT Plus / Brookfield)", "DSC (Differential Scanning Calorimetry)", "Rheometer (Anton Paar / TA Instruments)", "GC-MS (Gas Chromatography-Mass Spectrometry)", "HPLC (High-Performance Liquid Chromatography)", "FTIR (Fourier Transform Infrared Spectroscopy)", "Colorimeter (Konica Minolta CM-700d)", "Water Activity Meter (NovaSys / Rotronic)", "Viscometer (Brookfield)", "Mfract (Marsden Fractograph)", "Sensory Panel Software (Sensometer / Compusense)", "Minitab", "R (sensR/sensTools)", "SPSS", "Excel", "InDesign / LaTeX", "MATLAB", "TGA (Thermogravimetric Analyzer)", "XRD (X-ray Diffractometer)", "NIR (Near-Infrared Spectroscopy)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "SciFinder"),
)
