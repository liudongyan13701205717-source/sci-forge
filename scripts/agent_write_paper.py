"""方案 A 固化脚本：初始化一个"由 agent 直接成文"的论文项目脚手架。

背景：SciForge不配置任何 LLM API key。论文正文由 agent（opencode
等）直接用当前对话模型写入项目章节文件，再调用 export_document 导出 PDF/LaTeX。
本脚本负责：
  1) 按 DocStore 的 SECTION_ORDER 创建空章节文件（占位，避免 export 报"无章节"）；
  2) 输出一份"成文清单"（chapter checklist）供 agent 依序填充；
  3) 在项目根生成 WRITING_PROTOCOL.md，记录无 key 成文的契约。

用法：
    python scripts/agent_write_paper.py <paper_id> [--topic "研究方向"]

成文流程（agent 遵循）：
    1. 运行本脚本生成脚手架。
    2. 对每个章节调用 MCP 工具 write_section(paper_id, section, prompt, format)
       —— prompt 中写明"由 agent 用当前模型写出完整正文，不留占位"。
    3. 全部写完后再调用 export_document(paper_id, "pdf") 导出。
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sciforge.core import get_layout
from sciforge.write.doc import DocStore

_SECTION_ORDER = DocStore.SECTION_ORDER

_HEADINGS = {
    "abstract": "摘要（200-300 字：问题/方法/结果/结论）",
    "introduction": "引言（动机、现状、贡献三点、结构）",
    "problem": "研究问题（形式化定义与设定）",
    "assumptions": "假设与前提",
    "notation": "符号说明（表）",
    "modeling": "建模（公式与环境）",
    "solution": "求解（方法/算法/复杂度）",
    "results": "结果与分析（实验设置、表格、曲线、消融）",
    "references": "参考文献（规范引用）",
    "appendix": "附录（可选项）",
}

_PROTOCOL = """# 无 Key 成文协议（方案 A：agent 直接成文）

SciForge**不配置**任何 LLM API key。论文正文由 agent 用当前对话模型
直接写入项目章节，再由 sciforge 本地工具导出。

## 步骤
1. 运行 `python scripts/agent_write_paper.py <paper_id>` 生成脚手架。
2. 对每个章节调用 MCP 工具 `write_section`，prompt 需明确"写出完整正文，不留占位"。
3. 全部章节完成后调用 `export_document` 导出 PDF/LaTeX。

## 配套科研工具（同样免 key / 模板优先，可 LLM 增强）
- ideate_paper：选题构思与缺口分析
- research_plan：完整研究计划书
- literature_review：文献综述（OpenAlex 免 key 检索）
- auto_title_abstract：标题/摘要/关键词提炼
- venue_suggest：投稿/期刊匹配
- peer_review：模拟同行评审
- paper_polish：润色/一致性/完整性检查
- inject_results / research_verdict：复现结果并入论文与决策
"""


def main() -> int:
    ap = argparse.ArgumentParser(description="初始化 agent 成文项目脚手架")
    ap.add_argument("paper_id", help="论文/项目标识")
    ap.add_argument("--topic", default="", help="研究方向（写入清单说明）")
    args = ap.parse_args()

    layout = get_layout()
    doc = DocStore(layout, args.paper_id)
    root = layout.project_dir(args.paper_id)

    # 1) 创建空章节占位，保证 export 可识别结构
    created = []
    for sec in _SECTION_ORDER:
        p = doc.section_path(sec)
        if not p.exists():
            p.write_text(f"（{_HEADINGS[sec]}）\n", encoding="utf-8")
            created.append(sec)

    # 重建 doc.md（含空章节）
    doc.rebuild_doc()

    # 2) 成文清单（供 agent 依序填充）
    checklist = []
    for i, sec in enumerate(_SECTION_ORDER, 1):
        checklist.append(f"{i}. {_HEADINGS[sec]}  →  write_section(paper_id='{args.paper_id}', section='{sec}', ...)")
    checklist_txt = "\n".join(checklist)

    # 3) 写协议
    (root / "WRITING_PROTOCOL.md").write_text(_PROTOCOL, encoding="utf-8")

    print("=" * 60)
    print(f"项目脚手架已初始化：{root}")
    print(f"章节占位：{len(created)} 个已创建；doc.md 已重建。")
    print(f"protocol: {root / 'WRITING_PROTOCOL.md'}")
    print("=" * 60)
    print("成文清单（agent 依序填充，每章写完整正文，勿留占位）：")
    print(checklist_txt)
    print("-" * 60)
    print(f"topic: {args.topic or '（未指定，可取 write_section 各章 prompt 自行落实）'}")
    print("完成后调用：export_document(paper_id=%r, target='pdf')" % args.paper_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
