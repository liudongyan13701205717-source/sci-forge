"""导游学科论文支持：解说讲解、行程设计与游客体验的研究方法、评分与访谈分析注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="guiding_tour_leading",
    aliases=("guiding_tour_leading", "导游", "旅游解说", "tour guiding", "行程设计", "itinerary design", "游客体验", "visitor experience", "解说设计"),
    paper_types={
        "research": ("abstract", "introduction（解说与游客体验研究动机）", "methodology（线路、受众与量表或访谈方案）", "results（满意度、停留时长与理解度）", "discussion（解说策略的影响）", "references"),
        "case_study": ("abstract", "introduction", "case description（景区、线路与受众背景）", "analysis（解说内容与行程结构）", "results（满意度与体验反馈）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（解说研究与体验理论）", "evidence synthesis（解说策略与受众研究综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"sample": "游客样本量、来源与抽样方式须说明", "instruments": "量表（如 5 点 Likert）与访谈提纲须附于正文或注明出处", "ethics": "游客访谈须取得知情同意并匿名化处理"},
    conventions=("解说文本按段落与停留点编号", "游客数量与停留时长分别以人次与 min 报告", "满意度用 5 点 Likert，须报告均值与标准差", "引用景区与遗产地资料须标注管理与保护单位", "术语首次出现给出中英文对照"),
    key_venues=("Annals of Tourism Research", "Tourism Management", "Journal of Sustainable Tourism", "旅游学刊", "旅游科学"),
    units_and_formulas_notes=("停留时长与步行距离分别用 min 与 m 或 km 报告", "游客量按日或季节单位给出（人·次）", "满意度均值报告至小数点后两位（如 M = 4.32, SD = 0.61）", "公式用 LaTeX（amsmath）；满意度 = 评分总和 / 受访者人数"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Google Earth Pro", "AllTrails", "Wikiloc", "Komoot", "Maps.me", "Trailforks", "Strava", "Garmin inReach Mini", "Garmin Epsilon", "eBird", "iNaturalist", "Seek by iNaturalist", "NatureID", "FloraNova", "Google Translate", "DeepL", "Canva", "Microsoft PowerPoint", "Apple Keynote", "Wikimedia Commons"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
