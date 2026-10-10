"""服装工业学科论文支持：服装产业/供应链/时尚管理体裁、APA 引用样式与产业分析注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="clothing_industry",
    aliases=("clothing_industry", "服装工业", "服装产业", "时尚产业",
             "服装供应链管理", "服装制造",
             "apparel industry", "fashion industry", "garment manufacturing",
             "textile and apparel industry", "clothing supply chain"),
    paper_types={
        "research": (
            "abstract",
            "introduction（产业背景与问题）",
            "literature review",
            "methodology（数据来源、抽样、访谈/问卷/案例设计）",
            "findings",
            "discussion",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "background",
            "case description",
            "analysis",
            "implications",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "state of the art",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份，Journal of Fashion Marketing and Management 规范）",
    reporting_standards={
        "survey": "问卷研究遵循 APA 7 报告规范",
        "case_study": "案例研究遵循 Eisenhardt (1989) 与 Yin (2018) 的规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "supply_chain": "供应链分析须说明数据来源、时间窗口与样本企业范围",
    },
    conventions=(
        "术语须区分服装（garment）与服饰（apparel）与纺织（textile）",
        "供应链层级须明确界定（Tier 1/2/3）与数据来源",
        "案例研究须披露访谈对象、时间与地点",
        "问卷采用 5 级或 7 级 Likert 量表并注明 α 系数",
        "涉及企业案例须获得知情同意并匿名化处理",
    ),
    key_venues=(
        "Journal of Fashion Marketing and Management",
        "International Journal of Fashion Management",
        "Fashion Theory",
        "International Journal of Consumer Studies",
        "Journal of Operations Management",
        "Sustainability",
        "Supply Chain Management: An International Journal",
    ),
    units_and_formulas_notes=(
        "订单量、产量、库存量须注明计量单位与时间窗口",
        "成本与效率指标须注明币种与汇率（如适用）",
        "问卷分析给出 Cronbach's α、CFA 与 AVE/CR",
        "统计推断使用 P 值、效应量与 95% CI",
        "公式用 amsmath；指标名称首次出现处给出定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SAP Ariba", "SAP S/4HANA", "Oracle NetSuite", "JDA", "Blue Yonder", "IBM Planning Analytics", "Gerber AccuMark", "Lectra Modaris", "CLO 3D", "BrowZwear", "MarkerMaster", "Kaledo", "Spendesk", "Tableau", "Power BI", "R (lavaan)", "SPSS", "NVivo", "MaxQDA", "Python (pandas)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "Scopus"),
)
