"""出版设计学科论文支持：书籍/版面/装帧设计评价体裁、印刷工业标准与颜色口径注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="publishing_design",
    aliases=("publishing_design", "出版设计", "书籍设计", "版式设计", "装帧设计", "印前设计", "book design", "typographic design"),
    paper_types={
        "research": ("abstract", "introduction（设计问题与依据）", "methodology（评价方法与样本）", "results（评价数据）", "discussion（设计启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（设计方案）", "analysis（形式与工艺分析）", "results（用户/读者反应）", "discussion（改进方向）", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（作品与文献综合）", "future directions（设计趋势）", "references"),
    },
    citation_style="APA 7（书籍条目注明版次/印次/装帧形式）",
    reporting_standards={"design_evaluation": "设计评价报告量表信度与评分者一致性", "print_spec": "印前参数遵循 ISO 12647/ISO 2846 等印刷工业标准", "color_study": "色彩测量注明仪器校准与观察条件（D50/D65）"},
    conventions=("尺寸用毫米并注明开本（16/32 开）", "印刷颜色区分 CMYK 与专色（Pantone）并注明色号", "字体须给出字号（磅）与字重", "分辨率给 dpi（印刷 300 dpi 以上）", "作品引用给出书名/图版号/年份"),
    key_venues=("Typografia: International Journal of the Typographic Arts", "Design Studies", "Journal of Communication Design", "包装工程", "中国印刷"),
    units_and_formulas_notes=("面积用 mm²，长度用 mm，字号用 pt", "色域与色差用 ΔE（CIE 色空间）", "纸样厚度给 mm/白度给 %", "印前数据校验须报分辨率与出血（3 mm）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe InDesign", "Adobe Photoshop", "Adobe Illustrator", "Adobe Acrobat Pro", "QuarkXPress", "Microsoft Word", "LaTeX", "Affinity Publisher", "GIMP", "Inkscape", "Xara Designer Pro", "Scribus", "LibreOffice Draw", "CorelDRAW", "Adobe Bridge", "Adobe Lightroom", "FontBook", "Pantone Color System", "X-Rite ColorChecker", "Adobe Substance 3D"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
