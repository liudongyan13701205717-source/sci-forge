"""法律实教学科论文支持：诉讼、非诉业务、执业规范与司法实务研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="legal_practice",
    aliases=(
        "legal_practice",
        "法律实务",
        "法律执业",
        "legal practice",
        "law practice",
        "律师实务",
        "律师业",
        "advocacy",
        "诉讼实务",
    ),
    paper_types={
        "research": (
            "abstract（摘要）",
            "introduction（引言）",
            "methodology（研究方法）",
            "findings（发现）",
            "discussion（讨论）",
            "references（参考文献）",
        ),
        "case_study": (
            "abstract（摘要）",
            "introduction（引言）",
            "case description（案例事实）",
            "analysis（法律分析）",
            "outcome（结果）",
            "discussion（评析）",
            "references（参考文献）",
        ),
        "review": (
            "abstract（摘要）",
            "introduction（引言）",
            "theoretical overview（理论综述）",
            "evidence synthesis（实践综合）",
            "future directions（展望）",
            "references（参考文献）",
        ),
    },
    citation_style="Bluebook（Bluebook 21）",
    reporting_standards={
        "k1": "案例写作须引用卷宗号、案号与法院名称",
        "k2": "法律条文引用须含法律名称、章节号与生效日期",
        "k3": "案例匿名化处理时须声明遮蔽范围",
    },
    conventions=(
        "案号采用 (年) 法院代字 案类 字号 格式",
        "法律层级：宪法 > 法律 > 行政法规 > 部门规章",
        "案例引用须标年份与判决日期",
        "引注样式依 Bluebook 或 OSCOLA",
        "外国法引用须标译本出处",
    ),
    key_venues=(
        "Harvard Law Review",
        "Yale Law Journal",
        "Columbia Law Review",
        "中国法学",
        "法学研究",
    ),
    units_and_formulas_notes=(
        "诉讼时效：一般 3 年，特殊类型另规定",
        "利息计算以年利率 % 与天数为准",
        "执行案件以 (年) 执字第 X 号标注",
        "判决书引用遵循 Bluebook R. 10",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("vLex", "Casetext", "CoCounsel Thomson Reuters", "北大法宝", "威科先行", "法信", "中国裁判文书网", "DocuSign", "法大大电子签章", "案件管理系统", "律师事务所 OA", "尽职调查平台", "电子卷宗系统", "庭审系统", "MS Word", "WPS Office", "速录软件", "LexMachine（合同智能审查）", "Bluebook 引注插件", "Practical Law 法律实务平台"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "国家法律法规数据库"),
)
