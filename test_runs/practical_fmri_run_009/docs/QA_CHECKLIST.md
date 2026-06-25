# QA Checklist

Use this checklist before promoting any run as a successful reproducible output.

## Required Files

- Source PDF exists under `inputs/`.
- Course instruction file exists under `inputs/`.
- Extraction notes exist under `notes/`.
- Chapter plan exists under `outputs/`.
- `figure_plan.md` exists under `outputs/`.
- Polished Markdown exists under `outputs/`.
- Final PDF exists under `outputs/`.
- `figure_manifest.md` exists under `outputs/`.
- `figure_text_extracts.md` exists under `outputs/`.
- `source_coverage_audit.md` exists under `outputs/`.
- `source_coverage_audit.md` has exactly one entry per source PDF page and follows `docs/SOURCE_COVERAGE_AUDIT.md`.
- PDF export log exists under `outputs/`.

## Text Checks

- No obvious encoding corruption.
- No raw tool chatter or planning notes in the reader-facing manuscript.
- No source coverage map, QA notes, run manifest, quality-gate report, or other build-review section in the reader-facing manuscript/PDF.
- No placeholder or template artifacts such as `[visual or blank slide]`, `compact source wording can be restated as:`, or generic source-processing notes in the reader-facing manuscript/PDF.
- No repeated figure-explanation boilerplate such as `Panel sequence covering...`, generic "teaching role" paragraphs, or repeated protocol-choice paragraphs after many figures.
- No stale statements about planned figures or unfinished drafts.
- Chapter and appendix headings are present in the PDF when the source supports back matter.
- Every source PDF page is classified in `source_coverage_audit.md`, whether represented as a figure, prose, appendix/table/resource item, or intentionally omitted with a reason.
- No source coverage entry remains classified as `needs review` before promotion.
- Visual-rich source pages are not hidden as prose with generic handling such as "represented nearby", "nearby named figures", or "fully restated in prose".

## Figure Checks

- Figure labels in the manuscript match figure labels found in the PDF text.
- No figure row uses more than two side-by-side panels.
- The manifest is a curated figure set, not one rendered image per source slide.
- Meaningful arrows, labels, legends, edge tags, and annotations are visible.
- Figure-adjacent explanations are source-specific and not copied as the same generic paragraph under each figure.
- Dense figure sets are split into continued blocks.
- Continued figure assets are not stacked so densely that source labels, tables, or brain-image grids become unreadable.
- Table-heavy and small-label source slides are given enough page space, normally one generated continued-figure asset per PDF page.
- Synthetic figures are checked against the source for accuracy.
- Source-backed figures preserve content that would be lost in a redraw.
- The figure manifest includes every source page whose visual content contributes teaching evidence, unless the audit names an exact duplicate/decorative omission reason.

## PDF Checks

- PDF opens successfully.
- Table of contents and bookmarks are usable.
- Equations, tables, and captions render cleanly.
- Final renderer is Pandoc/XeLaTeX, not ReportLab.
- Render high-risk pages to images and inspect visually.

## Reproducibility Checks

- The run started from a clean template.
- No manuscripts, figures, or PDFs were copied from a previous run.
- `RUN_MANIFEST.md` records input file names, prompt version, agent files used, commands, output paths, and QA status.
- `qa/QUALITY_GATE.md` exists and reports pass before the run is promoted.
- Any failed or partial run is documented as such instead of patched into a final answer.
- Practical fMRI validation runs are compared against the golden reference for depth, appendices, and figure readability, not just file existence.
- Non-practical-fMRI courses are evaluated against source-proportional quality, not against the practical fMRI chapter/page/appendix counts.
