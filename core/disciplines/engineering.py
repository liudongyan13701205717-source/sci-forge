"""工程学科论文支持：设计标准、测试验证与性能指标规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="engineering",
    aliases=("engineering", "工程", "机械", "mechanical", "控制", "control",
             "机器人", "robotics", "制造", "manufacturing", "土木", "civil", "电气", "electrical"),
    paper_types={
        "research": (
            "abstract",
            "introduction（需求背景与现状不足）",
            "design requirements（设计需求与约束）",
            "methodology/design（设计方案与建模）",
            "prototype/implementation（样机与实现）",
            "test and validation（测试方案与验证结果）",
            "results and discussion",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction（工程背景）",
            "problem statement",
            "methodology（方法与实施过程）",
            "results（实测数据与指标）",
            "discussion（经验教训与推广条件）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "taxonomy（按技术路线分类的进展）",
            "challenges and future directions",
            "references",
        ),
    },
    citation_style="IEEE 编号（如 [1]，期刊缩写）",
    reporting_standards={
        "design": "设计依据的标准与规范须显式引用（ISO/IEC/ASME/ASTM/GB），并给出版本号",
        "testing": "测试条件、仪器型号与校准状态须声明；重复次数与不确定度给出",
        "metrics": "性能指标（效率、精度、功耗、寿命）定义与测量方法须可复现",
        "safety": "失效模式（FMEA）与安全裕度须讨论；危险工况单列",
        "uncertainty": "测量不确定度按 GUM 评定并随结果给出",
    },
    conventions=(
        "公式变量在首次出现处定义，全文记号一致（可附符号表）",
        "图注给出工况（转速、负载、温度）；坐标轴带单位",
        "表格三线制；对比数据给来源出处",
        "缩写首次出现给出全称；部件名与图纸编号一致",
        "系统框图/流程图矢量导出，信号流向清晰",
    ),
    key_venues=(
        "IEEE Transactions on Industrial Electronics",
        "IEEE/ASME Transactions on Mechatronics",
        "Mechanical Systems and Signal Processing",
        "Control Engineering Practice",
        "ASME Journal of Mechanical Design",
    ),
    units_and_formulas_notes=(
        "一律 SI 单位优先；工程惯用单位（psi、hp）须换算并列",
        "误差以绝对值与百分比并列给出；重复性/再现性分开报告",
        "传递函数/状态空间记法统一（连续 s 域与离散 z 域标明）",
        "公差与配合按 ISO 286 标注；表面粗糙度 Ra/Rz 注明",
        "能量/功率单位区分有功与视在（W 与 VA）",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("MATLAB", "AutoCAD", "ANSYS", "Python"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
