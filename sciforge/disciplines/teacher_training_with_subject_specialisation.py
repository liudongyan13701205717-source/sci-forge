"""学科专门化教师教育学科论文支持：学科教学知识/教学设计的体裁、APA 7 引用样式与研究注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_with_subject_specialisation",
    aliases=(
        "teacher_training_with_subject_specialisation",
        "教师教育",
        "学科教师培养",
        "学科教学知识",
        "Teacher training with subject specialisation",
        "subject-matter teacher education",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、教学问题与假设）",
            "methods（研究设计与数据采集）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "design_based_research": (
            "abstract",
            "introduction（设计诉求与理论基点）",
            "design cycle（设计—实施—反思迭代）",
            "findings（发现与原理提炼）",
            "design principles（设计原则）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与筛选方法）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份制，教育研究主流规范）",
    reporting_standards={
        "empirical": "实证研究须报告样本量、测量工具与信效度",
        "classroom_research": "课堂研究须说明情境、伦理审批与知情同意",
        "quantitative": "量化研究须报告效应量、置信区间与缺失数据处理",
        "systematic_review": "系统综述遵循 PRISMA 声明与 PROSPERO 注册",
        "mixed_methods": "混合方法研究遵循 MMRM（Creswell）报告规范",
    },
    conventions=(
        "被研究者用化名或编号匿名化，学校/地区作模糊处理",
        "量表题项与评分标准须在附录完整呈现",
        "信度报告 Cronbach's α；分析框架报告编码者与信度",
        "研究问题与假设须逐条对应结果小节",
        "教学干预须描述剂量（时长、频次）与对照设置"
    ),
    key_venues=(
        "Journal of Teacher Education",
        "Teaching and Teacher Education",
        "Journal of Research in Science Teaching",
        "Learning and Instruction",
        "Research in Science Education",
    ),
    units_and_formulas_notes=(
        "显著性用 p 值（标注校正方式）；效应量用 Cohen's d 或 η²",
        "公式用 amsmath；效应量与相关系数须给出估计区间",
        "显示公式仅在被正文引用时编号；行内公式避免复杂分式",
        "时间投入用课时（45/50 分钟）而非百分比"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("GeoGebra", "Desmos", "PhET Simulations", "Tinkercad", "CmapTools", "Google Classroom", "Nearpad", "Socrative", "Word Wall", "NVivo", "MAXQDA", "SPSS", "R", "Jamovi", "Microsoft Excel", "LaTeX", "Zotero", "Google Slides", "OneNote Class Notebook", "Miro"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC"),
)
