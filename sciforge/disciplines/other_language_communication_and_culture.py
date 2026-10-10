"""其他语言、传播与文化学科论文支持：非主流语种的语言研究、跨文化传播与语言文化比较。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_language_communication_and_culture",
    aliases=("Other Language, Communication And Culture", "其他语言、传播与文化", "Language And Communication Studies", "其他语言与传播", "Cross-Cultural Communication", "Language Documentation", "Linguistics", "Cultural Communication"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（研究结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "定性研究遵循COREQ访谈报告规范", "k2": "系统综述遵循PRISMA筛选流程", "k3": "混合方法研究遵循MMRE整合报告指南"
    },
    conventions=("跨文化研究须遵循文化尊重与知情同意的IRB伦理准则", "涉及濒危语言须提供语言代码（ISO 639-3）并附转写/转译说明", "田野研究须标明研究地点、语言变体与采集时间", "术语须区分口语、书面语与学术用法，注明使用语境", "文本引证需附原语言与英文对照翻译，并标注音译体系"),
    key_venues=("Annual Review of Applied Linguistics", "Language", "Journal of Pragmatics", "Discourse & Society", "International Journal of Bilingualism", "Journal of Multilingual and Multicultural Development"),
    units_and_formulas_notes=("转写转译遵循IPA音位转写与ISO 639-3语言代码标注规范", "语料频率统计注明采样窗口、去重方法与停用词表", "民族志数据引用注明田野记录编号、录音时长与受访同意", "跨文化问卷须提供原文与英文对照并标明量表信度（Cronbach α）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("ELAN", "PRAGMA", "TransANA", "AntConc", "Sketch Engine", "CLARIN", "ELDP", "Language Reactor", "Praat", "Audacity", "NVivo", "MAXQDA", "ATLAS.ti", "Zotero", "Endnote", "SPSS", "LaTeX", "Microsoft Word", "Overleaf", "FLEx（Field Linguistics Explorer）"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "Google Scholar"),
)
