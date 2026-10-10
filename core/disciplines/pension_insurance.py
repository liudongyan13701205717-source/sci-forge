"""养老保险学科论文支持：社会保障/精算/公共政策体裁、法学-经济学引用样式与精算记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pension_insurance",
    aliases=("pension insurance", "养老保险", "养老金保险", "social pension", "养老保险制度", "养老保险基金", "年金", "pension scheme", "社会保障"),
    paper_types={
        "research": ("abstract", "introduction（制度或财务问题）", "methodology（精算/统计/政策分析）", "results（可持续性与公平性）", "discussion（改革与比较）", "references"),
        "case_study": ("abstract", "introduction", "case description（制度/群体/地区）", "analysis（制度设计/资金平衡）", "results（影响与效应）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（养老金理论与政策文献）", "evidence synthesis（国际比较证据）", "future directions", "references"),
    },
    citation_style="APA/法学-经济学样式（社会保障与经济学领域；政策文本按官方文号引用）",
    reporting_standards={"actuarial": "精算假设计龄、死亡率、替代率与增长率须明确", "population": "人口数据须报告来源与年份（UN/Eurostat/国家统计局）", "policy": "政策文本引用须注明文号、发布机构与生效日期", "fairness": "公平性分析须报告基尼/洛伦兹等指标与分组口径", "sensitivity": "稳健性与敏感性分析须报告"},
    conventions=("国家制度按标准英文全称+缩写标注（如 OAS、SARS）", "替代率、缴费率、赡养率定义须明确", "精算贴现率、死亡率表引用须注明来源与年表", "涉及隐私的数据脱敏与法律合规须声明", "国际比较按人均购买力平价口径"),
    key_venues=("Journal of Public Economics", "Journal of Economic Literature", "Social Security Journal", "OECD Social, Employment and Migration Working Papers", "Public Finance Review", "Journal of Pension Economics & Finance"),
    units_and_formulas_notes=("金额按本币单位+年度标注（USD 2020 等）", "精算现值须报告贴现率与死亡率表来源", "赡养率、替代率、缴费率用百分比", "人口指标用千人或绝对数并注明年份"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("World Bank WGI 治理数据", "UN World Population Prospects", "Eurostat 欧盟统计", "OECD Pensions Database", "OECD Pension Projections", "LIMNOVA 生命表", "Prudential 精算模型", "Voya 精算平台", "PPO 精算软件", "Mackenzie 精算", "SSP 精算工具", "SPSS 统计分析", "R (actuarial) 精算", "Python (lifelines, actuar)", "Stata 统计", "EViews 计量分析", "SAS 统计分析", "World Bank Data Bank", "Bloomberg Terminal", "Excel（精算建模）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Statistical Office 国家统计局数据库"),
)
