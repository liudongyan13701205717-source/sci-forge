"""图形复制学科论文支持：印前处理、制版工艺与印刷色彩复制的设备、方法与色彩管理注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="graphic_reproduction",
    aliases=("graphic_reproduction", "图形复制", "图像复制", "print reproduction", "印刷复制", "印前处理", "prepress", "制版工艺", "色彩管理"),
    paper_types={
        "research": ("abstract", "introduction（复制质量问题与研究动机）", "methodology（原稿、制版与印刷流程）", "results（色彩、网点与批间差异）", "discussion（工艺参数对质量的影响）", "references"),
        "case_study": ("abstract", "introduction", "case description（承印物与印件规格）", "analysis（分色、网点与专色工艺分析）", "results（色值与外观检验结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（色彩学与复制原理）", "evidence synthesis（工艺与设备文献综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714",
    reporting_standards={"color_target": "色彩与外观目标须声明（如 ISO 12647-2 A/B 级、ISO 2846 专色）", "measurements": "密度、色差与网点须报告仪器型号、测量几何（45/0° 或 0/45°）与温湿度", "reproducibility": "批间与机间重复性须给出 ΔE*ab、ΔK、网点扩大率与样本量"},
    conventions=("分色顺序按 CMYK 报告，并注明叠印、加网角与加网线数", "色彩差以 ΔE*ab 报告，注明白点（D50/D65）与观察者（2°）", "网屏角度按 15°/30°/45°/75° 约定标注", "打样与上机色样须编号并记录拍摄条件", "引用印刷标准须写明 ISO 或 ANSI 编号与年份"),
    key_venues=("IST International Journal of Imaging Science", "The Color Research and Application", "Coloration Technology", "包装工程", "印刷学报"),
    units_and_formulas_notes=("纸张用 g/m²；网点面积用 %；加网线数用 lpi；扫描用 dpi", "色差用 ΔE*ab（CIE 1976），标注白点与观察者角度", "公式用 LaTeX（amsmath）；反射密度与网点扩大率定义须在正文给出", "测量结果给出具体数值与仪器条件（如 ΔE*ab = 1.4, D50, 2°）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "Adobe Acrobat Pro", "Adobe Acrobat Preflight", "Kodak Kapusta", "Kodak CGS", "Heidelberg Prinect", "EFI Fiery", "Harlequin RIP", "X-Rite i1 Pro 3", "Datacolor Spyder5", "GretagMacbeth Eye-One Advanced", "Heidelberg Speedmaster", "Komori Lithrone", "Roland SM-1000", "Canon Vela", "Xerox iGen 5", "Epson SureColor P80800", "Agfa Avinci"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
