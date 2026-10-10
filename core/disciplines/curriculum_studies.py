"""Curriculum studies 学科论文支持：课程知识/权力/制度批判体裁、芝加哥样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="curriculum_studies",
    aliases=(
        "curriculum_studies",
        "curriculum studies",
        "课程研究",
        "课程知识",
        "课程批评",
        "curriculum knowledge",
        "critical curriculum studies",
        "hidden curriculum",
        "隐形课程",
        "curriculum history",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "analysis（分析）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "historical_study": (
            "abstract",
            "introduction",
            "historiography（研究史回顾）",
            "archival sources（档案史料）",
            "analysis（分析）",
            "conclusions",
            "references",
        ),
        "critical_essay": (
            "abstract",
            "introduction",
            "argument（论证）",
            "counterarguments（反论回应）",
            "implications（意涵）",
            "references",
        ),
    },
    citation_style="Chicago 样式（人文课程研究遵循 Chicago 规范；实证取向部分可遵 APA 7）",
    reporting_standards={
        "archival": "档案研究遵循史料考证报告规范，政策文本须注明版本与生效时间",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "ethics": "涉及学生与教师的民族志研究须报告伦理审查与知情同意方式",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "课程须区分三种知识形态并分别标注：正式课程（official）、实践课程（practicum）、隐藏课程（hidden）",
        "理论立场须显式声明所属传统（如 Pinar 的 a-d-a / 批判课程理论 / 后结构主义课程研究）",
        "政策文件引用须给出全称、发文机关、文号与版本年份；译文须给出原文页码",
        "档案与访谈资料须注明采集时间、来源与保存机构",
        "历史叙述须区分史料事实与理论解释，避免以今律古",
        "反思性（reflexivity）须在方法部分讨论研究者位置",
    ),
    key_venues=(
        "Curriculum Inquiry",
        "Journal of Curriculum Studies",
        "Curriculum Journal",
        "Curriculum Perspectives",
        "Review of Research in Education",
        "British Journal of Educational Studies",
        "课程·教材·教法",
    ),
    units_and_formulas_notes=(
        "引文给出页码；古籍用卷/篇/页标注",
        "时间用统一纪年格式，历史数据须标注统计口径与换算依据",
        "样本量须报告；频数与百分比给出基数",
        "货币与学制改革前后的可比性须说明调整方式",
        "引文给出页码",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("Zotero", "EndNote", "Mendeley", "LaTeX", "Overleaf", "Voyant Tools", "Stanford Literary Lab", "AntConc", "LancsBox (Lancaster University Corpus Tools)", "NVivo", "MAXQDA", "ATLAS.ti", "QGIS", "ArcGIS Pro", "Gephi", "NetworkX", "Tableau", "RStudio", "Wikidata", "Europeana", "Internet Archive", "CLIO-online"),
    category="教育学",
    databases=("ERIC", "CNKI", "万方", "OpenAlex", "Crossref", "JSTOR", "ProQuest"),
)
