"""Teacher Training in Arts and Crafts 学科论文支持：艺术与设计类教师培训研究论文体裁、APA 引用样式与艺术教学学科教学法记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="teacher_training_in_arts_and_crafts",
    aliases=(
        "teacher_training_in_arts_and_crafts",
        "Teacher training in arts and crafts",
        "艺术与设计类教师培训",
        "艺术教师培养",
        "arts education",
        "design education",
        "craft pedagogy",
        "艺术教学",
        "视觉艺术教师培训",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与艺术/工艺教师培训问题）",
            "literature review",
            "methodology（研究设计与参与）",
            "findings",
            "discussion（对艺术教育与教师发展的意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case background（艺术教师培训项目案例）",
            "analysis",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "literature review",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（Studies in Art Education、Art Education、Teaching Art 遵循期刊规范）",
    reporting_standards={
        "sample": "样本须报告：参与者类型（初职/在职美术/设计/工艺教师）、人数 n、机构类型、学科领域",
        "design": "研究设计须报告：行动研究/民族志/质性/量化、数据收集方法（访谈/工作室观察/作品集分析/日志）",
        "ethics": "伦理审查须报告：机构审查（IRB/ERB）、知情同意、作品集使用授权",
        "curriculum": "课程与教学法须报告：项目式学习（PBL）、工作室教学法（Studio Teaching）、评价量规（Rubric）",
        "systematic_review": "系统综述遵循 PRISMA 2020 声明",
    },
    conventions=(
        "艺术教师培训研究遵循 NAfA（国家艺术教师协会）、YARM、ASE（澳大利亚艺术教育协会）、NCEFA（全国视觉教育联盟）框架",
        "艺术教学理论遵循 Dewey 实用主义、Rokeby 工作室学习、Crawford 工艺实践（Craft Practice as Research）、Duncan 视觉素养",
        "艺术作品评价量规遵循 NAfA Visual Thinking Strategies（VTS）、Bloom 分类（艺术领域）、Rubric 4 维（技能、构思、审美、表达）",
        "研究遵循 Kaupapa Māori、Tātou（毛利社区本位）如涉原住民艺术；伦理审查遵循 APA 伦理准则",
        "艺术工具与材料须报告材料名称、品牌、工艺步骤；摄影作品须报告相机、镜头、曝光参数",
        "符号约定：VTS、PBL、Studio Teaching 首次出现须给出全称；评价量规用 1-4 或 1-5 级评分",
    ),
    key_venues=(
        "Studies in Art Education",
        "Art Education: A Journal of Issues and Research",
        "Journal of Art & Design Education",
        "Studies in Art Education",
        "Teaching Art",
        "Curriculum Inquiry",
    ),
    units_and_formulas_notes=(
        "样本量报告 n 与观测数 N；作品评分用 1-4 级或 1-5 级评分（如 NAfA 4 级）；量表信度用 Cronbach α",
        "公式用 amsmath；效应量用 Cohen's d、η²、r；混合效应模型（HLM）须报告随机截距与斜率",
        "显著性用 *, **, *** 对应 10%/5%/1%；p 值报告精确值（p < .001 或 p = .032）",
        "所有比率与效应量保留 3 位小数；样本量 N 与参与者人数 n 须完整标注",
        "艺术工具材料命名遵循 ISO 标准（如纸张规格 A4/A3、颜料标准 Pantone TCX/TPG）；评价量规维度须明确",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe Creative Cloud", "Adobe Illustrator", "Adobe Photoshop", "Inkscape", "GIMP", "Procreate", "SketchUp", "Blender", "CLO 3D", "Moodle", "Google Classroom", "Zoom", "NVivo", "Atlas.ti", "Zotero", "EndNote", "SPSS", "R", "Google Docs", "Overleaf"),
    category="教育学",
    databases=("OpenAlex", "Crossref", "CNKI", "ERIC", "ProQuest"),
)
