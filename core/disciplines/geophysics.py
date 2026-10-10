"""地球物理学学科论文支持：地震学、电磁法、重磁力、地热与地球动力学。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="geophysics",
    aliases=(
        "geophysics",
        "地球物理学",
        "seismology",
        "地震学",
        "geomagnetism",
        "地磁学",
        "geoelectrics",
        "电法勘探",
        "gravimetry",
        "重力勘探",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（数据、方法、反演与建模）",
            "results（观测与结果）",
            "discussion（机制与解释）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（区域/台网背景）",
            "analysis（数据处理与分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="AGU（作者-年份，APA 变体）",
    reporting_standards={
        "data": "台网/仪器/时间基准/采样率/带宽须报告",
        "processing": "处理链须逐步报告算法、参数与验证",
        "inversion": "反演须报告先验、正则化、不确定度与多解性检验",
    },
    conventions=(
        "震相时间用 UTC；震级用 Mw/Ms/Mb 明确标记",
        "深度用 km；距离用 km；速度用 km/s",
        "台站坐标用 °N/°E 或投影坐标；高程用 m asl",
        "反演模型须给网格、先验、正则化参数与不确定度图",
        "频谱与波形图须给时间尺度、放大倍数与带宽",
    ),
    key_venues=(
        "Journal of Geophysical Research: Solid Earth",
        "Geophysical Journal International",
        "Earth and Planetary Science Letters",
        "Geophysical Research Letters",
        "Seismological Research Letters",
    ),
    units_and_formulas_notes=(
        "时间用 s/ms；频率用 Hz；周期用 s",
        "速度用 km/s 或 m/s；密度用 g/cm³ 或 kg/m³",
        "应力用 Pa 或 MPa；应变用无量纲或 %",
        "电磁量：电场 V/m、磁场 nT；电阻率 Ω·m",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("SeisComP", "ObsPy", "SAC", "SEISAN", "ProMAX", "Oasis montaj", "Kingdom", "GMT (Generic Mapping Tools)", "Python", "MATLAB", "R", "GOCAD", "Flac3D", "OpenSees", "SURFE", "SEGY 地震记录", "地震仪（宽频带）", "磁力仪", "重力仪", "Jupyter Notebook"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
