"""外语教师教育论文支持：第二语言教育领域教师培养、语言教学法与语料库研究的论文写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_in_second_languages",
    aliases=("teacher_training_in_second_languages", "Teacher training in second languages", "外语教师教育", "第二语言教师培养", "外语教学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "literature review（文献综述）",
            "methods（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "teaching design（教学设计）",
            "implementation（实施）",
            "evaluation（评估）",
            "conclusion",
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
    citation_style="APA 7",
    reporting_standards={
        "teaching_method": "语言教学法须描述教学目标、任务类型、语言输入与输出要求",
        "corpus_study": "语料库研究须注明语料库名称、版本、搜索参数与统计方法",
        "assessment": "语言测试须标注测试类型、信度、效度与常模",
        "pronunciation": "发音评估须使用国际音标（IPA），标注重音与语调模式",
    },
    conventions=(
        "语言术语须使用IPA国际音标标注，中文术语须全文统一",
        "语料库引用须标注版本、更新时间与检索参数，确保可重复",
        "翻译文本须区分直译与意译，标注翻译策略与理由",
        "语言测试结果须报告信度系数与标准化分数，区分原始分与百分位",
        "引用语言样本须标注来源、语境与语言变体（标准语/方言）",
    ),
    key_venues=(
        "Journal of Second Language Teacher Education",
        "Modern Language Journal",
        "Language Learning",
        "Journal of Second Language Writing",
        "Language Teaching Research",
    ),
    units_and_formulas_notes=(
        "语言样本须标注时长（秒/分钟）、采样率与转写方式",
        "语料库检索须注明检索参数（词形、词频、搭配）、搜索工具与版本",
        "标准化分数须明确参照常模、分母与标准化方法",
        "IPA标注须使用标准音标符号，元音长度与辅音清浊须准确标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("LanguageTool", "Grammarly", "Quizlet", "Duolingo", "Rosetta Stone", "Preply", "iTalki", "LingQ", "Anki", "Memrise", "Speechling", "Pronunciation Coach", "COCA", "BNC", "Lextutor", "Sketch Engine", "AntConc", "Linguee", "WordReference", "Reverso"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
