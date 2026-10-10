"""劳动法学科论文支持：劳动关系、劳动合同、工伤认定与劳动争议处理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="labour_law",
    aliases=(
        "labour_law",
        "劳动法",
        "Labor Law",
        "Employment Law",
        "Industrial Relations",
        "Labour Relations",
        "Workers Rights",
        "Occupational Law",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（绪论）",
            "methodology（研究方法）",
            "results（结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="Bluebook",
    reporting_standards={
        "k1": "ILO C158 劳动合同法",
        "k2": "GB/T 26974 劳动合同示范文本",
        "k3": "EU Directive 2003/88 工作时间指令",
    },
    conventions=(
        "引用法条须注明条款号与最新版本年份",
        "案例引用使用标准法律引用格式（Bluebook）",
        "比较法研究须说明立法例与国家管辖权",
        "数据报告须区分统计口径与地域",
        "涉及当事人隐私须匿名化处理",
    ),
    key_venues=(
        "Labor Law Journal",
        "Industrial and Labor Relations Review",
        "Comparative Labor Law & Policy Journal",
        "劳动与社会保障",
        "中外劳动法制比较",
    ),
    units_and_formulas_notes=(
        "工时以h/日、h/周表示",
        "加班费率：1.5×/2×/3×",
        "经济补偿：N（工作年限）×月工资",
        "赔偿金：2N",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("vLex", "北大法宝", "威科先行", "万律法律", "中国裁判文书网", "IROL", "ILO NORMLEX", "EUR-Lex", "SSRN", "Zotero", "EndNote", "RefWorks", "CiteULike", "Mendeley", "元典智库", "无讼", "SPSS", "NVivo", "Bluebook 引注插件", "Reflex（法律文本分析）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "HeinOnline", "ProQuest", "JSTOR"),
)
