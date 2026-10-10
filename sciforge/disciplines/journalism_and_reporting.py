"""新闻与报道学科论文支持：新闻报道/新闻生产体裁、APA 引用样式与报道记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="journalism_and_reporting",
    aliases=("journalism_and_reporting", "新闻与报道", "新闻报道", "新闻写作", "journalism and reporting", "news reporting", "news writing", "reporting"),
    paper_types={
        "research": ("abstract", "introduction（报道背景与问题）", "methodology（报道方法与调查）", "results（报道效果与数据）", "discussion（讨论与建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（报道案例）", "analysis（报道手法分析）", "results（社会效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（报道理论综述）", "evidence synthesis（报道实践综述）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；Journalism 遵循 APA 规范）",
    reporting_standards={"content_analysis": "内容分析遵循编码信度报告规范", "survey": "受众调查遵循 AAPOR 报告规范", "ethnographic": "民族志研究遵循 COREQ 报告规范"},
    conventions=("报道来源与时段须注明", "采访伦理与知情同意须交代", "编码信度须报告", "受众样本须说明", "语言与术语须统一"),
    key_venues=("Journalism", "Digital Journalism", "Journalism Studies", "International Journal of Communication", "Newspaper Research Journal"),
    units_and_formulas_notes=("统计量给出 M/SD/CI", "编码者间信度用 Cohen's κ", "受众样本量须报告", "时间用统一时区", "语言须标注语种与翻译说明"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("新闻采访录音设备（Zoom H5）", "专业摄像机（Sony F55）", "新闻摄影单反（Canon EOS R5）", "无人机航拍（DJI Mavic 3）", "GoPro 运动相机", "Audacity（音频处理）", "Adobe Premiere Pro（视频剪辑）", "OBS Studio（直播录制）", "Adobe Photoshop（图像处理）", "Google Maps（地理标记）", "MuckRock（政府文书检索）", "Civis-Cert（公民新闻网络）", "Signal（加密通讯）", "Proofig（文本校对）", "Grammarly（语法检查）", "Hemingway Editor（可读性）", "Zotero（参考文献管理）", "NVivo（质性分析）", "Python（文本挖掘）", "Moodle（教学平台）"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
