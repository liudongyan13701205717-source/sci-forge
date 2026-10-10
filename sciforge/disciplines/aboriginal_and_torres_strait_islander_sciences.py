"""Aboriginal And Torres Strait Islander Sciences 学科论文支持。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="aboriginal_and_torres_strait_islander_sciences",
    aliases=(
        "Aboriginal And Torres Strait Islander Sciences",
        "原住民科学",
        "ATSI Sciences",
        "Indigenous Sciences",
        "First Nations Science",
        "Aboriginal Science",
        "Torres Strait Islander Science",
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
        "ocap": "原住民科学数据须遵循 OCAP 原则（所有权、控制权、获取权、占有权）",
        "tekm": "传统生态知识须以原住民社区为主导发表方式，不可与定量数据混用",
        "field_data": "野外数据采集须记录采样方法、季节性信息与文化安全限制",
        "genomics_ethics": "涉及生物采样须遵循原住民基因伦理准则，数据所有权须事先约定",
    },
    conventions=(
        "传统生态知识（TEK）须以原住民社区为主导发表方式",
        "科学数据采集须与原住民科学合作机构联合开展",
        "数据所有权须事先约定，确保原住民社区可分享权",
        "涉及生物采样的研究须遵循原住民基因伦理准则",
    ),
    key_venues=(
        "Australian Journal of Botany",
        "Australian Journal of Zoology",
        "Indigenous Resource Management",
        "Journal of Applied Ecology",
        "Australian Zoologist",
        "Australian Mammalogist",
    ),
    units_and_formulas_notes=(
        "物种数据须注明采样方法与样方面积（m²）或样带长度（m），丰度以 ind/m² 或 ind/ha 计量",
        "环境样本（水/土/大气）须注明采样深度、季节与 GPS 坐标精度，传统生态知识须单独标注来源",
        "生物测量以毫米（mm）或厘米（cm）计量，体长须注明测量部位（如标准体长 SL 或全长 TL）",
        "DNA 条形码与基因分析须注明引物、测序平台与数据库比对结果，须遵循原住民基因伦理准则",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("R", "SPSS", "Stata", "QGIS", "ArcGIS", "iNaturalist", "eBird", "EndNote", "Python（NumPy/SciPy）", "MATLAB", "Microsoft Excel", "Tableau", "Microsoft Power BI", "Adobe Lightroom", "FieldMapper", "Google Earth Pro", "Mapbox", "Morpho", "Methoscope", "FieldLogger"),
    category="理学",
    databases=("OpenAlex",),
)
