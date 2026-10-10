"""残疾人保健学科论文支持：辅助技术、康复医学与残疾功能评估研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="health_care_of_the_disabled",
    aliases=("health_care_of_the_disabled", "残疾人保健", "残疾康复", "辅助技术", "无障碍设计", "康复医学", "功能评估"),
    paper_types={
        "research": ("abstract", "introduction（研究背景）", "methodology（实验设计）", "results（功能评估结果）", "discussion（讨论与临床应用）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例描述）", "analysis（功能分析）", "results（康复效果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="APA 7",
    reporting_standards={"k1": "RCT 遵循 CONSORT", "k2": "观察性研究遵循 STROBE", "k3": "系统综述遵循 PRISMA"},
    conventions=("残疾类型与等级须注明分级标准", "辅助技术须注明适配参数与定制信息", "功能评估工具须注明版本与信度", "干预方案须注明强度与周期", "结局指标须注明测量时间窗口"),
    key_venues=("Journal of Rehabilitation Medicine", "Assistive Technology", "Disability and Rehabilitation", "Archives of Physical Medicine and Rehabilitation", "中国康复医学杂志"),
    units_and_formulas_notes=("关节活动度：°（角度）", "握力：kg 或 N", "步速：m/s", "肌力：MMT 分级（0-5 级）"),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("肌电图仪（EMG）", "肌骨超声设备", "功能性电刺激系统（FES）", "脑机接口（BCI）设备", "康复机器人", "虚拟现实康复训练系统", "辅助技术适配评估软件", "步态分析系统", "握力与关节活动度检测仪", "3D 打印假肢定制系统", "言语康复评估系统", "认知功能训练软件", "无障碍环境评估工具", "功能独立性评定系统（FIM）", "日常生活能力评估量表（Barthel）", "康复处方管理系统", "辅助技术效果评价工具", "远程康复监测平台", "SPSS", "R 统计分析"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI", "辅助器具适配数据库"),
)
