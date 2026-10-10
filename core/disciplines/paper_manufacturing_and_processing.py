"""造纸与纸加工学科论文支持：纤维材料、制浆造纸工艺与纸品性能研究体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="paper_manufacturing_and_processing",
    aliases=(
        "paper_manufacturing_and_processing",
        "造纸与纸加工",
        "Paper Manufacturing and Processing",
        "造纸工程",
        "制浆造纸",
        "Pulp and Paper Science",
        "纸浆与造纸技术",
        "纸品加工",
        "paper science"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与问题）",
            "methodology（材料与方法）",
            "results（结果）",
            "discussion（讨论）",
            "references"
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references"
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references"
        ),
    },
    citation_style="GB/T 7714-2015",
    reporting_standards={
        "k1": "纤维与纸品性能测试遵循 ISO 与 TAPPI 标准",
        "k2": "工艺研究须报告原料、配比与设备参数",
        "k3": "耐久性研究须报告加速老化条件与判定阈值"
    },
    conventions=(
        "原料须报告树种、纤维种类、化学组成与制浆方式",
        "抄造与加工工艺参数须完整报告",
        "物理性能须报告测试标准与样张编号",
        "水分与厚度须在标准化条件下（如 ISO 6373）测定并报告",
        "结论须区分实验室试纸与现场纸样"
    ),
    key_venues=(
        "Cellulose",
        "Industrial & Engineering Chemistry Research",
        "BioResources",
        "Holzforschung",
        "中国造纸"
    ),
    units_and_formulas_notes=(
        "强度指标以 N/m、kN/m 或 J/m² 报告",
        "厚度与定量以 μm 与 g/m² 报告",
        "化学组分以质量百分比报告",
        "温度、时间与压力须给出完整工艺曲线"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("纤维板机（Sheet Machine）", "打浆度仪", "定量仪", "厚度仪（千分尺）", "耐折度仪", "抗张强度仪", "撕裂度仪", "断裂度仪", "水分仪", "白度仪", "pH 计", "XRF 分析仪", "扫描电镜（SEM）", "FTIR 光谱仪", "拉力试验机（UTM）", "圆网抄纸机（Fourdrinier）", "长网抄纸机（Long-Net）", "磨木浆机（Refiner）", "OriginPro", "Microsoft Excel"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
