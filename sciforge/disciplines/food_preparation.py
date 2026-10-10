"""烹饪与食品加工学科论文支持：烹饪工艺、食品制备与烹饪科学实验研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="food_preparation",
    aliases=("food_preparation", "烹饪", "食品制备", "烹饪工艺", "烹饪科学", "食品制作", "烘焙工艺", "中式烹饪"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "GB 14881 食品生产卫生标准", "k2": "Codex 食品工艺标准", "k3": "ISO 22000 食品安全管理"},
    conventions=("配方须注明各组分配比（质量分数）", "加热须注明温度、时间与加热方式", "感官评价须注明评分人数与量表（Hedonic）", "pH 值须注明测量温度", "样品编号须注明批次"),
    key_venues=("Food Chemistry", "Journal of Food Science", "Lebensmittel-Wissenschaft und-Technologie", "Food and Bioproducts Processing", "中国烹饪学报"),
    units_and_formulas_notes=("水分含量：%（w/w）", "蛋白质含量：g/100 g", "硬度单位：N", "温度单位：℃（加热）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("质构仪 (Texture Analyzer)", "色差仪 (Minolta CM-3600)", "质构剖面仪 (TPA)", "流变仪 (Rheometer)", "水分活度仪", "近红外光谱仪 (NIR)", "高速相机（烹饪过程记录）", "温度记录仪 (Thermocouple)", "电子天平", "真空密封机", "高压均质机", "SPSS（感官统计）", "Origin（数据绘图）", "RStudio", "LaTeX（排版）", "EndNote（文献管理）", "Python（数据处理）", "Adobe Illustrator（流程图）", "Sensory Evaluation Software", "ImageJ（食品形态分析）"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
