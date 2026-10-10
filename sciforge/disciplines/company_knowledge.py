"""企业知识管理学科论文支持：企业知识/组织知识管理体裁、APA 引用样式与知识管理注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="company_knowledge",
    aliases=(
        "company_knowledge", "企业知识管理", "knowledge management",
        "organizational knowledge management", "组织知识管理",
        "corporate knowledge", "企业知识", "enterprise knowledge management",
        "企业知识管理", "knowledge sharing", "知识共享",
        "tacit knowledge", "隐性知识", "explicit knowledge",
        "显性知识", "knowledge transfer", "知识转移",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与知识管理问题）",
            "literature review（文献综述）",
            "methods（方法与样本）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction（案例背景）",
            "company profile（公司概况）",
            "method（研究方法）",
            "findings（发现）",
            "analysis（分析）",
            "implications（启示）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "taxonomy（分类体系）",
            "main developments（按主题综述）",
            "outlook（展望）",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Journal of Knowledge Management 遵循 APA 规范）",
    reporting_standards={
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "quantitative": "定量研究遵循 CONSORT 或 PRISMA 声明",
        "case_study": "案例研究遵循案例研究规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "知识管理研究须明确知识类型（显性/隐性）与管理阶段（创建、存储、传播、应用）",
        "涉及员工访谈的研究须声明伦理审查与匿名化处理",
        "知识转移效果须报告量化指标（如生产率、创新产出）",
        "跨文化知识管理研究须交代文化情境差异",
        "企业案例研究须注明数据来源与匿名化处理",
    ),
    key_venues=(
        "Journal of Knowledge Management",
        "Knowledge Management Research & Practice",
        "International Journal of Information Management",
        "Journal of Business Strategy",
        "Management Learning",
        "Journal of Management Information Systems",
    ),
    units_and_formulas_notes=(
        "时间用统一纪年格式；货币用统一币种并注明年份",
        "涉及员工调查时给出样本量与回复率",
        "涉及绩效指标时注明来源与计算口径",
        "涉及统计检验时给出效应量与置信区间",
        "涉及知识图谱时给出实体数与关系数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Confluence", "Notion", "SharePoint", "Salesforce", "SAP", "ServiceNow", "Zendesk", "Jira", "Slack", "Microsoft Teams", "Google Workspace", "Monday.com", "Airtable", "Guru", "Document360", "Basecamp", "Trello", "Coda", "Miro", "Lucidchart", "NVivo", "SPSS", "Stata", "R (RStudio)", "Python (Jupyter)", "Tableau", "Microsoft Power BI", "EndNote", "Zotero", "Mendeley", "LaTeX", "Overleaf", "RefWorks", "JabRef", "Google Sheets", "Microsoft Excel", "GitLab", "GitHub"),
    category="管理学",
    databases=("OpenAlex", "CNKI", "万方", "Crossref", "JSTOR", "Google Scholar", "Scopus"),
)
