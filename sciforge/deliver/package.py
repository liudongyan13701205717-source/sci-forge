"""投稿材料一键打包（package）：把论文导出物、研究产物与复现交付物打成 zip，
并自动生成 cover letter 与投稿 checklist。

纯标准库 zipfile；产物落在 projects/{paper_id}/submission_*.zip。
"""

from __future__ import annotations

import json
import time
import zipfile
from pathlib import Path

from sciforge.core import Layout, clean_segment


def _project_files(root: Path) -> list[Path]:
    out = []
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        if "submission_" in rel and rel.endswith(".zip"):
            continue
        out.append(p)
    return out


def _task_files(layout: Layout, task_id: str) -> list[Path]:
    if not task_id:
        return []
    root = layout.task_dir(task_id)
    return [p for p in sorted(root.rglob("*")) if p.is_file()]


def _paper_head(layout: Layout, paper_id: str) -> dict:
    title, abstract = paper_id, ""
    meta = layout.project_dir(paper_id) / "research" / "metadata.json"
    if meta.exists():
        try:
            data = json.loads(meta.read_text(encoding="utf-8"))
            title = data.get("title") or paper_id
            abstract = data.get("abstract") or ""
        except (OSError, ValueError):
            pass
    return {"title": title, "abstract": abstract}


def _cover_letter(info: dict) -> str:
    title = info["title"]
    abstract = info["abstract"]
    return (
        f"# Cover Letter\n\n"
        f"Dear Editor / Program Chairs,\n\n"
        f"We are pleased to submit our manuscript titled「{title}」for your consideration.\n\n"
        "This work makes the following contributions:\n"
        "- 针对资源的系统化建模与求解方案（详见摘要与正文）。\n"
        "- 实验与复现产物完整可查，全部代码、数据与图表均可复现。\n\n"
        f"Abstract: {abstract[:400] or '（见稿件摘要）'}\n\n"
        "We believe the manuscript is within the scope of your venue and has not been "
        "published elsewhere. We look forward to your review.\n\n"
        "Sincerely,\nThe Authors\n"
    )


def _checklist(has_export: list[str]) -> str:
    items = [
        "标题 / 摘要 / 关键词 完整",
        "引言明确研究缺口与贡献",
        "方法章节含建模与求解表述",
        "实验结果含指标与图（可复现）",
        "参考文献格式统一且字段完整",
        "复现代化码 / 数据 / 图表打包齐全",
        "Cover letter 已附",
        "无隐私或未授权数据泄露",
    ]
    lines = [f"- [x] {it}" if it in (
        "复现代化码 / 数据 / 图表打包齐全",
        "Cover letter 已附",
    ) else f"- [ ] {it}" for it in items]
    return "\n".join(["# 投稿前 Checklist", ""] + lines + [
        "",
        f"已打包的导出物：{(', '.join(has_export) or '无')}",
        "说明：`[ ]` 项请作者人工确认后勾选。",
    ])


def package_submission(
    *,
    paper_id: str,
    layout: Layout,
    task_id: str = "",
) -> dict:
    """打包投稿材料；返回 {ok, zip_path, files:[...], cover_letter, checklist}。"""
    seg = clean_segment(paper_id)
    project = layout.projects_dir / seg
    if not project.exists():
        return {"ok": False, "paper_id": paper_id, "error": f"项目 {paper_id} 不存在。"}

    files = _project_files(project)
    if not files:
        return {"ok": False, "paper_id": paper_id, "error": f"项目 {paper_id} 无内容可打包。"}

    info = _paper_head(layout, paper_id)
    cover = _cover_letter(info)
    exported = [
        p.name for p in files
        if p.suffix.lower() in (".pdf", ".docx", ".tex", ".html")
    ]
    chk = _checklist(exported)

    ts = time.strftime("%Y%m%d_%H%M%S")
    zip_path = project / f"submission_{ts}.zip"

    manifest: list[dict] = []
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            arc = "paper/" + p.relative_to(project).as_posix()
            z.write(p, arc)
            manifest.append({"arc": arc, "size": p.stat().st_size})
        z.writestr("cover_letter.md", cover)
        manifest.append({"arc": "cover_letter.md", "size": len(cover.encode("utf-8"))})
        z.writestr("submission_checklist.md", chk)
        manifest.append({"arc": "submission_checklist.md", "size": len(chk.encode("utf-8"))})
        if task_id:
            for p in _task_files(layout, task_id):
                rel = p.relative_to(layout.task_dir(task_id)).as_posix()
                arc = "reproduction/" + rel
                z.write(p, arc)
                manifest.append({"arc": arc, "size": p.stat().st_size})

    return {
        "ok": True,
        "paper_id": paper_id,
        "zip_path": str(zip_path),
        "zip_size": zip_path.stat().st_size,
        "file_count": len(manifest),
        "files": manifest,
        "cover_letter": cover,
        "checklist": chk,
        "note": "如需上传审稿系统，直接使用该 zip；cover letter 与 checklist 已内置。",
    }