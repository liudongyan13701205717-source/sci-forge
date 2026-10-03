"""土木工程论文支持：结构设计、施工管理、基础设施安全。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="civil_engineering",
    aliases=("civil", "structural", "bridge", "geotechnical", "construction",
             "concrete", "steel", "土木", "结构工程", "桥梁", "隧道"),
    paper_types={
        "research": ("abstract", "introduction", "literature", "methodology", "results", "discussion", "conclusions", "references"),
        "case_study": ("abstract", "introduction", "project background", "analysis", "findings", "lessons", "references"),
        "design": ("abstract", "design criteria", "analysis", "calculations", "detailing", "review", "references"),
    },
    citation_style="ASCE（American Society of Civil Engineers）",
    reporting_standards={
        "design_code": "采用规范（ACI/AISC/GB）与版本须写明",
        "load": "荷载组合（恒/活/风/地震）与安全系数须列出",
        "material": "强度报告用标准试件，龄期明确",
        "test": "试验装置、加载制度、位移/应变测点布置须描述",
        "safety": "可靠性指标 β 与目标失效概率须给出",
    },
    conventions=(
        "单位 SI 为主（kN、MPa）；美国单位用 ft/kip/ksi",
        "截面图、配筋图按制图标准；钢筋直径用 φ 前缀",
        "有限元网格收敛分析报告；边界条件与接触假定提及",
        "误差和破坏模式用照片+简图；破坏准则给出（CCFT/Mohr-Coulomb）",
        "地震工给出地震动参数（PGA、Sa）、设防烈度",
    ),
    key_venues=(
        "Journal of Structural Engineering",
        "Engineering Structures",
        "Journal of Construction Engineering and Management",
        "ACI Structural Journal",
        "ASCE Journal of Bridge Engineering",
    ),
    units_and_formulas_notes=(
        "承载力 kN；变形 mm；应力 MPa；轴压比 n",
        "刚度 kN·m²；延性系数 μ；能耗能力",
        "规范公式引用编号，符号含义首现定义",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("AutoCAD", "SAP2000", "Revit", "ANSYS"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)