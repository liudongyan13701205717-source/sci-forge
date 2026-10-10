"""Curriculum development (theory) 学科论文支持：课程开发理论与流程体裁、教育学报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="curriculum_development",
    aliases=(
        "curriculum_development",
        "curriculum development (theory)",
        "curriculum development and theory",
        "课程开发",
        "课程论",
        "课程理论与开发",
        "instructional design",
        "curriculum theory",
        "instructional development",
        "curriculum planning and evaluation",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "methodology（研究方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "development_report": (
            "abstract",
            "introduction（需求分析）",
            "needs analysis（需求与差距分析）",
            "learning objectives（学习目标陈述）",
            "content and structure（内容体系与结构）",
            "assessment design（评价设计）",
            "validation and piloting（专家论证与试点）",
            "references",
        ),
        "framework_proposal": (
            "abstract",
            "introduction",
            "theoretical basis（理论基础）",
            "framework description（框架陈述）",
            "example application（应用示例）",
            "limitations（局限）",
            "references",
        ),
    },
    citation_style="APA 第7版（教育学主流规范，APA 7）",
    reporting_standards={
        "needs_analysis": "需求分析须报告数据源（政策文本、利益相关者访谈、成绩数据）与抽样",
        "objectives": "学习目标遵循行为目标表述规范（布鲁姆修订版认知层级），每条目标可测量",
        "validation": "课程论证须报告专家构成、修订轮次与一致性指标（Kendall's W / Kendall's H）",
        "pilot_study": "试点须报告受试规模、时长、实施保真度（fidelity）与前后测结果",
        "equity": "涉及教育公平评估须报告分组变量与差异检验方法",
    },
    conventions=(
        "课程开发流程须显式标注所依模型（如 Tyler 模式、TABA、Dick 系统开发、ADDIE、逆向设计）及所用版本",
        "学习目标统一使用「行为动词 + 内容 + 条件 + 标准」四要素表述，动词取自布鲁姆修订分类",
        "课程地图（curriculum map）须注明列维度（学段/模块）与行维度（目标/能力）的对应规则",
        "评价工具须区分形成性评价与总结性评价，并声明与目标的对齐关系（alignment matrix）",
        "修订轮次与意见采纳情况须逐条记录，形成可追溯的修订表",
        "政策引用须给出文件全称、发布机构、文号与年份",
    ),
    key_venues=(
        "Educational Researcher",
        "The Journal of Curriculum and Instruction",
        "Journal of Curriculum Studies",
        "Instructional Science",
        "Review of Instructional Design",
        "AACE Journal",
        "课程·教材·教法",
    ),
    units_and_formulas_notes=(
        "课时以 min/学时为单位统一计量，注明学时定义（45 min 或 48 min）",
        "信度报告 Cronbach's α 或 KR-20，效度以对齐矩阵覆盖率（%）表述",
        "专家一致性报告 Kendall's W 并给出显著性检验",
        "样本量与缺失率须报告；分组比较报告均值±标准差",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Moodle", "Canvas (Instructure)", "Blackboard Learn", "D2L Brightspace", "Articulate Storyline 360", "Articulate Rise 360", "iSpring Suite", "Adobe Captivate", "Lectora", "SCORM Cloud", "H5P", "Camtasia", "OASIS (Objectives & Strategies Alignment System)", "Miro", "Lucidspark", "XMind", "MindManager", "Kahana (Curriculum Mapping)", "Qualtrics", "Delphi21", "NVivo", "SPSS", "RStudio", "Zotero", "LaTeX"),
    category="教育学",
    databases=("ERIC", "CNKI", "万方", "OpenAlex", "Crossref", "Web of Science"),
)
