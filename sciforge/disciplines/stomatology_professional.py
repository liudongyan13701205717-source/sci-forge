"""口腔医学（同时设专业学位类别，代码为1052） 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="stomatology_professional",
    aliases=(
        "口腔医学（同时设专业学位类别，代码为1052）",
        "口腔医学",
        "Dental Medicine",
        "口腔",
        "口腔颌面外科学",
        "正畸学",
        "牙周病学",
        "牙体牙髓病学",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "main content",
            "conclusion",
            "references",
        ),
    },
    citation_style="APA",
    reporting_standards={
        "consort": "口腔随机对照试验须遵循 CONSORT 声明",
        "care": "病例报告须遵循 CARE 声明",
        "reccam": "病例系列须遵循 RECCAM 声明",
        "strobe": "口腔观察性研究须遵循 STROBE 声明",
        "prisma": "系统综述与 Meta 分析须遵循 PRISMA 声明",
    },
    conventions=(
        "口腔RCT须报告注册号、纳入与排除标准、样本量估计依据及脱落情况",
        "影像学研究（CBCT/曲面体层）须报告体素尺寸、扫描参数与图像质量标准",
        "正畸治疗评估须明确治疗指标（如覆𬌗覆盖、ANB角）及统计学意义",
        "病例报告须遵循CARE声明，病例系列须遵循RECAMC声明",
    ),
    key_venues=(
        "Journal of Dentistry",
        "Journal of Dental Research",
        "Journal of Clinical Periodontology",
        "American Journal of Orthodontics and Dentofacial Orthopedics",
        "中华口腔医学杂志",
        "Oral Surgery Oral Medicine Oral Pathology Oral Radiology",
    ),
    units_and_formulas_notes=(
        "CBCT 影像须报告体素尺寸（mm³）与扫描参数（kV/mAs），曲面体层须标注放大率",
        "正畸指标以角度（°）与毫米（mm）计量，覆𬌗覆盖须注明测量平面与参考线",
        "牙周袋深度以毫米（mm）计量，探诊须注明受力（25g）与探诊顺序",
        "疼痛评估采用 VAS 或 NRS 量表（0-10 分），样本量计算须报告 α 与 1-β",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("SPSS", "R", "Stata", "SAS", "Dolphin Imaging CBCT", "iTero Scanner", "Planmeca Romexis", "Sirona Orthophos", "3Shape Trios Scanner", "CEREC", "EndNote", "RevMan", "JBI Systematic Review Software", "MetaAnalyst", "Microsoft Excel", "Python", "Tableau", "JMP", "REDCap", "Cone Beam CT 分析软件"),
    category="医学",
    databases=("OpenAlex",),
)
