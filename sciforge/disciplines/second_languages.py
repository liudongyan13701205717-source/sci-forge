"""第二语言学科论文支持：二语习得/对比语言学/语言教学/语言测试体裁、APA 7 语言学术引用样式与语言学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="second_languages",
    aliases=("second_languages", "第二语言", "二语习得", "外语学习", "second language acquisition", "L2"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究意义）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据综合）",
            "future directions（展望）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "methodology": "研究方法须报告研究设计、参与者特征、数据收集与分析方法",
        "data": "语言数据须注明数据来源、标注方案与可信度",
        "measurement": "语言测试须报告信度、效度与标准化信息",
        "ethics": "涉及人类被试研究须报告伦理审查与伦理同意",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "语言实例须标注来源、说话人/作者与采集时间",
        "音韵描写须使用 IPA 国际音标",
        "语料标注须注明标注方案与标注者信度",
        "术语须首次出现时给出英文全称与中文译名",
        "引用语言材料须保留原文并附译文",
    ),
    key_venues=(
        "Second Language Research",
        "Applied Linguistics",
        "Language Learning",
        "The Modern Language Journal",
        "System",
    ),
    units_and_formulas_notes=(
        "词频用 tokens/lemma；语法复杂度用 CN-Complex 等指标",
        "时间用分钟或词/分钟；错误率用 errors/100 words",
        "公式用 amsmath；统计公式须编号",
        "统计结果给出均值 ± 标准差与样本量；显著性用 p 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("AntConc 语料分析", "LANCHA 语料库标注", "ELAN 字幕标注", "praat 语音分析", "CLAN CHAT 儿童语言分析", "Corpus Workbench", "CQPweb 语料查询", "Sketch Engine", "NVivo 质性分析", "R 统计分析", "Python 文本处理", "LaTeX 排版", "Origin 绘图", "SPSS 统计软件", "FLEx 语言田野调查", "OpenSubtitles 字幕语料", "CC-CEDICT 英汉词典", "Praat 声学分析", "Glossa Linguistic 语言描写", "L2 Development Sequence"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)