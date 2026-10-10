"""老年医学学科论文支持：老年临床/衰弱体裁、AGS/JAGS 引用样式与老年医学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geriatrics",
    aliases=("geriatrics", "老年医学", "老年科", "老年病学", "老年健康", "老年综合评估", "老年综合征"),
    paper_types={
        "research": ("abstract", "introduction（背景与动机）", "methodology（设计与人组）", "results（结局与功能）", "discussion（机理与临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（老年病例描述）", "analysis（多病因分析）", "results（干预与转归）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（衰老与衰弱理论）", "evidence synthesis（证据综述）", "future directions", "references"),
    },
    citation_style="AGS/JAGS 样式（作者-年份；J Am Geriatr Soc 遵循 AGS 规范）",
    reporting_standards={"k1": "RCT 遵循 CONSORT", "k2": "观察性研究遵循 STROBE", "k3": "病例报告遵循 CARE"},
    conventions=("衰弱评估工具首次出现给全称", "功能状态 ADL/IADL 须报告", "多重用药定义须明确", "认知评估注明版本", "老年综合征定义须规范"),
    key_venues=("Journal of the American Geriatrics Society", "Age and Ageing", "The Journals of Gerontology Series A", "JAMA Internal Medicine", "The Lancet Healthy Longevity"),
    units_and_formulas_notes=("量表分数无量纲，时间用月/年", "公式用 amsmath，衰弱指数计算式须明确", "数值结果给均值 ± SD/SEM 与样本量", "生存分析给 HR 与 95% CI"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("老年人综合评估软件（CGA）", "Fried 衰弱表型评估工具", "Frailty Index 计算平台", "MoCA 认知量表系统", "Tinetti 平衡与步态评估", "Morse 跌倒风险量表", "STOMP 多重用药筛选", "Beers 标准审查工具", "SPSS", "R", "REDCap 数据收集", "Epi Info 生存分析", "Cochrane 系统综述工具 RevMan", "SAS", "Stata", "WHO 功能性评估分类（ICF）", "老年营养 MNA 量表", "步态分析系统", "可穿戴传感器步态监测", "老年人睡眠监测设备"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "老年综合评估数据库（EPA）"),
)
