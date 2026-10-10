"""丝网印刷学科论文支持：丝网印刷工艺/印刷技术/材料应用体裁与工艺规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="screen_printing",
    aliases=("screen_printing", "丝网印刷", "丝印", "网版印刷", "screen printing", "silkscreen", "网版技术", "印花工艺"),
    paper_types={
        "research": ("abstract", "introduction（工艺问题与研究动机）", "methodology（材料与工艺设计）", "results（印刷性能结果）", "discussion（工艺优化讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（丝印案例）", "analysis（工艺与效果分析）", "results（应用效果）", "discussion（启示）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（丝印综述）", "evidence synthesis（工艺对比）", "future directions", "references"),
    },
    citation_style="Chicago 风格（印刷工艺研究常用芝加哥引用）",
    reporting_standards={"case_study": "案例研究遵循 COREQ 规范", "survey": "问卷遵循 AAPOR 规范", "process": "工艺实验遵循 ISO 12647 规范"},
    conventions=("网目数须给出（LPI 或目数）", "油墨规格须给出品牌与型号", "干燥条件须给出温度与时间", "承印物须明确材质", "色彩须给出 CMYK 或 Pantone 号"),
    key_venues=("Journal of Printing Science and Technology", "Journal of Coatings Technology", "Color Research and Application", "Journal of Adhesion", "Journal of Printing Industry", "Packaging Technology and Science"),
    units_and_formulas_notes=("网目数以 LPI 记", "油墨粘度以 mPa·s 记", "干燥温度以 °C 记", "干燥时间以 s 或 min 记"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe Illustrator", "Adobe Photoshop", "CorelDRAW", "InkScape", "Screen Printing Machine (Mimaki)", "Silk Screen Exposure Unit", "Ink Viscosity Viscometer", "Colorimeter (X-Rite)", "Spectrophotometer (Konica Minolta)", "Densitometer (Kodak)", "UV Curing System", "Heat Press", "Screen Printing Table", "Emulsion Mixer", "Screen Drying Oven", "Water-based Ink Tester", "Solvent Analyzer", "Adhesion Tester (3M)", "Wash Test (ASTM)", "Rub Test (ASTM D2001)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
