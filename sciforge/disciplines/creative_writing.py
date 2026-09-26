"""创意写作学科论文支持：创作/教学/批评体裁、MLA 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="creative_writing",
    aliases=("creative_writing", "创意写作", "创作学", "写作学"),
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
        "practice_based": (
            "abstract",
            "introduction",
            "creative process（创作过程）",
            "work（作品）",
            "reflection（反思）",
            "conclusions（结论）",
            "references",
        ),
        "pedagogical_study": (
            "abstract",
            "introduction",
            "course design（课程设计）",
            "implementation（实施）",
            "evaluation（评估）",
            "discussion（讨论）",
            "references",
        ),
    },
    citation_style="MLA 样式（作者-页码；New Writing 遵循 MLA 规范）",
    reporting_standards={
        "practice": "实践研究遵循创作实践报告规范",
        "pedagogical": "教学研究遵循教学研究报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "survey": "调查研究遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "作品与创作过程须区分",
        "教学设计与评估须说明",
        "引文给出页码",
        "理论框架须明确",
        "反思性须讨论",
    ),
    key_venues=(
        "New Writing",
        "Journal of Creative Writing Studies",
        "TEXT: Journal of Writing and Writing Courses",
        "Creative Writing: Teaching Theory & Practice",
        "Writing in Practice",
        "Journal of Writing Research",
    ),
    units_and_formulas_notes=(
        "引文给出页码",
        "版本与版次须注明",
        "字数用 字/词 计数",
        "时间用统一格式",
        "百分比给出基数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "文学作品"),
    tools=(
        "Scrivener 长文写作管理",
        "Microsoft Word 文稿编辑",
        "LaTeX 作品排版",
        "Zotero 文献管理",
        "NVivo 创作过程质性编码",
    ),
    category="文学",
    databases=("CNKI", "万方", "OpenAlex", "Crossref"),
)