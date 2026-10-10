"""社会政策学科论文支持：福利体制/循证政策/政策评估体裁、Chicago 引用样式与政策研究规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="social_policy",
    aliases=("social_policy", "社会政策", "福利政策", "公共政策", "welfare policy", "policy analysis", "social welfare", "public policy"),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与政策分析框架）",
            "methods（数据、模型、识别策略）",
            "results（结果与稳健性）",
            "discussion（讨论与政策含义）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（政策情境、制度与文本）",
            "analysis（政策过程与文本分析）",
            "results",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "literature search（政策文献检索）",
            "evidence synthesis（政策证据综合）",
            "future directions",
            "references"
        )
    },
    citation_style="Chicago 作者-年份（Journal of European Social Policy 遵循 APA；JSS 与 WPR 遵循 Chicago）",
    reporting_standards={
        "causal_inference": "政策评估遵循 Rubin 潜在结果框架：平行趋势、事件时间、稳健性（安慰剂、剔除、DID）",
        "qualitative": "质性研究遵循 COREQ 清单：政策过程、访谈、文件编码、反思性",
        "systematic_review": "循证综述遵循 PRISMA 与 GRADE 分级：偏倚风险、证据强度、异质性",
        "policy_simulation": "政策仿真报告参数、初始条件、随机种子与情景；结果给出置信区间"
    },
    conventions=(
        "政策情境须报告：政策文本版本、时间窗口、执行机构、目标群体定义",
        "福利体制分类（Esping-Andersen 三类）须声明并说明跨国可比性",
        "政策评估方法（DID/RD/PSM）须报告识别假设、平行趋势图与稳健性检验",
        "跨制度比较须声明统计单位（人/户/企业）与时间口径",
        "定量表格三线制；类别变量给频数与百分比（注明基数 N）"
    ),
    key_venues=(
        "Journal of European Social Policy",
        "Journal of Social Policy",
        "World Politics Review",
        "Policy Studies",
        "Social Policy & Society"
    ),
    units_and_formulas_notes=(
        "政策覆盖率 = 受益人数 / 目标人数 × 100%；财政支出占 GDP 百分比给出分母定义",
        "平均处理效应 ATE = E[Y(1) - Y(0)]；处理组平均效应 ATET = E[Y(1) - Y(0) | D=1]",
        "政策时点（year、month、week）与政策前/后窗口须声明；事件时间图给出处",
        "百分比给出基数 N；加权数据注明权重变量与权重比（design effect）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("R", "RStudio", "Stata", "SPSS", "Python", "NVivo", "MAXQDA", "Dedoose", "ATLAS.ti", "Qualtrics", "SurveyMonkey", "Tableau", "Power BI", "ArcGIS", "PolicyMap", "Qlik Sense", "Mendeley", "Zotero", "EndNote", "Excel"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI")
)
