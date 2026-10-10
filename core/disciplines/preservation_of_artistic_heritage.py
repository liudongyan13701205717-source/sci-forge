"""艺术遗产保护学科论文支持：文物材料分析、修复工艺与保存环境监测研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="preservation_of_artistic_heritage",
    aliases=(
        "preservation of artistic heritage", "艺术遗产保护", "文物修复",
        "conservation and restoration", "保护与修复",
        "cultural heritage conservation", "文化遗产保护",
        "painting conservation", "绘画修复",
        "archaeological science", "考古科学",
        "material analysis", "材料分析",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（病害问题与保护需求）",
            "methodology（检测方法与修复试验设计）",
            "results（材料表征与修复效果）",
            "discussion（机理分析与工艺适用性）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（文物现状与病害调查）",
            "analysis（修复方案与工艺选择）",
            "results（修复前后对比与稳定性）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（保护理论与干预原则）",
            "evidence synthesis（工艺与材料研究证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver",
    reporting_standards={
        "k1": "材料表征须报告仪器型号、加速电压与采样参数",
        "k2": "修复干预须遵循最小干预与可逆性原则并说明理由",
        "k3": "环境监测须报告温湿度记录周期与布点位置",
    },
    conventions=(
        "文物描述须区分原件、后世添加与修复部位",
        "检测前须完成无损检测再择机取样并记录取样位置",
        "颜料与材质结论须多方法交叉验证",
        "修复记录须保留操作前中后影像与工艺参数",
        "环境数据以年均值与极值同时报告并标注仪器校准",
    ),
    key_venues=(
        "Studies in Conservation",
        "Heritage Science",
        "Journal of Cultural Heritage",
        "Restaurator",
        "ICCROM Quaterly",
    ),
    units_and_formulas_notes=(
        "温湿度以 %RH 与 ℃ 表示，推荐 50%RH 与 20 ℃ 为基准",
        "色度以 CIE L*a*b* 或 Delta E*ab 表示并注明观察条件",
        "光谱数据注明激发波长、积分时间与光谱范围",
        "机械性能以 MPa 表示并注明测试试样尺寸与标准",
        "老化试验须注明光源类型、辐照度与总辐照量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "专利", "教案与教材", "报告", "数据集"),
    tools=("Zeiss Sigma 场发射扫描电子显微镜", "Nicolet 傅里叶变换红外光谱仪", "Bruker 拉曼光谱仪", "Thermo Fisher 扫描电子能量色散谱仪", "PerkinElmer 热重分析仪", "Bruker 同步辐射 XRD 衍射仪", "Karl Fischer 卡尔费休水分仪", "Datacolor 分光测色仪", "Olympus VHX 数码显微镜", "Nikon 偏光光学显微镜", "Fluke 温湿度记录仪", "GSI 高光谱成像系统", "GOM ATOS 三维扫描仪", "Artec 三维扫描系统", "Adobe Photoshop 图像修复", "Autodesk Maya 文物建模", "MATLAB 数据处理", "Python OpenCV", "Python SciPy", "Microsoft Excel"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
