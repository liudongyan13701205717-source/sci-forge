"""精密机械学科论文支持：精密加工、精密测量与超精密装备研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="precision_mechanics",
    aliases=(
        "precision mechanics", "精密机械", "精密加工",
        "precision engineering", "精密工程",
        "ultraprecision machining", "超精密加工",
        "precision measurement", "精密测量",
        "machine tool accuracy", "机床精度",
        "micro-machining", "微纳加工",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（加工需求与科学问题）",
            "methodology（加工工艺、测量方法与实验设计）",
            "results（几何精度、表面质量与尺寸精度）",
            "discussion（机理分析与工艺窗口）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（工件与装备背景）",
            "analysis（误差源辨识与补偿过程）",
            "results（加工前后精度对比）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（误差机理与运动学理论）",
            "evidence synthesis（工艺与装备研究证据）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "k1": "几何精度按 ISO 230 系列与 GB/T 17421 报告",
        "k2": "表面粗糙度按 ISO 4287 报告并注明取样长度",
        "k3": "标定须注明标准器溯源链与环境温度控制",
    },
    conventions=(
        "尺寸精度以 μm 或 nm 表示并注明测量仪器与不确定度",
        "表面粗糙度注明 Ra/Rz 与取样长度参数",
        "温度控制须说明恒温区间与温度波动范围",
        "切削参数完整报告（主轴转速、进给、切深、冷却方式）",
        "误差分析须区分重复性与准确度",
    ),
    key_venues=(
        "Precision Engineering",
        "International Journal of Machine Tools and Manufacture",
        "CIRP Annals - Manufacturing Technology",
        "Journal of Manufacturing Processes",
        "Precision Engineering (Elsevier)",
    ),
    units_and_formulas_notes=(
        "定位精度与重复定位精度须分开报告（μm @ 行程）",
        "Ra 按 ISO 4287 算术平均偏差（μm），取样长度 0.25 mm",
        "切削力以 N 为单位并注明分力方向",
        "刀具寿命以 m 或工件数表示并注明判据",
        "测量不确定度须给出合成标准不确定度与扩展不确定度（k=2）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Zeiss Contura 三坐标测量机", "Mitutoyo Surftest SJ-6000 表面粗糙度仪", "Laser Interferometer Renishaw RLV20", "Renishaw RE40 转台测头", "Keyence VR-5300 轮廓粗糙度仪", "Taylor Hobson Surtronic S700", "Mahr MarVista 光学扫描仪", "GOM ATOS 双光子激光扫描仪", "Nikon METROLOGY 光学显微镜", "Olympus VHX 数码显微镜", "Zeiss Confocal Microscope", "Duncan 圆度仪", "Siena 直线度测量仪", "Santec 激光干涉仪", "MATLAB Simulink", "ANSYS Mechanical", "Abaqus FEA", "COMSOL Multiphysics", "Python (pandas, scipy)", "MATLAB (Curve Fitting)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
