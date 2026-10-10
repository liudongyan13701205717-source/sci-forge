"""皮草与皮革生产学科论文支持：鞣制工艺、皮革化学与可持续皮料管理体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="skins_and_leather_production",
    aliases=(
        "skins_and_leather_production",
        "皮草生产",
        "皮革生产",
        "tanning",
        "Leather Technology",
        "Hide Processing",
        "鞣制",
        "皮革化学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "methods（工艺/实验方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工厂/皮料案例）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份）",
    reporting_standards={
        "chemical": "化学品添加量以皮重百分比（% p.c.w.s.）报告",
        "environmental": "废水排放须符合 GB 30486 或 ISO 14001 限值",
        "testing": "力学性能按 ISO 16292/GB/T 5255 报告",
        "review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "工艺步骤遵循 LWG 皮装认证标准或 ISO 14522 分类",
        "所有化学品须给出 CAS 号与浓度",
        "染料用量以 owf（on weight of flesh）百分比计",
        "废水处理报告 COD、BOD、SS、pH 五项",
        "图表须标注测试条件与置信区间",
    ),
    key_venues=(
        "Leather & Leather Technology",
        "Journal of the Leather Research",
        "TAPPI Journal",
        "Journal of Industrial Textiles",
        "皮革科学与工程",
    ),
    units_and_formulas_notes=(
        "鞣剂用量：% p.c.w.s.（占生皮干重百分比）",
        "染料浓度：% owf（占湿皮重百分比）",
        "皮厚以 mm 计；密度以 g/cm³ 计",
        "废水 COD 以 mg/L 计；pH 无单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ZwickRoell Z010", "Instron 5969", "Tinius Olsen Impact Tester", "Brombacher", "Kohler", "Safex", "Leather Test System", "Autoclave", "Tanning Drum", "Dyeing Machine", "Cromatography (HPLC)", "UV-Vis Spectrophotometer", "XRF Analyzer", "SEM-EDS", "Python（pandas）", "MATLAB", "LaTeX", "Endnote", "Photoshop", "Adobe InDesign"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI", "Scopus"),
)
