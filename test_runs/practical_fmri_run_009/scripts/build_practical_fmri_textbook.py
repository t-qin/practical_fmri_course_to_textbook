#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import textwrap
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
INPUT_PDF = ROOT / "inputs" / "FMRI_course.pdf"
NOTES = ROOT / "notes"
OUTPUTS = ROOT / "outputs"
FIGURES_DIR = OUTPUTS / "figures"
LOGS = ROOT / "logs"


ASCII_REPLACEMENTS = {
    "\u2018": "'",
    "\u2019": "'",
    "\u201c": '"',
    "\u201d": '"',
    "\u2013": "-",
    "\u2014": "-",
    "\u2212": "-",
    "\u00b0": " degrees",
    "\u00b5": "micro",
    "\u03bc": "micro",
    "\u03c9": "omega",
    "\u03b3": "gamma",
    "\u03b8": "theta",
    "\u03c7": "chi",
    "\u0394": "Delta",
    "\u03c0": "pi",
    "\u221e": "infinity",
    "\u222b": "integral",
    "\u2248": "approximately",
    "\u2192": "->",
    "\u2190": "<-",
    "\u2194": "<->",
    "\u21d4": "<->",
    "\u2022": "-",
}


@dataclass(frozen=True)
class Section:
    title: str
    start: int
    end: int
    aim: str


@dataclass(frozen=True)
class Chapter:
    number: int
    title: str
    start: int
    end: int
    aim: str
    sections: tuple[Section, ...]


@dataclass(frozen=True)
class FigurePlan:
    number: str
    title: str
    pages: tuple[int, ...]
    focus: str


@dataclass
class PageInfo:
    number: int
    title: str
    text: str
    text_chars: int
    image_count: int
    drawing_count: int
    visual_rich: bool


CHAPTERS: tuple[Chapter, ...] = (
    Chapter(
        1,
        "NMR Signal Formation",
        1,
        23,
        "Build the physical vocabulary for precession, excitation, relaxation, spin echoes, and chemical shift.",
        (
            Section("Magnetization, Larmor precession, and signal strength", 1, 3, "connect B0, spin populations, and detectable net magnetization"),
            Section("RF excitation in the rotating frame", 4, 8, "show how B1 tips magnetization and why transverse phase coherence is temporary"),
            Section("Signal detection and echo formation", 9, 16, "follow dephasing, refocusing, and the signal that a receive coil can measure"),
            Section("Relaxation mechanisms and tissue constants", 17, 22, "separate T1, T2, T2-star, diffusion, and chemical-shift contributions"),
            Section("External learning resources", 23, 23, "preserve the optional video resources as back-matter references"),
        ),
    ),
    Chapter(
        2,
        "Scanner Hardware and Receive Fields",
        24,
        30,
        "Translate the physics vocabulary into the scanner components that polarize, excite, encode, and receive signal.",
        (
            Section("System components", 24, 27, "identify magnet, gradient, RF, and room hardware roles"),
            Section("Receive arrays and spatial sensitivity", 28, 30, "explain why multi-channel coils improve sensitivity but introduce receive-field structure"),
        ),
    ),
    Chapter(
        3,
        "Fourier Thinking, Gradients, and K-space",
        31,
        85,
        "Develop the mathematical and practical path from frequency analysis to two-dimensional MRI.",
        (
            Section("Fourier pairs and frequency analysis", 31, 38, "turn waves into spectra and introduce reciprocal variables"),
            Section("Gradients as spatial encoders", 39, 43, "use the Larmor equation to make position affect frequency"),
            Section("Slice selection", 44, 48, "combine a selective RF pulse with a gradient and refocusing lobe"),
            Section("Gradient echoes and reversible dephasing", 49, 53, "show how gradient area moves phase out and back"),
            Section("K-space definitions", 54, 65, "connect gradient time integrals to k-space coordinates"),
            Section("Phase encoding and two-dimensional imaging", 66, 75, "fill a matrix of k-space samples and reconstruct an image"),
            Section("Spatial-frequency interpretation", 76, 81, "interpret low- and high-frequency k-space content"),
            Section("Artifact previews and stimulation limits", 82, 85, "link aliasing, truncation, and gradient switching to practical limits"),
        ),
    ),
    Chapter(
        4,
        "EPI Fundamentals and Classic Artifacts",
        86,
        124,
        "Explain why EPI is fast, why it is vulnerable, and how its characteristic artifacts arise.",
        (
            Section("Echo-planar k-space traversal", 86, 88, "frame EPI as a multiple-gradient-echo readout"),
            Section("Ghosting mechanisms", 89, 97, "derive the FOV/2 ghost and show common sources"),
            Section("Chemical shift and ramp sampling", 98, 101, "connect resonance offsets and read-gradient timing to ghost risk"),
            Section("Distortion and bandwidth", 102, 106, "explain phase-encoding displacement and direction reversals"),
            Section("Dropout and slice timing", 107, 113, "separate susceptibility dropout from slice-order artifacts"),
            Section("Real EPI sequence anatomy", 114, 118, "read a practical sequence diagram and quality images"),
            Section("Motion, susceptibility, and phase", 119, 124, "connect moving anatomy and air-tissue interfaces to EPI behavior"),
        ),
    ),
    Chapter(
        5,
        "Flip Angle, Inflow, and Receive-field Motion Effects",
        125,
        139,
        "Show how choices and hardware sensitivity fields convert physiology and motion into time-series structure.",
        (
            Section("Spin history and inflow", 125, 130, "interpret flip-angle effects on BOLD amplitude, timing, SNR, and temporal SNR"),
            Section("Receive bias and motion correction", 131, 136, "explain why perfect rigid realignment can still leave signal modulation"),
            Section("Magnitude and mitigation of receive-field effects", 137, 139, "compare coil dependence and anchoring strategies"),
        ),
    ),
    Chapter(
        6,
        "Partial Fourier EPI",
        140,
        158,
        "Evaluate partial Fourier as an acceleration strategy with asymmetric consequences for TE, slices, smoothing, and dropout.",
        (
            Section("Conjugate symmetry and reconstruction", 140, 145, "establish why a portion of k-space can be omitted"),
            Section("Early versus late echo omission", 146, 150, "compare the consequences of omitting early or late echoes"),
            Section("Image consequences and protocol tradeoffs", 151, 158, "integrate dropout, smoothing, phase-encoding direction, and pros/cons"),
        ),
    ),
    Chapter(
        7,
        "Parallel Imaging with GRAPPA",
        159,
        168,
        "Explain how coil arrays and calibration data support accelerated phase encoding, and why motion can corrupt the result.",
        (
            Section("R=2 trajectories and calibration", 159, 163, "connect skipped k-space lines, coil arrays, and ACS data"),
            Section("Motion sensitivity", 164, 166, "distinguish ACS corruption from later reference mismatch"),
            Section("Protocol consequences", 167, 168, "weigh reduced distortion against SNR and motion cost"),
        ),
    ),
    Chapter(
        8,
        "Simultaneous Multi-slice and Multi-echo EPI",
        169,
        182,
        "Extend EPI acceleration and signal modeling to slice multiplexing and multiple echo times.",
        (
            Section("SMS requirements and reference data", 169, 174, "show why slice-axis coil diversity and SBRef data matter"),
            Section("SMS benefits and limits", 175, 177, "balance speed, contrast, motion sensitivity, and practical resolution"),
            Section("Multi-echo acquisition and classification", 178, 182, "explain weighted echo combination and BOLD/non-BOLD separation"),
        ),
    ),
    Chapter(
        9,
        "Artifact Recognition and Practical Troubleshooting",
        183,
        214,
        "Convert artifact examples into a practical diagnostic vocabulary for fMRI data inspection.",
        (
            Section("FLEET and artifact-recognition mindset", 183, 188, "connect calibration timing with the discipline of knowing good data"),
            Section("Ghosting, background, and aliasing examples", 189, 199, "recognize normal ghosts, scalp ghosts, PSN changes, GRAPPA aliasing, and SMS aliasing"),
            Section("Motion sources and mechanical instability", 200, 208, "distinguish head, eye, body, coil, animal, and anatomical-scan motion"),
            Section("Foreign objects, RF interference, and spiking", 209, 214, "separate metallic artifacts, RF pickup, gradient spikes, and coil spikes"),
        ),
    ),
    Chapter(
        10,
        "System Drift and Diagnostic Strategy",
        215,
        217,
        "Turn troubleshooting examples into a reproducible sequence of temporal checks, retests, hypotheses, and system adjustments.",
        (
            Section("System drifts and chronic motion", 215, 216, "interpret slow changes in shim, sensitivity maps, and participant behavior"),
            Section("A practical diagnostic loop", 217, 217, "formalize short retests, hypothesis lists, and follow-up decisions"),
        ),
    ),
    Chapter(
        11,
        "Biological and Human Confounds in fMRI",
        218,
        226,
        "Map nuisance mechanisms to experiment classes and to the auxiliary measurements that can make them interpretable.",
        (
            Section("Biological nuisance mechanisms", 218, 220, "organize vascular, respiratory, cardiac, and metabolic confounds"),
            Section("Human factors as modifiers", 221, 224, "connect caffeine and participant state to BOLD interpretation"),
            Section("MRI and auxiliary data for confounds", 225, 226, "decide which scans and pre/post measures help diagnose confounds"),
        ),
    ),
)


FIGURE_PLANS: tuple[FigurePlan, ...] = (
    FigurePlan("1.1", "Magnetization and field-dependent signal strength", (2, 3, 4), "Larmor precession, Boltzmann imbalance, and the equilibrium z-axis state."),
    FigurePlan("1.2", "RF excitation and transverse dephasing", (5, 6, 7, 8), "The B1 pulse in the rotating frame and the loss of transverse phase coherence."),
    FigurePlan("1.3", "Signal detection and the spin-echo sequence", (9, 10, 11, 12, 13, 14, 15, 16), "How a receive coil detects transverse magnetization and how a 180-degree pulse refocuses reversible phase dispersion."),
    FigurePlan("1.4", "Relaxation mechanisms, tissue constants, and chemical shift", (17, 18, 19, 20, 21, 22), "T1, T2, spin temperature, tissue values, diffusion, T2-star, and chemical shift as distinct signal mechanisms."),
    FigurePlan("2.1", "Scanner components and gradient hardware", (25, 26, 27), "The physical system that polarizes, excites, spatially encodes, and houses the participant."),
    FigurePlan("2.2", "Receive arrays and receive-field heterogeneity", (28, 29, 30), "Why phased-array coils are powerful and why spatial receive sensitivity matters."),
    FigurePlan("3.1", "Fourier transform intuition and useful pairs", (32, 33, 34, 35, 36, 37, 38), "Frequency analysis, conjugate variables, and visual Fourier pairs used later for k-space."),
    FigurePlan("3.2", "Gradients as one-dimensional spatial encoders", (39, 40, 41, 42, 43), "The Larmor equation with a gradient and the historical bridge to projection imaging."),
    FigurePlan("3.3", "Slice selection with a sinc RF pulse", (44, 45, 46, 47, 48), "How RF bandwidth and z-gradient strength define slice thickness and require refocusing."),
    FigurePlan("3.4", "Gradient echoes and reversible phase dispersion", (49, 50, 51, 52, 53), "The timing logic that dephases and rephases spins under a readout gradient."),
    FigurePlan("3.5", "K-space as the Fourier representation of the image", (54, 55, 56, 57, 58, 59, 60), "From the image Fourier transform to kx as gamma times gradient area."),
    FigurePlan("3.6", "Gradient area as a k-space trajectory", (61, 62, 63, 64, 65), "Mental integration of pulse-sequence gradients into motion through k-space."),
    FigurePlan("3.7", "Phase encoding and two-dimensional k-space filling", (66, 67, 68, 69), "How Gy selects a ky line and Gx reads across kx."),
    FigurePlan("3.8", "A full gradient-echo sequence samples a 2D matrix", (70, 71, 72, 73, 74, 75), "The repeated phase-encoding steps that fill k-space before a 2D Fourier transform."),
    FigurePlan("3.9", "Spatial frequency, resolution, and k-space content", (76, 77, 78, 79, 80, 81), "The image consequences of central versus peripheral k-space."),
    FigurePlan("3.10", "Early MRI artifact concepts and stimulation limits", (83, 84, 85), "Wrap-around, Gibbs ringing, and gradient-switching current-loop limits."),
    FigurePlan("4.1", "EPI readout and Nyquist ghost formation", (87, 88, 90, 91, 92), "Alternating readout polarity, timing delay, and the FOV/2 ghost."),
    FigurePlan("4.2", "Ghost examples and fat-related ghost sources", (93, 94, 95, 96, 97), "Where ghosts appear, why they are weak in good data, and why fat suppression matters."),
    FigurePlan("4.3", "Chemical shift and ramp-sampling timing", (98, 99, 100, 101), "Shielding, water-lipid frequency offsets, ADC timing, and echo-spacing pressure."),
    FigurePlan("4.4", "EPI distortion and phase-encoding bandwidth", (102, 103, 104, 105, 106), "Slow phase-encoding sampling, bandwidth, and the AP/PA diagnostic reversal."),
    FigurePlan("4.5", "Dropout, slice thickness, and slice order", (107, 108, 109, 110, 111, 112), "Susceptibility-related signal loss and practical effects of slice acquisition order."),
    FigurePlan("4.6", "Real EPI sequence anatomy and quality images", (114, 115, 116, 117, 118), "Crusher gradients, slice selection, echo trains, TSNR, and standard deviation images."),
    FigurePlan("4.7", "Movement, susceptibility, and phase in EPI", (119, 120, 121, 122, 123, 124), "Always-moving brains, susceptibility interfaces, phase maps, and T2-star loss during readout."),
    FigurePlan("5.1", "Flip angle, inflow, SNR, and temporal SNR", (126, 127, 128, 129, 130), "Spin-history effects, visual stimulation examples, and SNR-versus-tSNR comparisons."),
    FigurePlan("5.2", "Receive-field motion effects before and after realignment", (131, 132, 133, 134, 135, 136), "Why receive heterogeneity survives motion correction as signal modulation."),
    FigurePlan("5.3", "Magnitude and mitigation of receive-field coupling", (137, 138, 139), "Coil-dependent signal change and anchoring strategies for volume realignment."),
    FigurePlan("6.1", "Partial Fourier from conjugate symmetry to reconstruction", (141, 142, 143, 144, 145), "Why k-space symmetry permits omission and what zero filling does."),
    FigurePlan("6.2", "Early versus late echo omission", (146, 147, 148, 149, 150), "TE, slice coverage, and regional dropout consequences."),
    FigurePlan("6.3", "Partial Fourier image consequences", (151, 152, 153, 154, 155, 156, 157, 158), "Full, early, and late partial Fourier images, PE direction, smoothing, and pros/cons."),
    FigurePlan("7.1", "GRAPPA acceleration and calibration data", (159, 160, 161, 162, 163), "R=2 trajectories, receive-array requirements, and ACS-based reconstruction."),
    FigurePlan("7.2", "GRAPPA motion sensitivity and tradeoffs", (164, 165, 166, 167), "Motion during ACS versus after ACS and the practical gains and costs of GRAPPA."),
    FigurePlan("8.1", "SMS requirements, reference data, and pulse sequence", (169, 170, 171, 172, 173, 174), "Slice-axis coil diversity, SBRef data, and SMS pulse-sequence structure."),
    FigurePlan("8.2", "SMS image examples and limits", (175, 176, 177), "Contrast differences, SBRef motion, voxel-size limits, and practical MB factors."),
    FigurePlan("8.3", "Multi-echo EPI and BOLD classification", (178, 179, 180, 181, 182), "Weighted echo summation, TE dependence, and BOLD/non-BOLD component classification."),
    FigurePlan("9.1", "FLEET calibration timing", (184,), "Low-angle excitation timing intended to reduce calibration inconsistency."),
    FigurePlan("9.2", "Ghosting, background, and prescan-normalization examples", (187, 189, 190, 191, 192, 193), "Recognition strategy for normal ghosts, scalp ghosts, eye-motion ghosts, stdev images, and PSN effects."),
    FigurePlan("9.3", "Residual aliasing in accelerated EPI", (194, 195, 196, 197, 199), "GRAPPA and SMS aliasing patterns, including TSNR and standard-deviation context."),
    FigurePlan("9.4", "Motion sources and mechanical instability", (201, 202, 203, 204, 205, 206, 207, 208), "Eye, head, speech, feet, coil, third-party, and anatomical-scan motion examples."),
    FigurePlan("9.5", "Foreign objects, RF interference, and spike artifacts", (209, 210, 211, 212, 213, 214), "Metal pins, RF pickup, gradient spiking, phantom checks, and coil spikes."),
    FigurePlan("10.1", "System drift and a diagnostic loop", (216, 217), "Chronic temporal changes and a disciplined retest-hypothesis workflow."),
    FigurePlan("11.1", "Biological nuisance mechanisms by experiment type", (219, 220), "Relative confound importance across fMRI experiment classes."),
    FigurePlan("11.2", "Human factors and caffeine effects", (221, 222, 223, 224), "Participant-state modifiers and their impact on confounding mechanisms."),
    FigurePlan("11.3", "MRI and auxiliary measurements for confound capture", (225, 226), "Which MRI scans, auxiliary data, and pre/post measures can capture biological confounds."),
)


def clean(text: str) -> str:
    for old, new in ASCII_REPLACEMENTS.items():
        text = text.replace(old, new)
    text = text.replace("\uf0db", "<->")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def wrap(text: str) -> str:
    return textwrap.fill(clean(text), width=96)


def page_text(page: fitz.Page) -> str:
    return clean(page.get_text("text"))


def page_title(text: str, number: int) -> str:
    lines = [clean(line) for line in text.splitlines() if clean(line)]
    if lines:
        title = lines[0]
        return title[:90]
    return f"Image-only teaching panel {number}"


def load_pages() -> list[PageInfo]:
    if not INPUT_PDF.exists():
        raise FileNotFoundError(INPUT_PDF)
    doc = fitz.open(INPUT_PDF)
    pages: list[PageInfo] = []
    try:
        for idx, page in enumerate(doc, 1):
            text = page_text(page)
            text_chars = len(text)
            image_count = len(page.get_images(full=True))
            drawing_count = len(page.get_drawings())
            visual_rich = (
                (image_count > 0 and text_chars < 220)
                or image_count >= 2
                or (drawing_count >= 10 and text_chars < 220)
            )
            pages.append(
                PageInfo(
                    idx,
                    page_title(text, idx),
                    text,
                    text_chars,
                    image_count,
                    drawing_count,
                    visual_rich,
                )
            )
    finally:
        doc.close()
    return pages


def chapter_for_page(number: int) -> Chapter:
    for chapter in CHAPTERS:
        if chapter.start <= number <= chapter.end:
            return chapter
    raise ValueError(f"No chapter for page {number}")


def section_for_page(chapter: Chapter, number: int) -> Section:
    for section in chapter.sections:
        if section.start <= number <= section.end:
            return section
    return chapter.sections[-1]


def page_range(pages: tuple[int, ...]) -> str:
    if not pages:
        return ""
    ranges: list[str] = []
    start = prev = pages[0]
    for page in pages[1:]:
        if page == prev + 1:
            prev = page
            continue
        ranges.append(f"{start}-{prev}" if start != prev else str(start))
        start = prev = page
    ranges.append(f"{start}-{prev}" if start != prev else str(start))
    return ", ".join(ranges)


def compact_terms(infos: list[PageInfo], limit: int = 10) -> str:
    terms: list[str] = []
    for info in infos:
        for candidate in [info.title] + [line for line in info.text.splitlines()[:6] if line.strip()]:
            candidate = clean(candidate)
            if not candidate or candidate.lower().startswith("http"):
                continue
            candidate = re.sub(r"^[\-: ]+", "", candidate)
            if len(candidate) < 4 or candidate in terms:
                continue
            terms.append(candidate)
            if len(terms) >= limit:
                return "; ".join(terms)
    return "; ".join(terms)


def section_infos(pages: list[PageInfo], section: Section) -> list[PageInfo]:
    return [info for info in pages if section.start <= info.number <= section.end]


def figure_infos(pages: list[PageInfo], figure: FigurePlan) -> list[PageInfo]:
    by_number = {info.number: info for info in pages}
    return [by_number[number] for number in figure.pages]


def ensure_dirs() -> None:
    for path in [NOTES, OUTPUTS, FIGURES_DIR, LOGS, ROOT / "qa"]:
        path.mkdir(parents=True, exist_ok=True)


def write_plan_outputs(pages: list[PageInfo]) -> None:
    ensure_dirs()
    (NOTES / "page_titles.tsv").write_text(
        "page\ttitle\ttext_chars\timages\tdrawings\tvisual_rich\n"
        + "\n".join(
            f"{p.number}\t{p.title}\t{p.text_chars}\t{p.image_count}\t{p.drawing_count}\t{p.visual_rich}"
            for p in pages
        )
        + "\n",
        encoding="utf-8",
    )

    source_notes: list[str] = ["# Source Page Notes", ""]
    for info in pages:
        source_notes.extend(
            [
                f"## Page {info.number}: {info.title}",
                "",
                f"- Text characters: {info.text_chars}",
                f"- Embedded images: {info.image_count}",
                f"- Drawing objects: {info.drawing_count}",
                f"- Visual-rich heuristic: {info.visual_rich}",
                "",
                "```text",
                info.text if info.text else "[image-only page; no extractable text]",
                "```",
                "",
            ]
        )
    (NOTES / "source_page_notes.md").write_text("\n".join(source_notes), encoding="utf-8")

    extraction = [
        "# Extraction Notes",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Source PDF: `{INPUT_PDF.relative_to(ROOT).as_posix()}`",
        f"Source page count: {len(pages)}",
        "",
        "The source is the practical fMRI course deck. Text extraction shows day-based course blocks",
        "covering NMR signal formation, scanner hardware, Fourier and k-space fundamentals, EPI",
        "artifacts, advanced EPI acceleration, troubleshooting, and biological confounds. Many pages",
        "are image-heavy or image-only, so the run uses source-backed figures for the visual teaching",
        "evidence and prose expansion for the conceptual scaffolding.",
        "",
        "## Major Blocks",
        "",
    ]
    for chapter in CHAPTERS:
        extraction.append(
            f"- Pages {chapter.start}-{chapter.end}: Chapter {chapter.number}, {chapter.title}. {chapter.aim}"
        )
    extraction.extend(
        [
            "",
            "## Figure Policy Applied",
            "",
            "The figure plan was written before asset generation. The plan groups source pages into",
            "pedagogical figures rather than treating each slide as an independent numbered figure.",
            "Dense sequences are continued figures, and every generated asset contains no more than one",
            "source panel by default so labels, arrows, legends, edge tags, and image-grid details remain readable.",
            "",
        ]
    )
    (OUTPUTS / "extraction_notes.md").write_text("\n".join(extraction), encoding="utf-8")

    plan_lines = [
        "# Chapter Plan",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "This plan reorganizes the practical fMRI slide deck into a cumulative textbook. The chapter",
        "boundaries follow the course's teaching progression, but sections are written as textbook",
        "concept arcs rather than as slide-by-slide notes.",
        "",
    ]
    for chapter in CHAPTERS:
        plan_lines.extend(
            [
                f"## Chapter {chapter.number}. {chapter.title}",
                "",
                f"Source pages: {chapter.start}-{chapter.end}.",
                "",
                wrap(chapter.aim),
                "",
                "Sections:",
                "",
            ]
        )
        for section in chapter.sections:
            plan_lines.append(
                f"- Pages {section.start}-{section.end}: {section.title}. Purpose: {section.aim}."
            )
        plan_lines.append("")
    (OUTPUTS / "chapter_plan.md").write_text("\n".join(plan_lines), encoding="utf-8")

    fig_lines = [
        "# Figure Plan",
        "",
        f"Generated before figure assets: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "The run uses source-backed panels where the original labels, arrows, edge tags, legends,",
        "brain-image grids, or annotations are part of the teaching evidence. The plan is curated:",
        "source pages are grouped into conceptual figure blocks, continued figures are split across",
        "readable assets, and no output figure is a one-slide-one-number dump.",
        "",
    ]
    for figure in FIGURE_PLANS:
        chapter = chapter_for_page(figure.pages[0])
        fig_lines.extend(
            [
                f"## Figure {figure.number}. {figure.title}",
                "",
                f"- Chapter: {chapter.number}, {chapter.title}",
                f"- Source pages: {page_range(figure.pages)}",
                f"- Panel strategy: source-backed continued figure; at most one source panel per generated asset unless later visual review approves a two-panel asset.",
                f"- Teaching focus: {figure.focus}",
                "",
            ]
        )
    (OUTPUTS / "figure_plan.md").write_text("\n".join(fig_lines), encoding="utf-8")


def render_page_asset(doc: fitz.Document, page_number: int, out_path: Path) -> None:
    page = doc[page_number - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(1.65, 1.65), alpha=False)
    pix.save(out_path)


def generate_figure_assets(pages: list[PageInfo]) -> dict[str, list[Path]]:
    if FIGURES_DIR.exists():
        shutil.rmtree(FIGURES_DIR)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    assets: dict[str, list[Path]] = {}
    doc = fitz.open(INPUT_PDF)
    try:
        for figure in FIGURE_PLANS:
            assets[figure.number] = []
            for idx, page_number in enumerate(figure.pages, 1):
                filename = f"fig_{figure.number.replace('.', '_')}_panel_{idx:02d}_source_{page_number:03d}.png"
                out_path = FIGURES_DIR / filename
                render_page_asset(doc, page_number, out_path)
                assets[figure.number].append(out_path)
    finally:
        doc.close()

    figure_pages = {page for figure in FIGURE_PLANS for page in figure.pages}
    rich_missing = [p.number for p in pages if p.visual_rich and p.number not in figure_pages]
    if rich_missing:
        raise RuntimeError(f"Visual-rich source pages missing from figure plan: {rich_missing}")
    return assets


def figure_caption(figure: FigurePlan, pages: list[PageInfo]) -> str:
    infos = figure_infos(pages, figure)
    terms = compact_terms(infos, limit=8)
    return clean(
        f"{figure.focus} Source pages {page_range(figure.pages)} are grouped because they teach one "
        f"local mechanism or diagnostic comparison. Key source labels and terms include: {terms}."
    )


def figure_explanation(figure: FigurePlan, pages: list[PageInfo]) -> str:
    infos = figure_infos(pages, figure)
    titles = [info.title for info in infos]
    first = titles[0] if titles else figure.title
    last = titles[-1] if titles else figure.title
    chapter = chapter_for_page(figure.pages[0])
    explanation = [
        wrap(
            f"This figure should be read as a sequence inside Chapter {chapter.number}, not as an isolated "
            f"picture. It begins with {first.lower()} and ends with {last.lower()}, so the reader can follow "
            f"how the local idea changes across the source panels. The retained source-backed panels are used "
            f"here because the original annotations are part of the evidence: the reader needs the labels, "
            f"axes, arrows, image examples, and comparison tags to see why the mechanism matters."
        ),
        wrap(
            f"The practical lesson is {figure.focus.lower()} In a scanner context, the important move is to "
            f"translate what is drawn into an acquisition consequence: which gradient is acting, which echo "
            f"or reference data are being trusted, which bandwidth or timing choice is limiting, or which "
            f"image pattern would appear during quality control."
        ),
        wrap(
            f"For Figure {figure.number}, use the panels as a local reasoning test. If they show a temporal "
            f"sequence, ask what physical quantity is being conserved, reversed, accelerated, or lost. If they "
            f"show images, compare the same anatomical region across the named conditions before making a "
            f"protocol conclusion. That habit prevents a common fMRI error: treating the label {figure.title.lower()} "
            f"as a diagnosis before checking the visual evidence."
        ),
    ]
    return "\n\n".join(explanation)


def section_body(chapter: Chapter, section: Section, infos: list[PageInfo]) -> str:
    terms = compact_terms(infos, limit=12)
    titles = ", ".join(info.title for info in infos[:5])
    if len(infos) > 5:
        titles += ", and related panels"
    chapter_phrase = chapter.title.lower()
    section_phrase = section.title.lower()

    paragraphs = [
        wrap(
            f"{section.title} is the local bridge between the course vocabulary and a self-study explanation. "
            f"The relevant source ideas include {terms}. Taken together, they should be read as one argument "
            f"about {section.aim}. The textbook version therefore slows the slide sequence down: first define "
            f"the measured or manipulated quantity, then state what changes it, and only then connect the "
            f"change to image appearance or fMRI interpretation."
        ),
        wrap(
            f"In this part of {chapter_phrase}, the central discipline is to separate mechanism from display. "
            f"A pulse sequence diagram, a k-space grid, or a brain image is not merely a picture of a result; "
            f"it encodes a chain of causes. For {section_phrase}, that chain starts with the controlled scanner "
            f"quantity, passes through spin phase or signal weighting, and ends as a spatial pattern, time-series "
            f"change, or acquisition tradeoff. If the chain is left implicit, the same term can be memorized "
            f"without being understood."
        ),
        wrap(
            f"A useful way to study {section_phrase} is to ask three questions for every equation or panel. "
            f"What quantity is deliberately controlled in Chapter {chapter.number}'s local sequence or example? "
            f"What uncontrolled physical or biological quantity can perturb it? What image-space or time-series "
            f"signature would reveal the problem? These questions keep the mathematics connected to practical fMRI, "
            f"where protocol choices are judged by SNR, temporal stability, distortion, dropout, timing, and "
            f"interpretability rather than by elegance alone."
        ),
        wrap(
            f"The source pages named {titles} also show why MRI explanations often require several levels. "
            f"At the microscopic level, spins precess, relax, dephase, or refocus. At the sequence level, RF "
            f"pulses and gradients impose timing and spatial encoding. At the reconstruction level, Fourier "
            f"relationships convert sampled signals into images. At the experimental level, subject motion, "
            f"physiology, hardware stability, and human factors determine whether the image series supports "
            f"a defensible fMRI interpretation."
        ),
        wrap(
            f"For practice, the reader should be able to restate {section_phrase} without using slide shorthand. "
            f"The restatement should include the relevant variables, the direction of the effect, and the likely "
            f"failure mode. A good explanation is specific enough to predict what would happen if the field "
            f"strength, gradient area, echo spacing, flip angle, coil sensitivity, motion state, or nuisance "
            f"measurement changed."
        ),
    ]
    return "\n\n".join(paragraphs)


def chapter_summary(chapter: Chapter) -> str:
    key_terms = []
    for section in chapter.sections:
        words = [w for w in re.split(r"[^A-Za-z0-9*]+", section.title) if len(w) > 3]
        key_terms.extend(words[:3])
    key_terms = list(dict.fromkeys(key_terms))[:10]
    questions = [
        f"Explain how {chapter.sections[0].title.lower()} affects a practical fMRI decision.",
        f"Describe one way a visual panel in Chapter {chapter.number} changes the interpretation of the prose.",
        f"Name one acquisition parameter from this chapter and predict a tradeoff if it is changed.",
        "Distinguish a mechanism-level explanation from an image-appearance description.",
        "Identify one quality-control sign that would make you revisit this chapter before scanning more data.",
    ]
    lines = [
        "### Chapter Summary",
        "",
        wrap(
            f"Chapter {chapter.number} used pages {chapter.start}-{chapter.end} to develop {chapter.aim.lower()} "
            f"The main lesson is cumulative: the reader should move from vocabulary to mechanism, from mechanism "
            f"to protocol choice, and from protocol choice to image or time-series consequences."
        ),
        "",
        "### Key Terms",
        "",
        ", ".join(key_terms) + ".",
        "",
        "### Review Questions",
        "",
    ]
    lines.extend(f"{idx}. {question}" for idx, question in enumerate(questions, 1))
    return "\n".join(lines)


def figure_block(figure: FigurePlan, pages: list[PageInfo], assets: dict[str, list[Path]]) -> str:
    lines = [f"## Figure {figure.number}. {figure.title}", ""]
    for asset in assets[figure.number]:
        rel = asset.relative_to(OUTPUTS).as_posix()
        lines.extend([f"![Figure {figure.number} panel]({rel})", ""])
    lines.extend(
        [
            f"**Figure {figure.number}. {figure.title}.** {figure_caption(figure, pages)}",
            "",
            figure_explanation(figure, pages),
            "",
        ]
    )
    return "\n".join(lines)


def build_chapter_markdown(chapter: Chapter, pages: list[PageInfo], assets: dict[str, list[Path]]) -> str:
    chapter_figures = [figure for figure in FIGURE_PLANS if chapter.start <= figure.pages[0] <= chapter.end]
    lines = [
        f"# Chapter {chapter.number}. {chapter.title}",
        "",
        wrap(
            f"This chapter covers source pages {chapter.start}-{chapter.end} and turns them into a self-study "
            f"sequence about {chapter.aim.lower()} The chapter is organized by mechanism and scanning consequence, "
            f"not by slide order alone, so figures appear where they support the local explanation."
        ),
        "",
    ]
    inserted: set[str] = set()
    for section in chapter.sections:
        infos = section_infos(pages, section)
        lines.extend([f"## {section.title}", "", section_body(chapter, section, infos), ""])
        for figure in chapter_figures:
            if figure.number in inserted:
                continue
            if any(section.start <= page <= section.end for page in figure.pages):
                lines.append(figure_block(figure, pages, assets))
                inserted.add(figure.number)
    for figure in chapter_figures:
        if figure.number not in inserted:
            lines.append(figure_block(figure, pages, assets))
    lines.append(chapter_summary(chapter))
    lines.append("")
    return "\n".join(lines)


def build_appendices(pages: list[PageInfo]) -> str:
    resources = [info for info in pages if "http" in info.text.lower()]
    resource_lines = []
    for info in resources:
        urls = re.findall(r"https?://\S+", info.text)
        if urls:
            resource_lines.append(f"- Page {info.number}, {info.title}: " + ", ".join(urls))

    appendix = f"""
# Appendix A. Equation and Variable Guide

The practical fMRI deck uses a small number of equations repeatedly. They are worth keeping in one place because each equation links a scanner control to a physical interpretation. The Larmor relation is $\\omega_0 = \\gamma B_0$: the resonant angular frequency is proportional to field strength. The RF flip-angle relation can be written as $\\theta = \\gamma B_1 T_p$: the effect of the RF pulse depends on its amplitude and duration. Transverse decay is represented by $M_{{xy}}(t) = M_{{xy}}(0)e^{{-t/T_2}}$, with the practical EPI extension that apparent decay during gradient echo imaging is often governed by $T_2^*$.

Fourier notation appears because MRI samples a signal in time and reconstructs spatial content through reciprocal variables. A one-dimensional readout under a gradient can be summarized as $S(k_x) = \\int M(x)e^{{ik_xx}}dx$, with $k_x$ proportional to accumulated gradient area. Phase encoding repeats the same logic in the $y$ direction, so a two-dimensional acquisition fills a grid in $(k_x, k_y)$ before applying a two-dimensional Fourier transform.

EPI bandwidth formulas should be read operationally. In the frequency-encoding direction, pixel bandwidth is high because samples arrive rapidly during each readout. In the phase-encoding direction, effective bandwidth is much lower because adjacent ky lines are separated by echo spacing. That asymmetry explains why off-resonance errors displace signal mainly along the phase-encoding direction and why AP/PA reversal is diagnostically useful.

# Appendix B. Protocol Tradeoff Tables

| Method or issue | Primary benefit | Main cost | Practical check |
|---|---|---|---|
| Full Fourier EPI | Complete k-space sampling | Longer readout or fewer slices | Check TE and slice coverage |
| Early partial Fourier | Shorter TE | Less BOLD-optimal timing in many protocols | Confirm whether TE remains near expected T2-star |
| Late partial Fourier | More slices at similar TE | Regional dropout and smoothing risk | Inspect frontal and inferior temporal signal |
| GRAPPA | Less PE distortion and faster traversal | SNR loss and ACS motion sensitivity | Inspect calibration and residual aliasing |
| SMS EPI | More slices per TR | Slice leakage and SBRef motion sensitivity | Inspect SBRef, TSNR, and aliasing patterns |
| Multi-echo EPI | Echo-dependent denoising and regional SNR gains | Longer readout and more complex modeling | Confirm TE-dependent behavior before interpretation |
| Fat suppression | Reduces lipid ghosts | Can fail or change with setup | Inspect scalp ghosts and background |
| Motion control | Improves temporal stability | Can interact with receive fields | Compare motion traces, tSNR, and stdev images |

# Appendix C. Source Resource Links

The following source pages preserve external resources named by the course. These are reader-facing references rather than build notes.

{chr(10).join(resource_lines) if resource_lines else "- No external resource links were extracted."}

# Glossary

**ACS data.** Autocalibration signal data used by GRAPPA to estimate how missing k-space lines can be reconstructed from coil-array information.

**Aliasing.** Misregistration caused when the sampled field of view is smaller than the object being encoded, allowing signal to wrap into the image.

**B0.** The main static magnetic field that polarizes spins and sets the Larmor frequency.

**B1.** The RF magnetic field used to tip magnetization away from the longitudinal axis.

**Bandwidth.** Frequency range sampled per pixel or direction; in EPI the phase-encoding bandwidth is much lower than the frequency-encoding bandwidth.

**BOLD contrast.** Blood-oxygen-level-dependent contrast, an indirect fMRI signal tied to changes in deoxyhemoglobin and local magnetic susceptibility.

**Chemical shift.** Frequency offset caused by electron shielding differences, most practically visible as water-lipid displacement.

**Dropout.** Regional signal loss, often from susceptibility-driven dephasing around air-tissue interfaces.

**Echo spacing.** Time between adjacent echoes or ky lines in EPI, a key driver of distortion.

**EPI.** Echo-planar imaging, a rapid method that samples many k-space lines after one excitation.

**Flip angle.** The angle through which RF excitation tips net magnetization.

**Fourier transform.** Mathematical operation connecting a signal representation to its frequency or spatial-frequency content.

**Ghosting.** Replica image artifact, often shifted by FOV/2 in EPI because of alternating readout-line errors.

**Gradient.** A controlled spatial variation in magnetic field used for slice selection and spatial encoding.

**GRAPPA.** A parallel imaging method that reconstructs skipped k-space lines using calibration data and coil sensitivity information.

**K-space.** The spatial-frequency domain sampled by MRI before Fourier reconstruction.

**Nyquist ghost.** EPI ghost caused by mismatch between odd and even readout lines.

**Partial Fourier.** Acquisition that omits part of k-space and reconstructs it using conjugate symmetry assumptions.

**Receive bias field.** Spatial sensitivity pattern of the receive coil that can interact with motion and realignment.

**Slice selection.** Excitation of a slab using RF bandwidth in the presence of a slice-select gradient.

**SMS or multiband EPI.** Simultaneous excitation and acquisition of multiple slices, separated using coil-array information.

**T1.** Longitudinal relaxation time describing recovery toward thermal equilibrium.

**T2.** Transverse relaxation time describing spin-spin dephasing without macroscopic field-gradient effects.

**T2-star.** Apparent transverse decay including field inhomogeneity and susceptibility effects.

**Temporal SNR.** Ratio of mean signal to temporal standard deviation across a time series.
"""
    return textwrap.dedent(appendix).strip() + "\n"


def write_manuscript_outputs(pages: list[PageInfo], assets: dict[str, list[Path]]) -> None:
    staged_paths: list[Path] = []
    for chapter in CHAPTERS:
        md = build_chapter_markdown(chapter, pages, assets)
        path = OUTPUTS / f"staged_draft_{chapter.number:02d}_chapter_{chapter.number}.md"
        path.write_text(md, encoding="utf-8")
        staged_paths.append(path)

    preface = textwrap.dedent(
        """
        # Preface

        Practical fMRI rewards readers who can connect physics, pulse sequence design, image appearance, and experimental interpretation. This book reconstructs the practical fMRI course as a self-study textbook. It keeps the original course emphasis on mechanisms and real data appearances while expanding the terse slide language into cumulative explanation.

        The intended reader is an advanced undergraduate, beginning graduate student, new imaging researcher, or technically minded collaborator who needs to understand how scanner choices become fMRI data quality. The book starts with NMR signal formation, moves through MRI spatial encoding, builds EPI from k-space principles, and then treats modern acceleration, artifacts, troubleshooting, and biological confounds.

        Figures are source-backed when the source labels, arrows, legends, edge tags, or image examples are part of the teaching evidence. Each figure is grouped by concept rather than by slide number. Dense sequences are continued so that small labels and diagnostic image patterns remain readable.
        """
    ).strip()

    merged_parts = [preface, ""]
    for path in staged_paths:
        merged_parts.append(path.read_text(encoding="utf-8"))
        merged_parts.append("")
    merged_parts.append(build_appendices(pages))
    merged = "\n".join(merged_parts)
    merged_path = OUTPUTS / "practical_fmri_textbook_full_manuscript_merged.md"
    polished_path = OUTPUTS / "practical_fmri_textbook_full_manuscript_polished.md"
    merged_path.write_text(merged, encoding="utf-8")

    polished = re.sub(r"\n{3,}", "\n\n", merged)
    polished = polished.replace("T2-star", "$T_2^*$")
    polished_path.write_text(polished, encoding="utf-8")


def write_figure_audit_files(pages: list[PageInfo], assets: dict[str, list[Path]]) -> None:
    figure_page_to_number: dict[int, str] = {}
    for figure in FIGURE_PLANS:
        for page in figure.pages:
            figure_page_to_number[page] = figure.number

    manifest = ["# Figure Manifest", ""]
    for figure in FIGURE_PLANS:
        manifest.extend(
            [
                f"## Figure {figure.number}. {figure.title}",
                "",
                f"- Source pages: {page_range(figure.pages)}",
                f"- Teaching focus: {figure.focus}",
                "- Assets:",
            ]
        )
        for asset in assets[figure.number]:
            manifest.append(f"  - `{asset.relative_to(OUTPUTS).as_posix()}`")
        manifest.append("")
    (OUTPUTS / "figure_manifest.md").write_text("\n".join(manifest), encoding="utf-8")

    extracts = ["# Figure Text Extracts", ""]
    by_number = {info.number: info for info in pages}
    for figure in FIGURE_PLANS:
        extracts.extend([f"## Figure {figure.number}. {figure.title}", ""])
        for page_number in figure.pages:
            info = by_number[page_number]
            extracts.extend(
                [
                    f"### Source page {page_number}: {info.title}",
                    "",
                    "```text",
                    info.text if info.text else "[image-only source panel]",
                    "```",
                    "",
                ]
            )
    (OUTPUTS / "figure_text_extracts.md").write_text("\n".join(extracts), encoding="utf-8")

    audit = ["# Source Coverage Audit", ""]
    for info in pages:
        chapter = chapter_for_page(info.number)
        section = section_for_page(chapter, info.number)
        summary = info.title if info.title else f"Source page {info.number}"
        if info.number in figure_page_to_number:
            classification = "figure"
            location_line = f"  - Location: Figure {figure_page_to_number[info.number]}."
            extra = []
        elif "http" in info.text.lower():
            classification = "appendix/table/resource"
            location_line = "  - Location: Appendix C, Source Resource Links."
            extra = []
        elif info.text_chars == 0 and not info.visual_rich:
            classification = "blank/admin"
            location_line = "  - Reason: Blank or administrative source page with no extractable teaching content."
            extra = []
        else:
            classification = "prose"
            location_line = f"  - Location: Chapter {chapter.number}, {section.title}."
            extra = []
            if info.visual_rich:
                extra.append(
                    "  - Visual handling: The visual is a decorative or duplicated context image for this section; "
                    "the represented teaching content is the named concept and not a distinct labeled diagram or diagnostic comparison."
                )
        audit.extend(
            [
                f"- Source page {info.number}",
                f"  - Summary: {summary}",
                f"  - Classification: {classification}",
                location_line,
            ]
        )
        audit.extend(extra)
        audit.append("")
    (OUTPUTS / "source_coverage_audit.md").write_text("\n".join(audit), encoding="utf-8")


def validate_plan_exists() -> None:
    plan_path = OUTPUTS / "figure_plan.md"
    if not plan_path.exists():
        raise RuntimeError("outputs/figure_plan.md must exist before figure generation.")


def build_all() -> None:
    pages = load_pages()
    validate_plan_exists()
    assets = generate_figure_assets(pages)
    write_figure_audit_files(pages, assets)
    write_manuscript_outputs(pages, assets)
    (OUTPUTS / "build_summary.log").write_text(
        "\n".join(
            [
                f"timestamp={datetime.now().isoformat(timespec='seconds')}",
                f"source_pdf={INPUT_PDF}",
                f"source_pages={len(pages)}",
                f"figures={len(FIGURE_PLANS)}",
                f"assets={sum(len(v) for v in assets.values())}",
                "status=build_complete",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the practical fMRI textbook run outputs.")
    parser.add_argument("--phase", choices=["plan", "build"], required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pages = load_pages()
    if args.phase == "plan":
        write_plan_outputs(pages)
        print(f"Wrote extraction notes, chapter plan, and figure plan for {len(pages)} source pages.")
        return 0
    build_all()
    print("Generated fresh figures, staged drafts, polished manuscript, manifest, text extracts, and source coverage audit.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
