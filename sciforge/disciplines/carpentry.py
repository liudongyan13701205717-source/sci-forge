"""木工（家具）学科论文支持：家具结构设计/木材力学/木工工艺流程体裁与引用样式。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="carpentry",
    aliases=(
        "carpentry",
        "furniture",
        "furniture making",
        "woodworking",
        "furniture design",
        "cabinet making",
        "木工",
        "家具制作",
        "家具木工",
        "木作",
        "家具设计",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（设计背景与木材选材动机）",
            "design and method（构造方案、接合方式与工艺流程）",
            "results（力学测试与工艺参数结果）",
            "discussion（结构优化、木材行为与可制造性）",
            "conclusions",
            "references",
        ),
        "design": (
            "abstract",
            "design brief（设计约束与使用场景）",
            "development（草图、建模与原型迭代）",
            "prototype testing（试制与试验）",
            "conclusions",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "taxonomy（按材质/接合/工艺分类）",
            "state of the art",
            "challenges and outlook",
            "references",
        ),
    },
    citation_style="APA 7（设计与工艺类）；材料测试引用 GB / ASTM 标准编号",
    reporting_standards={
        "species": "树种须给出中文常用名与拉丁学名，注明来源产地",
        "moisture": "含水率须报告测量方法与标准（GB/T 1925 或 ISO 3130）",
        "mechanics": "力学性能（MOE/MOR/ICS）须注明试验标准与试样含水率",
        "joinery": "接合构造须图示尺寸与公差；榫卯名称中英并列",
        "process": "工艺参数（砂磨目数、胶黏剂品牌与固含量、干燥制度）须完整可复现",
    },
    conventions=(
        "树种名称须同时给出中文常用名与拉丁学名（如橡胶木 Hevea brasiliensis）",
        "木材力学性能符号全文统一（MOE 抗弯弹性模量、MOR 抗弯强度、ICS 顺纹抗剪强度）",
        "接合方式须图示构造细节；榫卯名称中英并列（mortise and tenon 榫眼榫头）",
        "含水率、硬度、强度等数值须注明试验标准与试样条件",
        "所有工艺参数（砂磨目数、胶黏剂品牌与固含量、干燥制度）须完整可复现",
    ),
    key_venues=(
        "Wood Science and Technology",
        "Journal of Wood Science",
        "Forest Products Journal",
        "Maderas Ciencia y Tecnologia",
        "Holz research",
        "The International Journal of Furniture Manufacturing and Design",
    ),
    units_and_formulas_notes=(
        "强度与模量用 MPa；含水率用 %（绝干重或绝湿重基准须注明）",
        "硬度用 Janka（N）或巴西尔硬度（N），须注明测试方向（径切/弦切）",
        "时间用 min/h；厚度用 mm；长度用 mm",
        "公式用 amsmath；力与力矩公式须标量纲",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Fusion 360", "SolidWorks", "AutoCAD", "Rhino 3D", "SketchUp", "Vectric VCarve", "SolidCAM", "Shapeoko CNC 雕刻机", "Formlabs 3D 打印机", "Shining 3D 3D 扫描仪", "Protimeter 木材水分仪", "Instron 万能材料试验机", "巴西尔硬度计", "ZEISS 扫描电子显微镜", "ImageJ", "ANSYS 有限元分析", "OpenCV", "Grain 木材含水率仪", "Janka 硬度计", "Wood 木材力学测试平台"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
