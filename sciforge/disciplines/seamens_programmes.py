"""海员培训项目学科论文支持：STCW 合规培训/航海教育/船员资质/培训体系评估体裁、IMO 培训报告规范与航海教育度量记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="seamens_programmes",
    aliases=("seamens_programmes", "海员培训", "航海教育项目", "船员培训", "maritime training programmes"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、问题与研究意义）",
            "data and methods（数据与方法）",
            "results（结果）",
            "discussion（讨论）",
            "conclusions（结论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（综述）",
            "evidence synthesis（证据综合）",
            "future directions（展望）",
            "references",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "training": "培训报告遵循 IMO STCW 公约培训与发证规则",
        "evaluation": "培训评估须报告评估指标、学员表现与通过率",
        "simulator": "模拟器训练须报告训练时长、场景复杂度与学员评分",
        "data": "培训数据须报告样本量、数据来源与质量控制措施",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "培训课程须注明对应 STCW 章节与规则编号",
        "培训效果须报告通过率、评分分布与技能考核结果",
        "学员背景须说明前学历、工作年限与证书等级",
        "培训课程时长须注明总学时与理论/实践学时比",
        "引用 STCW 条款须标注具体章节与年份版本",
    ),
    key_venues=(
        "Maritime Education and Training Review",
        "Journal of Maritime Engineering",
        "Safety Science",
        "Ocean Engineering",
        "Nautical Institute Journal",
    ),
    units_and_formulas_notes=(
        "培训时长用 h；通过率用 %；评分用百分制或五级制",
        "学时分配须注明理论/模拟器/实操比例",
        "公式用 amsmath；培训效果评估公式须编号",
        "统计结果给出均值 ± 标准差与样本量；显著性用 p 值标注",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Maritime Training Management System", "STCW Compliance Software", "Ship Simulator 航海模拟器", "ECDIS 电子海图系统", "Crewing System 船员管理系统", "VR Training Platform 虚拟现实培训", "Learning Management System (LMS)", "Marine Weather Routing System", "AIS 自动识别系统", "Radar 雷达训练模块", "Gyrocompass 陀螺罗经", "GPS 差分定位仪", "MATLAB 数据分析", "R 统计建模", "LaTeX 排版", "Origin 绘图", "SPSS 统计分析", "Python 数据分析", "Qualisystems 培训评估", "SimNet 网络仿真"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)