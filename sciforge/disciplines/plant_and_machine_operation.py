"""农机操作学科论文支持：精准农业/自动驾驶/机具性能评价体裁、ASABE 引用样式与农机操作记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="plant_and_machine_operation",
    aliases=("plant_and_machine_operation", "农机操作", "农业机械操作", "agricultural machinery operation", "农机驾驶", "tractor operation", "精准农业", "precision agriculture", "自动驾驶农机", "autonomous farm machinery", "农机电控", "agricultural automation"),
    paper_types={
        "research": ("abstract", "introduction（引言）", "methodology（方法与试验设计）", "results（性能与作业数据）", "discussion（作业效率与影响）", "references"),
        "case_study": ("abstract", "introduction", "case description（案例与作业流程）", "analysis（机具配置与操作）", "results（作业效率对比）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（农机自动化综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ASABE 样式（国内期刊遵循 GB/T 7714）",
    reporting_standards={"ASABE R38.1": "农机性能报告规范", "ISO 16497": "农机驾驶操作规范", "ISO 10547": "农机安全评估", "ASTM D1602": "土壤机械性质测试", "ISO 9865": "农机试验方法"},
    conventions=("机具型号与配置须完整（马力、悬挂类别、作业幅宽）", "作业参数（深度、速度、转速）须给出", "效率指标（作业速率、单位油耗、故障率）标准化", "自动驾驶系统（RTK/HDG/LGS）须说明", "样本量、地块、土壤类型须报告"),
    key_venues=("Computers and Electronics in Agriculture", "Bioresource Technology", "Journal of Terramechanics", "ASABE Annual Meeting", "农业机械学报"),
    units_and_formulas_notes=("功率 kW、马力 hp；扭矩 N·m", "速度 km/h；作业幅宽 m", "油耗 L/h；单位作业油耗 L/ha", "深度 cm；角度 °"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("John Deere CommandCenter", "John Deere GreenStar", "John Deere StarFire", "John Deere SectionController", "John Deere Yield Monitoring", "Case IH AFS Connect", "Case IH Section Control", "Case IH YieldMap", "New Holland NaviCom", "New Holland Section Control", "New Holland AutoTrac", "CLAAS Telematics", "CLAAS CommandLine", "Trimble AgCommander", "Trimble Ag Command", "Trimble AgriGPS", "Trimble Farmworks", "Topcon AgriGPS", "Raven SteerGuide", "Raven See & Spray"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
