"""航空工程学科论文支持：空气动力学、结构与飞行控制建模、CFD 仿真注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aeronautical_engineering",
    aliases=(
        "aeronautical_engineering",
        "航空工程",
        "航空学",
        "飞行力学",
        "航空宇航工程",
        "Aeronautics",
        "Aerospace Engineering",
        "Flight Mechanics",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题陈述与研究动机）",
            "governing equations and assumptions（控制方程与基本假设）",
            "methodology（建模方法、网格策略、边界条件、求解器设置）",
            "results and discussion（结果展示、网格无关性验证、与风洞/飞测数据对比）",
            "conclusion（主要结论、局限性与未来工作）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "historical overview",
            "methodological landscape（分类综述主流建模方法）",
            "open challenges",
            "conclusion",
            "references",
        ),
    },
    citation_style="AIAA 样式（编号制，如 [1]；或使用 Chicago 作者-日期样式）",
    reporting_standards={
        "governing_equations": "须完整列出控制方程（N-S/Euler）并注明求解形式（原始/线性化/离散）",
        "mesh_independence": "CFD 研究须报告网格无关性验证，至少提供三组网格的对比",
        "boundary_conditions": "边界条件须明确说明类型、数值与物理依据",
        "turbulence_model": "湍流模型选择须说明理由，必要时报告模型对比",
        "experimental_comparison": "数值结果须与风洞实验或飞测数据进行定量对比",
    },
    conventions=(
        "采用国际单位制（SI），无量纲参数（Re/Ma/C_D/C_L）须显式定义",
        "公式中的流体动力学术语须首次出现时给出标准英文缩写与中文译名",
        "CFD 网格图须注明单元类型、边距函数与关键区域的网格密度",
        "实验数据报告须注明风洞段长度、来流方向与天平校准误差",
        "图表坐标轴须标注量纲与误差棒，对比曲线须用不同线型区分",
    ),
    key_venues=(
        "AIAA Journal",
        "Journal of Aircraft",
        "Aerospace Science and Technology",
        "Journal of Fluid Mechanics",
        "Computer Methods in Applied Mechanics and Engineering",
        "Acta Astronautica",
    ),
    units_and_formulas_notes=(
        "长度单位：米（m）；压力单位：帕（Pa）；密度单位：千克每立方米（kg/m³）",
        "雷诺数 Re = ρVL/μ，马赫数 Ma = V/a，须显式给出特征长度 L 与音速 a",
        "阻力系数 C_D = F_D/(0.5ρV²S)，升力系数 C_L = F_L/(0.5ρV²S)，参考面积 S 须注明",
        "时间单位：秒（s）；频率单位：赫兹（Hz）；角速度单位：弧度每秒（rad/s）",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("ANSYS Fluent", "CATIA V5", "MATLAB", "Simulink", "XFOIL", "OpenFOAM", "SU2", "ParaView", "Tecplot", "ICEM CFD", "ANSYS Mechanical", "NASTRAN", "Abaqus", "CFD-Post", "XFLR5", "Star-CCM+", "SolidWorks", "风洞", "动平衡机", "空气动力天平"),
    category="工学",
    databases=("OpenAlex",),
)
