"""风力涡轮机学科论文支持：风电机组设计、运行性能与疲劳寿命评估。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="wind_turbines",
    aliases=(
        "wind turbines",
        "风力涡轮机",
        "风力发电",
        "风电机组",
        "wind energy",
        "wind power",
        "wind energy systems",
        "风力发电工程",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究背景与问题）",
            "theoretical framework（理论模型与假设）",
            "methodology（建模/仿真/测试方法）",
            "results（性能结果与对比分析）",
            "discussion（机理讨论与局限性）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "project description（风电场/机组描述）",
            "operational data analysis（运行数据分析）",
            "performance evaluation（性能评估）",
            "recommendations（优化建议）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "turbine design evolution（设计演变综述）",
            "control strategies（控制策略综述）",
            "materials and reliability（材料与可靠性综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE 样式",
    reporting_standards={
        "site characterization": "风电场评估须报告风速/风向统计（含 99% 分位数）与湍流强度",
        "turbine specifications": "机组参数须完整报告（额定功率、额定风速、叶片长度、轮毂高度）",
        "measurement protocol": "风速/功率测量须符合 IEC 61400-12 标准，标注时窗与采样率",
        "availability reporting": "可用率须区分计划检修与非计划停机（IEC 61400-26）",
    },
    conventions=(
        "风速测量高度标注 hub height（轮毂高度），单位 m",
        "功率曲线按 IEC 61400-12 标准分 30min 风速区间绘制",
        "湍流强度用 IT = σu/U（标准差/均值），单位 %",
        "叶片载荷单位 kN（集中力）或 kN/m（分布载荷）",
        "疲劳寿命单位百万循环（×10⁶ cycles）",
    ),
    key_venues=(
        "Wind Energy",
        "Journal of Wind Engineering and Industrial Aerodynamics",
        "Wind Energy Science",
        "Applied Energy",
        "Energy Conversion and Management",
    ),
    units_and_formulas_notes=(
        "风速单位 m/s；功率单位 kW 或 MW",
        "风能公式：P = ½·ρ·A·v³（ρ 空气密度 kg/m³，A 扫掠面积 m²）",
        "功率系数 Cp = P_actual / P_available（理论最大 0.593，Betz 极限）",
        "容量因子（Capacity Factor）= 实际发电量 /（额定功率×8760h）×100%",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("风资源评估软件（如 WindPRO）", "风功率预测系统（如 WindPower Prediction Tool）", "CFD 仿真软件（ANSYS Fluent）", "叶片结构分析软件（ANSYS Mechanical）", "有限元分析软件（ABAQUS）", "多体动力学软件（Multibody Dynamics，如 Adams）", "风洞实验设备（如 NREL 风洞）", "风速/风向测量仪（如 Vaisala WINDTURBINE）", "叶片载荷监测传感器（应变片/加速度计）", "SCADA 数据采集系统（风机控制平台）", "无人机叶片巡检系统（如 DJI Matrice 300 RTK）", "叶片复材成型设备（真空导流成型系统）", "疲劳试验机（如 MTS 电液伺服系统）", "有限元后处理软件（ABAQUS CAE）", "Python 仿真脚本（PyMOTR、FastFream）", "MATLAB/Simulink 控制仿真", "LaTeX 学术排版", "EndNote 文献管理", "Tecplot 流动可视化", "Paraview 多物理场可视化"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
