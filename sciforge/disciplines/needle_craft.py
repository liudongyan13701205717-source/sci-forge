"""针线工艺学科论文支持：缝纫/针织/编织/纺织手工体裁、艺术学样式与工艺记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="needle_craft",
    aliases=("needle_craft", "针线工艺", "sewing crafts", "textile crafts",
             "手工纺织", "缝纫工艺", "针织工艺", "编织工艺", "手工针线"),
    paper_types={
        "research": ("abstract", "introduction（背景、动机与工艺问题）", "methodology（工艺与试样方法）", "results（作品与结构数据）", "discussion（工艺启示）", "references"),
        "case_study": ("abstract", "introduction", "case description（作品/传承/工艺案例背景）", "analysis（工艺与结构分析）", "results（作品改进与验证）", "discussion", "references"),
        "review": ("abstract", "introduction", "theoretical overview（工艺史与技法综述）", "evidence synthesis（作品与传承证据综合）", "future directions", "references"),
    },
    citation_style="APA 样式或艺术学样式（作者-年份）",
    reporting_standards={
        "methodology": "工艺试样须遵循材料、针法、尺寸与工序报告规范",
        "heritage": "传统工艺研究须遵循非遗保护与传承人记录规范",
        "experiment": "工艺实验须遵循效标参照与可重复性规范",
    },
    conventions=(
        "针法与结构术语（如针法编号、走线方向）须给出出处与图示",
        "材料（面料、线材、针具）须标注成分、规格与来源",
        "尺寸用 mm/cm 并说明测量点",
        "作品图须给出比例尺、拍摄角度与工艺步骤",
        "工艺传承与流派须注明来源与传承人",
    ),
    key_venues=(
        "Textile Research Journal",
        "Journal of Textile Science and Technology",
        "Heritage and Society",
        "Journal of Craft Research",
        "Fashion, Textiles and Culture",
    ),
    units_and_formulas_notes=(
        "尺寸用 mm/cm、张力用 N、密度用 根/10cm",
        "公式用 amsmath；织物密度与结构计算式须完整",
        "样品给出件数、批次与代表性",
        "效果评估给出量度维度与信度系数",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("缝纫机", "十字绣工具", "刺绣绷架", "手缝针", "珠针", "卷尺", "顶针", "织布机", "编织针", "钩针", "蕾丝编织架", "织布梭", "织针", "打纬机", "打纬梭", "绣花绷架机", "绣线收纳", "编织机", "剪线工具", "缝纫剪"),
    category="艺术学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
