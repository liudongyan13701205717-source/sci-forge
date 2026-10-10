"""装帧/装订艺术学科论文支持：书籍装帧设计/工艺体裁、艺术学引用样式与装帧记法注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="bookbinding",
    aliases=(
        "bookbinding",
        "Bookbinding",
        "装帧设计",
        "书籍装帧",
        "装订术",
        "装帧艺术",
        "装帧工艺",
        "书籍艺术",
        "book design",
        "book arts",
        "书籍装帧设计",
        "装订工艺",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction",
            "materials and methods（工艺描述与材料分析）",
            "results（结构、视觉或耐久性测试）",
            "discussion",
            "references",
        ),
        "design": (
            "abstract",
            "design brief",
            "structure and binding technique",
            "materials and cover",
            "typography and layout",
            "appendices（样张与图纸）",
            "references",
        ),
        "conservation": (
            "abstract",
            "condition assessment",
            "treatment plan",
            "materials analysis",
            "results",
            "references",
        ),
    },
    citation_style="艺术史（Art Bulletin）样式（作者-年份，Chicago Manual of Style 第 17 版）",
    reporting_standards={
        "materials": "书籍材料（纸张、皮革、线、胶水）须明确",
        "process": "装帧工艺流程须完整描述",
        "dimensions": "开本、书脊、厚度须以 mm 报告",
        "typography": "字体、字号、字距须完整列出",
    },
    conventions=(
        "开本规格用 ISO 216 或传统开本（32 开、16 开、大 16 开）",
        "字体用字体名称首次出现处给出（如 Garamond, 12pt）",
        "装帧类型用术语（平装、精装、线装、蝴蝶装、锁线装）",
        "工艺用中文术语（如锁线、烫金、压凹、UV）",
        "书脊宽度 = 页数 × 单页厚度",
    ),
    key_venues=(
        "Book Design Quarterly",
        "Papers of the Bibliographic Society of America",
        "Print Quarterly",
        "Journal of Paper Conservation",
        "BookHistory",
        "Archives and Manuscripts: Records of Culture",
        "International Journal of Design",
    ),
    units_and_formulas_notes=(
        "开本规格用 ISO 216（A4、A5 等）或传统开本",
        "厚度用 mm 或 pt 报告",
        "字体用 pt 表示字号",
        "纸张克重以 g/m² 报告",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "教案与教材", "报告", "数据集"),
    tools=("Adobe InDesign", "Adobe Illustrator", "Adobe Photoshop", "QuarkXPress", "Affinity Publisher", "Serif Affinity Designer", "Procreate", "Sketchbook Pro", "Cricut Maker", "Die Cutter", "Foil Stamping Press", "Embossing Press", "Bone Folder", "Awl", "Bookbinding Punch", "Bookbinding Sewing Machine", "Book Press", "Letterpress Printer", "Hot Foil Transfer Press", "Bookbinding Needle"),
    category="艺术学",
    databases=("OpenAlex", "Google Scholar", "Bibliographic Society", "Library of Congress", "JSTOR"),
)
