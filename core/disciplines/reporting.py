"""新闻报导学科论文支持：新闻调查、传播效果与媒介伦理研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="reporting",
    aliases=(
        "reporting",
        "新闻报导",
        "新闻报道",
        "新闻学",
        "Reporting",
        "Journalism",
        "News Reporting",
        "Investigative Journalism"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "methodology（方法与样本）",
            "results（结果）",
            "discussion（讨论与意义）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（报道/事件）",
            "analysis（内容/框架分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（新闻理论）",
            "evidence synthesis（研究进展）",
            "future directions",
            "references"
        ),
    },
    citation_style="APA 7 样式（新闻学主流；Communication Research 遵循 APA）",
    reporting_standards={
        "content_analysis": "内容分析须报告编码表、编码员间一致性（Kappa）与样本",
        "survey": "问卷调查须报告抽样、问卷与响应率",
        "experiment": "传播效果实验须报告设计、变量与操纵检验"
    },
    conventions=(
        "新闻文本引用给出媒体、日期与版次",
        "术语首现英文原词加中文译名",
        "抽样与样本量须报告",
        "统计显著性用 α=.05（或明确设定）",
        "伦理审查与知情同意须报告"
    ),
    key_venues=(
        "Journalism & Communication Monographs",
        "Journalism Studies",
        "Communication Research",
        "Journal of Communication",
        "International Journal of Communication"
    ),
    units_and_formulas_notes=(
        "样本量 n 与置信区间须报告",
        "显著性水平 α 与 p 值须明确",
        "时间用统一格式（YYYY-MM-DD）",
        "百分比精确到小数点后 1 位"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("CMS (Content Management System)", "WordPress", "Adobe InDesign", "Adobe Photoshop", "Adobe Premiere Pro", "Adobe After Effects", "Adobe Audition", "OBS Studio", "Canva", "Grammarly", "Hemingway Editor", "AP Stylebook", "Reuters Stylebook", "PressReader", "Dow Jones Factiva", "Bloomberg Terminal", "NVivo", "SPSS", "Tableau", "Adobe Lightroom"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "LexisNexis"),
)
