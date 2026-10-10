"""青少年服务学科论文支持：青少年福利与社会工作研究、APA 引用样式与服务评估注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="youth_services",
    aliases=("youth_services", "青少年服务", "青年福利服务", "youth services", "youth welfare", "child protection"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与服务问题）",
            "literature review（青少年服务研究综述）",
            "methods（方法与设计）",
            "results（结果）",
            "discussion（讨论与意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "context（服务情境）",
            "case description（案例描述）",
            "analysis（分析）",
            "implications（意义）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and search（范围与检索）",
            "evidence synthesis（证据综合）",
            "future directions（未来方向）",
            "references",
        ),
    },
    citation_style="APA 第 7 版样式（作者-年份）",
    reporting_standards={
        "service_design": "服务设计须报告目标、对象、内容与交付方式",
        "outcome_measurement": "成果测量须报告指标、工具与信效度",
        "youth_wellbeing": "青少年福祉须遵循 SDYI/WHO 等标准",
        "ethics": "青少年研究伦理审批与知情同意须给出",
        "statistics": "统计检验与样本量须报告",
    },
    conventions=(
        "服务类型遵循心理健康/教育/福利/保护等分类",
        "青少年福祉遵循 SDYI/WHO 等定义",
        "服务评估遵循逻辑模型与 MEASURE 等框架",
        "青少年参与情况须完整报告",
        "服务情境描述完整（社区、年龄、文化）"
    ),
    key_venues=(
        "Child & Youth Care Forum",
        "Journal of Youth and Adolescence",
        "Children and Youth Services Review",
        "Youth Violence and Juvenile Justice",
        "Journal of Child and Family Studies"
    ),
    units_and_formulas_notes=(
        "服务时长用小时/月表示",
        "青少年福祉用 SDYI 量表（1-5）评估",
        "样本量 n 与置信区间须给出",
        "p 值用 <0.05/<0.01/<0.001 表示显著性"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Qualtrics", "SurveyMonkey", "SPSS", "R (lme4)", "Stata", "MPlus", "SmartPLS", "NVivo", "Atlas.ti", "MAXQDA", "Tableau", "Power BI", "Excel", "SACWIS (儿童福利信息系统)", "CCWIS (儿童福利信息系统)", "Youth Policy Tool (Youth Policy Initiative)", "Youth Voice Tool", "Youth Wellbeing Toolkit", "Youth Development Framework", "Social Work Case Management Software"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
