"""语音学学科论文支持：声学语音学/发音语音学/实验语音学体裁、IPA/APA 引用样式与语音学注记。"""

from __future__ import annotations

from sciforge.disciplines.base import Discipline

DISCIPLINE = Discipline(
    name="phonetics",
    aliases=("phonetics", "语音学", "声学语音学", "发音语音学",
             "experimental phonetics", "语音学实验", "声学分析",
             "语流音变", "音位声学", "speech analysis"),
    paper_types={
        "research": (
            "abstract",
            "introduction（研究问题与背景）",
            "methodology（实验设计与方法）",
            "results（声学分析结果）",
            "discussion（讨论）",
            "references",
        ),
        "case_study": (
            "abstract",
            "introduction",
            "case description（案例描述）",
            "analysis（语音分析）",
            "results（发现）",
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
    citation_style="APA 或 Linguistic Society of America (LSA) 样式",
    reporting_standards={
        "experiment": "实验遵循 ARRIVE/SAFELANG 规范",
        "audio": "音频采集遵循 ELRA/ELDC 规范",
        "transcription": "语音转写遵循 IPA/PHOINICS 规范",
        "corpus": "语料库遵循 ELRA/ELDC 规范",
        "acoustic": "声学分析遵循 SAFELANG 规范",
        "systematic_review": "系统综述遵循 PRISMA 声明",
    },
    conventions=(
        "国际音标（IPA）须用 Unicode 规范",
        "声学参数（F0、F1-F4、时长）须规范",
        "波形与频谱图须给出参数",
        "语料库来源与授权须注明",
        "采样率与位深须注明",
    ),
    key_venues=(
        "Journal of Phonetics",
        "Phonetics and Phonemic Analysis",
        "Laboratory Phonology",
        "Journal of Acoustic Phonetics",
        "Applied Linguistics",
        "Journal of the Acoustical Society of America",
    ),
    units_and_formulas_notes=(
        "频率用 Hz；时长用 ms",
        "采样率（44.1 kHz）与位深（16-bit）须注明",
        "波形与频谱图须给出参数",
        "声学分析遵循 SAFELANG 规范",
        "语料库来源与授权须注明",
    ),
    paper_capable=True,
    contribution_forms=("论文", "学术专著", "文学作品", "教案与教材", "译文", "报告", "数据集"),
    tools=("Praat 语音分析", "Adobe Audition 音频编辑", "Sonic Visualiser 频谱分析", "Audacity 音频处理", "Wavesurfer 波形与音素标注", "x-ray 成像（电子舌）", "语音 MRI 成像", "CHILDES 儿童语言语料库", "TalkBank 语言语料库", "L2-ARCTIC 语料库", "Speech Corpora for Chinese", "SIL Palenq ue IPA 输入", "IPAFont Unicode IPA", "Resampler 重采样", "Resonance Analyzer 共振峰分析", "eSpeak 语音合成", "Google Speech-to-Text 转写", "Python Praat 包", "MFA（Montreal Forced Aligner）", "ELAN 多模态标注"),
    category="文学",
    databases=("OpenAlex", "Crossref", "CNKI", "ELRA", "ELDC"),
)
