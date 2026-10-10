"""道德学科论文支持：道德哲学/伦理学/规范伦理学体裁、Chicago 引用样式与哲学论证注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="morals",
    aliases=(
        "morals", "道德", "伦理", "ethics", "moral philosophy", "道德哲学",
        "moral psychology", "道德心理学", "规范伦理学"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methodology（论证方法与文本分析）",
            "results（论证结果与分析）",
            "discussion（哲学意义与回应）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（道德案例描述）",
            "analysis（道德论证分析）",
            "results（伦理结论）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（道德理论框架）",
            "evidence synthesis（道德论证综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份；哲学期刊遵循芝加哥格式）",
    reporting_standards={
        "argumentative": "论证遵循哲学论证报告规范",
        "textual_analysis": "文本分析遵循经典文本研究规范",
        "case_analysis": "案例分析遵循哲学案例分析规范",
    },
    conventions=(
        "论证结构须清晰（前提/结论/反驳）",
        "哲学家姓名与生卒年须首次给出",
        "经典著作使用规范译名",
        "道德术语（义务、德性、后果）须界定",
        "论证类型（演绎/归纳/溯因）须明确",
    ),
    key_venues=(
        "Ethics",
        "Journal of Philosophy",
        "Mind",
        "Philosophical Review",
        "Philosophy and Public Affairs",
    ),
    units_and_formulas_notes=(
        "论证用形式语言（命题/谓词/量词）",
        "公式用 amsmath；模态逻辑用 □/◇ 符号",
        "显示公式仅在被引用时编号",
        "文本引用须给出精确页码与版本",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "译文", "报告", "数据集"),
    tools=("语料库分析工具 AntConc", "Sketch Engine", "语义网络分析软件 GEXf", "Python (NLTK/spacy)", "逻辑论证分析工具 LogiCola", "Philosophers.org", "Prolog (概念分析)", "Rationale (论证映射)", "Google Books (语料库)", "WordNet", "Voyant Tools", "Prooftypes", "Rhetorica (论证可视化)", "NetLogo (伦理决策模型)", "Qualtrics", "NRC Emotion Lexicon", "Gephi (知识图谱)", "ArgMining", "EthosDB", "文本相似度检测工具"),
    category="哲学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
