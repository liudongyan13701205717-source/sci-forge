"""车辆涂装学科论文支持：色漆-清漆体系配色、附着力与耐候评价的体裁、材料领域引用样式与涂装工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="vehicle_painting",
    aliases=(
        "vehicle_painting",
        "车辆涂装",
        "汽车涂装",
        "车身喷漆",
        "color coating",
        "automotive paint",
        "paint matching",
        "金属漆"
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（涂装缺陷与技术瓶颈）",
            "methods（配方/工艺设计与测试方案）",
            "results（色差、膜厚、附着力与耐候结果）",
            "discussion（机理与缺陷成因讨论）",
            "conclusion",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（对象、底色与漆膜状态）",
            "methods（预处理、调配与喷涂工艺）",
            "results（外观评价与仪器测量结果）",
            "discussion（缺陷复盘与改进）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（涂层体系与工艺路线综述）",
            "evidence synthesis（配方-工艺-性能证据归纳）",
            "future directions",
            "references",
        ),
    },
    citation_style="Elsevier 材料类样式（数字编号，作者-年份备选，附 DOI）",
    reporting_standards={
        "配方描述": "须列出各组分的化学名称、质量分数与固含量，注明溶剂与稀释比",
        "工艺条件": "喷涂报告环境温湿度、膜厚（干膜）、喷涂距离与层数；固化报告升温曲线与保温时间",
        "性能测试": "按标准报告方法（如 ASTM D3359 百格法、ASTM D4285 色差），说明样品数量与统计口径",
        "耐候评价": "老化试验注明光源类型、辐照强度、温湿度与总试验时长，结果按试验小时数分组"
    },
    conventions=(
        "全文采用 SI 单位：膜厚 μm、粘度 s（KU 值）、色差 ΔE*、光泽度 %、温度 ℃",
        "颜色按 CIE L*a*b* 或 Pantone/Ral 色卡标注，色差统一以 ΔE* 报告",
        "膜厚分干膜与湿膜分别标注，单位统一 μm，禁止混用 mil",
        "配方以质量分数表示并注明加料顺序；配比精确到小数点后一位",
        "样品命名体现“基材-底漆-面漆-工艺条件”四段式，全文一致"
    ),
    key_venues=(
        "Progress in Organic Coatings",
        "Corrosion Science",
        "Surface and Coatings Technology",
        "Journal of Coatings Technology and Research",
        "涂料工业"
    ),
    units_and_formulas_notes=(
        "色差按 CIELAB 计算 ΔE*00 = √(ΔL*² + ΔC*² + ΔH*²)，报告时说明是否采用 CIEDE2000 修正",
        "膜厚以干膜计，DFT 单位 μm；湿膜/干膜比按固含量换算",
        "光泽度按 20°/60°/85° 几何角度报告，单位 %，须注明测量角度",
        "盐雾试验按 ASTM B117 报告小时数与腐蚀等级（0-5 级）"
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Graco 无气喷涂机", "SATA 6000 HVLP 喷枪", "Riemer 油漆混配机", "BYK Visicolor 配色系统", "色差仪 BYK McChrome", "光泽度仪 BYK-Gardner", "涂层测厚仪 Elcometer", "湿膜厚度规", "BYK 旋转粘度计", "Q-FOG 盐雾试验箱", "Q-Panel 氙灯老化箱", "百格刀附着力测试器", "铅笔硬度计", "红外烘烤灯", "水帘喷漆房", "喷砂房", "随机轨道打磨机", "抛光机", "环境温湿度记录仪", "静电喷涂机"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
