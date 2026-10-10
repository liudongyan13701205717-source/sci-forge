"""烘焙与糕点工艺学科论文支持：食品工程/感官评价体裁、食品科学引用样式与工艺参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pastry_cooking",
    aliases=("pastry cooking", "烘焙与糕点工艺", "糕点工艺", "西点工艺", "bread baking", "pâtisserie", "食品工艺", "食品科学", "烘焙科学"),
    paper_types={
        "research": ("abstract", "introduction（工艺或消费问题）", "methodology（配方与工艺设计）", "results（质构/感官/货架期）", "discussion（机理与工业化）", "references"),
        "case_study": ("abstract", "introduction", "case description（产品与工艺流程）", "analysis（配方与工艺变量）", "results（产品表现）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（食品科学理论）", "evidence synthesis（配方与工艺综述）", "future directions", "references"),
    },
    citation_style="Vancouver/APA 样式（食品科学领域常用；配方与工艺须可复现引用）",
    reporting_standards={"recipe": "配方须给出精确质量或体积比、原料来源与状态", "process": "工艺参数（温度、时间、湿度、搅拌转速）须报告并给出精度", "sensory": "感官评价遵循 ISO 8589 与 GB/T 系列", "nutrition": "营养标签遵循 GB 28050 或当地法规", "replication": "重复实验次数与统计检验须报告"},
    conventions=("配方使用质量比（baker's percentage）或体积比须明确", "温度单位用 °C；时间用 min/h", "原料首次出现给出学名或商品名与规格", "工艺流程图按 ISO 图示规范绘制", "感官评价员资格与培训须说明"),
    key_venues=("Food Hydrocolloids", "Journal of Cereal Science", "LWT - Food Science and Technology", "Food Chemistry", "Journal of Food Engineering", "Journal of Culinary Science & Technology"),
    units_and_formulas_notes=("温度用 °C；体积用 mL/L；时间用 min/h", "配方比例给出 %（baker's percentage）并注明基准", "含水率、失重率、pH 等物理量定义须明确", "感官评分遵循 9 点或 15 点标度并标注"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("食品流变仪", "质构仪（TA.XT）", "烘箱与蒸汽炉", "恒温恒湿培养箱", "色差仪（Colorimeter）", "电子天平", "食品水分测定仪", "气相色谱-质谱联用仪（GC-MS）", "高效液相色谱仪（HPLC）", "近红外光谱分析仪（NIR）", "pH 计", "电子显微镜（SEM）", "SPSS 统计分析", "R 统计分析", "Python (NumPy, SciPy)", "OriginPro 绘图", "Minitab 实验设计", "ImageJ 图像处理", "Minitab Design-Expert", "Food-4-All 数据集"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
