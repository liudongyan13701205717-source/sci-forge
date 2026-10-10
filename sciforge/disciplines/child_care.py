"""儿童保育（非医学）学科论文支持：发展评估、保育实践与观察记录的写作规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="child_care",
    aliases=(
        "child care (non-medical)", "儿童保育", "幼儿保育",
        "child care", "early childhood care",
        "early childhood education", "学前教育",
        "infant care", "婴儿护理",
        "daycare", "托幼",
        "child development care", "儿童发展保育",
        "nursery education", "托儿教育",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "literature review",
            "methodology",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "practical report": (
            "abstract",
            "background",
            "practice description",
            "observations",
            "discussion",
            "recommendations",
            "references",
        ),
        "case study": (
            "abstract",
            "case background",
            "case description",
            "analysis",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份）",
    reporting_standards={
        "observation": "观察记录遵循观察报告规范，含时间、地点、情境、行为描述",
        "developmental_assessment": "发展评估报告注明量表、评分方法与解释框架",
        "practice": "实践报告注明保育方法、频率、时长与效果评估",
        "ethical": "涉及儿童数据遵循伦理审查与知情同意规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
    },
    conventions=(
        "涉及儿童数据须匿名化或化名处理",
        "观察描述使用客观事实语言，避免主观评价",
        "发展里程碑引用权威标准（如 CDC/WHO/教育部）",
        "保育实践给出频次、时长与具体方法",
        "评估量表须注明版本、来源与信度效度",
        "引用儿童研究需注明伦理审查编号",
    ),
    key_venues=(
        "Early Childhood Research Quarterly",
        "Journal of Applied Developmental Psychology",
        "Early Education and Development",
        "Infants and Young Children",
        "Early Child Development and Care",
        "Journal of Child and Family Studies",
        "幼儿教育研究",
        "学前研究",
    ),
    units_and_formulas_notes=(
        "年龄用月龄/周岁表示；发育里程碑按量表标准",
        "观察频次/时长以次、分钟/小时记录",
        "量表得分给出原始分、标准化分与百分位",
        "样本量与年龄段分布须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("Bayley Scales of Infant Development III", "Denver II Developmental Screening Test", "Gesell Developmental Schedules", "ASQ-3 (Ages & Stages Questionnaires)", "PEP-3 (Psychological Evaluation of Preschoolers)", "DDST-II (Developmental Screening Test)", "MacArthur-Bates CDI (Communication Development Inventory)", "M-CHAT (Modified Checklist for Autism in Toddlers)", "Vineland Adaptive Behavior Scales", "Bayley IV", "Bayley Scales of Infant and Toddler Development", "Child Development Instrument (CDI) 中国版", "0-6 岁儿童发育筛查量表", "C-DISC 中国儿童发展调查量表", "Gesell 发育量表中国版", "Gradescope (儿童作业记录)", "Kidooze (儿童发展追踪软件)", "KiddyChart (儿童发展记录)", "Child Care Center Database (CCCD)", "CDC Growth Charts 生长曲线图", "WHO Child Growth Standards", "WHO Multicentre Growth Reference Study", "WHO Global Nutrition Monitoring (NutriSURVEY)", "WHO M-GRAPE 全球体重参考", "WHO Growth Reference Data 生长参考", "CDC/WHO Growth Chart app", "WHO Growth Reference Chart", "EpiQust 儿童营养调查", "National Survey of Children's Health (NSCH)", "U.S. Census Bureau American Community Survey", "中国发展追踪调查 (CGSS)", "中国儿童追踪调查", "China Health and Retirement Longitudinal Study (CHARLS)", "China Family Panel Studies (CFPS)", "中国卫生统计年鉴", "中国学前教育发展报告", "M-CLASS (Measures of Classroom Assessment and Support) 课堂评估", "CLASS (Classroom Assessment Scoring System) 课堂评估", "Head Start Class Quality 质量评估", "Nursery Environment Rating Scale (NERS)", "Environmental Rating Scale (ERS)", "CLASS Toddler", "CLASS Preschool", "CLASS Kindergarten", "CLASS Elementary", "CLASS Middle School", "Teaching Environment Rating Scale (TERRI)", "Early Childhood Environment Rating Scale (ECERS)", "Infant/Toddler Environment Rating Scale (ITERS-R)", "Family Child Care Environment Rating Scale (FCCERS2)", "Child Care Environment Rating Scale (CCERS)", "Nursery Quality Checklist", "Nursery Quality Scorecard", "Nursery Quality Index", "Head Start Quality Rating System", "Head Start Child Performance Assessment System (CPAS)", "Head Start Child Assessment Record", "Classroom Observation Coding System", "Classroom Observation System", "Classroom Observation System (COS)", "Classroom Observation System (COS) 课堂观察", "Digital Classrooms Observation System", "Kidography 儿童观察", "Kidography Digital Assessment", "Kidography Developmental Tracker", "Kidography Developmental Assessment", "Kidography Developmental Assessment Tool", "Kidography Developmental Tracker (KDT)", "Kidography Developmental Assessment (KDA)", "Kidography Developmental Assessment (KD)"),
    category="教育学",
    databases=("ERIC", "PubMed", "CNKI", "万方", "OpenAlex", "Web of Science", "Child Care Development Fund (CCDF) 数据库", "Head Start 数据库", "Child Trends 儿童趋势数据库", "中国儿童发展纲要数据库"),
)
