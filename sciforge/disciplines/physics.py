"""物理学科论文支持：SI 单位、CODATA 常量与 GUM 不确定度规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="physics",
    aliases=("physics", "物理", "量子", "quantum", "粒子", "particle", "凝聚态",
             "condensed matter", "光学", "optics", "引力", "gravity", "天体", "astrophysics"),
    paper_types={
        "letter": (
            "abstract",
            "introduction（动机与关键结果预告）",
            "setup/model（理论或实验设置）",
            "results（核心结果与分析）",
            "discussion（意义与展望）",
            "methods（实验细节，可入补充材料）",
            "references",
        ),
        "research": (
            "abstract",
            "introduction",
            "theory（理论框架与推导）",
            "experimental setup（装置、校准与流程）",
            "results and analysis（数据与误差分析）",
            "discussion（与理论及其他实验对照）",
            "conclusion",
            "acknowledgments（致谢与资助）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction（领域现状与综述范围）",
            "fundamentals（基础概念与记号）",
            "main developments（按主题组织的进展与关键实验）",
            "outlook（开放问题与技术路线）",
            "references",
        ),
    },
    citation_style="编号（APS REVTeX / Physical Review 样式，如 [1]）",
    reporting_standards={
        "units": "一律使用 SI 单位制（BIPM SI Brochure 第 9 版）；非 SI 单位须在首次出现处换算标注",
        "constants": "基本物理常数引用 CODATA 2022 推荐值并注明来源",
        "uncertainty": "测量结果按 GUM（JCGM 100）表示：± 不确定度、置信水平（k=2 或 95%）与分量来源",
        "data": "数据可用性声明：原始数据存档于公开仓库并给出登录号",
        "statistics": "拟合优度、系统误差传播与自由度须显式给出",
    },
    conventions=(
        "量符号斜体、单位符号正体（如 m = 5 kg）；矢量/张量用粗斜体并声明记号",
        "缩写首次出现给出全称；探测器/装置名用首字母大写专有名",
        "图表自含：caption 可独立阅读，须给出工况（温度、磁场、能量等）",
        "理论曲线与数据点同图对比时注明误差棒含义（统计/系统/总）",
        "首次出现的物理效应/定律给出引用（如 Josephson effect [12]）",
    ),
    key_venues=(
        "Physical Review Letters",
        "Physical Review X",
        "Nature Physics",
        "Physical Review A-E",
        "Reviews of Modern Physics",
    ),
    units_and_formulas_notes=(
        "能量/质量常用自然单位制（ℏ=c=1）时必须在首次出现处声明换算因子",
        "大/小数值用科学计数法或 SI 词头（µ、n、G），全文一致",
        "公式编号仅对被引用者编号；方程变量在随后一句中定义",
        "光谱/能级以 cm⁻¹ 或 eV 表示并注明零点约定",
        "角度、磁感应强度等派生单位按 SI 导出单位书写（rad、T）",
    ),
    paper_capable=True,
    contribution_forms=("论文",),
    tools=("LaTeX", "MATLAB", "Python (NumPy/SciPy)", "COMSOL", "Origin"),
    category="理学",
    databases=("arXiv", "OpenAlex", "Crossref", "Semantic Scholar", "Zenodo"),
)
