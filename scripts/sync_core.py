#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sciforge <-> sciforge-desktop 核心同步脚本（单向投影 + 一致性校验）。

用途
----
把「源仓」sciforge 的核心库逐字节投影到「消费方」sciforge-desktop 的 core/ 下，
并提供不写盘的一致性校验，供本地与 CI 使用。

设计约束（与 docs/architecture/core-sync.md 一致）
--------------------------------------------------
* 方向单一：源仓 -> 消费方。脚本不提供反向同步。
* 逐字节复制：使用 shutil.copy2，比对用 SHA-256，因此投影文件必须与源文件逐字节相同。
* 绝不删除：脚本不含任何删除操作。目标侧多出来的文件只报告、不动。
* 只用标准库：argparse / dataclasses / hashlib / json / pathlib / shutil / sys。
* 不调用 subprocess / os.system，不使用 shutil.rmtree，无递归删除。

模式
----
  --dry-run  （默认）只列出将要发生的差异，不写任何文件。
  --apply         把缺失/不一致的文件复制到目标侧。
  --check         只校验；发现漂移时以非零退出码结束，供 CI 判定。

退出码
------
  0  正常结束。--check 模式下表示不存在「目标缺失」与「内容不一致」。
  1  --check 检出漂移（存在缺失或内容不一致的文件）。
  2  用法或环境错误（路径不存在、清单为空等）。

注意：目标侧多出来的文件（如源侧重命名后遗留的孤儿 .py）按设计只报告、不删除，
因此不计入漂移、也不影响退出码。清理孤儿需人工执行，不能只凭 --check 退出码为 0
就断定目标侧没有多余文件。

本脚本在两个仓库中各存一份，内容完全一致；运行时根据脚本自身位置推断默认路径，
因此同一份文件既能在源仓跑，也能在消费方跑。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

TOOL_NAME = "sync_core.py"
REPORT_SCHEMA = 1

# ---------------------------------------------------------------------------
# 同步清单：源仓包目录 -> 目标仓 core/ 下的相对目录
# ---------------------------------------------------------------------------
# (源包子目录, 目标侧相对目录, 说明)
# 目标侧相对目录为 "" 表示直接落在 core/ 根下（锚点目录 core/）。
#
# 清单只列目录，因此源包根下的散文件（__init__.py / __main__.py / cli.py /
# server.py）天然不在同步范围内 —— 它们是 MCP 形态的传输层入口，由源仓独占。
# 逐目录说明见 docs/architecture/core-sync-mapping.md。
MANIFEST: tuple[tuple[str, str, str], ...] = (
    (
        "core",
        "",
        "锚点目录：布局/Layout/项目记忆与可选 LLM 连接层。投影后直接成为 core/ 本身，"
        "其 __init__.py 将覆盖消费方 core/__init__.py 的占位 stub。",
    ),
    ("claims", "claims", "claim->source 核验、完整性门、Material Passport。"),
    ("deliver", "deliver", "交付物清单与投稿材料打包。"),
    ("disciplines", "disciplines", "学科 registry（2026-09-26 实测 264 个 .py）。"),
    ("export", "export", "Markdown/LaTeX/HTML/DOCX 导出与 PDF 渲染。"),
    ("parse", "parse", "论文 PDF 解析。"),
    ("reproduce", "reproduce", "五步复现闭环：任务、代码生成、沙箱、编排、静态点评。"),
    ("research", "research", "研究线与科研/论文工具集（2026-09-26 实测 29 个 .py）。"),
    ("review", "review", "多视角评审面板与评审准入门。"),
    ("science", "science", "科学数据连接器框架，含 science/sources/。"),
    ("venue", "venue", "期刊/会议模板与匹配度评分。"),
    ("write", "write", "论文文档存储、章节模板与校验。"),
)

# 不参与同步的目录名与后缀（缓存与编译产物）
SKIP_DIR_NAMES = frozenset({"__pycache__"})
SKIP_SUFFIXES = (".pyc", ".pyo", ".orig", ".rej")

# 差异状态
STATUS_IDENTICAL = "identical"
STATUS_MISSING = "missing-in-target"
STATUS_DIFFERS = "content-differs"
STATUS_TARGET_ONLY = "target-only"

# 退出码
EXIT_OK = 0
EXIT_DRIFT = 1
EXIT_USAGE = 2


# ---------------------------------------------------------------------------
# 小工具
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """返回文件内容的 SHA-256 十六进制摘要。分块读取，避免大文件占满内存。"""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(131072), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_skipped(path: Path) -> bool:
    """判断单个路径是否属于缓存/编译产物等不应同步的内容。"""
    if path.name in SKIP_DIR_NAMES or path.name.startswith("."):
        return True
    return path.suffix in SKIP_SUFFIXES


def walk_files(root: Path) -> list[Path]:
    """递归列出 root 下所有应参与同步的文件（已排序，跳过缓存产物）。"""
    found: list[Path] = []
    for path in root.rglob("*"):
        if is_skipped(path):
            continue
        if path.is_file():
            found.append(path)
    return sorted(found, key=lambda p: p.relative_to(root).as_posix())


def default_roots(repo: Path | None = None) -> tuple[Path, Path]:
    """按脚本自身位置推断默认的源根与目标根。

    脚本位于 <repo>/scripts/sync_core.py，因此 <repo> = Path(__file__).parents[1]。
    repo 参数仅供测试注入；省略时按 __file__ 推断。

    * 若 <repo>/sciforge 为目录（源仓的包目录就在仓根下），说明脚本跑在源仓，
      源根 = <repo>/sciforge，目标根 = <repo>/../sciforge-desktop/core。
    * 否则认为脚本跑在消费方仓，源根 = <repo>/../sciforge/sciforge，
      目标根 = <repo>/core。
    """
    if repo is None:
        repo = Path(__file__).resolve().parent.parent
    if (repo / "sciforge").is_dir():
        return repo / "sciforge", repo.parent / "sciforge-desktop" / "core"
    return repo.parent / "sciforge" / "sciforge", repo / "core"


# ---------------------------------------------------------------------------
# 报告数据结构
# ---------------------------------------------------------------------------
@dataclass
class Entry:
    """单个文件的比对结果。"""

    status: str
    target: str  # 相对目标根的 posix 路径
    source: str  # 相对源根的 posix 路径；target-only 时为空串
    source_sha256: str | None = None
    target_sha256: str | None = None
    source_size: int | None = None
    target_size: int | None = None


@dataclass
class ManifestRow:
    """清单中一个目录的落地情况。"""

    source_subdir: str
    target_subdir: str
    note: str
    source_exists: bool
    source_files: int


@dataclass
class Report:
    """完整报告。文本与 JSON 两种输出共用同一份数据。"""

    mode: str
    source_root: str
    target_root: str
    source_root_exists: bool
    target_root_exists: bool
    manifest: list[ManifestRow] = field(default_factory=list)
    entries: list[Entry] = field(default_factory=list)
    written: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def count(self, status: str) -> int:
        return sum(1 for entry in self.entries if entry.status == status)

    @property
    def drift(self) -> bool:
        return self.count(STATUS_MISSING) > 0 or self.count(STATUS_DIFFERS) > 0

    def to_dict(self) -> dict:
        return {
            "schema": REPORT_SCHEMA,
            "tool": TOOL_NAME,
            "mode": self.mode,
            "source_root": self.source_root,
            "target_root": self.target_root,
            "source_root_exists": self.source_root_exists,
            "target_root_exists": self.target_root_exists,
            "summary": {
                "total_source_files": self.count(STATUS_IDENTICAL)
                + self.count(STATUS_MISSING)
                + self.count(STATUS_DIFFERS),
                "identical": self.count(STATUS_IDENTICAL),
                "missing_in_target": self.count(STATUS_MISSING),
                "content_differs": self.count(STATUS_DIFFERS),
                "target_only": self.count(STATUS_TARGET_ONLY),
                "written": len(self.written),
            },
            "drift": self.drift,
            "manifest": [
                {
                    "source_subdir": row.source_subdir,
                    "target_subdir": row.target_subdir,
                    "note": row.note,
                    "source_exists": row.source_exists,
                    "source_files": row.source_files,
                }
                for row in self.manifest
            ],
            "notes": list(self.notes),
            "written": list(self.written),
            "entries": [
                {
                    "status": entry.status,
                    "target": entry.target,
                    "source": entry.source,
                    "source_sha256": entry.source_sha256,
                    "target_sha256": entry.target_sha256,
                    "source_size": entry.source_size,
                    "target_size": entry.target_size,
                }
                for entry in self.entries
            ],
        }


# ---------------------------------------------------------------------------
# 核心流程
# ---------------------------------------------------------------------------
def collect_source(source_root: Path) -> tuple[dict[str, Path], list[ManifestRow]]:
    """按清单收集源侧文件。

    返回 (目标侧相对路径 -> 源文件绝对路径, 清单落地情况)。
    """
    mapping: dict[str, Path] = {}
    rows: list[ManifestRow] = []
    for subdir, target_subdir, note in MANIFEST:
        src_dir = source_root / subdir
        if not src_dir.is_dir():
            rows.append(ManifestRow(subdir, target_subdir, note, False, 0))
            continue
        files = walk_files(src_dir)
        for src_file in files:
            rel_inside = src_file.relative_to(src_dir).as_posix()
            target_rel = f"{target_subdir}/{rel_inside}" if target_subdir else rel_inside
            mapping[target_rel] = src_file
        rows.append(ManifestRow(subdir, target_subdir, note, True, len(files)))
    return mapping, rows


def collect_target(target_root: Path) -> dict[str, Path]:
    """列出目标根下所有已存在的文件，用于识别目标自有文件。"""
    if not target_root.is_dir():
        return {}
    return {
        path.relative_to(target_root).as_posix(): path
        for path in walk_files(target_root)
    }


def compare(source_root: Path, target_root: Path, mode: str) -> Report:
    """逐文件比对源与目标，产出报告；apply 模式下顺带写入差异文件。"""
    report = Report(
        mode=mode,
        source_root=str(source_root),
        target_root=str(target_root),
        source_root_exists=source_root.is_dir(),
        target_root_exists=target_root.is_dir(),
    )

    if not report.source_root_exists:
        report.notes.append(
            f"源根不存在：{source_root}。请用 --source 指定 sciforge 仓的 sciforge/ 包目录。"
        )
        return report

    source_files, manifest_rows = collect_source(source_root)
    report.manifest = manifest_rows

    missing_dirs = [row.source_subdir for row in manifest_rows if not row.source_exists]
    if missing_dirs:
        report.notes.append(
            "清单中以下源目录不存在，已跳过："
            + "、".join(missing_dirs)
            + "。若目录被重命名，请同步更新本脚本的 MANIFEST。"
        )

    if not report.target_root_exists and mode != "apply":
        report.notes.append(
            f"目标根不存在：{target_root}。消费方 core/ 尚未投影，"
            "所有源侧文件都会被判定为「目标缺失」。"
        )

    target_files = collect_target(target_root)

    entries: list[Entry] = []
    for target_rel in sorted(source_files):
        src_file = source_files[target_rel]
        src_hash = sha256_of(src_file)
        dst_file = target_files.get(target_rel)

        if dst_file is None:
            entries.append(
                Entry(
                    status=STATUS_MISSING,
                    target=target_rel,
                    source=src_file.relative_to(source_root).as_posix(),
                    source_sha256=src_hash,
                    source_size=src_file.stat().st_size,
                )
            )
            continue

        dst_hash = sha256_of(dst_file)
        if dst_hash == src_hash:
            entries.append(
                Entry(
                    status=STATUS_IDENTICAL,
                    target=target_rel,
                    source=src_file.relative_to(source_root).as_posix(),
                    source_sha256=src_hash,
                    target_sha256=dst_hash,
                    source_size=src_file.stat().st_size,
                    target_size=dst_file.stat().st_size,
                )
            )
        else:
            entries.append(
                Entry(
                    status=STATUS_DIFFERS,
                    target=target_rel,
                    source=src_file.relative_to(source_root).as_posix(),
                    source_sha256=src_hash,
                    target_sha256=dst_hash,
                    source_size=src_file.stat().st_size,
                    target_size=dst_file.stat().st_size,
                )
            )

    for target_rel in sorted(target_files):
        if target_rel in source_files:
            continue
        dst_file = target_files[target_rel]
        entries.append(
            Entry(
                status=STATUS_TARGET_ONLY,
                target=target_rel,
                source="",
                target_sha256=sha256_of(dst_file),
                target_size=dst_file.stat().st_size,
            )
        )

    report.entries = entries

    if report.count(STATUS_TARGET_ONLY) > 0:
        report.notes.append(
            "目标侧存在源侧没有的文件，已按「消费方自有」处理：只报告，脚本永不删除它们。"
        )

    if mode == "apply" and not report.target_root_exists:
        try:
            target_root.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            report.notes.append(f"无法创建目标根目录：{exc}")
            return report
        report.target_root_exists = True

    if mode == "apply":
        for entry in report.entries:
            if entry.status not in (STATUS_MISSING, STATUS_DIFFERS):
                continue
            src_file = source_root / Path(entry.source)
            dst_file = target_root / Path(entry.target)
            try:
                dst_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, dst_file)
            except OSError as exc:
                report.notes.append(f"写入失败 {entry.target}：{exc}")
                continue
            report.written.append(entry.target)

    return report


# ---------------------------------------------------------------------------
# 输出
# ---------------------------------------------------------------------------
STATUS_LABEL = {
    STATUS_IDENTICAL: "一致",
    STATUS_MISSING: "目标缺失",
    STATUS_DIFFERS: "内容不一致",
    STATUS_TARGET_ONLY: "目标自有",
}


def render_text(report: Report, max_list: int) -> str:
    """渲染人类可读报告。"""
    lines: list[str] = []
    lines.append(f"{TOOL_NAME} — 模式 {report.mode}")
    lines.append(f"  源根:   {report.source_root}"
                 f"  [{'存在' if report.source_root_exists else '不存在'}]")
    lines.append(f"  目标根: {report.target_root}"
                 f"  [{'存在' if report.target_root_exists else '不存在'}]")
    lines.append("")

    lines.append(f"清单（{len(report.manifest)} 项）:")
    for row in report.manifest:
        if row.source_exists:
            mark = "OK"
            detail = f"源 {row.source_files} 文件"
        else:
            mark = "缺失"
            detail = "源目录不存在"
        target_label = f"{row.target_subdir}/" if row.target_subdir else "(core/ 根)"
        lines.append(f"  [{mark:<4}] {row.source_subdir + '/':<14} -> {target_label:<16} {detail}")
    lines.append("")

    summary = report.to_dict()["summary"]
    lines.append("统计:")
    lines.append(f"  源侧文件总数   {summary['total_source_files']}")
    lines.append(f"  一致          {summary['identical']}")
    lines.append(f"  目标缺失      {summary['missing_in_target']}")
    lines.append(f"  内容不一致    {summary['content_differs']}")
    lines.append(f"  目标自有      {summary['target_only']}（只报告，不删除）")
    if report.mode == "apply":
        lines.append(f"  本次已写入    {summary['written']}")
    lines.append("")

    drift_entries = [
        e for e in report.entries if e.status in (STATUS_MISSING, STATUS_DIFFERS)
    ]
    if not drift_entries:
        lines.append("差异: 无（两仓 core 已一致）")
    else:
        shown = drift_entries if max_list <= 0 else drift_entries[:max_list]
        header = f"差异清单（共 {len(drift_entries)} 条"
        header += f"，显示前 {len(shown)} 条）:" if max_list > 0 and len(shown) < len(drift_entries) else " 条）:"
        lines.append(header)
        for entry in shown:
            lines.append(f"  [{STATUS_LABEL[entry.status]}] {entry.target}")
            lines.append(f"      源 {entry.source}  sha256={entry.source_sha256[:16]}…")
            if entry.status == STATUS_DIFFERS:
                lines.append(
                    f"      目标 sha256={entry.target_sha256[:16]}…  "
                    f"源 {entry.source_size}B / 目标 {entry.target_size}B"
                )

    target_only = [e for e in report.entries if e.status == STATUS_TARGET_ONLY]
    if target_only:
        shown = target_only if max_list <= 0 else target_only[:max_list]
        lines.append("")
        suffix = " …" if max_list > 0 and len(shown) < len(target_only) else ""
        lines.append(f"目标自有文件（共 {len(target_only)} 条，显示 {len(shown)} 条）{suffix}:")
        for entry in shown:
            lines.append(f"  [目标自有] {entry.target}")

    if report.notes:
        lines.append("")
        lines.append("说明:")
        for note in report.notes:
            lines.append(f"  - {note}")

    lines.append("")
    if report.mode == "check":
        verdict = "检出漂移，--check 以退出码 1 结束" if report.drift else "未检出漂移，退出码 0"
        lines.append(f"结论: {verdict}")
    elif report.mode == "apply":
        lines.append(f"结论: 已写入 {len(report.written)} 个文件；目标侧多余文件未删除。")
    else:
        lines.append("结论: dry-run，未写任何文件。改用 --apply 落盘，或 --check 取得校验退出码。")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 命令行
# ---------------------------------------------------------------------------
def build_parser(default_source: Path, default_target: Path) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=TOOL_NAME,
        description=(
            "把 sciforge（源仓）的核心库逐字节投影到 sciforge-desktop（消费方）的 core/，"
            "并提供不写盘的一致性校验。单向：源仓 -> 消费方；脚本永不删除目标侧文件。"
        ),
        epilog=(
            "示例：\n"
            "  python scripts/sync_core.py --dry-run          # 预览差异（默认）\n"
            "  python scripts/sync_core.py --apply             # 落盘同步\n"
            "  python scripts/sync_core.py --check             # 校验，有漂移则退出码 1\n"
            "  python scripts/sync_core.py --check --json      # 机器可读输出\n"
            "\n"
            "退出码：0 正常（--check 下表示一致）；1 --check 检出漂移；2 用法/环境错误。"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        dest="mode",
        action="store_const",
        const="dry-run",
        help="只列出差异，不写盘（默认模式）",
    )
    mode.add_argument(
        "--apply",
        dest="mode",
        action="store_const",
        const="apply",
        help="把缺失/不一致的文件复制到目标侧",
    )
    mode.add_argument(
        "--check",
        dest="mode",
        action="store_const",
        const="check",
        help="只校验；发现漂移时以退出码 1 结束（供 CI 使用）",
    )
    parser.set_defaults(mode="dry-run")

    parser.add_argument(
        "--source",
        type=Path,
        default=default_source,
        metavar="DIR",
        help=f"源根，即 sciforge 仓的 sciforge/ 包目录（默认：{default_source}）",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=default_target,
        metavar="DIR",
        help=f"目标根，即消费方的 core/ 目录（默认：{default_target}）",
    )
    parser.add_argument(
        "--json",
        dest="as_json",
        action="store_true",
        help="以 JSON 输出完整报告（不加 --max-list 截断）",
    )
    parser.add_argument(
        "--max-list",
        type=int,
        default=40,
        metavar="N",
        help="文本输出中每类差异最多显示 N 条，0 表示不限制（默认 40）",
    )
    parser.add_argument(
        "--list-manifest",
        action="store_true",
        help="打印同步清单（源目录 -> 目标目录 -> 说明）后退出",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    default_source, default_target = default_roots()
    parser = build_parser(default_source, default_target)
    args = parser.parse_args(argv)

    if args.list_manifest:
        if args.as_json:
            payload = [
                {
                    "source_subdir": sub,
                    "target_subdir": tgt,
                    "note": note,
                }
                for sub, tgt, note in MANIFEST
            ]
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(f"同步清单（{len(MANIFEST)} 项，源根 -> 目标根）：")
            for sub, tgt, note in MANIFEST:
                target_label = f"{tgt}/" if tgt else "(core/ 根)"
                print(f"  {sub + '/':<14} -> {target_label:<16} {note}")
        return EXIT_OK

    if args.max_list < 0:
        parser.error("--max-list 不能为负数；用 0 表示不限制")

    source_root = args.source.expanduser().resolve()
    target_root = args.target.expanduser().resolve()

    if source_root == target_root:
        print("错误：--source 与 --target 指向同一目录。", file=sys.stderr)
        return EXIT_USAGE
    if source_root in target_root.parents:
        print(
            f"错误：目标根 {target_root} 位于源根 {source_root} 内部，"
            "会把投影写回源仓。",
            file=sys.stderr,
        )
        return EXIT_USAGE

    report = compare(source_root, target_root, args.mode)

    if args.as_json:
        print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(render_text(report, args.max_list))

    if not report.source_root_exists:
        return EXIT_USAGE
    if args.mode == "check" and report.drift:
        return EXIT_DRIFT
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
