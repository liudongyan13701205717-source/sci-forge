"""传统与互补医学学科论文支持：循证医学/传统疗法体裁、Complementary Therapies in Clinical Practice 引用样式与中医记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="traditional_and_complementary",
    aliases=("traditional_and_complementary", "传统与互补医学", "补充替代医学", "替代医学", "传统医学",
             "complementary and alternative medicine", "CAM", "traditional medicine", "中医", "民族医学"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与治疗问题）",
            "methods（试验设计与疗效评价）",
            "results（临床终点与安全性）",
            "discussion（机制探索与循证评价）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "methods（检索策略与纳入标准）",
            "results（Meta 分析与证据分级）",
            "discussion（临床意义与局限性）",
            "references",
        ),
        "case_report": (
            "abstract",
            "introduction",
            "case description（病史与治疗经过）",
            "results（疗效与转归）",
            "discussion（与文献的对比）",
            "references",
        ),
    },
    citation_style="Vancouver 样式（数字编号，按引用顺序排列）",
    reporting_standards={
        "randomized_trials": "随机对照试验遵循 CONSORT 声明",
        "systematic_reviews": "系统综述/Meta 分析遵循 PRISMA 声明",
        "case_reports": "病例报告遵循 CARE 清单",
        "safety_monitoring": "不良事件报告遵循 ICH E2A 指南",
        "sample_size": "样本量计算须报告检验力（power≥0.8）",
    },
    conventions=(
        "药物名称用通用名，中成药用批准文号标注",
        "草药用拉丁学名（斜体）+ 中文名",
        "剂量单位：g、mg 或 mL/kg",
        "疗效评价标准（如中医证候积分）须注明",
        "统计学方法遵循 STROBE 或 CONSORT 报告规范",
    ),
    key_venues=(
        "Complementary Therapies in Clinical Practice",
        "Evidence-Based Complementary and Alternative Medicine",
        "Phytomedicine",
        "Journal of Ethnopharmacology",
        "Chinese Medicine",
    ),
    units_and_formulas_notes=(
        "药物剂量单位：g、mg、mL 或 μg/kg",
        "浓度单位：mg/mL 或 %",
        "疗效评分：证候积分（分）或视觉模拟评分（VAS, 0-10）",
        "公式用 amsmath 排版；统计检验须报告 p 值与效应量",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "RevMan", "Stata", "EndNote", "Origin Pro", "Python", "MATLAB", "高效液相色谱仪（HPLC）", "气相色谱仪（GC）", "质谱仪", "酶标仪", "流式细胞仪", "实时 PCR 仪", "扫描电子显微镜（SEM）", "透射电子显微镜（TEM）", "红外光谱仪（FTIR）", "中药粉碎机", "旋转蒸发仪", "超声提取仪"),
    category="医学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC", "Cochrane Library"),
)
