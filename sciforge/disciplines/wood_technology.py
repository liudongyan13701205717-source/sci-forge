"""木材工艺学科论文支持：木材科学与改性处理体裁、APA 引用样式与木材科学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wood_technology",
    aliases=("wood technology", "木材工艺", "木材科学", "木材科学与技术", "木材加工技术",
             "wood science", "wood technology", "timber technology"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与科学问题）",
            "materials and methods（材料、处理与测试）",
            "results（物理力学与化学数据）",
            "discussion（木材机理与应用）",
            "references",
        ),
        "material_study": (
            "abstract",
            "introduction",
            "materials and methods（试样、处理与表征）",
            "results（表征与性能数据）",
            "discussion（材料机理）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按主题综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 样式（作者-年份；Wood Science and Technology 多用 Springer 规范）",
    reporting_standards={
        "material_testing": "材料测试须报告标准（ASTM/ISO/GB）、试样与条件",
        "mechanical": "力学测试须报告加载方式、速率与试样尺寸",
        "chemical_analysis": "化学分析须报告方法、仪器与重复数",
        "statistical": "须报告重复数、统计方法与显著性",
    },
    conventions=(
        "木材树种须给出学名（属种）与产地",
        "含水率用 % 并说明测定条件（绝干基准）",
        "密度用 kg/m³ 或 g/cm³ 并注明含水率状态",
        "力学指标（MOE/MOR）须注明测试标准",
        "处理工艺（热处理/防腐/改性）须量化",
    ),
    key_venues=(
        "Wood Science and Technology",
        "Holzforschung",
        "European Journal of Wood and Wood Products",
        "BioResources",
        "Journal of Wood Science",
        "Forest Products Journal",
    ),
    units_and_formulas_notes=(
        "密度用 kg/m³；含水率用 %",
        "MOE 用 MPa 或 GPa；MOR 用 MPa",
        "尺寸用 mm；质量用 g/kg",
        "化学组分用 %（质量分数）；灰分用 %",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("万能材料试验机 (universal testing machine)", "含水率测定仪", "密度测定仪", "扫描电镜 (SEM)", "显微切片机 (microtome)", "X 射线衍射仪 (XRD)", "FTIR 光谱仪", "热重分析仪 (TGA)", "差示扫描量热仪 (DSC)", "动态力学分析仪 (DMA)", "气候箱 (climate chamber)", "木材干燥窑", "防腐处理设备", "涂饰设备", "ImageJ", "木材识别软件", "R", "Python (scikit-learn)", "SAS", "SPSS"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
