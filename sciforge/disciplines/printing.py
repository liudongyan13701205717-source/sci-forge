"""印刷学科论文支持：胶印/数码印刷流程、色彩复制与批次一致性的设备、方法与色彩管理注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="printing",
    aliases=("printing", "印刷", "印刷技术", "印刷工艺", "print production", "胶印", "数码印刷", "offset printing", "digital printing"),
    paper_types={
        "research": ("abstract", "introduction（印刷质量与研究动机）", "methodology（原稿、制版、加印与印后流程）", "results（色彩、网点与批次差异）", "discussion（工艺参数对质量的影响）", "references"),
        "case_study": ("abstract", "introduction", "case description（印件规格与承印物）", "analysis（分色、网点与专色工艺分析）", "results（色值与外观检验结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（色彩学与印刷复制原理）", "evidence synthesis（工艺与设备文献综合）", "future directions", "references"),
    },
    citation_style="GB/T 7714",
    reporting_standards={"k1": "印件规格与承印物须完整声明（尺寸、克重、涂层）", "k2": "色彩与外观目标须声明标准等级（如 ISO 12647-2 A/B 级）", "k3": "批次与机间重复性须给出 ΔE*ab、网点扩大率与样本量"},
    conventions=("分色按 CMYK 报告并注明加网线数与网点角", "色差以 ΔE*ab 报告并标注白点（D50/D65）与观察者（2°）", "测量须注明仪器型号、测量几何（45/0° 或 0/45°）与温湿度", "承印物注明 g/m² 与涂层类型", "引用印刷标准须写明 ISO 或 ANSI 编号与年份"),
    key_venues=("印刷学报", "包装工程", "The Color Research and Application", "IST International Journal of Imaging Science", "Coloration Technology"),
    units_and_formulas_notes=("纸张用 g/m²；网点面积用 %；加网线数用 lpi；扫描用 dpi", "色差用 ΔE*ab（CIE 1976），标注白点与观察者角度", "反射密度用 D 表示并区分实测与计算值", "公式用 LaTeX（amsmath）并给出定义"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "Adobe Acrobat Preflight", "Kodak Kapusta", "Kodak CGS", "Heidelberg Prinect", "EFI Fiery", "Harlequin RIP", "X-Rite i1 Pro 3", "Datacolor Spyder5", "Heidelberg Speedmaster", "Komori Lithrone", "Roland SM-1000", "Canon Vela", "Xerox iGen 5", "HP Indigo", "Epson SureColor P80800", "Agfa Avinci", "Konica Minolta CM-2600d"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
