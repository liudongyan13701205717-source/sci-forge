"""其他创意艺术与写作学科论文支持：未被其他细类归入的创意艺术创作与写作研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="other_creative_arts_and_writing",
    aliases=(
        "other_creative_arts_and_writing", "其他创意艺术与写作",
        "other creative arts and writing", "其他创意艺术与写作",
        "creative arts", "创意艺术",
        "creative writing", "创意写作",
        "other art", "其他艺术",
        "arts not elsewhere classified", "艺术未另分类",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（创作背景与研究问题）",
            "methodology（创作方法与过程）",
            "results（作品与创作成效）",
            "discussion（艺术意义与价值）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（作品/创作个案）",
            "analysis（形式与内容分析）",
            "results（评价与反馈）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论与流派综述）",
            "evidence synthesis（作品与批评证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Chicago Notes-Bibliography",
    reporting_standards={
        "k1": "创作过程须报告媒介、工具、时间与作者意图",
        "k2": "作品评价须区分作者自评、同行评议与观众反馈",
        "k3": "文本分析须报告取样范围、编码规则与信度检验",
    },
    conventions=(
        "作品名称与译名须首次出现时并列标注",
        "引用文学作品须用斜体并标注版本与页码",
        "图示与插图须标注创作者、拍摄者与许可状态",
        "统计检验注明方法、p 值与效应量",
        "术语中英并列且全文统一",
    ),
    key_venues=(
        "PMLA",
        "Critical Inquiry",
        "JMLA (Journal of Modern Literature)",
        "Contemporary Literature",
        "《文学评论》",
        "《文艺研究》",
    ),
    units_and_formulas_notes=(
        "统计检验注明 t/F/χ² 值、p 值与效应量",
        "作品计量以字符数、镜头数、帧率等客观口径标注",
        "引用页码用阿拉伯数字并前后一致",
        "年代与时期用国际通行纪年法",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Scrivener", "Adobe Creative Cloud", "Adobe InDesign", "Adobe Photoshop", "Adobe Illustrator", "Adobe Premiere Pro", "Final Cut Pro", "DaVinci Resolve", "Pro Tools", "Blender", "Unity", "Unreal Engine", "Procreate", "Avid Media Composer", "LaTeX", "Microsoft Word", "Google Docs", "Zotero", "EndNote", "Canva"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
