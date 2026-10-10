"""体育综合学科论文支持：竞技/大众体育体裁、APA 引用样式与体育学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="sports",
    aliases=("sports", "体育", "体育运动", "竞技体育", "大众体育", "physical education and sports"),
    paper_types={
        "research": ("abstract", "introduction（背景）", "methods（方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（综述）", "evidence synthesis（证据）", "future directions", "references"),
    },
    citation_style="APA 7th（体育学研究主流）",
    reporting_standards={
        "quantitative_study": "定量研究遵循 CONSORT/STROBE，报告效应量与 95% CI",
        "qualitative_study": "质性研究遵循 COREQ 或 SRQR 清单",
        "program_evaluation": "体育项目评估遵循 Kirkpatrick 模型与 RE-AIM",
    },
    conventions=(
        "受试者或运动员人口学特征（年龄、性别、训练年限）须报告",
        "运动项目与竞赛水平（业余/半职业/职业）须区分",
        "测试方案须可复现，含测试时间、场地与装备",
        "体育项目名词首次出现给出全称与英文对照",
        "数据缺失、脱落样本须说明",
    ),
    key_venues=(
        "Journal of Sports Sciences",
        "Sports Medicine",
        "International Review of Sport & Exercise Psychology",
        "Research Quarterly for Exercise, Health, and Fitness",
        "身体文化与体育评论 (Sport Education Review)",
    ),
    units_and_formulas_notes=(
        "力量指标用 kg 或 W/kg；耐力用 min 或 km",
        "主观感受用 RPE（6-20 或 CR-10），量表须注明",
        "公式用 amsmath；相对强度与功率换算须明确",
        "数值结果给出均值 ± SD/SEM 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Catapult 惯性传感器", "Polar 心率监测", "Garmin 运动手表", "Wahoo 功率计", "Hudl 视频分析", "Wysopal 战术软件", "FinalBall 数据分析", "InStat 比赛数据", "Whoop 恢复监测", "Oura Ring 睡眠监测", "InBody 体成分分析仪", "Kistler 测力台", "K5 代谢车", "Trackman 雷达追踪", "Sony PXW 高速摄像机", "R", "SPSS", "NVivo 质性分析", "Tableau 数据可视化", "Google Sheets"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "PubMed"),
)
