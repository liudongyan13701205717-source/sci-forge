"""拍卖学 (Auctioneering) 学科论文支持：拍卖实务、机制设计、市场研究、法律。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="auctioneering",
    aliases=(
        "Auctioneering", "拍卖学", "拍卖", "auction",
        "拍卖经营与管理", "auction management",
        "auction theory", "拍卖理论", "艺术品拍卖", "art auction",
        "机制设计", "mechanism design",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "theory or methodology",
            "case study / data / model",
            "results",
            "discussion",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "case background",
            "auction design",
            "process",
            "results",
            "analysis",
            "conclusions",
        ),
        "review": (
            "abstract",
            "historical overview",
            "main schools",
            "open questions",
            "references",
        ),
    },
    citation_style="APA 7 或 经济学/法学 APA 样式",
    reporting_standards={
        "data": "拍卖成交数据须声明来源（拍卖行/政府/公开数据库），含成交价与保留价",
        "mechanism": "拍卖类型（英/美/荷/Sealed-bid）、规则、佣金结构须完整披露",
        "valuation": "估价方法（比较法/收益法/成本法）须声明",
        "ethics": "委托人身份、瑕疵披露、串标规避须符合《拍卖法》",
    },
    conventions=(
        "拍品分类按国标《拍卖标的分类》或行业习惯（艺术品/机动车/无形资产等）",
        "标的描述须含编号、名称、来源（provenance）、状况（condition report）",
        "佣金/服务费比例按《拍卖法》及行业惯例分档列示",
        "成交价含佣金与不含佣金须区分（hammer price vs. buyer's premium）",
        "货币单位统一（CNY/USD/HKD）并声明时点",
        "引用《中华人民共和国拍卖法》条款须注明年份版本",
    ),
    key_venues=(
        "Journal of Economic Theory",
        "Econometrica",
        "American Economic Review",
        "RAND Journal of Economics",
        "Journal of Auction Theory",
        "中国拍卖",
        "中国拍卖行业协会会刊",
        "Review of Economic Studies",
        "Games and Economic Behavior",
        "Journal of Law and Economics",
    ),
    units_and_formulas_notes=(
        "金额单位 CNY/USD，注明币种与年份",
        "佣金比例用百分号，注意保留价与成交价换算",
        "拍卖时长用 min/h，参与人数区分注册与举牌",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("阿里拍卖", "京东拍卖", "公物仓", "人民法院司法拍卖平台", "中国拍卖行业协会信息系统", "雅昌拍卖", "Artnet", "MutualArt", "OBSIDIAN", "Sotheby's", "Christie's", "Bonhams", "Heritage Auctions", "Paddle", "eBay Gavel", "Gavel", "Q1 Auction", "SPSS", "Stata", "R (linearmodels)", "Python (NumPy/SciPy)", "EViews", "SAS", "Excel (VBA / Power Query)", "Tableau"),
    category="经济学",
    databases=("CNKI", "OpenAlex", "Crossref", "JSTOR", "ArtNet", "中国拍卖协会会刊"),
)
