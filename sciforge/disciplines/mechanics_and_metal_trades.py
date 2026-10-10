"""力学与金属工艺学科论文支持：金属材料力学性能、工艺规程体裁与试验注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mechanics_and_metal_trades",
    aliases=("mechanics_and_metal_trades", "力学与金属工艺", "金属材料", "金属工艺", "mechanics of materials", "metal mechanics", "材料力学", "金属加工", "mechanical properties of metals"),
    paper_types={
        "research": ("abstract", "introduction（材料背景与研究动机）", "methodology（试验与制备方法）", "results（力学性能与微观结构数据）", "discussion（机理分析与工程应用）", "references"),
        "case_study": ("abstract", "introduction", "case description（材料/构件描述）", "analysis（失效分析与力学评估）", "results（性能测试数据）", "discussion（改进建议）", "references"),
        "review": ("abstract", "introduction", "material science overview（材料综述）", "evidence synthesis（研究证据整合）", "future directions", "references"),
    },
    citation_style="ASME 样式（材料力学遵循 ASME 规范）",
    reporting_standards={
        "tensile_test": "拉伸试验遵循 ASTM E8/E8M 或 ISO 6892",
        "hardness_test": "硬度测试遵循 ASTM B753（维氏）/E92（洛氏）",
        "fatigue_test": "疲劳试验遵循 ASTM E466",
        "impact_test": "冲击试验遵循 ASTM E23",
        "metallography": "金相分析遵循 ASTM E3 或 ISO 6507",
    },
    conventions=(
        "材料牌号、状态（退火/正火/淬火）须注明",
        "试验温度、速率与夹具条件须完整报告",
        "微观组织描述须包含晶粒尺寸与相组成",
        "力学性能给出标准值 ± 不确定度",
        "公式推导须标注边界条件与假设",
    ),
    key_venues=(
        "Acta Materialia",
        "Scripta Materialia",
        "International Journal of Plasticity",
        "Journal of Materials Engineering and Performance",
        "Metallurgical and Materials Transactions A",
        "Materials Science and Engineering A",
    ),
    units_and_formulas_notes=(
        "应力用 MPa/GPa；应变用无量纲；硬度用 HV/HRC",
        "公式用 amsmath；本构关系须编号",
        "疲劳寿命用循环次数 N；冲击能量用 J",
        "试样尺寸与几何形状须给出图或表格",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Universal Testing Machine", "Hardness Tester", "Tensile Testing Machine", "Compression Testing Machine", "Impact Testing Machine", "Fatigue Testing Machine", "Tribology Testing Machine", "Thermal Analysis Equipment", "Microscope", "SEM (Scanning Electron Microscope)", "XRD (X-Ray Diffraction)", "MET (Metallographic Etcher)", "Specimen Preparation Machine", "Hardness Indenter", "Fractography Equipment", "Residual Stress Analyzer", "Thermal Dilatometer", "Differential Scanning Calorimeter", "Nanoindentation Tester", "Cyclic Loading Machine"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
