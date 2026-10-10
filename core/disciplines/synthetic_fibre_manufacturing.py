"""Synthetic Fibre Manufacturing 学科论文支持：合成纤维聚合、纺丝与拉伸工艺论文体裁、ACS 引用样式与聚酯/聚酰胺工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="synthetic_fibre_manufacturing",
    aliases=(
        "synthetic_fibre_manufacturing",
        "Synthetic fibre manufacturing",
        "化纤制造",
        "合成纤维",
        "聚合物加工",
        "spinning process",
        "polyester manufacturing",
        "polyamide fibre",
        "polymer spinning",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与纤维制造问题）",
            "methods（聚合、纺丝与拉伸工艺）",
            "results（力学、热学、形貌与性能数据）",
            "discussion（结构与性能关联）",
            "data availability",
            "references",
        ),
        "process_study": (
            "abstract",
            "introduction",
            "process design（工艺流程与参数）",
            "experiments（工艺试验与表征）",
            "results（工艺-性能映射）",
            "outlook",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "main developments（按纤维品种/工艺综述）",
            "challenges",
            "outlook",
            "references",
        ),
    },
    citation_style="ACS 样式（作者-年份；Polymer、J Appl Polym Sci 遵循 ACS 规范）",
    reporting_standards={
        "polymerization": "聚合反应须报告原料纯度、催化剂种类与用量、反应温度与压力、停留时间、转化率与分子量分布（Mw/Mn）",
        "spinning": "纺丝工艺须报告喷丝板孔径、纺丝速度、热箱温度曲线、卷绕速度与张力",
        "characterization": "纤维表征须报告测试标准（ISO/ASTM/GB）、样品尺寸、环境与仪器型号",
        "rheology": "熔体流变须报告剪切速率区间、温度、稳态与瞬态测量模式、平行板/毛细管几何",
        "systematic_review": "系统综述遵循 PRISMA 2020 声明",
    },
    conventions=(
        "纤维品种缩写遵循行业惯例：PET（聚酯）、PA6/PA66（聚酰胺）、PBT、PBT/PET、PTT（热塑性聚酯弹性体）、POM（聚甲醛）、PVDF、PPTA",
        "力学量：拉伸强度 MPa、断裂伸长率 %、弹性模量 GPa；测试条件（拉伸速度 mm/min、标距 mm、环境温湿度）须完整",
        "热学量：熔点 Tm、玻璃化转变 Tg、结晶温度 Tc 用 °C；DSC 加热/冷却速率须注明",
        "分子量：数均 Mn、重均 Mw、黏均 Mv；Mw/Mn 为分散度 PDI",
        "纤维几何：直径 μm、圆形度 %、单丝密度 ccm（纤度 dtex）须注明测量方法",
        "样品数量：n≥5 或报告样本数；结果给出均值 ± SD",
    ),
    key_venues=(
        "Polymer",
        "European Polymer Journal",
        "Journal of Applied Polymer Science",
        "Polymer Engineering & Science",
        "Textile Research Journal",
        "Journal of Applied Polymer Physics / J Appl Phys",
    ),
    units_and_formulas_notes=(
        "长度用 mm/cm/m；力用 N/kN；强度用 MPa；模量用 GPa；温度用 °C；分子量用 g/mol",
        "拉伸强度 σ = F/A（F 为最大载荷、A 为原始截面积）；断裂伸长率 ε = (L-L_0)/L_0 × 100%",
        "DSC 结晶度 X_c = (ΔH_m - ΔH_m,ref)/(ΔH_m,ref) × 100%；FTIR 结晶度按伯努利方程 X_c = (A_0 - A)/(A_0 - A_c)",
        "公式用 amsmath；负反馈用 \\times；显示公式仅在正文引用时编号；行内公式避免复杂分式",
        "数值结果给出均值 ± SD 与样本数 n；工艺参数与表征条件须完整列出；不确定度按 GUM 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Aspen Plus", "HYSYS", "COMSOL Multiphysics", "POLYSPIN", "DMTSP", "MTS Insight", "Instron 5940", "Netzsch DSC", "TA Instruments Q100", "Netzsch TGA", "Nicolet iS50 FTIR", "Bruker D8 XRD", "ZEISS Sigma SEM", "Keyence VHX-7000", "Anton Paar Rheometer MCR", "Haake Rheotest", "Melt Flow Indexer", "Karl Fischer", "CASSI", "MATLAB (Simulink)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "arXiv"),
)
