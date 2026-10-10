"""新闻与信息类（其他）学科论文支持：新闻与信息学交叉研究体裁、APA 引用样式与信息科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="journalism_and_information_not",
    aliases=("journalism_and_information_not", "新闻与信息类其他", "新闻信息学", "新闻与信息研究", "journalism and information", "information studies", "information science", "information management"),
    paper_types={
        "research": ("abstract", "introduction（问题背景）", "methodology（检索与分析方法）", "results（数据与发现）", "discussion（意义与建议）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（信息流程分析）", "results（效果评估）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式（作者-年份；Journal of Documentation 遵循 APA 规范）",
    reporting_standards={"systematic_review": "系统综述遵循 PRISMA 声明", "user_study": "用户研究遵循用户研究报告规范", "IR": "信息检索遵循 TREC 评估规范"},
    conventions=("检索策略与来源须完整说明", "查全率与查准率须报告", "用户样本与任务须定义", "数据清洗与预处理须交代", "隐私与数据合规须说明"),
    key_venues=("Journal of Documentation", "Information Processing & Management", "Information Systems Journal", "Journal of the Association for Information Science and Technology", "Library Journal"),
    units_and_formulas_notes=("查准率用 Precision；查全率用 Recall", "F1 = 2PR/(P+R)", "样本量与置信区间须报告", "时间窗口须统一", "数据来源与许可须注明"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Python（Scrapy 爬虫）", "Apache Lucene（全文检索）", "Elasticsearch（检索引擎）", "Bloom Filters（去重）", "TextRank（文本摘要）", "BERT（语义检索）", "SPSS（统计）", "R（统计与文本挖掘）", "NVivo（质性编码）", "Zotero（文献管理）", "CiteULike（协作标注）", "Mendeley（参考管理）", "Moodle（教学平台）", "COUNTER 数据标准工具", "IRIS 开源学术出版平台", "Python（BeautifulSoup 网页解析）", "Apache Solr（检索引擎）", "Snowflake（数据仓库）", "AWS Lambda（数据处理流水线）", "PostgreSQL（全文检索扩展）"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "Google Scholar（文献检索）", "Scopus（期刊数据库）", "Web of Science（引文索引）", "JSTOR（学术数据库）", "ProQuest（学位论文库）"),
)
