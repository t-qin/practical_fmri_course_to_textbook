#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

import fitz

from source_coverage_audit import validate_audit


FORBIDDEN_READER_HEADINGS = [
    'Source Coverage Map',
    'QA Notes',
    'Quality Gate',
    'Run Manifest',
    'Build Log',
    'Validation Results',
]

FORBIDDEN_READER_PHRASES = [
    '[visual or blank slide]',
    'compact source wording can be restated as:',
    'The source material is primarily visual here',
    'Panel sequence covering',
    'The panel is retained at full readable scale so labels, arrows, legends, image-grid relationships, and annotations remain visible.',
    'The teaching role of this figure is to make the abstract mechanism visible.',
    'Read the labels first, then follow the sequence from the earliest controlled event to the measured consequence.',
    'In practical fMRI use, the figure should be connected back to protocol choice.',
]

REPEATED_PARAGRAPH_MIN_CHARS = 120
REPEATED_PARAGRAPH_MAX_ALLOWED = 8


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Validate that a course-to-textbook run meets the golden-reference quality floor.')
    parser.add_argument('--root', default='.')
    parser.add_argument('--input-pdf', default=None, help='Source slide PDF. Defaults to the single PDF under inputs/.')
    parser.add_argument('--polished-md', default=None, help='Polished manuscript Markdown. Defaults to the single *polished*.md under outputs/.')
    parser.add_argument('--polished-pdf', default=None, help='Final polished PDF. Defaults to the single *polished*.pdf under outputs/.')
    parser.add_argument('--profile', choices=['auto', 'generic', 'practical-fmri'], default='auto')
    parser.add_argument('--practical-fmri-min-pages', type=int, default=150)
    parser.add_argument('--practical-fmri-min-pdf-text-chars', type=int, default=180000)
    return parser.parse_args()


def status(ok: bool) -> str:
    return 'PASS' if ok else 'FAIL'


def resolve_path(root: Path, value: str | None) -> Path | None:
    if not value:
        return None
    path = Path(value)
    return path if path.is_absolute() else root / path


def find_single(root: Path, value: str | None, pattern: str, label: str) -> tuple[Path, str]:
    explicit = resolve_path(root, value)
    if explicit is not None:
        return explicit, ''
    matches = sorted(root.glob(pattern))
    if len(matches) == 1:
        return matches[0], ''
    if not matches:
        return root / pattern.replace('*', 'MISSING'), f'No {label} matched {pattern}.'
    listed = ', '.join(path.relative_to(root).as_posix() for path in matches)
    return matches[0], f'Multiple {label} files matched {pattern}; pass an explicit path. Matches: {listed}'


def display_path(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def detect_profile(requested: str, root: Path, input_pdf: Path, md_text: str) -> str:
    if requested != 'auto':
        return requested
    del root
    haystack = ' '.join([input_pdf.name.lower(), md_text[:2000].lower()])
    if input_pdf.name.lower() == 'fmri_course.pdf' or 'practical fmri' in haystack:
        return 'practical-fmri'
    return 'generic'


def forbidden_reader_hits(text: str, markdown: bool) -> list[str]:
    hits: list[str] = []
    for heading in FORBIDDEN_READER_HEADINGS:
        if markdown:
            pattern = rf'(?im)^#{{1,6}}\s*{re.escape(heading)}\s*$'
        else:
            pattern = rf'(?im)^{re.escape(heading)}\s*$'
        if re.search(pattern, text):
            hits.append(heading)
    lower_text = text.lower()
    for phrase in FORBIDDEN_READER_PHRASES:
        if phrase.lower() in lower_text:
            hits.append(phrase)
    return hits


def repeated_long_paragraphs(text: str) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    for raw in re.split(r'\n\s*\n', text):
        paragraph = re.sub(r'\s+', ' ', raw.strip())
        if len(paragraph) < REPEATED_PARAGRAPH_MIN_CHARS:
            continue
        if paragraph.startswith('|') and paragraph.endswith('|'):
            continue
        counts[paragraph] = counts.get(paragraph, 0) + 1
    repeated = [(paragraph, count) for paragraph, count in counts.items() if count > REPEATED_PARAGRAPH_MAX_ALLOWED]
    return sorted(repeated, key=lambda item: (-item[1], item[0]))


def figure_image_counts(md_text: str) -> list[tuple[str, int]]:
    counts: list[tuple[str, int]] = []
    pattern = re.compile(
        r'(?ms)^#{2,5}\s*(Figure\s+\d+(?:\.\d+)?\..*?)\n\n(.*?)(?=\n\n\*\*Figure\s+\d+(?:\.\d+)?)'
    )
    for match in pattern.finditer(md_text):
        title = re.sub(r'\s+', ' ', match.group(1)).strip()
        image_count = len(re.findall(r'(?m)^!\[Figure', match.group(2)))
        if image_count:
            counts.append((title, image_count))
    return counts


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    outputs = root / 'outputs'
    qa = root / 'qa'
    qa.mkdir(parents=True, exist_ok=True)

    input_pdf, input_pdf_issue = find_single(root, args.input_pdf, 'inputs/*.pdf', 'source PDF')
    polished_md, polished_md_issue = find_single(root, args.polished_md, 'outputs/*polished*.md', 'polished Markdown')
    polished_pdf, polished_pdf_issue = find_single(root, args.polished_pdf, 'outputs/*polished*.pdf', 'polished PDF')
    figure_plan = outputs / 'figure_plan.md'
    manifest = outputs / 'figure_manifest.md'
    source_coverage_audit = outputs / 'source_coverage_audit.md'
    pandoc_log = outputs / 'pandoc_export.log'
    pdf_export_log = outputs / 'pdf_export.log'
    quality_report = qa / 'QUALITY_GATE.md'

    checks: list[tuple[str, bool, str]] = []
    for path in [input_pdf, polished_md, polished_pdf, figure_plan, manifest, source_coverage_audit]:
        checks.append((f'required file exists: {display_path(root, path)}', path.exists(), ''))
    for name, issue in [
        ('source PDF selection is unambiguous', input_pdf_issue),
        ('polished Markdown selection is unambiguous', polished_md_issue),
        ('polished PDF selection is unambiguous', polished_pdf_issue),
    ]:
        checks.append((name, not issue, issue))

    slide_count = 0
    if input_pdf.exists():
        doc = fitz.open(input_pdf)
        try:
            slide_count = doc.page_count
        finally:
            doc.close()

    md_text = polished_md.read_text(encoding='utf-8', errors='replace') if polished_md.exists() else ''
    profile = detect_profile(args.profile, root, input_pdf, md_text)
    manifest_text = manifest.read_text(encoding='utf-8', errors='replace') if manifest.exists() else ''
    coverage_result = validate_audit(input_pdf, source_coverage_audit)
    log_text = ''
    for path in [pandoc_log, pdf_export_log]:
        if path.exists():
            log_text += '\n' + path.read_text(encoding='utf-8', errors='replace')

    figure_refs = re.findall(r'!\[Figure', md_text)
    slide_asset_refs = len(re.findall(r'slide_\d{3}\.(?:jpg|png)', manifest_text))
    one_slide_per_figure = bool(slide_count and len(figure_refs) >= int(slide_count * 0.75) and slide_asset_refs >= int(slide_count * 0.75))
    reportlab_used = 'reportlab' in log_text.lower()
    pandoc_used = pandoc_log.exists() and ('xelatex' in log_text.lower() or 'pandoc' in log_text.lower())
    side_by_side = ' | ![Figure' in md_text or '<td' in md_text.lower()
    forbidden_md = forbidden_reader_hits(md_text, markdown=True)
    repeated_md = repeated_long_paragraphs(md_text)
    figure_counts = figure_image_counts(md_text)
    dense_figure_blocks = [(title, count) for title, count in figure_counts if count > 2]
    page_break_match = re.search(r'continued_figure_page_breaks=(\d+)', log_text.lower())
    continued_page_breaks = int(page_break_match.group(1)) if page_break_match else 0

    checks.append(('final renderer is Pandoc/XeLaTeX', pandoc_used and not reportlab_used, 'ReportLab final output is below the golden-reference standard.'))
    checks.append(('run is not one rendered slide image per figure', not one_slide_per_figure, f'figure_refs={len(figure_refs)}, slide_count={slide_count}, slide_asset_refs={slide_asset_refs}'))
    checks.append(('Markdown does not construct side-by-side figure tables', not side_by_side, 'Use continued figure blocks instead.'))
    checks.append(('reader-facing Markdown excludes build/QA/template artifacts', not forbidden_md, ', '.join(forbidden_md)))
    repeated_md_detail = '; '.join(f'{count}x: {paragraph[:90]}' for paragraph, count in repeated_md[:5])
    if len(repeated_md) > 5:
        repeated_md_detail += f'; plus {len(repeated_md) - 5} more'
    checks.append(('reader-facing Markdown does not repeat long boilerplate paragraphs', not repeated_md, repeated_md_detail))
    checks.append(('source coverage audit covers every source page', coverage_result.ok, coverage_result.detail()))
    dense_detail = '; '.join(f'{title} ({count} assets)' for title, count in dense_figure_blocks[:8])
    if len(dense_figure_blocks) > 8:
        dense_detail += f'; plus {len(dense_figure_blocks) - 8} more'
    checks.append(('continued figure blocks are explicitly paginated', not dense_figure_blocks or continued_page_breaks >= len(dense_figure_blocks), dense_detail or f'continued_figure_page_breaks={continued_page_breaks}'))

    pdf_ok = False
    outline_count = 0
    page_count = 0
    pdf_text = ''
    if polished_pdf.exists():
        doc = fitz.open(polished_pdf)
        try:
            pdf_ok = True
            page_count = doc.page_count
            outline_count = len(doc.get_toc(simple=True))
            pdf_text = '\n'.join(page.get_text('text') for page in doc)
        finally:
            doc.close()
    checks.append(('PDF opens', pdf_ok, f'page_count={page_count}'))
    checks.append(('PDF has bookmarks or outline entries', outline_count > 0, f'outline_count={outline_count}'))
    forbidden_pdf = forbidden_reader_hits(pdf_text, markdown=False)
    repeated_pdf = repeated_long_paragraphs(pdf_text)
    checks.append(('reader-facing PDF excludes build/QA/template artifacts', not forbidden_pdf, ', '.join(forbidden_pdf)))
    repeated_pdf_detail = '; '.join(f'{count}x: {paragraph[:90]}' for paragraph, count in repeated_pdf[:5])
    if len(repeated_pdf) > 5:
        repeated_pdf_detail += f'; plus {len(repeated_pdf) - 5} more'
    checks.append(('reader-facing PDF does not repeat long boilerplate paragraphs', not repeated_pdf, repeated_pdf_detail))

    if profile == 'practical-fmri':
        pdf_text_chars = len(pdf_text)
        has_appendix = bool(re.search(r'(?im)^Appendix\s+[A-Z]\b|^#\s+Appendix\s+[A-Z]\b', pdf_text + '\n' + md_text))
        checks.append(('practical fMRI PDF has golden-reference depth', page_count >= args.practical_fmri_min_pages, f'page_count={page_count}, minimum={args.practical_fmri_min_pages}'))
        checks.append(('practical fMRI text depth is substantial', pdf_text_chars >= args.practical_fmri_min_pdf_text_chars, f'pdf_text_chars={pdf_text_chars}, minimum={args.practical_fmri_min_pdf_text_chars}'))
        checks.append(('practical fMRI output includes reader-facing appendices', has_appendix, 'Expected Appendix A or equivalent reader-facing back matter.'))

    failed = [item for item in checks if not item[1]]
    lines = [
        '# Quality Gate',
        '',
        f'Generated: {datetime.now().isoformat(timespec="seconds")}',
        f'Overall status: {"FAIL" if failed else "PASS"}',
        f'Profile: {profile}',
        '',
        '## Checks',
        '',
    ]
    for name, ok, detail in checks:
        suffix = f' - {detail}' if detail else ''
        lines.append(f'- {status(ok)} {name}{suffix}')
    lines.extend([
        '',
        '## Policy',
        '',
        'A failed quality gate means the reusable kit must be improved and the next numbered test run must start from scratch.',
        '',
    ])
    quality_report.write_text('\n'.join(lines), encoding='utf-8')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
