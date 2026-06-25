# Scratch Run Protocol

Each validation run must be treated as a fresh real-world user attempt, not as a continuation of a prior build.

## Start Conditions

- Begin from a clean copy of `course_to_textbook_kit/template_project/`.
- Copy in exactly one source slide PDF under `inputs/`.
- Copy in the course instruction file or write a new course-specific instruction note under `inputs/`.
- Leave `outputs/`, `notes/`, `logs/`, and `qa/` empty except for placeholder files.
- Do not copy manuscripts, generated figures, export logs, or PDFs from any earlier run.

## Required Build Sequence

1. Read the base prompt, this protocol, and the golden reference standard.
2. Extract page-level source notes from the slide PDF.
3. Create a chapter plan and `outputs/figure_plan.md` before generating figures.
4. Draft the manuscript in staged blocks.
5. Merge the staged drafts into one full manuscript.
6. Generate curated figures from the figure plan.
7. Create `outputs/source_coverage_audit.md` with exactly one entry per source PDF page, following `docs/SOURCE_COVERAGE_AUDIT.md`.
8. Build the polished Markdown manuscript.
9. Export the final PDF with Pandoc/XeLaTeX.
10. Run `scripts/quality_gate.py`.
11. Complete the QA checklist and record the result in `RUN_MANIFEST.md`.

## Failure Handling

A failed run should not be patched into a reference result. Use failures to improve the kit, then start the next numbered run from scratch.

Examples of hard failures:

- The final PDF was exported with ReportLab or another non-book renderer.
- The output renders most source slides as one figure each.
- `outputs/figure_plan.md` is missing or was created after the figures.
- Figures drop labels, arrow callouts, legends, edge tags, or informative source panels.
- Visual-rich source pages are classified as prose with generic handling such as "represented nearby", "nearby named figures", or "fully restated in prose" instead of becoming figures/resources or concrete duplicate/decorative omissions.
- Dense or table-heavy figure sequences are compressed into pages where labels and table text are not realistically readable.
- Build-review content such as `Source Coverage Map`, `QA Notes`, quality-gate reports, or run manifests appears in the reader-facing PDF.
- The manuscript repeats generic figure-explanation boilerplate after many figures instead of writing source-specific figure-adjacent prose.
- The practical fMRI validation output is a compact summary rather than a product structurally comparable to the golden reference.
- `outputs/source_coverage_audit.md` is missing, has fewer entries than the source PDF has pages, has duplicate page entries, lacks required `Summary:`, `Classification:`, `Location:`, or `Reason:` fields, or still contains `needs review`.
- The PDF exists but has not been reviewed by a human.

## Acceptance Standard

A run may be promoted only when it passes the quality gate, satisfies the QA checklist, and is judged by human review to match the practical fMRI golden reference in product quality.
