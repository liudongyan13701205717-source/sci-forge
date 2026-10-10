"""社会学与文化研究学科论文支持：话语/表征/文化生产分析体裁、ASA/Chicago 引用样式与质性编码注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sociology_and_cultural_studies",
    aliases=("sociology_and_cultural_studies", "社会学与文化研究", "文化研究", "社会文化分析", "媒体文化", "亚文化研究"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="ASA 样式（作者-年份；文化研究文本可用 Chicago 注释体）",
    reporting_standards={
        "ethics": "涉及亚文化/边缘群体的田野伦理审查与知情同意须报告",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "representation": "引证受访者的去标识化规则与语言转写约定须声明",
    },
    conventions=(
        "理论框架须交代谱系（葛兰西/福柯/霍尔/布尔迪厄等）",
        "民族志与文本分析的证据须可回溯到编码或出处",
        "概念翻译须标注英文原词（hegemony、habitus、discourse）",
        "研究者立场与位置性（positionality）须声明",
        "案例描述与理论诠释分层呈现",
    ),
    key_venues=(
        "Society & Culture",
        "Media, Culture & Society",
        "Cultural Studies",
        "Australian Journal of Social Issues",
        "Popular Culture",
    ),
    units_and_formulas_notes=(
        "话语/文本分析给出语料总量、来源与采样窗口",
        "编码一致性给 Cohen's κ 或 Krippendorff's α",
        "网络与传播图给出节点数、边数与布局算法",
        "统计符号斜体（M、SD、p、d），效应量给置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "ATLAS.ti", "MAXQDA", "QualCoder", "Sketch Engine", "Voyant Tools", "Reflexiv", "R", "Python", "Stata", "SPSS", "Gephi", "Zotero", "EndNote", "Mendeley", "LaTeX", "Microsoft Word", "Adobe Acrobat", "OBS Studio", "Qualtrics"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "JSTOR Text Analysis"),
)
