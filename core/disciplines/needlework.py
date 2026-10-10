"""刺绣工艺学科论文支持：刺绣艺术/中国传统工艺/民族纺织体裁、艺术学样式与刺绣记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="needlework",
    aliases=("needlework", "刺绣工艺", "embroidery arts", "embroidery crafts",
             "中国刺绣", "苏绣", "湘绣", "粤绣", "蜀绣"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与刺绣艺术问题）", "methodology（针法与试样方法）", "results（作品与艺术数据）", "discussion（艺术启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（作品/绣种/传承人案例背景）", "analysis（针法与艺术分析）", "results（作品改进与验证）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（刺绣史与流派综述）", "evidence synthesis（作品与传承证据综合）", "future directions", "references"),
    },
    citation_style="艺术学/Chicago 样式（作者-年份）",
    reporting_standards={
        "methodology": "刺绣试样须遵循针法、线材、底布与工序报告规范",
        "heritage": "非遗绣种研究须遵循非遗保护与传承人记录规范",
        "artistic_analysis": "艺术分析须遵循形式、构图、色彩与纹样报告规范",
    },
    conventions=(
        "针法与流派术语（如齐针、套针、钉线）须给出出处与图示",
        "绣种（苏、湘、粤、蜀、京、鲁等）须标注地域与代表传承人",
        "线材（丝、棉、绒、金属线）与底布须标注成分与规格",
        "作品图须给出比例尺、拍摄角度与针法特写",
        "纹样与图样须注明来源、时代与出处",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of Craft Research",
        "Fashion, Textiles and Culture",
        "Heritage and Society",
        "Journal of Textile Science and Technology",
    ),
    units_and_formulas_notes=(
        "尺寸用 mm/cm、密度用 针/cm²、张力用 N",
        "公式用 amsmath；针法密度与结构计算式须完整",
        "样品给出件数、批次与代表性",
        "艺术评估给出量度维度与信度系数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("绣绷", "绣针", "绣线", "缎面针线", "苏绣工具包", "湘绣工具包", "十字绣套装", "珠绣针", "打结针", "钩针", "编织针", "蕾丝编织架", "刺绣模板", "绣花绷架机", "绣线收纳", "剪线工具", "绣绷架", "绣花底布", "绣花画稿", "绣花工具包"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
