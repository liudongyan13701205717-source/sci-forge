"""合作学科论文支持：组织行为学/团队动力学体裁、APA 引用样式与管理学写作约定。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="cooperation",
    aliases=(
        "合作", "协作", "团队合作", "Co-operation", "Cooperation",
        "Collaboration", "Interpersonal Coordination",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
        "review": (
            "摘要",
            "引言",
            "理论框架",
            "文献综述",
            "整合与讨论",
            "结论",
            "参考文献",
        ),
        "empirical": (
            "摘要",
            "引言",
            "理论假设",
            "方法",
            "结果",
            "讨论",
            "参考文献",
        ),
    },
    citation_style="APA 第 7 版",
    reporting_standards={
        "measurement": "合作行为须使用标准化量表测量（如 CSQ、Team Scale）",
        "context": "须报告研究背景（组织、行业、文化）",
        "reliability": "量表须报告 Cronbach's α 或 AVE",
        "confounding": "须讨论可能的混淆变量（如文化因素）",
    },
    conventions=(
        "区分'合作'（cooperation）与'协作'（collaboration）的概念边界",
        "量表引用须注明原版来源与中文修订情况",
        "跨文化研究须说明文化维度（如 Hofstede 维度）",
        "效应量报告 Cohen's d 或 η²",
        "区分合作结果（outcome）与合作过程（process）指标",
    ),
    key_venues=(
        "Academy of Management Review",
        "Journal of Management Studies",
        "Small Group Research",
        "Journal of Organizational Behavior",
        "Group Dynamics: Theory, Research, and Practice",
        "管理世界",
    ),
    units_and_formulas_notes=(
        "量表数据使用均值±标准差报告",
        "路径分析系数标注显著性水平",
        "多群组分析须报告模型拟合指数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("MS Teams", "Slack", "Asana", "Monday.com", "Trello", "Notion", "Jira", "Miro", "Mural", "Figma（团队协作）", "Google Workspace", "SPSS", "AMOS（结构方程模型）", "Mplus", "NVivo（质性分析）", "ATLAS.ti", "Collaboration Research Repository（CRR）", "SurveyMonkey（团队调查工具）", "Zoom（远程协作）", "ClickUp（项目管理）"),
    category="管理学",
    databases=("Scopus", "Web of Science", "PsycINFO", "中国知网", "Hbr.org（哈佛商业评论数据库）", "GLOBE Project（全球领导力研究数据库）"),
)
