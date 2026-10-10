"""创意与专业写作学科论文支持：文本创作、写作研究、批评与出版工艺体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="creative_and_professional_writing",
    aliases=(
        "creative and professional writing",
        "创意与专业写作",
        "创意写作",
        "专业写作",
        "商业写作",
        "technical writing",
        "professional writing",
        "business writing",
        "编辑出版",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "methodology",
            "analysis",
            "discussion",
            "conclusions",
            "references",
        ),
        "creative_process": (
            "abstract",
            "introduction",
            "the creative process",
            "the text",
            "revision notes",
            "reflection",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope",
            "synthesis",
            "implications",
            "references",
        ),
        "publication": (
            "abstract",
            "introduction",
            "manuscript",
            "editorial notes",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "manuscript": "稿件版本与修改记录须完整",
        "revision": "修改版本间差异须可追溯",
        "style": "行文须遵循芝加哥写作手册",
        "citation": "参考文献须完整且格式统一",
    },
    conventions=(
        "创作文本与批评性分析须明确区分",
        "引用给作者-页码；不同版本注明版本信息",
        "写作研究给样本量、编码方式与响应率",
        "术语统一；中英术语首现给中文全称并附英文原词",
        "修订记录给出版本标识与修改日期",
    ),
    key_venues=(
        "The Journal of Creative Writing Practice",
        "Journal of Writing Research",
        "College Composition and Communication",
        "Writing Program Review",
        "Journal of the Association of Teachers of Technical Writing",
        "Technical Communication Quarterly",
        "Text Technology",
        "PCCW: Peer-Reviewed Journal of Undergraduate Writing",
        "The Journal of Professional Writing",
        "Journal of Technical Writing and Communication",
    ),
    units_and_formulas_notes=(
        "引用格式遵循芝加哥手册",
        "字数按字符或词数计；版本须注明",
        "写作过程稿保留修改痕迹",
        "时间用统一格式",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "软件与代码", "教案与教材", "译文", "报告", "数据集"),
    tools=("Scrivener", "Microsoft Word", "Google Docs", "LaTeX", "Overleaf", "ProWritingAid", "Grammarly", "Hemingway Editor", "MWriter", "Ulysses", "iA Writer", "Drafts", "Bear", "Notion", "Zotero", "Mendeley", "Turnitin", "iThenticate", "Airtable", "Trello", "Asana", "Canva", "Adobe InDesign", "Adobe Acrobat", "InCopy", "Vellum", "Atticus", "Reedsy", "WordCounter", "LanguageTool", "Scribendi", "Writer"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "MLA International Bibliography", "Google Scholar"),
)
