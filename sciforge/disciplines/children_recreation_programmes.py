"""儿童娱乐与休闲项目学科论文支持：儿童活动、营期活动与休闲学习研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="children_recreation_programmes",
    aliases=(
        "children recreation programmes", "儿童娱乐项目",
        "儿童休闲项目", "儿童活动项目",
        "children's recreation", "儿童娱乐活动",
        "child recreation", "儿童休闲学习",
        "recreation education", "休闲教育",
        "youth recreation", "青少年休闲",
        "camp programme", "营地项目",
        "after-school programme", "课后项目",
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
        "case study": (
            "abstract",
            "background",
            "programme description",
            "results",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "state of the art",
            "challenges and future",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份）",
    reporting_standards={
        "observation": "观察记录遵循观察报告规范",
        "intervention": "干预研究遵循 PRECIS-2 报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "ethical": "涉及儿童数据遵循伦理审查与知情同意规范",
    },
    conventions=(
        "涉及儿童数据须匿名化或化名处理",
        "活动/项目描述给出目标、频次、时长与效果评估",
        "评估量表须注明版本、来源与信度效度",
        "伦理审查编号须在文首声明",
        "引用儿童研究须注明法律/伦理依据",
    ),
    key_venues=(
        "Journal of Park Science",
        "Leisure Sciences",
        "Journal of Leisure Research",
        "Journal of Outdoor Recreation and Tourism",
        "Early Education and Development",
        "Youth Services Quarterly",
        "Journal of Child and Family Studies",
        "中国儿童青少年研究",
    ),
    units_and_formulas_notes=(
        "年龄用月龄/周岁表示；活动频次/时长以次、分钟/小时记录",
        "量表得分给出原始分、标准化分与百分位",
        "样本量与年龄段分布须报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("Bayley IV 婴儿发育量表", "Denver II Developmental Screening Test", "Gesell Developmental Schedules", "ASQ-3 (Ages & Stages Questionnaires)", "DDST-II Developmental Screening Test", "MacArthur-Bates CDI", "M-CHAT-R/F 自闭症筛查", "Pediatric Symptom Checklist (PSC-17)", "Strengths and Difficulties Questionnaire (SDQ)", "Child Behavior Checklist (CBCL)", "Youth Self-Report (YSR)", "Parenting Behavior Inventory (PBI)", "HOME (Home Environment Scale)", "Family Environment Scale (FES)", "Kidography (儿童观察记录)", "Kidography Developmental Assessment", "Kidography Digital Assessment (KDA)", "National Association for Sport and Physical Activity Participation (NASPAP)", "National Recreation & Park Association (NRPA)", "Child Trends Database", "CDC Youth Risk Behavior Surveillance System (YRBSS)", "National Survey of Children's Health (NSCH)", "CDC Childhood Physical Activity Guidelines", "ACSM (American College of Sports Medicine) 青少年健康指南", "WHO Physical Activity Guidelines for Children and Adolescents", "WHO 儿童青少年身体活动指南", "CATCH (Creating Active Teenagers and Children)", "CATCH 儿童活动干预项目", "Project EX (Project Excalibur)", "Project EX 儿童活动干预", "Physical Activity in Children and Youth (PAC) 项目", "SPARK (Stride of Progress in Academic and Recreational Kids)", "After-School Specials 课后节目", "Boys & Girls Clubs of America 俱乐部", "YMCA 少年宫", "Girl Scouts of the USA 女童军", "Boy Scouts of America 男童军", "4-H Club 4H 青年会", "Campfire Girls 森林女孩", "YMCA 中国少年宫", "中国少年宫 (Chinese Palace of Youth)", "中国儿童少年科技促进会", "中国休闲学研究会", "中国体育科学学会", "中国户外休闲协会", "中国休闲教育协会", "中国青少年发展基金会", "中国儿童少年体育科学学会", "Outdoor Education Association", "Outdoor Education Association (UK)", "Outdoor Education Association International", "National Association for Outdoor & Environmental Education (NAOE)", "National Outdoor Leaders Training Field (NOLTF)", "National Outdoor Education Centre", "National Outdoor Leadership School (NOLS)"),
    category="教育学",
    databases=("ERIC", "PubMed", "CNKI", "万方", "OpenAlex", "Web of Science", "National Recreation Association (NRA) 数据库", "Youth Sports U.S. 数据库", "National Recreation & Park Association (NRPA) 数据库"),
)
