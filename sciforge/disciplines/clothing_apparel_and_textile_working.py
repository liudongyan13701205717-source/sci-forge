"""服装、纺织与纺织加工学科论文支持：纺织服装工程体裁、ASTM 引用样式与纺织检测记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="clothing_apparel_and_textile_working",
    aliases=("clothing_apparel_and_textile_working", "服装与纺织加工",
             "纺织工程", "服装工程", "纺织服装", "纺织加工",
             "textile engineering", "apparel technology", "textile processing",
             "clothing manufacturing"),
    paper_types={
        "research": (
            "abstract（结构化摘要）",
            "introduction（背景与产业/学术问题）",
            "materials and methods（原料、设备、工艺参数与试验方法）",
            "results",
            "discussion",
            "conclusion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "state of the art",
            "future directions",
            "references",
        ),
    },
    citation_style="ASTM 样式（数字编号，ASTM J. Research / Textile Research Journal 规范）",
    reporting_standards={
        "test_method": "测试方法须标注 ISO/ASTM 标准编号与版本年份",
        "experimental": "实验研究遵循 ASTM E29/E6 与 GB/T 相关标准",
        "product_testing": "产品检测遵循 ISO 105（色牢度）、ISO 3759（断裂强度）、ISO 5077（透气性）等",
        "reproducibility": "试验重复数、样本制备与预处理条件须完全披露",
    },
    conventions=(
        "纤维/纱线/织物样品描述须含成分、规格、克重与预处理条件",
        "工艺参数（车速、张力、温度、湿度）须用 SI 单位与具体数值给出",
        "试验须报告重复次数与均值 ± 标准差；显著性检验采用 t 检验或 ANOVA",
        "标准编号须给出标准号、版本年份与语言版本",
        "结论须明确可推广的边界（原料、工艺、环境条件）",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of Industrial Textiles",
        "Journal of the Textile Institute",
        "Journal of Engineered Fibers and Fabrics",
        "Indian Journal of Fibre & Textile Research",
        "ASTM International Journal",
        "Clothing and Textiles Research Journal",
    ),
    units_and_formulas_notes=(
        "断裂强度用 N 或 cN/tex；伸长率与回弹率用 %",
        "透气性用 mm/s 或 l/m²·s；透湿用 g/m²·24h",
        "色牢度评级采用 1-5 级制；磨毛与起毛程度按 ISO 12945-2",
        "统计推断给出均值 ± SD 与 P 值",
        "公式用 amsmath；工艺变量符号须首次定义",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("TexLab (TextileLab)", "Uster Tester 6", "HVI Tester", "Mettler Toledo Tensile Tester", "Instron 5965", "ATP-System", "Helmus", "Brommer BAE-4", "SMTI Permeat", "ATP-24 Air Permeability Tester", "ATP Colorimeter", "Kestrel", "CAD (Gerber AccuMark)", "CAD (Lectra)", "Patterning (Optitex)", "CLO 3D", "BrowZwear", "MATLAB", "Python (numpy/scipy)", "SolidWorks"),
    category="工学",
    databases=("ScienceDirect", "PubMed", "OpenAlex", "Crossref"),
)
