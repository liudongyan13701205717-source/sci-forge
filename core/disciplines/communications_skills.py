"""通信技能/沟通技能学科论文支持：人际沟通/公共关系/演讲训练体裁、APA 引用样式与教学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="communications_skills",
    aliases=("communications skills", "沟通技能", "沟通技巧",
             "人际传播", "公共关系", "interpersonal communication",
             "communication skills", "public speaking",
             "business communication"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与理论框架）",
            "literature review（文献综述）",
            "methodology（研究方法与培训设计）",
            "findings（培训效果与数据分析）",
            "discussion（讨论与实践意义）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景与培训概况）",
            "analysis（多维度效果分析）",
            "implications（启示与改进建议）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "scope and method（综述范围与方法）",
            "state of the art（现状分类）",
            "gaps and outlook（缺口与展望）",
            "references",
        ),
    },
    citation_style="APA 第7版样式（作者-年份制）",
    reporting_standards={
        "empirical": "实证研究遵循 APA 报告规范，须报告样本量、统计检验与效应量",
        "training_evaluation": "培训效果评估须采用前后测设计并报告效应量",
        "case_study": "案例研究须标注应用场景与实施细节",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "experimental": "实验研究须控制变量并报告随机化方法",
    },
    conventions=(
        "沟通技能研究须明确研究对象、情境与评估指标",
        "培训效果评估须采用前后测设计，报告效应量与显著性",
        "教学案例须标注应用场景、目标群体与实施周期",
        "跨文化研究须说明文化背景与等效性检验",
        "访谈研究须报告编码框架与信度",
    ),
    key_venues=(
        "Journal of Communication",
        "Public Communication",
        "Communication Research",
        "Quarterly Journal of Speech",
        "Journal of Business Communication",
        "现代传播",
        "国际新闻界",
    ),
    units_and_formulas_notes=(
        "统计结果报告均值 ± 标准差与样本量",
        "显著性检验报告 t/F/χ² 值与 p 值",
        "效应量报告 Cohen's d / η² / ω²",
        "信度报告 Cronbach's α 或 Kappa 系数",
        "培训效果须报告预测试/后测试得分变化",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("NVivo", "SPSS", "Qualtrics", "SurveyMonkey", "Tableau", "OBS Studio", "Zoom", "Microsoft Teams", "Google Meet", "Slack", "Notion", "Miro", "Prezi", "Camtasia", "Adobe Premiere Pro", "DaVinci Resolve", "Lightroom", "Photoshop", "PowerPoint", "Canva", "Trello", "Asana", "Monday.com", "Google Forms", "Typeform", "Kahoot!"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "Web of Science"),
)
