"""科研方法论学科论文支持：科研方法论/研究方法论体裁、APA 引用样式与科研方法论记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="research_methodology",
    aliases=("research_methodology", "科研方法论", "研究方法论", "研究设计", "research methods"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与方法论问题）",
            "methods（方法框架与论证）",
            "results（方法评估数据）",
            "discussion（方法论意义）",
            "references",
        ),
        "methodological_review": (
            "abstract",
            "introduction",
            "method landscape（方法谱系）",
            "comparison（方法比较与评估）",
            "recommendations（方法建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Res Synth Methods 遵循 Wiley 规范）",
    reporting_standards={
        "methodological": "方法论研究遵循方法评估报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "meta_analysis": "荟萃分析遵循 PRISMA 声明",
        "simulation": "仿真研究遵循仿真实验报告规范",
        "preregistration": "预注册研究遵循预注册报告规范",
    },
    conventions=(
        "方法适用范围与假设须明确",
        "方法评估基准与指标须报告",
        "与既有方法的对比须系统",
        "局限性（偏差、适用条件）须讨论",
        "可复现性（代码、数据）须声明",
    ),
    key_venues=(
        "Research Synthesis Methods",
        "Journal of Research Methodology",
        "Organizational Research Methods",
        "Sociological Methods & Research",
        "Psychological Methods",
        "Journal of Clinical Epidemiology",
    ),
    units_and_formulas_notes=(
        "指标无量纲或按定义；比例用 %",
        "公式用 amsmath；偏差与效能计算式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与运行次数",
        "模拟结果给出置信区间与收敛诊断",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著"),
    tools=("统计分析软件（SPSS/R）", "质性编码软件（NVivo）", "PRISMA 流程图工具"),
    category="交叉学科",
    databases=("OpenAlex", "Crossref", "arXiv", "Semantic Scholar", "Zenodo"),
)