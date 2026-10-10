"""组织培养技术学科论文支持：植物组织培养/细胞再生体裁、Plant Cell Reports 引用样式与组织培养记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="tissue_culture_technology",
    aliases=("tissue_culture_technology", "组织培养技术", "植物组织培养", "细胞培养", "愈伤组织",
             "plant tissue culture", "micropropagation", "细胞再生", "茎尖培养"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与组织培养问题）",
            "materials and methods（外植体与培养基配制）",
            "results（增殖率与生根率）",
            "discussion（机理与规模化展望）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（物种案例）",
            "methods（培养体系优化）",
            "results（繁殖系数与移栽成活率）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview",
            "evidence synthesis",
            "future directions",
            "references",
        ),
    },
    citation_style="Vancouver 样式（数字编号，按引用顺序排列）",
    reporting_standards={
        "sterility": "无菌操作条件须声明（超净台/生物安全柜规格）",
        "medium_specification": "培养基成分（激素浓度、琼脂、pH）须逐项报告",
        "environmental_conditions": "光照、温度、湿度与暗培养时长须记录",
        "statistical_design": "重复数≥3，随机区组或完全随机设计须声明",
    },
    conventions=(
        "植物名称用拉丁学名斜体表示",
        "激素浓度单位用 mg/L 或 μmol/L",
        "增殖系数定义须明确（新生株丛数/原始外植体数）",
        "培养周期以周（w）为单位报告",
        "pH 调整用 1 mol/L HCl 或 NaOH 调节须注明",
    ),
    key_venues=(
        "Plant Cell, Tissue and Organ Culture",
        "In Vitro Cellular and Developmental Biology - Plant",
        "Plant Cell Reports",
        "Plant Science",
        "Plant Cell Physiology",
    ),
    units_and_formulas_notes=(
        "激素浓度单位：mg/L 或 μmol/L",
        "光照强度单位：μmol/(m²·s)",
        "增殖系数与生根率以百分比（%）报告",
        "公式用 amsmath 排版；培养基配方以表格形式呈现",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("超净工作台", "高压蒸汽灭菌锅", "pH 计", "电子天平", "电热恒温培养箱", "光照培养箱", "植物组织培养架", "液氮罐", "离心机", "倒置显微镜", "高压灭菌过滤装置", "电导率仪", "分光光度计", "超纯水机", "冰箱", "振荡培养仪", "PCR 仪", "凝胶电泳仪", "Origin", "SPSS"),
    category="农学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
