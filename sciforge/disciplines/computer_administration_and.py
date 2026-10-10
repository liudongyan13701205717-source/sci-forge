"""计算机管理与信息化服务学科论文支持：基础设施管理/运维/SRE 体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_administration_and",
    aliases=("computer administration", "计算机管理", "计算机与信息管理",
             "IT management", "信息化服务", "信息系统管理", "IT administration",
             "computer management", "计算机服务管理"),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work",
            "method（管理框架/方法/工具）",
            "case study or evaluation",
            "results",
            "conclusion",
            "references",
        ),
        "system_paper": (
            "abstract",
            "introduction",
            "background and motivation",
            "design and implementation",
            "deployment and evaluation",
            "lessons learned",
            "conclusion",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "scope and method",
            "taxonomy",
            "case studies",
            "gaps and outlook",
            "references",
        ),
    },
    citation_style="IEEE 编号样式（IT 期刊/会议常用）",
    reporting_standards={
        "experimental": "实验报告须给出管理规模、部署环境、KPI 与对照基线",
        "case_study": "案例研究需说明组织背景、样本量、观察周期与干预内容",
        "reproducibility": "脚本与配置文件（Ansible/Terraform/Helm）须公开",
        "measurement": "观测指标（延迟、CPU、内存、SLO）须说明采样窗口",
        "ethics": "涉及用户数据的运维须声明数据脱敏与合规",
    },
    conventions=(
        "管理对象规模（服务器数/用户数/租户数）须在方法中显式声明",
        "自动化脚本给出版本号与变更记录，配置以 IaC 表达（Terraform/Ansible）",
        "KPI/SLI/SLO 定义须明确，指标口径统一",
        "运维流程以架构图与拓扑图给出，含关键路径标注",
        "结论须区分管理改进与业务收益，避免混淆因果",
    ),
    key_venues=(
        "USENIX ATC",
        "ACM ICSE-SEIP",
        "IEEE Cloud Computing",
        "IEEE Communications Magazine",
        "IEEE Network",
        "ACM Computing Surveys",
    ),
    units_and_formulas_notes=(
        "响应时间/延迟用 ms；吞吐用 req/s 或 GB/s；利用率以 % 表示",
        "可用性以小数（99.9%）与年度维护窗口（分钟/年）同时给出",
        "资源规模以 CPU 核数、内存 GB、存储 TB 描述",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("Ansible", "Terraform", "Puppet", "Chef", "SaltStack", "Docker", "Kubernetes", "Prometheus", "Grafana", "Nagios", "Zabbix", "Packer", "HashiCorp Vault", "Jenkins", "GitLab CI", "ArgoCD", "Ansible Tower", "CloudWatch", "Splunk", "Elasticsearch", "Kibana", "PagerDuty", "OpenTelemetry", "Linux", "PowerShell", "Bash"),
    category="工学",
    databases=("arXiv", "OpenAlex", "Crossref"),
)
