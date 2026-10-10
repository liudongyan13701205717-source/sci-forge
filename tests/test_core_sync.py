"""core/ 投影同步脚本的行为测试：默认目标解析 + 双向一致性。

覆盖 2026-10-06 事故：default_roots() 的源仓判定多写了一层
（repo/sciforge/sciforge），导致脚本把源仓误判为消费方仓，
不带 --target 时静默同步到源仓自己的 core/ 镜像，
而真正的桌面仓 core/ 长期收不到更新。
"""

from __future__ import annotations

import importlib.util
import json
import shutil
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync_core.py"


def _load(script_path: Path):
    """从指定路径加载 sync_core.py（需注册 sys.modules，否则 dataclass 解析失败）。"""
    spec = importlib.util.spec_from_file_location("sync_core_under_test", script_path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _build_source_repo(root: Path) -> Path:
    """搭建最小源仓布局：scripts/ + sciforge/<pkg> + 自己的 core/ 镜像。"""
    repo = root / "sciforge"
    (repo / "scripts").mkdir(parents=True)
    (repo / "sciforge" / "disciplines").mkdir(parents=True)
    (repo / "sciforge" / "disciplines" / "a.py").write_text("X = 1\n", encoding="utf-8")
    (repo / "sciforge" / "disciplines" / "b.py").write_text("X = 2\n", encoding="utf-8")
    (repo / "core" / "disciplines").mkdir(parents=True)
    (repo / "core" / "disciplines" / "a.py").write_text("X = 1\n", encoding="utf-8")
    return repo


def _build_desktop_repo(root: Path, stale: bool = True) -> Path:
    desktop = root / "sciforge-desktop"
    (desktop / "core" / "disciplines").mkdir(parents=True)
    (desktop / "core" / "disciplines" / "a.py").write_text(
        "STALE\n" if stale else "X = 1\n", encoding="utf-8"
    )
    return desktop


# ---------- 默认根解析 ----------

def test_default_roots_detects_source_repo(tmp_path):
    mod = _load(SCRIPT)
    repo = tmp_path / "sciforge"
    (repo / "sciforge" / "disciplines").mkdir(parents=True)

    source, target = mod.default_roots(repo=repo)

    assert source == repo / "sciforge"
    assert target == tmp_path / "sciforge-desktop" / "core"


def test_default_roots_detects_consumer_repo(tmp_path):
    mod = _load(SCRIPT)
    repo = tmp_path / "sciforge-desktop"
    repo.mkdir()

    source, target = mod.default_roots(repo=repo)

    assert source == tmp_path / "sciforge" / "sciforge"
    assert target == repo / "core"


# ---------- 关键回归：源仓布局下默认必须打到桌面仓 ----------

def test_main_defaults_to_desktop_repo_not_local_mirror(tmp_path, monkeypatch):
    """源仓布局 + 不带 --target：目标必须是桌面仓 core/，不是源仓自己的 core/。"""
    src_repo = _build_source_repo(tmp_path)
    desktop = _build_desktop_repo(tmp_path)
    shutil.copy(SCRIPT, src_repo / "scripts" / "sync_core.py")

    mod = _load(src_repo / "scripts" / "sync_core.py")
    seen: dict[str, Path] = {}
    real_compare = mod.compare

    def spy(source_root, target_root, mode):
        seen["source"], seen["target"] = source_root, target_root
        return real_compare(source_root, target_root, mode)

    monkeypatch.setattr(mod, "compare", spy)
    monkeypatch.chdir(src_repo)

    rc = mod.main(["--check", "--json"])

    assert seen["source"] == src_repo / "sciforge"
    assert seen["target"] == desktop / "core"
    assert seen["target"] != src_repo / "core"
    assert rc == mod.EXIT_DRIFT


def test_apply_roundtrip_reaches_desktop_repo(tmp_path, monkeypatch):
    """--apply 后桌面仓内容真正更新，且 --check 归零。"""
    src_repo = _build_source_repo(tmp_path)
    desktop = _build_desktop_repo(tmp_path, stale=True)
    shutil.copy(SCRIPT, src_repo / "scripts" / "sync_core.py")

    mod = _load(src_repo / "scripts" / "sync_core.py")
    monkeypatch.chdir(src_repo)

    assert mod.main(["--apply", "--json"]) == mod.EXIT_OK
    assert (desktop / "core" / "disciplines" / "a.py").read_text(encoding="utf-8") == "X = 1\n"
    assert (desktop / "core" / "disciplines" / "b.py").exists()
    assert mod.main(["--check", "--json"]) == mod.EXIT_OK


def test_target_only_orphans_do_not_affect_exit_code(tmp_path, monkeypatch, capsys):
    """孤儿只报告、不计漂移：--check 退出码为 0，但 summary.target_only 为 1。

    这正是 2026-10-06 的陷阱：源侧重命名后桌面仓遗留 1051/1052 孤儿，
    内容同步好后 --check 仍返回 0，不能据此断定目标侧没有多余文件。
    """
    src_repo = _build_source_repo(tmp_path)
    desktop = _build_desktop_repo(tmp_path, stale=False)
    (desktop / "core" / "disciplines" / "b.py").write_text("X = 2\n", encoding="utf-8")
    (desktop / "core" / "disciplines" / "1051.py").write_text(
        "DISCIPLINE = None\n", encoding="utf-8"
    )
    shutil.copy(SCRIPT, src_repo / "scripts" / "sync_core.py")

    mod = _load(src_repo / "scripts" / "sync_core.py")
    monkeypatch.chdir(src_repo)

    rc = mod.main(["--check", "--json"])
    payload = json.loads(capsys.readouterr().out)

    assert payload["summary"]["target_only"] == 1
    assert payload["summary"]["missing_in_target"] == 0
    assert payload["summary"]["content_differs"] == 0
    assert payload["drift"] is False
    assert rc == mod.EXIT_OK
    orphans = [
        e["target"] for e in payload["entries"] if e["status"] == mod.STATUS_TARGET_ONLY
    ]
    assert orphans == ["disciplines/1051.py"]
