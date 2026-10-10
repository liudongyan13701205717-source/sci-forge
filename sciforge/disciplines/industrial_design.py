"""工业设计论文支持：产品设计、人机交互、CMF、可持续设计与创新方法。"""
from __future__ import annotations
from sciforge.disciplines.base import Discipline
DISCIPLINE = Discipline(
    name="industrial_design",
    aliases=("industrial_design", "工业设计", "product_design", "HCI", "design_research", "user_experience_design", "CMF_design", "sustainable_design", "design_thinking"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法论）", "results（结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（分析）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 或 IEEE（人机交互）",
    reporting_standards={"usability": "可用性测试须遵循 ISO 9241-11 报告任务、样本、成功率、时间与 SUS 分数", "cmf": "CMF 研究须报告材料、色彩（Pantone/孟塞尔）、表面处理工艺", "sustainability": "可持续评估须遵循 LCA/ISO 14040-14044 生命周期方法"},
    conventions=("图像须标注拍摄视角与比例", "参数化设计须说明变量与约束", "CMF 须给出材料代码与工艺", "用户研究须报告样本量与取样框架", "原型阶段须按低保真/高保真标注"),
    key_venues=("Design Studies", "International Journal of Industrial Ergonomics", "Journal of Product Innovation Management", "Industrial Design", "Design Issues"),
    units_and_formulas_notes=("尺寸以 mm、公差以 mm 或 ± 表示", "人机数据以第 5/50/95 百分位表达", "LCA 报告 kg CO2e、kg 当量", "色彩以 Pantone/RGB/CMYK 表达"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Rhino", "Rhino Grasshopper", "SolidWorks", "Fusion 360", "Catia", "NX", "Creo", "KeyShot", "Maya", "3ds Max", "Blender", "Adobe Illustrator", "Adobe Photoshop", "Figma", "SolidWorks Simulation", "ANSYS", "MATLAB", "R", "NVivo", "UsabilityHub"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
