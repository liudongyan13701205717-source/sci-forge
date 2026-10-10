"""网页设计学科论文支持：UI/UX 设计、前端开发与可访问性工程的体裁与规范。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="web_design",
    aliases=("web_design", "网页设计", "Web设计", "前端设计", "UI/UX设计",
             "web design", "UI design", "UX design", "user interface design",
             "web development", "user experience"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与研究问题）",
            "literature review（文献综述）",
            "methods（方法，含可用性测试设计）",
            "results（结果）",
            "discussion（讨论）",
            "design implications（设计启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "design brief（设计需求）",
            "design process（设计流程）",
            "implementation（实现）",
            "usability evaluation（可用性评估）",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "design paradigms（设计范式综述）",
            "tools and frameworks（工具与框架综述）",
            "accessibility standards（可访问性标准综述）",
            "future directions",
            "references",
        ),
    },
    citation_style="IEEE",
    reporting_standards={
        "usability_testing": "可用性测试须说明任务设计、参与者数量、评价指标（任务完成率、时间、SUS 评分等）",
        "accessibility": "可访问性评估须标注 WCAG 版本与合规等级（A、AA 或 AAA）",
        "performance": "性能指标须包含加载时间、CLS（累积布局偏移）、LCP（最大内容绘制）、INP（交互到下一帧延迟）等 Core Web Vitals",
    },
    conventions=(
        "HTML/CSS/JavaScript 代码遵循 WCAG 2.1 AA 级可访问性标准",
        "颜色对比度 ≥ 4.5:1（正文）或 3:1（大文本，≥18pt 或 14pt 加粗）",
        "响应式设计断点按 12 列网格系统定义，标注最小/最大宽度",
        "图片 alt 属性须完整且描述性，装饰性图片设置 alt=\"\"",
        "代码注释遵循 JSDoc 或 TSDoc 标准",
    ),
    key_venues=(
        "CHI (Conference on Human Factors in Computing Systems)",
        "International Journal of Human-Computer Studies",
        "WICOM (Web and Consumer Media)",
        "International Journal of Web Design",
        "IEEE Transactions on Professional Communication",
    ),
    units_and_formulas_notes=(
        "响应式设计断点：px 或 rem",
        "字体大小：px 或 pt",
        "颜色以 HEX 或 RGB 标注",
        "加载时间以 ms 或 s 为单位",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Figma", "Sketch", "Adobe XD", "Visual Studio Code", "Webflow", "WordPress", "Bootstrap", "Tailwind CSS", "Lighthouse", "Chrome DevTools", "Git", "Storybook", "Vite", "Webpack", "Zeplin", "Contentful", "Sanity", "Python", "LaTeX", "Adobe Photoshop"),
    category="工学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
