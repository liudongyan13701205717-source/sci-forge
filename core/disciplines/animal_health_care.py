"""动物医疗保健学科论文支持：兽医学/动物疫病/临床诊疗体裁、Vancouver/CAVR 样式与兽医诊疗注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="animal_health_care",
    aliases=("animal health care", "动物医疗保健", "兽医学", "veterinary medicine",
             "动物疫病防控", "animal disease control", "兽医临床",
             "veterinary clinical medicine", "动物保健", "animal health",
             "动物福利", "animal welfare", "兽医公共卫生", "veterinary public health",
             "动物繁殖学", "theriogenology", "预防兽医学",
             "preventive veterinary medicine", "动物营养与健康"),
    paper_types={
        "research": (
            "abstract",
            "introduction（临床或疫病问题与假设）",
            "methods（动物来源、分组、诊断流程与终点）",
            "results（临床指标、病理与流行病学）",
            "discussion（机理、传播与防控意义）",
            "limitations",
            "references",
        ),
        "clinical_trial": (
            "abstract",
            "introduction",
            "methods（随机化、盲法、剂量与终点）",
            "results（疗效、安全性与依从性）",
            "discussion（与既往试验对比）",
            "references",
        ),
        "case_report": (
            "abstract",
            "introduction（新颖性声明）",
            "case presentation（基线、体格检查与实验室结果）",
            "intervention and outcomes（处置方案与随访）",
            "discussion",
            "references",
        ),
        "epidemiological": (
            "abstract",
            "introduction",
            "methods（调查设计、抽样与暴露定义）",
            "results（分布、关联与风险因素）",
            "discussion（防控建议）",
            "references",
        ),
    },
    citation_style="Vancouver 样式（编号制；JAVMA 遵循 CAVR 规范）",
    reporting_standards={
        "randomized_trial": "RCT 报告遵循 CONSORT 声明",
        "observational": "观察性研究遵循 STROBE 声明",
        "diagnostic_test": "诊断试验遵循 STARD 2015 声明",
        "case_report": "病例报告遵循 CARE 指南",
        "epidemiology": "流行病学研究遵循 STROBE 与 EPIVET 规范",
        "welfare": "福利评估遵循 WMSC 与 AVMA 评估框架",
    },
    conventions=(
        "疾病名称与病原分类引用国际通用名称（ICTVDG）",
        "剂量按 mg/kg 或 IU/kg 报告并注明给药途径（口服/肌注/静脉）",
        "疗效按时间窗（给药后 24 h/48 h/72 h）分别报告并附样本量",
        "诊断试验的灵敏度与特异度须同时报告并给出 95% CI",
        "缩写首次出现给出全称（如 PCR = polymerase chain reaction）",
    ),
    key_venues=(
        "Journal of the American Veterinary Medical Association",
        "Veterinary Record",
        "Veterinary Microbiology",
        "Preventive Veterinary Medicine",
        "Journal of Veterinary Internal Medicine",
        "BMC Veterinary Research",
        "Theriogenology",
    ),
    units_and_formulas_notes=(
        "体重用 kg；体长用 cm；体温用 °C",
        "药物浓度用 mg/mL 或 µg/mL；给药剂量按 mg/kg 计算",
        "血清学与免疫学指标给出单位（IU/mL 或吸光度 OD 值）",
        "病理与影像测量给出均值 ± SD 与范围",
        "统计结果给出均值 ± SE、p 值与 95% CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("IDEXX eVetManager", "Midas Vet", "Vetspire (Covetrus)", "AWV", "IDEXX PROCyte", "Abaxis VetScan VS2", "IDEXX VetScan VETtest VET4DX Plus", "IDEXX SNAP", "i-STAT Vet", "Sysmex CV5800", "BioMérieux VITEK 2", "Applied Biosystems QuantStudio", "Roche LightCycler 480", "BD FACSCanto II", "SonoScape X9 Vet", "VetUS Vet1", "GE OEC Elite Vet", "Siemens SOMATOM", "Agfa Vet DR", "AANA Vet", "GraphPad Prism", "R"),
    category="农学",
    databases=("PubMed", "OpenAlex", "CNKI", "Europe PMC"),
)
