"""平面设计学科论文支持：视觉传达、版面与品牌设计的研究方法、作品案例评述与评审规范注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="graphic_design",
    aliases=("graphic_design", "平面设计", "平面美术", "visual communication", "视觉传达", "视觉设计", "layout design", "版面设计", "品牌设计"),
    paper_types={
        "research": ("abstract", "introduction（设计问题与研究动机）", "methodology（设计方法、实验或问卷流程）", "results（作品与数据结果）", "discussion（设计决策与影响）", "references"),
        "case_study": ("abstract", "introduction", "case description（项目背景与委托条件）", "analysis（风格、版面与受众分析）", "results（交付物与受众反馈）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（设计理论与流派）", "evidence synthesis（代表作品与文献综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"case_selection": "案例选择须说明标准与代表性（委托方、媒介、时间范围）", "design_process": "设计流程（调研—草图—定稿—输出）须完整披露", "evaluation_protocol": "受众测试与专家评审的评分量表、样本量与信度须报告"},
    conventions=("正文按章节编号；作品图必须编号并在文中引用", "图注写明软件或媒介、尺寸与色彩空间（RGB/CMYK/Pantone）", "字体、字重与字号层级在正文与图注中保持一致", "引用设计作品须标注作者、年份、出处与版权许可", "术语首次出现给出中英文对照"),
    key_venues=("Design Studies", "Design Issues", "Journal of Design Research", "Visual Communication", "Communication Design Quarterly"),
    units_and_formulas_notes=("尺寸用 mm；印刷分辨率 ≥300 dpi，屏幕 72/96 dpi", "色彩以 Pantone 或 CMYK 数值给出，并注明色彩管理配置文件（如 Adobe RGB 1998、sRGB）", "栅格与基准网格尺寸须说明（如 12 栏、基准网格 8 mm）", "排版公式（如版面模块宽高比、面积比）在正文中给出定义并编号"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Photoshop", "Adobe Illustrator", "Adobe InDesign", "Adobe After Effects", "Adobe Experience Design", "Figma", "Sketch", "Affinity Designer", "Affinity Publisher", "Affinity Photo", "CorelDRAW", "Inkscape", "Adobe Bridge", "Adobe Acrobat Pro", "Canva", "Gravit Designer", "Adobe Substance 3D Stager", "Spline", "Miro", "Framer"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
