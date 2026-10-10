"""新闻采编学科论文支持：新闻写作/媒介素养/传播研究体裁、APA 引用样式与新闻学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="news_reporting",
    aliases=("news_reporting", "新闻采编", "News Reporting", "news writing",
             "新闻写作", "journalism", "新闻学", "传播学",
             "数字新闻", "digital journalism"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与理论）",
            "methodology（田野与内容分析）",
            "results（发现与统计）",
            "discussion（意义与影响）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（报道案例）",
            "analysis（话语与框架）",
            "results（受众与效果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（传播理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份）",
    reporting_standards={
        "style_guide": "写作风格遵循 AP Stylebook 或《人民日报》编辑体例",
        "ethics": "报道伦理遵循 SPJ Code of Ethics",
        "attribution": "信息源须标注且可核验",
        "fact_check": "事实核查遵循 Reuters FactCheck 规范",
        "copyright": "版权与转载许可须声明",
    },
    conventions=(
        "标题采用倒金字塔结构",
        "直接引语用双引号，间接引语用冒号",
        "机构名首次出现须全称+缩写",
        "数字遵循 AP 规则（10 以下用文字）",
        "图表须编号并标注来源",
    ),
    key_venues=(
        "Journal of Communication",
        "New Media & Society",
        "Journalism Studies",
        "国际新闻界",
        "新闻与传播研究",
        "传播与社会",
    ),
    units_and_formulas_notes=(
        "样本量以 N 标注",
        "百分比保留一位小数",
        "统计用 amsmath",
        "引用须标注媒体与日期",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "软件与代码", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo", "Adobe Photoshop", "Adobe Premiere Pro", "Adobe Lightroom", "Canva", "Final Cut Pro", "OBS Studio", "Audacity", "Zotero", "Grammarly", "Muck Rack", "Cision", "Google Analytics", "Twitter/X Analytics", "WordPress", "AP Stylebook", "Reuters FactCheck", "Google Docs", "Pencil", "Newsroom CMS"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
