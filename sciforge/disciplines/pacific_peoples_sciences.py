"""太平洋人民科学学科论文支持：太平洋海洋、地质、气候与原住民科学交叉的实证研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="pacific_peoples_sciences",
    aliases=("Pacific Peoples Sciences", "太平洋人民科学", "Pacific Marine Sciences", "Pacific Earth Sciences", "Pacific Oceanography", "Pacific Geochemistry", "Pacific Meteorology", "Pacific Biodiversity"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（研究方法）", "results（研究结果）", "discussion（讨论）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例描述）", "analysis（案例分析）", "results（研究结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7 / AGU",
    reporting_standards={
        "k1": "海洋观测遵循GOOS标准", "k2": "系统综述遵循PRISMA筛选流程", "k3": "海洋学方法遵循SOPAC标准"
    },
    conventions=("海洋观测遵循SOPAC区域标准与ICES数据标准", "地质数据使用UTC时间与WGS84坐标", "原住民知识须获得社区知情同意并说明知识归属", "跨学科术语须给出英文—本地语言对照表", "气候数据须注明来源（观测/再分析/模型）与偏差校正方法"),
    key_venues=("Journal Of Geophysical Research: Oceans", "Marine Biology", "Coral Reefs", "Ocean Dynamics", "Pacific Climate Assessment", "Continental Shelf Research"),
    units_and_formulas_notes=("海洋观测使用SOPAC区域标准（水色、温度、盐度）", "地质年代遵循国际标准地质年代表", "气候数据标注来源（观测/再分析/模型）与偏差校正方法", "遥感反演须给出误差与置信度评估"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("OceanDataLab", "Argo Float", "CtdSensor", "Sea-BAT", "OceanModellingTools", "ROMS", "NEMO", "MITgcm", "COAWST", "Hycom", "PythOcean", "Tide & Current", "Argo Data", "Argo Data Platform", "Argo Float Tracker", "MarineAtlas", "OceanDataViewer", "MarineDataExplorer", "SODA", "AquaMOD"),
    category="理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
