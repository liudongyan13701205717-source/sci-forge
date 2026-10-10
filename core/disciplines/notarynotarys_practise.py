"""公证员执业学科论文支持：公证实务/法律职业/民商事公证体裁、法律引用样式与公证业务记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="notarynotarys_practise",
    aliases=("notarynotarys_practise", "公证员执业", "Notary Practise",
             "公证实务", "notarial practice", "公证业务",
             "法律职业", "legal profession", "民商事公证"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与公证问题）",
            "methodology（案例与实证方法）",
            "results（法律发现与统计）",
            "discussion（法理与实践意义）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（公证案例）",
            "analysis（法律适用与分析）",
            "results（公证结论与效力）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（公证理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="GB/T 7714 样式（中国国标，作者-年份）",
    reporting_standards={
        "laws": "引用法律法规须注明全称与生效日期",
        "cases": "引用案例须标注法院、案号与日期",
        "notary": "公证业务遵循《公证法》与《公证程序规则》",
        "ethics": "遵循中国公证协会《公证员执业道德规范》",
        "data": "公证数据遵循司法部公证数据规范",
    },
    conventions=(
        "法律术语遵循《法律术语词典》",
        "法条引用遵循法律体系层次",
        "案例引用须完整案号",
        "数字用阿拉伯数字",
        "图表编号并标注来源",
    ),
    key_venues=(
        "中国公证",
        "法律适用",
        "法学杂志",
        "中国法学",
        "法学研究",
        "政法论坛",
    ),
    units_and_formulas_notes=(
        "引用法律法规须完整",
        "案号用阿拉伯数字",
        "日期用 YYYY-MM-DD",
        "金额用人民币符号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("全国公证信息管理系统", "中国公证协会", "中国裁判文书网", "人民法院在线服务", "国家企业信用信息公示系统", "北大法宝", "法信", "威科先行", "Google Docs", "Microsoft Word", "WPS Office", "Adobe Acrobat", "EndNote", "Zotero", "Mendeley", "Notary Database", "公证文书模板系统", "电子签章系统", "人脸识别系统", "区块链存证系统"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
