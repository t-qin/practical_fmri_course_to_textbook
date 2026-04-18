#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import textwrap
import re
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUT_DIR = BASE / 'outputs'
MD_PATH = OUT_DIR / 'practical_fmri_textbook_full_manuscript_polished.md'
PDF_PATH = OUT_DIR / 'practical_fmri_textbook_full_manuscript_polished.pdf'
STAMP_PATH = OUT_DIR / 'LAST_REBUILD_STAMP.txt'
TEMP_MD_PATH = OUT_DIR / '_pandoc_build_input.md'
TEMP_TEX_PATH = OUT_DIR / '_pandoc_build_output.tex'
TEMP_PDF_PATH = OUT_DIR / '_pandoc_build_output.pdf'
LOG_PATH = OUT_DIR / 'pandoc_export.log'

TITLE = 'Practical fMRI: From NMR Foundations to EPI Artifacts, Advanced Acquisition, and Biological Confounds'
SUBTITLE = 'A textbook-style reconstruction and expansion of the Ben Inglis fMRI course slides for long-term self-study'
AUTHOR = 'Grounded in the Ben Inglis fMRI course slides with explicit scientific supplements'

SUBSCRIPT_TO_LATEX = {
    '₀': '$_0$',
    '₁': '$_1$',
    '₂': '$_2$',
    '₃': '$_3$',
    '₄': '$_4$',
    '₅': '$_5$',
    '₆': '$_6$',
    '₇': '$_7$',
    '₈': '$_8$',
    '₉': '$_9$',
}

IMAGE_LINE_RE = re.compile(r'^!\[(.*?)\]\(([^)]+)\)\s*$')
FIGURE_CAPTION_RE = re.compile(r'^\*\*(Figure\s+\d+\.\d+\.\s+.*?)\*\*\s*$')
LIST_ITEM_RE = re.compile(r'^(\s*)([-*+] |\d+\. )')


def require_binary(name: str) -> str:
    path = shutil.which(name)
    if not path and name == 'pandoc':
        candidates = [
            Path(r'C:\Program Files\Quarto\bin\tools\pandoc.exe'),
            Path.home() / 'AppData' / 'Local' / 'Temp' / 'pandoc' / 'pandoc-3.1.12.3' / 'pandoc.exe',
        ]
        for candidate in candidates:
            if candidate.exists():
                path = str(candidate)
                break
    if not path:
        raise RuntimeError(f'Required binary not found in PATH: {name}')
    return path



def normalize_unicode_subscripts(text: str) -> str:
    return ''.join(SUBSCRIPT_TO_LATEX.get(ch, ch) for ch in text)



def latex_escape_text(text: str) -> str:
    replacements = {
        '\\': r'\textbackslash{}',
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
    }
    return ''.join(replacements.get(ch, ch) for ch in text)



def convert_markdown_figures_to_latex(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        image_match = IMAGE_LINE_RE.match(line.strip())
        if image_match:
            image_paths = [image_match.group(2).strip()]
            j = i + 1
            while True:
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j >= len(lines):
                    break
                extra_image_match = IMAGE_LINE_RE.match(lines[j].strip())
                if not extra_image_match:
                    break
                image_paths.append(extra_image_match.group(2).strip())
                j += 1
            k = j
            while k < len(lines) and not lines[k].strip():
                k += 1
            if k < len(lines):
                caption_match = FIGURE_CAPTION_RE.match(lines[k].strip())
                if caption_match:
                    full_caption = caption_match.group(1).strip()
                    resolved_paths = []
                    for image_path in image_paths:
                        image_fs_path = Path(image_path)
                        if not image_fs_path.is_absolute():
                            image_fs_path = (OUT_DIR / image_fs_path).resolve()
                        resolved_paths.append(image_fs_path.as_posix())
                    if len(resolved_paths) == 1:
                        out.extend([
                            r'\begin{figure}[H]',
                            r'\centering',
                            rf'\includegraphics[width=0.98\linewidth,height=0.78\textheight,keepaspectratio]{{{resolved_paths[0]}}}',
                            rf'{{\small {latex_escape_text(full_caption)}}}',
                            r'\end{figure}',
                            '',
                        ])
                    else:
                        for image_tex_path in resolved_paths:
                            out.extend([
                                r'\begin{center}',
                                rf'\includegraphics[width=0.98\linewidth,height=0.78\textheight,keepaspectratio]{{{image_tex_path}}}',
                                r'\end{center}',
                                '',
                            ])
                        out.extend([
                            r'\begin{center}',
                            rf'\small {latex_escape_text(full_caption)}',
                            r'\end{center}',
                            '',
                        ])
                    i = k + 1
                    continue
        out.append(line)
        i += 1
    return '\n'.join(out)



def normalize_markdown_lists(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        is_list = bool(LIST_ITEM_RE.match(line))
        if is_list and out and out[-1].strip():
            out.append('')
        out.append(line)
        next_line = lines[i + 1] if i + 1 < len(lines) else None
        if is_list and next_line is not None and next_line.strip() and not LIST_ITEM_RE.match(next_line):
            out.append('')
        i += 1
    return '\n'.join(out)



def build_pandoc_input() -> str:
    text = MD_PATH.read_text(encoding='utf-8')
    text = normalize_unicode_subscripts(text)
    text = convert_markdown_figures_to_latex(text)
    text = normalize_markdown_lists(text)

    preface_marker = '\n# Preface\n'
    preface_idx = text.find(preface_marker)
    if preface_idx == -1:
        raise RuntimeError('Could not locate # Preface in manuscript; refusing to build malformed Pandoc input.')
    text = text[preface_idx + 1:]

    text = re.sub(r'\n# Table of Contents\n.*?(?=\n# Chapter 1\.)', '\n', text, flags=re.S)

    chapter1 = '\n# Chapter 1. Why MRI and fMRI Work: A Practical Orientation\n'
    if chapter1 not in text:
        raise RuntimeError('Could not locate Chapter 1 heading in manuscript.')
    text = text.replace(chapter1, '\n\\mainmatter\n\n# Chapter 1. Why MRI and fMRI Work: A Practical Orientation\n', 1)

    glossary = '\n# Glossary\n'
    if glossary in text:
        text = text.replace(glossary, '\n\\backmatter\n\n# Glossary\n', 1)

    metadata = textwrap.dedent(
        f'''\
        ---
        title: "{TITLE}"
        subtitle: "{SUBTITLE}"
        author: "{AUTHOR}"
        documentclass: book
        classoption:
          - oneside
          - openany
        fontsize: 11pt
        geometry: margin=0.75in
        mainfont: "Latin Modern Roman"
        sansfont: "Latin Modern Sans"
        monofont: "Latin Modern Mono"
        mathfont: "Latin Modern Math"
        colorlinks: true
        linkcolor: blue
        urlcolor: blue
        toc: true
        toc-depth: 2
        header-includes:
          - |
            \\usepackage{{bookmark}}
          - |
            \\usepackage{{float}}
          - |
            \\usepackage{{graphicx}}
          - |
            \\setlength{{\\emergencystretch}}{{3em}}
        ---

        \\frontmatter

        '''
    )
    return metadata + text.lstrip()



def run() -> None:
    pandoc = require_binary('pandoc')
    xelatex = require_binary('xelatex')

    TEMP_MD_PATH.write_text(build_pandoc_input(), encoding='utf-8')

    pandoc_cmd = [
        pandoc,
        str(TEMP_MD_PATH),
        '--from', 'markdown+tex_math_single_backslash+tex_math_dollars+raw_tex+pipe_tables+table_captions',
        '--standalone',
        '--top-level-division=chapter',
        '--resource-path', f'{OUT_DIR}:{BASE}',
        '-t', 'latex',
        '-o', str(TEMP_TEX_PATH),
    ]
    pandoc_result = subprocess.run(
        pandoc_cmd,
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',
    )

    log_parts = []
    if pandoc_result.stdout:
        log_parts.append('PANDOC STDOUT\n' + pandoc_result.stdout)
    if pandoc_result.stderr:
        log_parts.append('PANDOC STDERR\n' + pandoc_result.stderr)
    if pandoc_result.returncode != 0:
        LOG_PATH.write_text('\n\n'.join(log_parts) + '\n', encoding='utf-8')
        raise RuntimeError(f'Pandoc LaTeX generation failed; see {LOG_PATH}')

    xelatex_logs = []
    with tempfile.TemporaryDirectory(prefix='fmri_book_tex_') as temp_dir:
        temp_dir_path = Path(temp_dir)
        temp_tex_path = temp_dir_path / 'build.tex'
        temp_pdf_path = temp_dir_path / 'build.pdf'
        shutil.copy2(TEMP_TEX_PATH, temp_tex_path)

        for run_idx in (1, 2):
            latex_cmd = [xelatex, '-interaction=nonstopmode', '-halt-on-error', temp_tex_path.name]
            latex_result = subprocess.run(
                latex_cmd,
                cwd=temp_dir_path,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace',
            )
            block = [f'XELATEX RUN {run_idx}']
            if latex_result.stdout:
                block.append('STDOUT\n' + latex_result.stdout)
            if latex_result.stderr:
                block.append('STDERR\n' + latex_result.stderr)
            xelatex_logs.append('\n'.join(block))
            if latex_result.returncode != 0:
                LOG_PATH.write_text('\n\n'.join(log_parts + xelatex_logs) + '\n', encoding='utf-8')
                raise RuntimeError(f'XeLaTeX compilation failed; see {LOG_PATH}')

        if not temp_pdf_path.exists():
            LOG_PATH.write_text('\n\n'.join(log_parts + xelatex_logs) + '\n', encoding='utf-8')
            raise RuntimeError(f'Expected intermediate PDF missing: {temp_pdf_path}')

        shutil.copy2(temp_pdf_path, TEMP_PDF_PATH)

    shutil.copy2(TEMP_PDF_PATH, PDF_PATH)
    LOG_PATH.write_text('\n\n'.join(log_parts + xelatex_logs) + '\n', encoding='utf-8')

    stamp = textwrap.dedent(
        f'''\
        Last successful Pandoc/XeLaTeX export to canonical PDF.
        timestamp_local={datetime.now().astimezone().isoformat()}
        pandoc={pandoc}
        xelatex={xelatex}
        input={TEMP_MD_PATH}
        tex={TEMP_TEX_PATH}
        output={PDF_PATH}
        '''
    )
    STAMP_PATH.write_text(stamp, encoding='utf-8')
    print(PDF_PATH)


if __name__ == '__main__':
    try:
        run()
    except Exception as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        sys.exit(1)
