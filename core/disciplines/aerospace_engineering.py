"""航空航天工程论文支持：飞行力学、推进系统、结构与材料、飞行测试数据。"""
from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aerospace_engineering",
    aliases=("aerospace", "aeronautics", "astronautics", "航空航天工程", "航空工程"),
    paper_types={
        "research": ("abstract", "introduction", "theoretical framework", "methodology", "results", "discussion", "conclusions", "references"),
        "review": ("abstract", "introduction", "classification", "comparative analysis", "trends", "conclusions", "references"),
        "technical_note": ("abstract", "introduction", "technical content", "results", "conclusions", "references"),
    },
    citation_style="AIAA style（编号），如 [1] 或 (Author and Author Year)",
    reporting_standards={
        "wind_tunnel": "风洞试验须报告雷诺数、马赫数、攻角范围、模型缩比与壁面修正",
        "flight_test": "飞行测试须声明试飞架次、传感器型号、校准方法与不确定度",
        "cfd": "CFD 须报告网格收敛指数(GCI)、湍流模型、边界条件与求解器设置",
        "structural": "结构试验须报告载荷谱、应变片布置与安全裕度",
    },
    conventions=(
        "坐标系用机体轴/风轴须声明；角度用度（°），小攻角用弧度时须标注",
        "无量纲化系数用 CL/CD/CM 标准符号；推力用 N 或 lbf 须统一",
        "材料性能数据须引 MIL-HDBK 或 CMH-17 数据源",
        "图须含误差棒或蒙特卡洛散布带；时间历程图标注采样率",
    ),
    key_venues=(
        "AIAA Journal",
        "Journal of Aircraft",
        "Journal of Spacecraft and Rockets",
        "Progress in Aerospace Sciences",
        "Aerospace Science and Technology",
    ),
    units_and_formulas_notes=(
        "速度用 m/s 或 knots（须统一）；高度用 m 或 ft（须统一）",
        "推力/重量比无量纲；雷诺数 Re = ρvL/μ",
        "翼载用 kg/m² 或 lb/ft²；比冲 Isp 用 s",
    ),
    paper_capable=True,
    contribution_forms=("论文", "专利"),
    tools=("ANSYS", "CATIA", "MATLAB", "风洞试验"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
