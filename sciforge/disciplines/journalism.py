"""新闻学学科论文支持：新闻生产/内容/受众体裁、APA 引用样式与社科统计记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="journalism",
    aliases=("journalism", "新闻学", "新闻研究", "新闻传播", "新闻与传播", "新闻与传播学", "新闻与信息研究", "新闻业研究"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）", "methodology（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；Journalism & Mass Communication Quarterly 遵循 APA 规范）",
    reporting_standards={"content_analysis": "内容分析遵循编码信度报告规范", "survey": "调查研究遵循 AAPOR 报告规范", "qualitative": "质性研究遵循 COREQ/SRQR 报告规范"},
    conventions=("抽样框架与时段须说明", "编码者间信度须报告", "新闻伦理与知情同意须交代", "数据来源须注明", "局限与推广性须讨论"),
    key_venues=("Journalism & Mass Communication Quarterly", "Journalism", "Digital Journalism", "Journalism Studies", "Newspaper Research Journal"),
    units_and_formulas_notes=("统计量给出 M/SD/SE/CI", "信度用 Cohen's κ 或 Krippendorff's α", "频数与百分比给出基数", "样本量须报告", "时间用统一时区与格式"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("新闻剪报与档案检索系统", "NVivo（内容编码）", "R（统计与文本挖掘）", "SPSS", "Python（Jieba/NLTK 文本处理）", "Gephi（网络可视化）", "Python（Scrapy 爬虫）", "MuckRock（公开文书检索）", "Wayback Machine（网页存档）", "TrackedChanges（修订追踪）", "Audacity（录音处理）", "OBS Studio（视频制作）", "Google Analytics（受众分析）", "Twitter API（社交媒体数据）", "LinkedIn API（从业者数据）", "RefWorks（文献管理）", "Zotero（参考文献管理）", "Moodle（教学平台）", "Canva（图文设计）", "Adobe InDesign 版面设计工具"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "LexisNexis（法律新闻检索）", "Factiva（新闻数据库）"),
)
