"""Aboriginal And Torres Strait Islander Culture, Language And History 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aboriginal_and_torres_strait_islander_culture_language_and_history",
    aliases=(
        "Aboriginal And Torres Strait Islander Culture, Language And History",
        "原住民文化与语言历史",
        "ATSI Culture, Language and History",
        "First Nations Culture",
        "Indigenous Australian Studies",
        "Yarn and Story",
        " Aboriginal Linguistics",
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
        "ocap": "原住民数据须遵循 OCAP 原则（所有权、控制权、获取权、占有权）",
        "care": "原住民数据治理须遵循 CARE 原则（集体性、代理权、互惠、伦理）",
        "cultural_safety": "田野研究须记录文化安全协议与知情同意过程",
    },
    conventions=(
        "引用原住民知识须遵循OCAP原则（所有权、控制权、获取权、获取权）",
        "田野调查须记录知情同意过程，并尊重社区文化安全协议",
        "涉及神圣知识或受控文化信息须标注可公开性等级",
        "叙述中尊重不同原住民语言和方言的地域分布",
    ),
    key_venues=(
        "Australian Aboriginal Studies",
        "Aboriginal History",
        "Journal of Australian Studies",
        "Pacific Affairs",
        "Journal of Indigenous Studies",
        "AIATSIS Research Publications",
    ),
    units_and_formulas_notes=(
        "语言记录须注明 ISO 639-3 语言代码与方言归属，田野录音须记录采样率（kHz）与位深度",
        "口述史访谈时长以分钟（min）计量，引语须标注说话者语言与翻译者",
        "文化信息的可公开性须分三级标注：完全公开、受限公开（社区授权后公开）、不可公开",
        "地图与地名记录须注明原住民语言拼写与英文通用名对照，坐标精度须标注（如 100m 网格）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "艺术作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("AIATSIS", "EndNote", "NVivo", "ELAN", "Anviz", "FieldRecorder", "Audacity", "Transana", "QGIS", "Google Earth Pro", "Mapbox", "Microsoft OneNote", "Adobe Lightroom", "Canva", "Zoom", "iRecording Studio", "Chatterbox Pro", "FLEx（Field Linguistics Explorer）", "Praat", "FLUTE"),
    category="法学",
    databases=("OpenAlex",),
)
