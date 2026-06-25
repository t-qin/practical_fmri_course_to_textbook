#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
import textwrap
from datetime import datetime
from pathlib import Path


IMAGE_LINE_RE = re.compile(r'^!\[(.*?)\]\(([^)]+)\)\s*$')
FIGURE_CAPTION_RE = re.compile(r'^\*\*(Figure\s+\d+(?:\.\d+)?\.\s+.*?)\*\*\s*(.*)$')
LIST_ITEM_RE = re.compile(r'^(\s*)([-*+] |\d+\. )')


def require_binary(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise RuntimeError(f'Required binary not found in PATH: {name}')
    return path


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


def convert_markdown_figures_to_latex(text: str, output_dir: Path, continued_images_per_page: int = 1) -> tuple[str, dict[str, int]]:
    continued_images_per_page = max(1, continued_images_per_page)
    stats = {
        'figure_blocks': 0,
        'continued_figure_blocks': 0,
        'continued_figure_images': 0,
        'continued_figure_page_breaks': 0,
    }
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        image_match = IMAGE_LINE_RE.match(lines[i].strip())
        if image_match:
            image_paths = [image_match.group(2).strip()]
            j = i + 1
            while True:
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j >= len(lines):
                    break
                extra = IMAGE_LINE_RE.match(lines[j].strip())
                if not extra:
                    break
                image_paths.append(extra.group(2).strip())
                j += 1
            k = j
            while k < len(lines) and not lines[k].strip():
                k += 1
            if k < len(lines):
                caption_match = FIGURE_CAPTION_RE.match(lines[k].strip())
                if caption_match:
                    caption_tail = caption_match.group(2).strip()
                    caption = caption_match.group(1).strip()
                    if caption_tail:
                        caption = f'{caption} {caption_tail}'
                    resolved = []
                    for image_path in image_paths:
                        p = Path(image_path)
                        if not p.is_absolute():
                            p = (output_dir / p).resolve()
                        resolved.append(p.as_posix())
                    if len(resolved) == 1:
                        stats['figure_blocks'] += 1
                        out.extend([
                            r'\begin{figure}[H]',
                            r'\centering',
                            rf'\includegraphics[width=0.98\linewidth,height=0.78\textheight,keepaspectratio]{{{resolved[0]}}}',
                            rf'{{\small {latex_escape_text(caption)}}}',
                            r'\end{figure}',
                            '',
                        ])
                    else:
                        stats['figure_blocks'] += 1
                        stats['continued_figure_blocks'] += 1
                        stats['continued_figure_images'] += len(resolved)
                        for idx, image_path in enumerate(resolved):
                            out.extend([
                                r'\begin{center}',
                                rf'\includegraphics[width=0.98\linewidth,height=0.78\textheight,keepaspectratio]{{{image_path}}}',
                                r'\end{center}',
                                '',
                            ])
                            if idx < len(resolved) - 1 and (idx + 1) % continued_images_per_page == 0:
                                out.extend([r'\clearpage', ''])
                                stats['continued_figure_page_breaks'] += 1
                        out.extend([
                            r'\begin{center}',
                            rf'\small {latex_escape_text(caption)}',
                            r'\end{center}',
                            '',
                        ])
                    i = k + 1
                    continue
        out.append(lines[i])
        i += 1
    return '\n'.join(out), stats


def normalize_markdown_lists(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    for idx, line in enumerate(lines):
        is_list = bool(LIST_ITEM_RE.match(line))
        if is_list and out and out[-1].strip():
            out.append('')
        out.append(line)
        next_line = lines[idx + 1] if idx + 1 < len(lines) else None
        if is_list and next_line is not None and next_line.strip() and not LIST_ITEM_RE.match(next_line):
            out.append('')
    return '\n'.join(out)


def build_pandoc_input(source_md: Path, output_dir: Path, title: str, subtitle: str, author: str, continued_images_per_page: int) -> tuple[str, dict[str, int]]:
    text = source_md.read_text(encoding='utf-8')
    text, stats = convert_markdown_figures_to_latex(text, output_dir, continued_images_per_page)
    text = normalize_markdown_lists(text)

    text = re.sub(r'\n# Table of Contents\n.*?(?=\n# Chapter\s+\d+\.)', '\n', text, flags=re.S)
    first_chapter = re.search(r'\n# Chapter\s+\d+\.', text)
    if first_chapter:
        text = text[:first_chapter.start()] + '\n\\mainmatter\n' + text[first_chapter.start():]
    if '\n# Glossary\n' in text:
        text = text.replace('\n# Glossary\n', '\n\\backmatter\n\n# Glossary\n', 1)

    metadata = textwrap.dedent(
        f'''\
        ---
        title: "{title}"
        subtitle: "{subtitle}"
        author: "{author}"
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
    return metadata + text.lstrip(), stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Export polished Markdown to a book-style PDF with Pandoc and XeLaTeX.')
    parser.add_argument('--input-md', default='outputs/practical_fmri_textbook_full_manuscript_polished.md')
    parser.add_argument('--output-pdf', default='outputs/practical_fmri_textbook_full_manuscript_polished.pdf')
    parser.add_argument('--title', default='Course Textbook')
    parser.add_argument('--subtitle', default='A textbook-style reconstruction of course slides for self-study')
    parser.add_argument('--author', default='Generated from source course materials')
    parser.add_argument('--continued-images-per-page', type=int, default=1, help='Maximum generated assets from a continued figure block to place on one PDF page.')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path.cwd()
    input_md = (root / args.input_md).resolve()
    output_pdf = (root / args.output_pdf).resolve()
    output_dir = input_md.parent
    log_path = output_dir / 'pandoc_export.log'
    stamp_path = output_dir / 'LAST_REBUILD_STAMP.txt'
    temp_md = output_dir / '_pandoc_build_input.md'
    temp_tex = output_dir / '_pandoc_build_output.tex'
    temp_pdf = output_dir / '_pandoc_build_output.pdf'

    if not input_md.exists():
        raise RuntimeError(f'Input Markdown does not exist: {input_md}')

    pandoc = require_binary('pandoc')
    xelatex = require_binary('xelatex')
    output_dir.mkdir(parents=True, exist_ok=True)
    pandoc_input, conversion_stats = build_pandoc_input(input_md, output_dir, args.title, args.subtitle, args.author, args.continued_images_per_page)
    temp_md.write_text(pandoc_input, encoding='utf-8')

    pandoc_cmd = [
        pandoc,
        str(temp_md),
        '--from', 'markdown+tex_math_single_backslash+tex_math_dollars+raw_tex+pipe_tables+table_captions',
        '--standalone',
        '--top-level-division=chapter',
        '--resource-path', f'{output_dir}:{root}',
        '-t', 'latex',
        '-o', str(temp_tex),
    ]
    logs: list[str] = [
        'FIGURE CONVERSION STATS\n' + '\n'.join(f'{key}={value}' for key, value in sorted(conversion_stats.items()))
    ]
    result = subprocess.run(pandoc_cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    logs.append('PANDOC COMMAND\n' + ' '.join(pandoc_cmd))
    if result.stdout:
        logs.append('PANDOC STDOUT\n' + result.stdout)
    if result.stderr:
        logs.append('PANDOC STDERR\n' + result.stderr)
    if result.returncode != 0:
        log_path.write_text('\n\n'.join(logs) + '\n', encoding='utf-8')
        raise RuntimeError(f'Pandoc LaTeX generation failed; see {log_path}')

    with tempfile.TemporaryDirectory(prefix='course_textbook_tex_') as tmp:
        tmp_dir = Path(tmp)
        tmp_tex = tmp_dir / temp_tex.name
        tmp_tex.write_text(temp_tex.read_text(encoding='utf-8'), encoding='utf-8')
        for pass_no in (1, 2):
            latex_cmd = [xelatex, '-interaction=nonstopmode', '-halt-on-error', tmp_tex.name]
            latex_result = subprocess.run(latex_cmd, cwd=tmp_dir, capture_output=True, text=True, encoding='utf-8', errors='replace')
            logs.append(f'XELATEX PASS {pass_no}\n' + latex_result.stdout + latex_result.stderr)
            if latex_result.returncode != 0:
                log_path.write_text('\n\n'.join(logs) + '\n', encoding='utf-8')
                raise RuntimeError(f'XeLaTeX failed on pass {pass_no}; see {log_path}')
        built_pdf = tmp_dir / temp_tex.with_suffix('.pdf').name
        if not built_pdf.exists():
            raise RuntimeError('XeLaTeX completed but did not produce a PDF.')
        shutil.copy2(built_pdf, temp_pdf)
        shutil.copy2(built_pdf, output_pdf)

    stamp_path.write_text(
        '\n'.join([
            'Last successful Pandoc/XeLaTeX export to canonical PDF.',
            f'timestamp_local={datetime.now().astimezone().isoformat()}',
            f'pandoc={pandoc}',
            f'xelatex={xelatex}',
            f'input={temp_md}',
            f'tex={temp_tex}',
            f'output={output_pdf}',
            '',
        ]),
        encoding='utf-8',
    )
    logs.append(f'OUTPUT\n{output_pdf}')
    log_path.write_text('\n\n'.join(logs) + '\n', encoding='utf-8')
    print(output_pdf)


if __name__ == '__main__':
    main()
