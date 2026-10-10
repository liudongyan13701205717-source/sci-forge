"""皮革制品生产学科论文支持：皮革制品设计、工艺流程、材料性能与质量控制。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="leather_goods_production",
    aliases=(
        "leather_goods_production",
        "皮革制品生产",
        "皮革制造",
        "leather manufacturing",
        "leather products",
        "皮具制作",
        "leather working",
        "tannery production",
        "皮革制品制造",
    ),
    paper_types={
        "research": (
            "abstract（摘要）",
            "introduction（引言）",
            "methodology（方法）",
            "results（结果）",
            "discussion（讨论）",
            "references（参考文献）",
        ),
        "case_study": (
            "abstract（摘要）",
            "introduction（引言）",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion（讨论）",
            "references（参考文献）",
        ),
        "review": (
            "abstract（摘要）",
            "introduction（引言）",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions（展望）",
            "references（参考文献）",
        ),
    },
    citation_style="APA 7",
    reporting_standards={
        "k1": "实验须报告皮革等级、部位、厚度与温度湿度控制",
        "k2": "性能测试须引用 ISO/ASTM 标准编号与不确定度",
        "k3": "对比试验须说明样品数与统计方法",
    },
    conventions=(
        "试样规格遵循 ISO 4027 与 ISO 4045",
        "厚度单位 mm，透气度单位 m³/(m²·s·kPa)",
        "拉力与撕裂强度单位 N/mm 或 kN/m",
        "色号引用 Pantone TCX 或 CMYK",
        "皮革等级用 Grade A/B/C 与部位号标注",
    ),
    key_venues=(
        "Journal of Industrial Textiles",
        "Polymer Degradation and Stability",
        "Leather and Rubber Week",
        "皮革化工",
        "中国皮革",
    ),
    units_and_formulas_notes=(
        "厚度按 ISO 4045 十点平均法测得",
        "透气度 Q = A × P / Δp",
        "拉伸强度 σ = F / (t × w)",
        "色牢度以灰卡级数 1-5 级评价",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("AutoCAD", "SolidWorks", "Rhino 3D", "Adobe Illustrator", "Adobe Photoshop", "MATLAB", "ANSYS", "COMSOL Multiphysics", "Python", "OriginPro", "皮革厚度仪 ISO 4045", "皮革透气度测试仪 ISO 11496", "皮革摩擦色牢度试验机 ISO 105-X12", "皮革耐折度试验机 ISO 4039", "皮革拉伸试验机", "色差仪 Konica Minolta SpectroEye", "傅里叶红外光谱仪 FTIR", "X 射线衍射仪 XRD", "扫描电镜 SEM", "皮革水分测定仪 ISO 16610"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
