#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import fitz


ALLOWED_CLASSIFICATIONS = {
    'figure',
    'prose',
    'appendix/table/resource',
    'duplicate/transition',
    'blank/admin',
    'external resource',
    'needs review',
}

OMISSION_CLASSIFICATIONS = {
    'duplicate/transition',
    'blank/admin',
    'external resource',
}

LOCATION_REQUIRED = {
    'figure',
    'prose',
    'appendix/table/resource',
}

PAGE_RE = re.compile(r'(?im)^\s*(?:[-*]\s*)?(?:source\s+)?page\s+(\d+)\b(?P<body>.*)$')
CLASSIFICATION_RE = re.compile(
    r'(?im)\b(?:classification|status)\s*:\s*'
    r'(figure|prose|appendix/table/resource|duplicate/transition|blank/admin|external resource|needs review)\b'
)
SUMMARY_RE = re.compile(r'(?im)\b(?:summary|source summary)\s*:\s*(\S.*)$')
LOCATION_RE = re.compile(r'(?im)\b(?:location|textbook location|final location|where)\s*:\s*(\S.*)$')
REASON_RE = re.compile(r'(?im)\b(?:reason|notes?|why omitted)\s*:\s*(\S.*)$')
VISUAL_HANDLING_RE = re.compile(r'(?im)\b(?:visual handling|visual rationale|why prose)\s*:\s*(\S.*)$')
VAGUE_VISUAL_HANDLING_RE = re.compile(
    r'(?i)\b('
    r'discussed in prose or represented|'
    r'either represented|'
    r'represented elsewhere|'
    r'represented by|'
    r'represented in nearby|'
    r'nearby named figures|'
    r'nearby curated figure sequence|'
    r'nearest curated figure block|'
    r'fully restated in the named chapter section|'
    r'duplicate, low-label example, or simple illustration|'
    r'source-specific panels .* represented|'
    r'no unique labels or arrows are omitted|'
    r'does not contain unique labels, arrows, legends, or diagnostic annotations'
    r')\b'
)
GENERIC_VISUAL_SUMMARY_RE = re.compile(r'(?i)^\s*visual source page\.?\s*$')


@dataclass
class AuditResult:
    ok: bool
    slide_count: int
    entries: int
    missing_pages: list[int]
    duplicate_pages: list[int]
    invalid_entries: list[str]
    needs_review_pages: list[int]

    def detail(self) -> str:
        parts = [
            f'slide_count={self.slide_count}',
            f'entries={self.entries}',
        ]
        if self.missing_pages:
            parts.append('missing_pages=' + ','.join(map(str, self.missing_pages[:30])))
            if len(self.missing_pages) > 30:
                parts.append(f'missing_pages_extra={len(self.missing_pages) - 30}')
        if self.duplicate_pages:
            parts.append('duplicate_pages=' + ','.join(map(str, self.duplicate_pages[:30])))
        if self.needs_review_pages:
            parts.append('needs_review_pages=' + ','.join(map(str, self.needs_review_pages[:30])))
        if self.invalid_entries:
            parts.append('invalid_entries=' + ' | '.join(self.invalid_entries[:8]))
            if len(self.invalid_entries) > 8:
                parts.append(f'invalid_entries_extra={len(self.invalid_entries) - 8}')
        return '; '.join(parts)


def resolve_path(root: Path, value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else root / path


def split_entry_blocks(text: str) -> list[tuple[int, str]]:
    matches = list(PAGE_RE.finditer(text))
    blocks: list[tuple[int, str]] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        page = int(match.group(1))
        blocks.append((page, text[start:end]))
    return blocks


def entry_classification(block: str) -> str | None:
    match = CLASSIFICATION_RE.search(block)
    return match.group(1).lower() if match else None


def has_summary(block: str) -> bool:
    return bool(SUMMARY_RE.search(block))


def summary_text(block: str) -> str:
    match = SUMMARY_RE.search(block)
    return match.group(1).strip() if match else ''


def has_location(block: str) -> bool:
    return bool(LOCATION_RE.search(block))


def has_reason(block: str) -> bool:
    return bool(REASON_RE.search(block))


def has_visual_handling(block: str) -> bool:
    return bool(VISUAL_HANDLING_RE.search(block))


def visual_handling_text(block: str) -> str:
    match = VISUAL_HANDLING_RE.search(block)
    return match.group(1).strip() if match else ''


def has_vague_visual_handling(block: str) -> bool:
    return bool(VAGUE_VISUAL_HANDLING_RE.search(visual_handling_text(block)))


def is_visual_rich(page: fitz.Page) -> bool:
    text_chars = len(page.get_text('text').strip())
    image_count = len(page.get_images(full=True))
    drawing_count = len(page.get_drawings())
    return (image_count > 0 and text_chars < 220) or (image_count >= 2) or (drawing_count >= 10 and text_chars < 220)


def validate_audit(input_pdf: Path, audit_path: Path) -> AuditResult:
    invalid: list[str] = []
    if not input_pdf.exists():
        return AuditResult(False, 0, 0, [], [], [f'missing source PDF: {input_pdf}'], [])
    if not audit_path.exists():
        doc = fitz.open(input_pdf)
        try:
            slide_count = doc.page_count
        finally:
            doc.close()
        return AuditResult(False, slide_count, 0, list(range(1, slide_count + 1)), [], [f'missing audit file: {audit_path}'], [])

    doc = fitz.open(input_pdf)
    slide_count = doc.page_count

    text = audit_path.read_text(encoding='utf-8', errors='replace')
    blocks = split_entry_blocks(text)
    seen: dict[int, int] = {}
    needs_review: list[int] = []

    try:
        for page, block in blocks:
            seen[page] = seen.get(page, 0) + 1
            page_in_range = 1 <= page <= slide_count
            if not page_in_range:
                invalid.append(f'page {page}: outside source range 1-{slide_count}')
            if not has_summary(block):
                invalid.append(f'page {page}: missing summary')
            classification = entry_classification(block)
            if not classification:
                invalid.append(f'page {page}: missing classification')
                continue
            if classification not in ALLOWED_CLASSIFICATIONS:
                invalid.append(f'page {page}: invalid classification {classification}')
            if classification == 'needs review':
                needs_review.append(page)
            if classification in LOCATION_REQUIRED and not has_location(block):
                invalid.append(f'page {page}: classification {classification} requires a location')
            if classification in OMISSION_CLASSIFICATIONS and not has_reason(block):
                invalid.append(f'page {page}: classification {classification} requires a reason')
            if page_in_range and classification == 'prose' and is_visual_rich(doc[page - 1]):
                if GENERIC_VISUAL_SUMMARY_RE.match(summary_text(block)):
                    invalid.append(f'page {page}: visual-rich prose entry has generic Summary')
                if not has_visual_handling(block):
                    invalid.append(f'page {page}: visual-rich source classified as prose requires Visual handling')
                elif has_vague_visual_handling(block):
                    invalid.append(f'page {page}: visual-rich prose entry has vague Visual handling')
    finally:
        doc.close()

    missing = [page for page in range(1, slide_count + 1) if page not in seen]
    duplicates = sorted(page for page, count in seen.items() if count > 1)
    ok = not missing and not duplicates and not invalid and not needs_review
    return AuditResult(ok, slide_count, len(blocks), missing, duplicates, invalid, needs_review)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Validate source slide coverage audit completeness.')
    parser.add_argument('--root', default='.')
    parser.add_argument('--input-pdf', default='inputs/source.pdf')
    parser.add_argument('--audit', default='outputs/source_coverage_audit.md')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    result = validate_audit(resolve_path(root, args.input_pdf), resolve_path(root, args.audit))
    print('PASS' if result.ok else 'FAIL')
    print(result.detail())
    return 0 if result.ok else 1


if __name__ == '__main__':
    sys.exit(main())
