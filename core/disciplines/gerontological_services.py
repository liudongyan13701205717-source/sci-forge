"""老年学服务学科论文支持：老年照护服务/社会老年学体裁、APA 引用样式与老年服务注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="gerontological_services",
    aliases=("gerontological services", "老年学服务", "老年照护服务", "老年服务", "老年社会服务", "长期照护", "老年福利"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（设计与人群）", "results（服务与结局）", "discussion（意义与局限）", "references"),
        "case_study": ("abstract", "introduction", "case description（个案服务描述）", "analysis（服务分析）", "results（干预效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（服务模型）", "evidence synthesis（证据综述）", "future directions", "references"),
    },
    citation_style="APA 7 样式（作者-年份；老年服务类期刊通用）",
    reporting_standards={"k1": "观察性研究遵循 STROBE", "k2": "质性研究遵循 COREQ", "k3": "服务评估遵循逻辑模型（logic model）"},
    conventions=("服务对象年龄构成须报告", "服务干预须定义明确", "生活质量量表给版本", "服务可及性指标须说明", "伦理与知情同意须交代"),
    key_venues=("Journal of Applied Gerontology", "Aging & Society", "The Gerontologist", "Journal of Aging and Social Policy", "Aging and Health"),
    units_and_formulas_notes=("服务量表分数无量纲", "公式用 amsmath，效果量计算须明确", "数值结果给均值 ± SD 与样本量", "服务周期以月/年计"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("English Longitudinal Study of Ageing（ELSA）", "REDCap 数据收集", "SPSS", "R", "NVivo 质性分析", "CARE 病例报告工具", "生活功能评估量表（SF-36）", "Glasgow Outcome Scale", "服务逻辑模型构建工具（Stake）", "混合方法分析（Convergent Design）", "Meta-Analysis（CMA）", "Stata", "Q 排序法（Q Method）", "时间地理法（Time Geography）", "服务满意度量表（Kano）", "EQUITY 公平性分析框架", "长护险精算模型工具", "社会网络分析（Gephi）", "老年友好社区评估工具（WHO SFIC）", "G*Power"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "Cohort 纵向队列数据库（HRS）"),
)
