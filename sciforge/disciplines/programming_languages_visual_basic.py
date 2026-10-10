"""Visual Basic 程序设计学科论文支持：桌面/办公自动化体裁、工具链版本披露与工程案例注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="programming_languages_visual_basic",
    aliases=(
        "programming_languages_visual_basic",
        "Visual Basic",
        "VB",
        "VBA",
        "VB.NET",
        "可视化编程",
        "事件驱动编程",
        "窗体编程",
        "Office 自动化",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与应用场景）",
            "methodology（开发方法）",
            "results（功能与性能结果）",
            "discussion（适用性与迁移）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（应用案例描述）",
            "analysis（设计与实现分析）",
            "results（运行与维护结果）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（VB 生态综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="ACM 样式（作者-年份）",
    reporting_standards={
        "application": "应用研究遵循软件工程案例报告规范",
        "case_study": "案例研究遵循 DSR-CASE 报告规范",
        "benchmark": "性能基准遵循标准基准报告规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
        "reproducibility": "可复现性须说明版本与运行环境",
    },
    conventions=(
        "须注明 VB 版本与环境（VB6/Classic、VB.NET、VBA）",
        "VB.NET 与 VB6 的语义差异须在文中区分",
        "事件驱动与模块依赖须图示说明",
        "ADO/ODBC/Winsock 等组件调用须注明依赖版本",
        "测试与兼容性问题须讨论",
    ),
    key_venues=(
        "Journal of Spreadsheet Modeling and Analysis",
        "Journal of Business Venturing",
        "Communications of the ACM",
        "IEEE Software",
        "ACM SIGSOFT Software Notes",
    ),
    units_and_formulas_notes=(
        "运行时间以毫秒计，采样次数须注明",
        "界面布局以像素或控件坐标描述",
        "公式用 amsmath；度量定义式须明确",
        "版本号须完整（如 .NET Framework 4.7.2）",
        "字符串与数组索引从 0 起，边界须检查",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "译文", "报告", "数据集"),
    tools=("Visual Studio", "VB.NET", "VB6", "VBA", "ADO", "ODBC", "MS Access", "Crystal Reports", "Winsock", "WinForms", "WPF", "MSTest", "NUnit", "TestComplete", "AutoIt", "Spy++", "WinDbg", "Reflexil", "IL Merge", "SlickEdit"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
