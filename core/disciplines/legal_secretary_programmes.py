"""法律秘书课程学科论文支持：法律文书、办公技能与法律文秘训练研究。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="legal_secretary_programmes",
    aliases=(
        "legal_secretary_programmes",
        "法律秘书课程",
        "法律秘书",
        "legal secretary",
        "law secretary",
        "legal office administration",
        "法律文秘",
        "法务助理",
        "legal assistant training",
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
            "case description（案例描述）",
            "analysis（分析）",
            "results（结果）",
            "discussion（评析）",
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
        "k1": "法律文书模板须标注版本、模板类型与使用场景",
        "k2": "速录与文字处理测试须报告准确率与速度",
        "k3": "课程评估须声明样本量与统计方法",
    },
    conventions=(
        "法律文书格式遵循党政机关公文格式",
        "速录术语以国家标准术语为准",
        "案号与文号引用遵循 Bluebook R. 10",
        "表格须标行标签与合计栏",
        "档案保管期限以年或永久标注",
    ),
    key_venues=(
        "Journal of Legal Education",
        "Legal Writing",
        "Legal Affairs Quarterly",
        "中国公证",
        "中国秘书科学",
    ),
    units_and_formulas_notes=(
        "打字速度以字/分钟 (wpm) 表示",
        "速录准确率以 % 表示",
        "档案分类号以 A-B 段字母数字组合",
        "文件字号格式为 (年) X 字第 X 号",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "教案与教材", "报告", "数据集"),
    tools=("北大法宝", "vLex", "中国裁判文书网", "威科先行", "法信", "DocuSign", "法大大电子签章", "MS Word", "WPS Office", "Excel", "PowerPoint", "速录软件", "会议记录软件", "庭审系统", "案件管理系统", "律师事务所 OA", "电子卷宗系统", "Qualtrics", "Bluebook 引注插件", "Clio（律所管理软件）"),
    category="法学",
    databases=("OpenAlex", "Crossref", "CNKI", "Westlaw", "LexisNexis", "国家法律法规数据库"),
)
