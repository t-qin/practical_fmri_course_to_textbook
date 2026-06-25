# Role

You are the repository executor for a course-slides-to-textbook project.

# Goal

Transform the source course slide PDF in `inputs/` into a polished, self-study textbook PDF. The output must preserve the source course's substantive concepts, figures, equations, and teaching structure while reorganizing them into a readable chapter manuscript.

# Hard Rules

- Read `prompts/base_textbook_prompt.md` before drafting.
- Read `docs/GOLDEN_REFERENCE_STANDARD.md` before designing the pipeline.
- Read `docs/RUN_PROTOCOL.md` before starting a scratch build.
- Read `docs/SOURCE_COVERAGE_AUDIT.md` before deciding that a source page can be omitted or represented outside a figure.
- Treat the course slide PDF as the authoritative source.
- Do not invent unsupported scientific claims.
- If a claim is added from general domain knowledge, mark it for verification in the QA notes.
- Keep every test run reproducible from scratch.
- Do not copy manuscripts, figures, or PDFs from any previous run.
- If you claim a file was generated or updated, verify that exact path exists on disk before reporting it.
- The final PDF must use the Pandoc/XeLaTeX exporter in `scripts/export_markdown_to_pdf.py` or an equivalent Pandoc/XeLaTeX path.
- Do not use ReportLab as the final product renderer.
- Do not render every source slide as one textbook figure.
- Do not include build-review sections such as `Source Coverage Map`, `QA Notes`, quality-gate reports, or run manifests in the reader-facing manuscript/PDF.
- Do not leave placeholder or template artifacts such as `[visual or blank slide]`, `compact source wording can be restated as:`, or source-processing notes in reader-facing text.
- Do not satisfy figure-adjacent explanation by repeating generic boilerplate after every figure. Figure explanations must be source-specific, source-grounded, and useful to the local concept.
- For the practical fMRI validation deck, target a product structurally comparable to the golden reference rather than a compact summary.
- For other courses, match the quality class but scale chapter count, page count, appendices, and figures to the actual source material.
- Create `outputs/source_coverage_audit.md` with one entry per source PDF page. Use only the classifications in `docs/SOURCE_COVERAGE_AUDIT.md`; represented pages need `Location:` and intentionally omitted pages need `Reason:`. Visual-rich pages classified as `prose` need concrete `Visual handling:` and cannot use vague "represented nearby" language. Resolve all `needs review` entries before promotion.
- A source page that contains substantive images, brain-image grids, arrows, edge labels, tables, diagrams, or source-specific visual evidence must normally be classified as `figure` or `appendix/table/resource`. Do not classify it as `prose` merely because the surrounding topic is discussed in the chapter.

# Figure Policy

- Use the order: title, figure, explanation.
- Keep meaningful labels, arrows, edge tags, legends, and annotations inside the figure image.
- Put source-specific explanation after the figure only when it teaches something local to that figure. Do not add repeated captions such as `Panel sequence covering...` or generic paragraphs telling the reader to inspect labels.
- Use no more than two panels side by side.
- Split dense figure sequences into continued figure blocks instead of compressing them.
- Put at most one generated continued-figure asset on a PDF page by default, especially for table-heavy slides, brain-image grids, or small-label source panels.
- Synthetic figures are allowed when they are accurate and more readable.
- Source-backed figures are required when a synthetic version would lose labels, anatomical markers, arrow-linked text, or source-specific content.
- The figure manifest must include every source page whose visual content contributes teaching evidence. If a visual source page is omitted, the audit must name the exact duplicate/decorative reason; generic phrases such as "nearby named figures" or "fully restated in prose" are not acceptable.

# Required Outputs

Produce these artifacts under `outputs/`:

- extraction notes
- chapter plan
- `figure_plan.md`
- staged manuscript drafts
- merged manuscript
- polished manuscript
- figure assets
- `figure_manifest.md`
- `figure_text_extracts.md`
- `source_coverage_audit.md`
- PDF export log
- final polished PDF

# Quality Gate

Run `python scripts/quality_gate.py` after export. A run that fails the quality gate is evidence for improving the kit and starting a new run, not a run to patch into success.

# Delivery Format

Return:

1. files_changed
2. commands_run
3. generated_outputs
4. validation_results
5. remaining_manual_steps
6. risks
7. suggested_next_step

Only list generated outputs that were verified on disk in the same turn.
