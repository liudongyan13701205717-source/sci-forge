"""艺术哲学学科论文支持：艺术本体/审美/艺术批评体裁、Chicago/APA 引用样式与艺术史注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="philosophy_of_art",
    aliases=("philosophy of art", "艺术哲学", "艺术美学",
             "aesthetics", "art criticism", "艺术批评", "美学",
             "美学哲学", "艺术理论", "art theory"),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题与背景）",
            "argument（论证）",
            "analysis（分析）",
            "objections（反驳）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（艺术分析）",
            "results（发现）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 或 APA 样式（艺术哲学/美学常用 Chicago）",
    reporting_standards={
        "argument": "核心论点须独立于证据简述",
        "aesthetic": "美学研究遵循 Aesthetics 传统",
        "art_history": "艺术史遵循 Iconography/Iconology 传统",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "empirical": "实证研究遵循 COREQ/SRQR 规范",
        "criticism": "艺术批评遵循艺术批评传统",
    },
    conventions=(
        "艺术作品给出艺术家/年代/馆藏",
        "图像使用须注明出处与授权",
        "美学原则用中文并注译原文",
        "术语用中文并注译",
        "区分美学与艺术批评",
    ),
    key_venues=(
        "British Journal of Aesthetics",
        "Journal of Aesthetics and Art Criticism",
        "Philosophy and the Contemporary Arts",
        "Journal of Aesthetics",
        "Aesthetica",
        "Journal of Religion and the Arts",
    ),
    units_and_formulas_notes=(
        "艺术作品给出艺术家/年代/馆藏",
        "图像使用须注明出处与授权",
        "引用给出页码",
        "术语用中文并注译",
        "区分美学与艺术批评",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("LaTeX 艺术哲学排版", "Overleaf 在线 LaTeX", "Zotero 文献管理", "EndNote", "Mendeley", "PhilArchive 预印本平台", "Stanford Encyclopedia of Philosophy (SEP)", "Google Arts & Culture", "Getty Thesaurus of Geographic Names (TGN)", "Getty AAT（艺术主题词典）", "ImageJ 图像分析", "Adobe Photoshop 图像分析", "GIMP 图像处理", "Color Theory 色彩分析", "Word（Microsoft Office）", "CSL 引用样式管理", "LogicGator 逻辑证明", "Adobe Lightroom", "OpenCV（计算机视觉分析）", "Adobe InDesign（版面设计）"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "Semantic Scholar", "PhilPapers", "JSTOR", "CNKI", "JSTOR 数据库", "PhilPapers 哲学数据库", "ARTstor 艺术数据库"),
)
