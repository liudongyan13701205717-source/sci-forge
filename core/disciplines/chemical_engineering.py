"""化学工程论文支持：过程工程、反应工程、传递现象。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="chemical_engineering",
    aliases=("chemical engineering", "process", "reactors", "separation",
             "catalysis", "fluid", "化工", "反应工程", "分离工程", "系统工程"),
    paper_types={
        "research": ("abstract", "introduction", "experimental", "results", "discussion", "conclusions", "references"),
        "process": ("abstract", "introduction", "process flowsheet", "equipment sizing", "economics", "optimization", "references"),
        "review": ("abstract", "introduction", "taxonomy", "state-of-art", "challenges", "references"),
    },
    citation_style="ACS（American Chemical Society）",
    reporting_standards={
        "materials": "化学品纯度、来源与表征须报告；催化剂组成与比表面积",
        "kinetics": "速率方程与参数须给出置信区间；机理验证",
        "scale": "放大与传热/传质准则数 Re/Sc/Sh 须列表",
        "eco": "原料单耗、能耗、Exergy 损失与三废量须统计",
        "safety": "HAZOP/LOPA 分析摘要须含",
    },
    conventions=(
        "无量纲数须定义（Re/Pr/Nu/Sc/Sh）；传递系数给关联式来源",
        "流程图（PFD）标注物流号；给物流衡算表（T、P、组成）",
        "反应器标体积与空速；分布器/填料型号说明",
        "数据表格注明标准状态（25°C, 1 atm 或电池实际条件）",
        "误差棒与平行实验次数须给",
    ),
    key_venues=(
        "AIChE Journal",
        "Chemical Engineering Science",
        "Industrial & Engineering Chemistry Research",
        "Chemical Engineering Journal",
        "Computers & Chemical Engineering",
    ),
    units_and_formulas_notes=(
        "热力学函数 kJ/mol；活度系数 γ；逸度 f",
        "反应速率 mol/(L·s)；空速 GHSV/LHSV h⁻¹",
        "传热系数 W/m²·K；传质系数 m/s",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("Aspen Plus", "MATLAB", "ChemDraw", "COMSOL"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)