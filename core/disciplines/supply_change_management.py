"""Supply change management 学科论文支持：供应链变更/需求预测/采购管理。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="supply_change_management",
    aliases=(
        "supply_change_management", "Supply change management",
        "供应变更管理", "供应链变更管理", "采购变更管理",
        "需求变更管理",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景与变更问题）",
            "methods（变更识别与处理方法）",
            "results（变更效率与成本数据）",
            "discussion（讨论与管理启示）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（企业/行业案例）",
            "analysis（变更原因与影响）",
            "results（变更成效）",
            "discussion",
            "references",
        ),
        "review": (
            "abstract",
            "introduction",
            "theoretical overview（理论综述）",
            "evidence synthesis（证据综合）",
            "future directions",
            "references",
        ),
    },
    citation_style="APA 7（作者-年份；括号式）",
    reporting_standards={
        "demand_forecast": "需求预测须报告模型、数据周期与预测精度（MAPE/RMSE）",
        "change_tracking": "变更追踪须报告变更类型、频次、影响范围与处理时限",
        "supplier_management": "供应商管理须报告评价指标体系与权重确定方法",
        "cost_analysis": "成本分析须注明计价单位与统计口径",
    },
    conventions=(
        "供应链层级（Tier 1/2/3）须注明",
        "变更类型（计划/非计划）须分类统计",
        "响应时间与交付周期须报告",
        "成本数据须注明币种与年份",
        "供应商分类须按重要度与绩效分层",
    ),
    key_venues=(
        "Journal of Operations Management",
        "International Journal of Production Economics",
        "Supply Chain Management: An International Journal",
        "生产计划与控制",
        "管理学报",
    ),
    units_and_formulas_notes=(
        "库存用 件或 万元；补货周期用 天",
        "变更处理时间用 h 或 天",
        "预测误差用 MAPE（%）或 RMSE",
        "成本用 万元/月；利润率用 %",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "教案与教材", "报告", "数据集"),
    tools=("SAP Ariba（采购变更管理）", "SAP SCM（供应链变更管理）", "Oracle SCM Cloud（供应链云平台）", "Coupa BSM（商业供应链管理系统）", "Jira Service Management（变更事件管理）", "ServiceNow Change Management（IT 变更管理）", "Microsoft Azure DevOps（变更流水线）", "Confluence（变更文档协作）", "SAP S/4HANA（ERP 供应链模块）", "Blue Yonder WMS（仓储管理系统）", "Manhattan Associates TMS（运输管理系统）", "Kinaxis RBP（需求变更响应）", "Oracle NetSuite ERP（供应链变更）", "Infor M3（制造与供应链）", "Siemens Opcenter（制造执行与变更）", "Planful（需求计划与预测）", "Supply Chain Guru（供应链可视化）", "Crayon（竞品变化追踪）", "Power BI（供应链分析报表）", "Tableau（供应链可视化）"),
    category="管理学",
    databases=("OpenAlex", "Crossref", "CNKI"),
)
