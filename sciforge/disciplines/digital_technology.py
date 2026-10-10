"""数字技术学科论文支持：数字出版、数字媒体与交互技术体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="digital_technology",
    aliases=(
        "digital_technology", "数字技术", "数字技术",
        "digital publishing", "数字出版",
        "digital media", "数字媒体",
        "digital interaction design", "数字交互设计",
        "digital transformation", "数字化转型",
        "web development", "网页开发",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（技术问题与背景）",
            "methodology（系统设计、实现与测试）",
            "results（性能评估与用户反馈）",
            "discussion（技术改进与展望）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "project description（项目描述）",
            "implementation（实现过程）",
            "results（效果评估）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "technology comparison（技术对比）",
            "current landscape（当前格局）",
            "future trends",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "implementation": "技术栈须明确（语言、框架、版本）",
        "testing": "测试方案须注明测试类型与环境",
        "performance": "性能指标须定义（加载时间、吞吐量、错误率）",
        "ethics": "用户数据须声明隐私保护与合规性",
    },
    conventions=(
        "代码遵循项目编码规范（如 PEP 8、Google Style Guide）",
        "版本控制遵循 Git 工作流",
        "API 文档遵循 OpenAPI/Swagger 规范",
        "测试结果须注明测试覆盖率",
        "性能数据须注明测试环境（硬件、浏览器、网络）",
    ),
    key_venues=(
        "IEEE Transactions on Visualization and Computer Graphics",
        "ACM Transactions on Computer-Human Interaction",
        "International Journal of Human-Computer Studies",
        "CHI Conference Proceedings",
        "IEEE Transactions on Human-Computer Interaction",
        "Journal of Web Semantics",
    ),
    units_and_formulas_notes=(
        "加载时间用 ms 表示",
        "文件大小用 MB 表示",
        "分辨率用 px 表示",
        "帧率用 FPS 表示",
        "测试覆盖率用 % 表示",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Git", "GitHub", "Visual Studio Code", "Sublime Text", "Atom", "Eclipse", "PyCharm", "IntelliJ IDEA", "Android Studio", "Xcode", "Unity", "Unreal Engine", "Blender", "Cinema 4D", "Maya", "Adobe Creative Suite", "Figma", "Sketch", "InVision", "Axure RP"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref", "IEEE Xplore", "ACM Digital Library"),
)
