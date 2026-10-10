"""母婴护理学科论文支持：母婴护理/产科护理/围产期护理体裁、CSE 引用样式与护理学记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="mother_craft_nursing",
    aliases=(
        "mother_craft_nursing", "母婴护理", "母亲护理", "maternity nursing", "产科护理",
        "围产期护理", "母婴保健", "perinatal care", "产后护理"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与护理问题）",
            "methodology（护理方法与测量）",
            "results（母婴数据与结果）",
            "discussion（护理意义与改进）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（母婴护理案例）",
            "analysis（护理过程与干预）",
            "results（母婴健康结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（母婴护理理论）",
            "evidence synthesis（护理证据综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="CSE/CSE/CNMA 样式（作者-年份；护理期刊遵循 CSE 规范）",
    reporting_standards={
        "clinical_trial": "临床试验遵循 CONSORT 声明",
        "nursing_study": "护理研究遵循 SPIRIT 声明",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "母婴数据须区分孕产妇与新生儿",
        "母乳喂养术语（纯/混合/配方）须界定",
        "疼痛评分（NRS/VAS）须报告",
        "新生儿 Apgar 评分须完整",
        "母婴健康指标单位须规范",
    ),
    key_venues=(
        "Journal of Obstetric, Gynecologic and Neonatal Nursing",
        "Midwifery",
        "Journal of Human Lactation",
        "International Journal of Nursing Studies",
        "Journal of Obstetrics and Gynaecology",
    ),
    units_and_formulas_notes=(
        "体温用 °C；体重用 kg；身高用 cm",
        "产程用宫口扩张 cm；胎心用 bpm",
        "公式用 amsmath；母乳喂养指导公式须明确",
        "数值结果给出均值 ± SD 与样本量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("母婴健康评估量表", "母乳喂养监测仪", "婴儿秤与生长测量系统", "电子体温计", "血氧仪", "胎心仪", "新生儿黄疸检测仪", "智能穿戴设备", "母乳分析仪", "母婴健康监测系统", "母乳喂养指导机器人", "家庭健康管理系统", "母婴健康问卷系统", "新生儿行为神经评定量表", "母婴互动视频分析系统", "母婴护理技能模拟人", "R (数据处理)", "SPSS", "Stata", "母婴护理远程监控系统"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
