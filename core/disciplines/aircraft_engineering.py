"""航空器工程学科论文支持：气动/结构/推进/飞控体裁与 CFD/CAE 记法。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aircraft_engineering",
    aliases=(
        "aircraft engineering",
        "航空器工程",
        "aerospace engineering",
        "aircraft design",
        "aircraft systems engineering",
        "飞行器设计",
        "飞行体工程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（工程问题、任务需求与目标）",
            "methods（数值模拟/试验/仿真方法与验证）",
            "results（气动力、结构、推进或飞控性能）",
            "discussion（与试验对比与工程意义）",
            "conclusion",
            "references",
        ),
        "design_report": (
            "任务需求",
            "方案与选型",
            "详细设计与计算",
            "验证与评估",
            "结论",
            "参考文献",
        ),
    },
    citation_style="AIAA 或 Elsevier 样式（标准附件按 ICAO/SAE/ASTM 编号引用）",
    reporting_standards={
        "numerical_validation": "CFD/结构仿真须披露网格无关性验证、湍流模型与收敛判据",
        "experimental_setup": "风洞/地面试验须披露模型比例、设备、边界条件与测量不确定度",
        "uncertainty_quantification": "关键结果须给出敏感性分析或不确定度预算",
        "traceability": "标准与规范引用须准确（如 SAE ARP、ASTM、ICAO、EASA CS）",
    },
    conventions=(
        "气动量须按非量纲化记法（如 Re、Ma、Cl、Cd、Cm），并按 SAE ARP 或 ICAO 编号引用",
        "CFD/结构仿真须披露湍流模型、网格密度与网格无关性验证方法",
        "符号与缩写首次出现须给出全称与来源标准",
        "涉及疲劳与结构耐久须按 ASTM E466 或 ISO 12107 报告试验条件",
        "推进系统须按 ISO 9906 或 ISO 14644 报告性能参数（推力、耗油量、单位推力）",
    ),
    key_venues=(
        "Journal of Aircraft",
        "AIAA Journal",
        "Aerospace Science and Technology",
        "Composite Structures",
        "Chinese Journal of Aeronautics",
        "航空学报",
        "Journal of Propulsion and Power",
        "Journal of Fluid Mechanics",
    ),
    units_and_formulas_notes=(
        "长度用 m，速度用 m/s 或 kt，角度用度或弧度并显式说明",
        "压力用 kPa 或 Pa，密度用 kg/m³，力用 N",
        "雷诺数 Re、马赫数 Ma 须按 SAE/ISO 定义给出",
        "气动系数（Cl、Cd、Cm）按 SAE ARP 或 ISO 非量纲化定义",
        "疲劳寿命须按 ASTM E466 或 ISO 12107 报告（如 Nf、S-N）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("XFOIL", "SU2", "OpenFOAM", "MATLAB", "ANSYS", "NASTRAN", "GEM", "Lido", "TopFlite", "Jeppesen", "CATIA", "SolidWorks", "Abaqus", "OpenVSP", "AVL", "XFlaps", "XFlower", "ParaView", "FEniCS", "Code_Aster", "SU2py", "SimScale"),
    category="工学",
    databases=("AIAA", "arXiv", "OpenAlex", "Crossref"),
)
