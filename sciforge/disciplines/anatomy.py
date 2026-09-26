"""解剖学学科论文支持：人体解剖/形态学体裁、Wiley 引用样式与解剖学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="anatomy",
    aliases=("anatomy", "解剖学", "人体解剖学", "human anatomy", "形态学",
             "morphology", "组织学", "histology", "神经解剖学", "neuroanatomy"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与解剖结构）",
            "materials and methods（标本、成像与测量）",
            "results（形态学数据）",
            "discussion（临床与进化意义）",
            "references",
        ),
        "imaging": (
            "abstract",
            "introduction",
            "methods（成像协议与分割）",
            "results（结构测量与变异）",
            "discussion（临床应用）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按系统/区域综述）",
            "outlook",
            "references",
        ),
    },
    citation_style="Wiley 样式（作者-年份；Clin. Anat. 遵循 Wiley 规范）",
    reporting_standards={
        "specimen_info": "标本来源、数量与保存方式须报告",
        "measurement_methods": "测量工具（卡尺、影像）与精度须报告",
        "terminology": "解剖术语遵循 Terminologia Anatomica",
        "ethics": "遗体捐献/伦理审批须说明",
        "statistics": "统计检验与变异范围须给出",
    },
    conventions=(
        "解剖术语用拉丁/英文标准术语（Terminologia Anatomica）",
        "方位术语（anterior、posterior、medial、lateral）统一",
        "测量值给出均值 ± SD 与范围",
        "影像解剖标注层面与序列（CT、MRI）",
        "变异与异常（accessory、variant）明确标注",
    ),
    key_venues=(
        "Clinical Anatomy",
        "Journal of Anatomy",
        "Anatomical Record",
        "Annals of Anatomy",
        "Surgical and Radiologic Anatomy",
        "Journal of Morphology",
    ),
    units_and_formulas_notes=(
        "长度用 mm/cm；角度用 °",
        "体积用 cm^3/mL",
        "公式用 amsmath；形态测量指数公式须明确",
        "显示公式仅在被引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与范围",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=(
        "三维显微解剖工作站",
        "光学显微镜",
        "断层解剖标本数字化平台",
        "游标卡尺",
        "3D Slicer",
    ),
    category="理学",
    databases=(
        "PubMed",
        "OpenAlex",
        "Crossref",
    ),
)