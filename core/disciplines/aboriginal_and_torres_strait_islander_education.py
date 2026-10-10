"""Aboriginal And Torres Strait Islander Education 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aboriginal_and_torres_strait_islander_education",
    aliases=(
        "Aboriginal And Torres Strait Islander Education",
        "原住民教育",
        "ATSI Education",
        "Indigenous Education",
        "First Nations Education",
        "Aboriginal Pedagogy",
        "Torres Strait Islander Education",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA",
    reporting_standards={
        "care": "原住民教育研究须遵循 CARE 原则（集体性、代理权、互惠、伦理）",
        "ocap": "原住民数据须遵循 OCAP 原则",
        "child_protection": "涉及儿童研究须遵循儿童参与研究的额外保护要求",
        "mixed_methods": "混合方法研究须报告定量与定性数据整合策略",
    },
    conventions=(
        "教育研究须反映原住民教育主权（CARE原则：集体性、代理权、互惠、伦理）",
        "课堂观察须尊重社区文化规范，事先获得学校及社区同意",
        "学习成果报告须包含定量数据及定性民族志分析",
        "涉及儿童数据须遵循儿童参与研究的额外保护要求",
    ),
    key_venues=(
        "Australian Journal of Indigenous Education",
        "Education Australia",
        "Journal of Aboriginal and Torres Strait Islander Educational Research",
        "Aboriginal Education Research Journal",
        "Asia Pacific Education Review",
        "International Journal of Multicultural and Multiracial Education",
    ),
    units_and_formulas_notes=(
        "学习成果须报告通过率（%）与平均分（M/SD），按原住民与非原住民分组比较",
        "教育干预效果须报告效应量（Cohen's d 或 Hedges' g）及 95% 置信区间",
        "问卷信度须报告 Cronbach's α，效度须报告构念效度指标",
        "班级规模以人数（n）计量，出勤率以百分比（%）报告并注明统计周期",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "NVivo", "JASP", "R", "Stata", "SurveyMonkey", "Qualtrics", "Google Forms", "EndNote", "Moodle", "Canvas", "Zoom", "Google Classroom", "Microsoft OneNote", "Adobe Capture", "iRecord", "Microsoft Excel", "ATLAS.ti", "Dedoose", "RefWorks"),
    category="教育学",
    databases=("OpenAlex",),
)
