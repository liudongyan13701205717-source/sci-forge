"""舞蹈学学科论文支持：编舞/历史/教育体裁、Chicago 引用样式与人文学科注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="dance",
    aliases=(
        "dance", "舞蹈", "舞蹈学", "舞蹈研究", "编舞学", "舞蹈教育",
        "choreography", "dance studies", "dance research", "dance history",
        "舞蹈史", "舞蹈批评",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（问题与背景）",
            "literature review（文献综述）",
            "analysis（分析）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "choreographic_analysis": (
            "abstract",
            "introduction",
            "work（作品）",
            "analytical framework（分析框架）",
            "findings（发现）",
            "conclusions（结论）",
            "references",
        ),
        "practice_based": (
            "abstract",
            "introduction",
            "creative process（创作过程）",
            "performance（演出）",
            "reflection（反思）",
            "conclusions（结论）",
            "references",
        ),
    },
    citation_style="Chicago 样式（作者-年份或注-书目；Dance Research Journal 遵循 Chicago 规范）",
    reporting_standards={
        "choreographic": "编舞分析遵循作品分析报告规范",
        "practice": "实践研究遵循创作实践报告规范",
        "historical": "历史研究遵循史料来源报告规范",
        "qualitative": "质性研究遵循 COREQ/SRQR 报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "作品信息（编导/舞团/首演日期）须完整",
        "记谱法须注明（如 Labanotation/BENNY 符号体系）",
        "演出语境须交代（剧场、观众、时长）",
        "引文给出页码",
        "分析框架须明确（如 Lysas/Allen/Deke 分析框架）",
    ),
    key_venues=(
        "Dance Research Journal",
        "Dance Chronicle",
        "Journal of Dance Education",
        "Dance Research",
        "Ballet Review",
        "Research in Dance Education",
        "Journal of Aesthetic Education",
    ),
    units_and_formulas_notes=(
        "时长用 分:秒",
        "引文给出页码",
        "版本与版次须注明",
        "时间用统一纪年格式",
        "货币用统一币种并注明年份",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("DanceForms", "Labanotation", "BENNY Motion Capture", "Vicon Vantage", "Motion Capture (Vicon/Vicon Shaker)", "Xsens MVN Animate", "OptiTrack", "Noitom Perception Neuron", "Rokoko SMPL-X", "CueMotion", "Pro-Dance (DanceNotationLab)", "Choreographer for Mac", "Final Cut Pro", "Adobe Premiere Pro", "Adobe After Effects", "DaVinci Resolve", "MAG3D", "Rokoko Studio", "Proximity (MoCap)", "MoCap Studio Pro", "DanceMotion Editor", "BodyBuilder (Choreo)", "Notate Me", "Labanotation Composer", "ChoreaTrack", "iDance"),
    category="艺术学",
    databases=("DOAJ", "OpenAlex", "Crossref", "CNKI"),
)
