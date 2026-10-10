"""Barbering 学科论文支持：理发/剃发/造型工艺体裁、APA 引用样式与美发行业记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="barbering",
    aliases=(
        "barbering",
        "理发",
        "理发与造型",
        "剃发与造型",
        "Barbering & Barbering Related Services",
        "Barbering and Barbering Related Services",
        "美发",
        "hairdressing",
        "hair styling",
        "男士理发",
        "barber",
        "理发技艺",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与工艺问题）",
            "literature review（文献综述）",
            "materials and methods（工艺方法与材料）",
            "results（结果与案例）",
            "discussion（讨论与工艺改进）",
            "conclusion（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景）",
            "technique（工艺步骤与技法）",
            "results（结果与观察）",
            "discussion（反思与改进）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（行业/工艺综述）",
            "outlook（趋势展望）",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；Cosmetics 遵循 MDPI 规范，IJCS 遵循 Elsevier 规范）",
    reporting_standards={
        "case_study": "案例研究遵循 SAGER 案例报告规范",
        "clinical_styling": "皮肤刺激与毛发健康相关研究遵循 CONSORT",
        "survey": "顾客满意度调查遵循 AAPOR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "所有涉及顾客的照片/画像须取得书面知情同意并注明匿名化处理",
        "工艺步骤用编号列表描述，每步注明工具型号、时长、压力或温度等关键参数",
        "化学处理（烫发、染发、漂发）须列出主要活性成分与浓度范围，避免仅写商品名",
        "英制/公制单位并列时优先公制（mm、°C、mL）并注明转换",
        "涉及皮肤、毛发安全的建议须标注证据等级，禁止以个案替代一般结论",
    ),
    key_venues=(
        "International Journal of Cosmetic Science",
        "Journal of Cosmetic Science",
        "Cosmetics",
        "Beauty Today",
        "Journal of Beauty Therapy",
        "Journal of Cosmetic Dermatology",
        "Journal of Personal Adhesives and Strips",
    ),
    units_and_formulas_notes=(
        "长度用 mm/cm；温度用 °C；体积用 mL；pH 无量纲",
        "染膏混合比用比例（如 1:1、1:2）而非百分比，除非涉及法规标注",
        "烫发液的波数/直径须用 mm 单位，避免仅写「中号/大号」",
        "图表标注工具型号时使用品牌 + 型号 + 序列号，禁止使用营销名",
        "涉及顾客数据的图表须用化名或编号，禁止使用真实姓名或面部特征",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Andis Master Ultra Clipper", "Wahl Senior Cordless Clipper", "BaBylissPRO Style & Fade Cordless", "Gisela Pro Clipper", "Fusion Barber Scissors (Morgan Creative Group)", "Malcolm Ross Straight Razor", "Schwarzkopf Professional", "Wella Professionals IGORA", "L'Oréal Professionnel", "Toni&Guy", "Redken", "Davines", "Aveda", "Milbon (TOKIO)", "Olaplex", "GHD Platinum+", "Cloud Nine Original", "Dyson Airwrap", "Dyson Supersonic", "Remington Pro", "Philips Multigroom", "SalonLogics", "Morgan Creative Group", "Vetress Pro", "Tondee Power Cordless", "Wahl Magic Clip", "Andis T-Outliner", "BaByliss Pro Dry", "Vaporizer 4000", "Matrix Biolage", "Kérastase", "Kevin Murphy Hair", "Bumble and bumble", "Moroccanoil Professional", "ColorWow (KMS)", "BioSilk", "Kenzo Professional Hairdressing", "Ojon Beauty", "Vegamour", "Milbon Phytotouch", "Davines Etnique", "Redken Extreme", "Aveda Nutritive", "Milbon Taft", "Wella WellaSpa"),
    category="管理学",
    databases=("OpenAlex", "CNKI", "万方", "PubMed"),
)
