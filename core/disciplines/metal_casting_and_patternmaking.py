"""金属铸造与模型制作学科论文支持：铸造工艺与模具设计。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="metal_casting_and_patternmaking",
    aliases=("metal_casting_and_patternmaking", "金属铸造与模型制作", "casting", "foundry", "模具", "model making", "熔模", "sand casting"),
    paper_types={
        "research": ("abstract", "introduction（工艺背景）", "methodology（试验设计）", "results（性能数据）", "discussion（工艺优化）", "references"),
        "case_study": ("abstract", "introduction", "case description（铸造案例）", "analysis（缺陷分析）", "results（合格品率）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（铸造理论）", "evidence synthesis（工艺对比）", "future directions", "references"),
    },
    citation_style="ASME",
    reporting_standards={"k1": "浇注试验须报告温度曲线与气氛", "k2": "力学性能须注明试样方向与测试标准", "k3": "缺陷率统计须注明检验方法与抽样量"},
    conventions=("合金牌号按标准标注（GB/ASTM/AISI）", "工艺参数注明单位（℃、mm、MPa）", "缺陷类型按 AFWP 分类报告", "统计结果报告均值±标准差", "试样编号须可追溯"),
    key_venues=("Journal of Materials Processing Technology", "Foundry Technology", "International Journal of Metalcasting", "Casting Technology", "ASME Journal of Mechanical Design"),
    units_and_formulas_notes=("浇注温度 ℃，硬度 HB/HRc，强度 MPa", "收缩率 = (干型尺寸 - 铸件尺寸)/干型尺寸 × 100%", "充型时间估算须注明模型几何", "缺陷率 = 缺陷数/总铸件数 × 100%"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Foundry Furnace", "Mold Making Machine", "Spectrometer", "Tensile Tester", "Hardness Tester", "Metallography", "Ultrasonic Flaw Detector", "CMM (Coordinate Measuring Machine)", "X-Ray Radiography", "Thermocouple", "FEM Software", "Ansys", "SolidWorks", "Fusion 360", "Moldflow", "Excel", "MATLAB", "OriginLab", "GraphPad Prism", "EndNote"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
