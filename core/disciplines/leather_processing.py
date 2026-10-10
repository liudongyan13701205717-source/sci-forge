"""皮革加工学科论文支持：鞣制、涂饰、染色与皮革化学工艺研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="leather_processing",
    aliases=(
        "leather_processing",
        "皮革加工",
        "皮革鞣制",
        "leather tanning",
        "tanning",
        "皮革化学品",
        "leather chemistry",
        "皮革涂饰",
        "leather finishing",
    ),
    paper_types={
        "research": (
            "abstract（摘要）",
            "introduction（引言）",
            "materials and methods（材料与方法）",
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
        "k1": "鞣制工艺须报告 tannin 用量、pH、温度、时间与浴比",
        "k2": "染色须报告染料浓度、温度、pH、助剂与固色工艺",
        "k3": "化学品毒性须按 REACH 或 GHS 规范申报",
    },
    conventions=(
        "铬鞣浴浓度以铬计 % (w/w) 表示",
        "pH 用玻璃电极 25℃ 校准",
        "含铬量以 Cr(III) 或 Cr 总量标注",
        "涂饰膜厚以 μm 单位报告",
        "染料用量以对干皮重量百分比 owf 表示",
    ),
    key_venues=(
        "Leather Journal",
        "Journal of Industrial Textiles",
        "Polymer Degradation and Stability",
        "Journal of Applied Polymer Science",
        "皮革化工",
    ),
    units_and_formulas_notes=(
        "浴比 = 水重 / 皮重，无量纲",
        "铬利用率 η = Cr_吸收 / Cr_投料 × 100%",
        "染色温度单位 ℃，pH 无量纲",
        "膜厚单位 μm，涂饰层数计次",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("皮革磨革机 Skiving Machine", "转鼓鞣制机 Drum Tanning", "涂饰机 Finishing Machine", "pH 计 Mettler Toledo", "铬含量测定仪", "导电率仪 Conductivity Meter", "Brix 糖度计", "傅里叶红外光谱仪 FTIR", "X 射线荧光光谱仪 XRF", "紫外可见光谱仪 UV-Vis", "气相色谱仪 GC", "高效液相色谱仪 HPLC", "皮革透气度测试仪", "皮革耐磨试验机", "皮革抗张力测试仪", "皮革撕裂强度测试仪", "MATLAB", "Python", "ChemDraw", "COMSOL Multiphysics"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
