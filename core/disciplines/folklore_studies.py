"""民俗学学科论文支持：民间文学、口头传统、仪式与非物质文化研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="folklore_studies",
    aliases=("folklore_studies", "民俗学", "民间文学", "口头传统", "非物质文化遗产", "民族志", "仪式研究", "地方传说"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论概述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Chicago Notes-Bibliography",
    reporting_standards={"k1": "IFol 田野调查伦理准则", "k2": "UNESCO 非遗记录规范", "k3": "国标 非物质文化遗产记录准则"},
    conventions=("受访者须匿名化并编号（如 P01）", "录音须注明时间码与转录版本", "仪式描述须注明日期、地点与季节", "方言词须附国际音标转写", "口述文本须注明讲述者年龄与性别"),
    key_venues=("Journal of American Folklore", "Folklore Studies", "Loudspeakers", "Ethnologia", "民俗研究"),
    units_and_formulas_notes=("时长单位：min/s", "录音频率须注明 Hz", "文本长度以字数计", "坐标须注明 WGS-84"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo（质性分析）", "ATLAS.ti", "MaxQDA", "ELAN 多模态标注工具", "Praat（语音分析）", "Audacity（录音处理）", "ZoomText（文本分析）", "LaTeX（排版）", "EndNote（文献管理）", "Zotero", "QGIS（地理编码）", "Dendrogram 词形分析", "Python NLTK（文本统计）", "IPA 音标工具", "Tobii 眼动仪（注意力研究）", "Sona 调查平台", "Dolphin MCMC", "OpenVSC", "ImageJ（图像标注）", "RStudio（统计检验）"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
