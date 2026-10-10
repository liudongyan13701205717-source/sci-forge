"""绘画学科论文支持：作品考证、材料与技法研究的艺术史体裁、艺术品科学检测数据报告规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="painting",
    aliases=(
        "painting",
        "绘画",
        "Painting (art)",
        "Painting Art",
        "绘画艺术",
        "Art History",
        "颜料与绘画材料研究",
        "油画与壁画",
        "painting materials analysis"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（材料与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（作品案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references"
        ),
    },
    citation_style="Chicago 艺术史样式（第17版，作者-日期式）",
    reporting_standards={
        "k1": "材料分析报告遵循艺术品科学检测数据报告规范",
        "k2": "艺术史考证须给出图像比对与文献依据",
        "k3": "系统综述遵循 PRISMA 声明"
    },
    conventions=(
        "作品著录须给出艺术家、题名、年代、材料、尺寸、收藏地与馆藏号",
        "图像呈现须标注拍摄条件与色差校正方式",
        "材料分析须注明检测手段、样品尺寸与无损或取样状态",
        "修复干预须遵循最小干预与可识别原则并留存前后影像",
        "年代与作者归属须并列陈述证据强度，避免绝对化断言"
    ),
    key_venues=(
        "Art Bulletin",
        "The Art Journal",
        "Journal of the Warburg and Courtauld Institutes",
        "Visible Language",
        "National Gallery Technical Bulletin"
    ),
    units_and_formulas_notes=(
        "作品尺寸以 cm 报告（宽×高）并注明是否含框",
        "颜料层与画布厚度以 μm 或 mm 报告并注明取样位置",
        "光谱数据以 nm 报告，峰位须与标准库比对",
        "颜料配比以重量百分比报告并注明溶剂"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "专利", "教案与教材", "报告", "数据集"),
    tools=("便携式 XRF 分析仪", "便携式拉曼光谱仪", "傅里叶变换红外显微仪（FTIR-µR）", "多光谱成像系统", "高光谱成像系统", "偏光显微镜", "扫描电镜-能谱仪（SEM-EDS）", "气相色谱-质谱联用仪（GC-MS）", "反射变换成像（RTI）", "反射成像系统", "红外热像仪", "紫外-可见分光光度计", "三维结构光扫描仪", "Adobe Photoshop", "Adobe Lightroom", "CorelDRAW", "Procreate", "Zotero", "OpenRefine", "Microsoft Excel"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
