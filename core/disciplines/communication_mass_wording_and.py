"""大众传播/媒体写作学科论文支持：传播学/新闻学体裁、APA 引用样式与传播研究记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="communication_mass_wording_and",
    aliases=("mass communication", "大众传播", "媒体写作", "新闻传播",
             "传播学", "媒体研究", "mass media", "journalism studies",
             "media and communication"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与理论框架）",
            "literature review（文献综述）",
            "methodology（研究方法与数据收集）",
            "findings（研究结果与数据分析）",
            "discussion（讨论与理论贡献）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例背景与概况）",
            "analysis（多维度分析）",
            "implications（启示与建议）",
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
        "content_analysis": "内容分析遵循编码框架规范，须报告编码信度",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "experimental": "实验研究须控制变量并报告随机化方法",
        "survey": "问卷调查须报告回收率、抽样方法与偏差分析",
    },
    conventions=(
        "传播学实证研究须明确数据来源、抽样方法与样本量",
        "内容分析须说明编码框架、编码员数量与信度（Kappa 系数）",
        "实验研究须控制变量并报告随机化方法与样本量",
        "媒体效果研究须区分短期与长期效果，避免过度归因",
        "跨文化比较研究须说明文化背景与等效性检验",
    ),
    key_venues=(
        "Journal of Communication",
        "Public Communication",
        "Communication Research",
        "Journal of Communication Inquiry",
        "Media, Culture & Society",
        "国际新闻界",
        "新闻与传播研究",
        "现代传播",
    ),
    units_and_formulas_notes=(
        "统计结果报告均值 ± 标准差与样本量",
        "显著性检验报告 t/F/χ² 值与 p 值",
        "效应量报告 Cohen's d / η² / ω²",
        "信度报告 Cronbach's α 或 Kappa 系数",
        "回归分析须报告 R² 与调整 R²",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("NVivo", "SPSS", "Qualtrics", "SurveyMonkey", "Tableau", "Adobe Premiere Pro", "Final Cut Pro", "Avid Media Composer", "DaVinci Resolve", "OBS Studio", "Camtasia", "Microsoft Teams", "Zoom", "Notion", "Miro", "Prezi", "WeChat", "Weibo", "Twitter/X", "CNN", "Reuters", "AP Stylebook", "Google Analytics", "Newspaper Next", "AllSides", "MediaCloud"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "万方", "Web of Science"),
)
