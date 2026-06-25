---
name: "course-to-textbook"
description: "Use when converting a course slide PDF into a reproducible textbook-style PDF with staged extraction, drafting, figure integration, PDF export, and QA."
---

# Course To Textbook

Use this skill when a user provides a course slide deck and wants a textbook-style PDF built from it.

## Workflow

1. Confirm the source PDF and instruction file are present in `inputs/`.
2. Read `docs/GOLDEN_REFERENCE_STANDARD.md`, `docs/RUN_PROTOCOL.md`, and `docs/SOURCE_COVERAGE_AUDIT.md`.
3. Extract page titles, topic blocks, and source text into `notes/`.
4. Create a chapter map, staged drafting plan, and `outputs/figure_plan.md`.
5. Draft chapters in manageable runs, then merge them into one manuscript.
6. Build curated figure assets and a polished manuscript.
7. Export the polished manuscript with `scripts/export_markdown_to_pdf.py`.
8. Run `python scripts/quality_gate.py` and the QA checklist in `docs/QA_CHECKLIST.md`.

## Figure Rules

- Output order is title, figure, explanation.
- Do not crop off meaningful labels, arrows, tags, legends, or annotations.
- Use at most two panels side by side.
- Split large figure sets into continued image blocks.
- Put at most one generated continued-figure asset on a PDF page by default when slides contain small labels, tables, or dense brain-image grids.
- Use source-backed figures when source-specific labels or callouts matter.
- Use synthetic figures only when they are accurate, complete, and easier to read.
- Never default to one rendered slide image per source slide.

## Reproducibility Rules

- Every test run starts from a clean copy of the template.
- Do not reuse manuscript, figure, or PDF outputs from another run.
- Record the source PDF, prompt version, agent files, commands, outputs, and QA status in `RUN_MANIFEST.md`.
- Verify generated files on disk before reporting them.
- A failed quality gate means improve the reusable kit and start a fresh numbered run.
- Keep build-review sections out of the final reader-facing manuscript/PDF; put source coverage maps, QA notes, and run manifests under `qa/` or `outputs/`.
- Keep placeholder and template artifacts such as `[visual or blank slide]`, `compact source wording can be restated as:`, and source-processing notes out of reader-facing text.
- For the practical fMRI validation deck, build toward golden-reference depth and back matter rather than a short summary.
- For other courses, match the quality class without copying practical fMRI's chapter count, page count, appendix count, or figure count.
- Create `outputs/source_coverage_audit.md` with one entry per source PDF page. Classify each page as `figure`, `prose`, `appendix/table/resource`, `duplicate/transition`, `blank/admin`, `external resource`, or `needs review`. Visual-rich pages classified as `prose` need concrete `Visual handling:` and cannot use vague "represented nearby" language. Resolve all `needs review` entries before promotion.
