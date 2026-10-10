"""社会福利未进一步定义学科论文支持：社会福利服务的微观实践与服务系统评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="welfare_not_further_defined",
    aliases=(
        "welfare not further defined",
        "社会服务",
        "社区服务",
        "个案管理",
        "social service",
        "community service",
        "case management",
        "社会工作服务",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题陈述与意义）",
            "literature review（理论框架与实证回顾）",
            "methodology（质性/量化/混合方法设计）",
            "findings（服务过程与成效发现）",
            "discussion（意义讨论与局限）",
            "conclusion（实践建议）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "service context（服务背景与对象描述）",
            "intervention process（介入过程描述）",
            "outcome measurement（成效评估方法）",
            "reflection（反思与改进建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "service models overview（服务模式综述）",
            "effectiveness evidence（成效证据综合）",
            "practice challenges（实践困境）",
            "recommendations（实践建议）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "participant consent": "质性研究须说明知情同意获取方式与伦理审查批准编号",
        "triangulation": "质性分析须说明三角验证策略（来源/方法/研究者三角化）",
        "effectiveness measurement": "服务成效评估须说明前测-后测设计、对照组设置与统计检验",
        "anonymization": "案例研究中当事人信息须彻底匿名化，敏感细节合理虚构",
    },
    conventions=(
        "服务对象描述避免标签化，采用「服务使用者/社区居民」等尊重性用语",
        "质性引文须标注受访者编码（如 P1、P2）并保留原文语言",
        "服务流程描述区分直接服务（direct practice）与间接服务（indirect practice）",
        "成效评估区分过程性指标（过程）与结果性指标（成效）",
        "反思性写作须区分个人经验与专业判断的边界",
    ),
    key_venues=(
        "British Journal of Social Work",
        "Social Work Research",
        "Journal of Advanced Nursing",
        "Qualitative Social Work",
        "Administration and Policy in Mental Health and Mental Health Services Research",
    ),
    units_and_formulas_notes=(
        "个案服务量单位：人次/人次·月",
        "成效指标：服务满意度（5 级 Likert 量表）、目标达成率（%）",
        "服务成本单位：元/人次；人力配置：全职当量（FTE）",
        "覆盖范围：服务人口覆盖率（%）= 实际服务人数/目标人口×100",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo 质性分析软件", "MAXQDA 质性编码工具", "ATLAS.ti 文本分析平台", "R 语言统计分析", "Stata 计量软件", "SPSS 统计分析软件", "Python 数据处理（pandas）", "SurveyMonkey 在线问卷平台", "Qualtrics 在线调研系统", "Tableau 数据可视化", " Gephi 社会网络分析", "VosViewer 文献计量可视化", "CiteSpace 知识图谱可视化", "LaTeX 学术排版", "EndNote 文献管理", "Joplin 田野笔记记录工具", "Audacity 录音转文字处理", "Otter.ai 语音转录平台", "Miro 白板协作工具", "Qualtrics XM 体验管理"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
