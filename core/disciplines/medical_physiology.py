"""医学生理学学科论文支持：器官系统与病理生理研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="medical_physiology",
    aliases=("medical_physiology", "医学生理学", "physiology", "病理生理", "器官生理", "生理机制", "稳态"),
    paper_types={
        "research": ("abstract", "introduction（生理背景与假说）", "methodology（实验设计）", "results（数据与统计）", "discussion（机制解释）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例/模型描述）", "analysis（生理机制分析）", "results（功能指标）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（系统生理概览）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="Vancouver",
    reporting_standards={"k1": "动物实验须报告品系、周龄、麻醉与安乐死方案", "k2": "离体组织功能测定须报告灌流液成分与温度", "k3": "统计须声明样本量依据与检验方法"},
    conventions=("首次出现标注全名与缩写", "图表标注生理变量单位（SI）", "动物伦理批准号须注明", "剂量与频率换算须写明", "正常参考范围须注明来源"),
    key_venues=("American Journal of Physiology", "Circulation Research", "Pflügers Archiv", "Physiological Reviews", "Journal of Physiology"),
    units_and_formulas_notes=("SI 单位：kPa（血压）、mV（膜电位）、J/kg（能量）", "血流量 Q=ΔP/R，须声明测量方式", "pH 与离子浓度须注明是否换算自 pCO2", "统计以 mean±SD 或 mean±SEM 报告"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Harmony Data Acquisition System", "PowerLab 8/35", "MyoSignal 2", "Tucker-Davis Systems", "ChartSoft", "OriginLab", "GraphPad Prism", "R (ggplot2)", "SPSS", "MATLAB", "LabVIEW", "Arduino-based custom rigs", "Hemodynamic Monitor", "Gas Chromatograph", "Electrolyte Analyzer", "Ultracentrifuge", "PCR System", "Flow Cytometer", "Microscope System", "ECCG System"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
