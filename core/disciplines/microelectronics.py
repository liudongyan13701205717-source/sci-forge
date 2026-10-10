"""微电子技术学科论文支持：器件、工艺与集成电路设计研究、案例与综述体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="microelectronics",
    aliases=("microelectronics", "微电子技术", "microelectronics_technology", "semiconductor", "ic_design", "vlsi", "nanoelectronics", "microsystems", "integrated_circuits", "semiconductor_processing", "photolithography"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与问题）", "methodology（器件/电路设计与实验方法）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（器件或工艺案例）", "analysis（性能与失效分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（微电子理论与技术综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="IEEE 样式（作者-年份；IEEE 电子器件/电路刊常用）",
    reporting_standards={"k1": "器件实验遵循 IEEE 器件测试规范", "k2": "电路设计遵循 IEEE 标准与可复现性要求", "k3": "工艺报告遵循半导体工艺数据规范（含不确定度）"},
    conventions=("器件参数（电压、电流、频率）须标注测试条件", "工艺步骤须注明设备与参数", "版图须注明尺度与层映射", "统计结果须给置信区间与样本量", "公式须编号并注明符号含义"),
    key_venues=("IEEE Transactions on Electron Devices", "IEEE Journal of Solid-State Circuits", "Nature Electronics", "IET Microelectronics", "Semiconductor Science and Technology"),
    units_and_formulas_notes=("电压用 V；电流用 mA；频率用 MHz/GHz", "掺杂浓度用 cm⁻³；尺寸用 nm/μm", "功率密度用 W/cm²", "公式用 amsmath；结果须给均值 ± 不确定度与样本量"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPICE", "Cadence Virtuoso", "Synopsys Design Compiler", "KLayout", "Photolithography scanner", "E-beam lithography", "CMP", "SEM", "TEM", "AFM", "Oscilloscope", "Signal generator", "Wafer fabrication line", "Dicing saw", "Wire bonder", "Characterization suite", "Python (NumPy, SciPy)", "MATLAB", "COMSOL Multiphysics", "TCAD (Sentaurus)"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
