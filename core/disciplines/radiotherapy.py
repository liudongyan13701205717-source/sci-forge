"""放射治疗学科论文支持：放疗计划/剂量学/影像引导体裁、ICRU 引用样式与剂量参数记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="radiotherapy",
    aliases=(
        "radiotherapy",
        "放射治疗",
        "放疗",
        "肿瘤放疗",
        "Radiotherapy",
        "Radiation Therapy",
        "放疗计划",
        "剂量学",
    ),
    paper_types={
        "research": ("abstract", "introduction（背景与治疗问题）", "methodology（治疗方案与计划）", "results（剂量学与临床结果）", "discussion（剂量学分析与临床意义）", "references"),
        "case_study": ("abstract", "introduction", "case description（病例描述）", "analysis（计划分析与剂量评估）", "results（结果）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（理论综述）", "evidence synthesis（证据综合）", "future directions", "references"),
    },
    citation_style="ICRU/ESTRO 样式（作者-年份；遵循 ICRU 剂量报告规范）",
    reporting_standards={
        "k1": "剂量学数据须遵循 ICRU 62/83 报告规范",
        "k2": "正常组织耐受剂量须遵循 QUANTEC 规范",
        "k3": "系统综述须遵循 PRISMA 声明",
    },
    conventions=(
        "剂量学参数（PTV 覆盖、D2cc、HI、CI）须完整报告",
        "剂量单位用 Gy（灰度），分次剂量须注明",
        "计划参数（射野数、MU、机架角）须标注",
        "设备型号与 TPS 软件版本须报告",
        "患者信息须去标识化",
    ),
    key_venues=(
        "International Journal of Radiation Oncology Biology Physics",
        "Radiotherapy and Oncology",
        "Practical Radiation Oncology",
        "Journal of Applied Clinical Medical Physics",
        "British Journal of Radiation Biology",
    ),
    units_and_formulas_notes=(
        "剂量单位用 Gy",
        "相对生物效果用 RBE",
        "统计量给出 M/SD 与 95% CI",
        "生存分析须报告 HR 与 CI",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Varian Eclipse", "Varian TrueBeam", "Accuray Halcyon", "Accuray Trilon", "Elekta Monarch", "Elekta Synergy", "Pinnacle TPS", "RayStation", "MIM Maestro", "Oncentra MasterPlan", "FLUKA", "Geant4", "EGSnrc", "MCNP", "MUMPS", "VMAT", "IMRT", "SBRT", "MOS.ai", "Ibis Imaging"),
    category="医学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
