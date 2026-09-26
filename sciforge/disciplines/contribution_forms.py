"""产出形式分类法：学科可产出的成果类型常量。

供 Discipline.contribution_forms 字段取值（可多值组合），也供
registry 的 list_by_contribution_form() 过滤使用。常量值为中文
可读标签，便于直接进入提示词与文档。

注意：本模块会被 registry 的 _discover() 扫描（不以 _ 开头），
但 _coerce() 对非 Discipline 值返回 None，因此字符串常量不会
污染 DISCIPLINES 注册表。
"""

from __future__ import annotations

PAPER = "论文"
ACADEMIC_MONOGRAPH = "学术专著"
LITERARY_WORK = "文学作品"
ARTWORK = "艺术作品"
SOFTWARE_AND_CODE = "软件与代码"
PATENT = "专利"
TEACHING_MATERIAL = "教案与教材"
TRANSLATION = "译文"
REPORT = "报告"
DATASET = "数据集"

CONTRIBUTION_FORMS: tuple[str, ...] = (
    PAPER,
    ACADEMIC_MONOGRAPH,
    LITERARY_WORK,
    ARTWORK,
    SOFTWARE_AND_CODE,
    PATENT,
    TEACHING_MATERIAL,
    TRANSLATION,
    REPORT,
    DATASET,
)