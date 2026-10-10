"""计算机视觉与多媒体计算学科论文支持：多媒体系统/编解码/计算摄影体裁。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="computer_vision_and_multimedia_computation",
    aliases=(
        "computer vision and multimedia computation",
        "计算机视觉与多媒体计算", "多媒体计算", "multimedia computation",
        "multimedia systems", "多媒体系统", "多媒体信息处理",
        "multimedia information processing", "计算摄影", "computational photography",
        "视频编码", "video coding",
    ),
    paper_types={
        "research": (
            "abstract",
            "introduction（背景、动机与问题）",
            "related work",
            "method（方法）",
            "experiments（实验）",
            "conclusion",
            "references",
        ),
        "benchmark": (
            "abstract",
            "introduction",
            "dataset/protocol",
            "metrics",
            "results",
            "references",
        ),
        "survey": (
            "abstract",
            "introduction",
            "historical overview",
            "taxonomy",
            "open problems",
            "references",
        ),
    },
    citation_style="IEEE 样式（期刊）或 ACM 样式（会议）",
    reporting_standards={
        "experimental": "实验须报告硬件/软件环境与样本量",
        "benchmark": "基准测试须包含数据集来源、划分与复现脚本",
        "video_metrics": "视频质量评估须给出客观（PSNR/SSIM/VMAF）与主观（MOS）双口径",
    },
    conventions=(
        "视频分辨率用 帧宽×帧高@帧率fps 统一表示",
        "编码码率用 bpp 或 kbps 并标注参考帧",
        "评估指标定义须与标准（ITU-R BT.PQ、VMAF 等）对齐",
        "模型/参数规模须报告，超参须给出",
    ),
    key_venues=(
        "IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)",
        "IEEE Transactions on Multimedia",
        "ACM Multimedia (MM)",
        "IEEE Transactions on Image Processing",
        "Journal of Visual Communication and Image Representation",
        "IEEE International Conference on Image Processing (ICIP)",
        "International Conference on Computational Photography (ICCP)",
    ),
    units_and_formulas_notes=(
        "码率用 kbps/bps 与 bpp；延迟用 ms；分辨率用 px",
        "公式用 amsmath；显示公式仅在被引用时编号",
        "数值结果给出均值 ± 标准差；显著性检验须报告 p 值",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "艺术作品", "软件与代码", "专利", "教案与教材", "报告", "数据集"),
    tools=("FFmpeg", "x265", "x264", "AV1 / libaom", "MediaPipe", "Open3D", "Blender", "Unreal Engine", "Unity", "GStreamer", "OpenCV", "PyTorch", "TensorFlow", "PIL (Pillow)", "ImageMagick", "ExifTool", "VMAF", "Dolby Vision", "DaVinci Resolve", "MediaInfo"),
    category="工学",
    databases=("OpenAlex", "Crossref", "IEEE Xplore", "arXiv"),
)
