"""纺织材料学科论文支持：纤维、织物与皮革材料性能表征研究体裁、ACS 引用样式与材料参数注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="textiles",
    aliases=(
        "textiles",
        "Textiles (clothes, footwear and leather)",
        "纺织材料",
        "纺织品与皮革",
        "织物材料",
        "纤维材料",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（材料背景与研究问题）",
            "materials and methods（材料制备与表征方法）",
            "results（性能与表征数据）",
            "discussion（结构-性能关系分析）",
            "conclusions",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（材料与应用案例）",
            "analysis（性能测试与失效分析）",
            "results",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（材料体系综述）",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="ACS 样式（编号引用）",
    reporting_standards={
        "material_specification": "材料须完整标注（纤维种类、规格、来源批次与处理工艺）",
        "characterization": "表征须注明仪器型号、测试条件与操作者校准状态",
        "standard_testing": "性能测试须遵循标准（ASTM、ISO、GB）并报告试样数与重复次数",
        "uncertainty": "测试结果须报告标准差或不确定度",
    },
    conventions=(
        "纤维化学组成与来源须标注（天然/合成/再生）",
        "织物组织须标明经纬密度与组织结构（平纹/斜纹/缎纹）",
        "测试条件（温度、湿度、静置时间）须注明",
        "图片须标注比例尺",
        "结论须区分材料内在性能与加工过程影响",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of Applied Polymer Science",
        "Composites Part A",
        "Journal of Industrial Textiles",
        "中国纺织",
    ),
    units_and_formulas_notes=(
        "纤维细度用旦尼尔（den）或微米（μm）",
        "织物克重用 g/m²，密度用根/cm",
        "强力用牛顿（N），断裂伸长率用百分比（%）",
        "耐磨性能用磨转数（cycle），色牢度用蓝标级（grade 1-5）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("MATLAB", "Python (NumPy, SciPy)", "R", "Minitab", "Origin", "ImageJ", "Adobe Photoshop", "MTEX", "Texcel CAD", "SolidWorks", "Instron 万能试验机", "Martindale 耐磨试验机", "Shirley 摩擦仪", "SEM（扫描电子显微镜）", "FTIR（红外光谱仪）", "XRD（X 射线衍射仪）", "DSC（差示扫描量热仪）", "色差仪（Colorimeter）", "水分/回潮率测定仪", "Zotero"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
