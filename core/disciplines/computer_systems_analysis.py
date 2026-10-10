"""计算机系统分析学科论文支持：系统分析与需求工程体裁、IEEE/APA 引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_systems_analysis",
    aliases=(
        "computer systems analysis", "计算机系统分析", "系统分析",
        "system analysis", "需求工程", "requirements engineering",
        "system requirements analysis", "系统需求分析", "业务分析", "business analysis",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work",
            "method（分析方法与设计技术）",
            "case study（案例验证）",
            "conclusion",
            "references",
        ),
        "empirical": (
            "abstract",
            "introduction",
            "methodology（研究设计与数据来源）",
            "results（分析发现）",
            "discussion（解释与启示）",
            "conclusion",
            "references",
        ),
        "position": (
            "abstract",
            "problem statement",
            "analysis",
            "implications",
            "references",
        ),
    },
    citation_style="APA 7（信息系统/软件工程常用）",
    reporting_standards={
        "empirical": "经验研究遵循 SE 经验研究规范",
        "case": "案例研究遵循 IS/SE 案例研究方法论",
        "requirements": "需求追溯与覆盖率须报告",
    },
    conventions=(
        "使用 UML/BPMN/DFD 术语须遵循各自标准定义（类/对象/参与者的区别）",
        "需求编号（FR/UR/NFR）与追溯矩阵须在方法或附录给出",
        "案例研究须标注案例选择准则与证据三角验证",
        "术语表首次出现即给出缩写与全称",
    ),
    key_venues=(
        "Journal of Systems and Software",
        "Requirements Engineering (RE)",
        "IEEE Transactions on Software Engineering",
        "IEEE Software",
        "Journal of Management Information Systems (JMIS)",
        "ACM Transactions on Software Engineering and Methodology (TOSEM)",
        "IEEE Transactions on Engineering Management",
    ),
    units_and_formulas_notes=(
        "需求覆盖率、追溯率、稳定性指标须给出计算式与分母口径",
        "时长与成本用统一货币/时间口径",
        "公式用 amsmath；统计量给出置信区间",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Enterprise Architect", "IBM Rational DOORS", "Hazel", "Polarion ALM", "Atlassian Jira", "Confluence", "Lucidchart", "Draw.io", "Microsoft Visio", "Bizagi Modeler", "Camunda BPMN", "PlantUML", "Mermaid", "SQuirreL SQL Manager", "Oracle Modeler", "Jama Connect", "CA Agile Central", "Azure DevOps", "Redmine", "Modelio"),
    category="工学",
    databases=("OpenAlex", "Crossref", "IEEE Xplore"),
)
