"""模型连接层（内部使用，不对用户暴露配置）。

读取本地配置 `~/.sci-forge/env`（JSON/KEY=VAL），提供 OpenAI 兼容的
chat.completions 调用。为规避硬依赖，用标准库 urllib 实现；若安装了 openai
包可用其实现（可选）。

配置读取优先级：环境变量 > 本地配置文件。
配置文件示例（~/.sci-forge/env）：
    CLAWSGO_SELF_LLM_BASE=http://localhost:11434/v1
    CLAWSGO_SELF_LLM_MODEL=qwen2.5:7b
    CLAWSGO_SELF_LLM_KEY=optional
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path

_HOME_ENV = Path.home() / ".sci-forge" / "env"

DEFAULT_SYSTEM = "你是一个严谨的科研工程助手。"


def _env_path() -> Path:
    p = os.environ.get("CLAWSGO_SELF_ENV_FILE")
    return Path(p) if p else _HOME_ENV


def load_env_file() -> dict:
    """读取本地 env 文件（不存在则返回空）。绝不打印 key。"""
    p = _env_path()
    if not p.exists():
        return {}
    try:
        text = p.read_text(encoding="utf-8")
    except OSError:
        return {}
    data: dict = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        data[k.strip()] = v.strip()
    return data


def configured() -> bool:
    """是否有可用的 LLM 端点。"""
    return bool(_base_url())


def _base_url() -> str | None:
    return (
        os.environ.get("CLAWSGO_SELF_LLM_BASE")
        or load_env_file().get("CLAWSGO_SELF_LLM_BASE")
    )


def _api_key() -> str | None:
    return (
        os.environ.get("CLAWSGO_SELF_LLM_KEY")
        or load_env_file().get("CLAWSGO_SELF_LLM_KEY")
    )


def _model() -> str:
    return (
        os.environ.get("CLAWSGO_SELF_LLM_MODEL")
        or load_env_file().get("CLAWSGO_SELF_LLM_MODEL")
        or "gpt-4o-mini"
    )


def _chat_urllib(messages: list[dict], *, temperature: float, max_tokens: int) -> str:
    base = _base_url().rstrip("/")
    url = base + "/chat/completions"
    payload = {
        "model": _model(),
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    key = _api_key()
    if key:
        req.add_header("Authorization", f"Bearer {key}")
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"LLM HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:500]}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"LLM 连接失败：{e.reason}") from e
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as e:
        raise RuntimeError(f"LLM 响应异常：{data}") from e


def chat(
    prompt: str,
    *,
    system: str = DEFAULT_SYSTEM,
    temperature: float = 0.4,
    max_tokens: int = 3000,
) -> str:
    """调用内部 LLM 完成一次对话。未配置时抛 RuntimeError。"""
    if not configured():
        raise RuntimeError(
            "未配置 LLM：请在 ~/.sci-forge/env 设置 CLAWSGO_SELF_LLM_BASE(=端点) "
            "与 CLAWSGO_SELF_LLM_MODEL。"
        )
    messages = [{"role": "system", "content": system}]
    messages.append({"role": "user", "content": prompt})
    return _chat_urllib(messages, temperature=temperature, max_tokens=max_tokens)
