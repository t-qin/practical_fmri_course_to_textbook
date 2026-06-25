# Claude Code Instructions

Use this folder as a clean course-slides-to-textbook workspace.

## Objective

Convert the course slide PDF in `inputs/` into a polished textbook-style PDF. Preserve the course's teaching content, but reorganize it into chapters, sections, captions, figures, and explanations suitable for self-study.

## Workflow

1. Read `prompts/base_textbook_prompt.md`.
2. Read `docs/GOLDEN_REFERENCE_STANDARD.md`.
3. Read `docs/RUN_PROTOCOL.md`.
4. Read `docs/SOURCE_COVERAGE_AUDIT.md`.
5. Inspect `inputs/README.md` and identify the source slide PDF and instruction file.
6. Extract the slide structure and write source notes under `notes/`.
7. Draft a chapter plan and `outputs/figure_plan.md`.
8. Draft the manuscript in staged blocks.
9. Build a merged manuscript.
10. Generate curated figures and a polished manuscript.
11. Export the final PDF with `scripts/export_markdown_to_pdf.py`.
12. Run `python scripts/quality_gate.py` and the checklist in `docs/QA_CHECKLIST.md`.

## Rules

- Start from empty outputs for every new test run.
- Do not reuse earlier generated figures, manuscripts, or PDFs.
- Do not render every slide as one figure.
- Do not use ReportLab as the final product renderer.
- Keep figure layouts readable: maximum two panels side by side.
- Put at most one generated continued-figure asset on a PDF page by default when labels, tables, or brain-image grids are dense.
- Preserve arrow-linked labels, legends, edge tags, and meaningful source annotations.
- Synthetic figures are acceptable only when accurate and more readable than a source crop.
- Keep build-review material such as source coverage maps, QA notes, quality-gate reports, and run manifests out of the reader-facing manuscript/PDF.
- Keep placeholder and template artifacts such as `[visual or blank slide]`, `compact source wording can be restated as:`, and source-processing notes out of reader-facing text.
- For the practical fMRI validation deck, target the golden reference quality class rather than a compact summary.
- For other course decks, scale the outline, length, figures, and appendices to the actual source material rather than copying the practical fMRI structure.
- Create `outputs/source_coverage_audit.md` with exactly one entry per source PDF page. Use the classifications in `docs/SOURCE_COVERAGE_AUDIT.md`; every represented page needs a final `Location:`, every intentionally omitted page needs a `Reason:`, and every visual-rich page classified as `prose` needs concrete `Visual handling:` without vague "represented nearby" language.
- Record all important build decisions in `RUN_MANIFEST.md` if this is a test run.
