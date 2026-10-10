"""Choreography 学科论文支持：编舞创作/舞蹈学体裁、APA 与运动科学报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="choreography",
    aliases=(
        "Choreography", "choreography", "choreographer",
        "choreographic works", "dance composition",
        "编舞", "舞蹈编排", "舞蹈创作", "舞谱记录", "编舞学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（创作语境与编舞问题）",
            "methodology（编舞方法/分析框架/田野方法）",
            "findings（编舞策略与身体/空间/时间分析）",
            "discussion（与舞蹈学、表演研究对话）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "work_description",
            "analysis",
            "performance_context",
            "references",
        ),
        "movement_analysis": (
            "abstract",
            "introduction",
            "movement_coding（Laban/RST 或编舞家自定编码）",
            "results（运动学/运动学参数）",
            "discussion",
            "references",
        ),
    },
    citation_style="APA 7 样式（作者-年份；Performance Research 期刊遵循 APA）",
    reporting_standards={
        "choreographic_analysis": "编舞分析采用 Laban Movement Analysis (LMA)、RST 或编舞家自定框架并明确编码规则",
        "fieldwork": "田野/编舞驻场研究遵循 IRB 伦理审查与知情同意",
        "motion_capture": "运动捕捉数据采集遵循 MoCap 精度、坐标系统与采样率报告规范",
        "performance_art": "作品研究应包含创作年份、剧目、创作者、演出场地与首演/巡演语境",
        "video_documentation": "舞段影像记录应报告镜头参数、视角与录制时间码",
    },
    conventions=(
        "作品首次出现给出正式名称、创作年份、编舞家、主要舞者与出品机构",
        "编舞时间/空间/动作描述采用 Laban/Bartenieff/RST 等标准术语并首次定义",
        "引用舞谱（Labanotation / Benesh / Eshkol-Wachman / DanceML）须指明版本或编号",
        "运动学数据报告采样率（Hz）、标记点数量与校准方法",
        "访谈/田野资料引用采用化名或匿名化并附伦理批件号",
    ),
    key_venues=(
        "Performance Research",
        "Dance Research Journal",
        "New Theatre Quarterly",
        "Contemporary Dance Research",
        "Journal of the Society for Psychodrama, Psychomovement and Gestalt Therapy",
        "Theatre Journal",
    ),
    units_and_formulas_notes=(
        "动作时间以秒/拍报告；采样率以 Hz；角度以度（°）或弧度",
        "运动学量纲一致（线性 mm/s，角速度 deg/s）；均值±SD 或中位数（IQR）",
        "编舞评分量表（如观众评价）报告 Likert 5/7 分尺度与评分者一致性（κ）",
        "统计方法（配对 t 检验、重复测量 ANOVA、效应量）须说明",
        "舞蹈影像以 fps 报告帧率；音轨以 BPM 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Labanotation 舞谱软件（LabanPro）", "Benesh Movement Notation", "Eshkol-Wachman Movement Notation", "DanceML 结构化编舞描述", "Motion Capture 光学捕捉系统 OptiTrack", "Vicon 运动捕捉系统", "Noitom Perception Neuron（惯性动捕）", "Xsens MVN（惯性运动捕捉）", "Adobe Premiere Pro", "DaVinci Resolve", "After Effects", "Final Cut Pro", "Pro Tools", "Logic Pro X", "MuseScore", "DanceML Studio", "Notation Studio (Kinetisys)", "Adobe Acrobat Pro（舞谱排版）", "Figma", "TableauNotate"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "Arts & Humanities Citation Index"),
)
