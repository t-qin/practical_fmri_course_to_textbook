# Base Course-To-Textbook Prompt

You are converting a course slide PDF into a self-study textbook PDF.

## Inputs

- One source course slide PDF in `inputs/`.
- Optional course-specific instruction notes in `inputs/`.

## Task

Transform the slide deck into a coherent textbook manuscript. Do not merely summarize slides. Reorganize the course into chapters and sections, preserve all substantive concepts, integrate meaningful figures, and expand terse slide bullets into readable explanatory prose.

The final manuscript should be a reader-facing textbook, not a build report. Keep source coverage maps, QA notes, quality-gate reports, run manifests, and other internal review material out of the final PDF. Do not leave placeholder or template artifacts such as `[visual or blank slide]`, `compact source wording can be restated as:`, `Panel sequence covering...`, or source-processing notes in reader-facing text.

## Required Pipeline

1. Extract the slide deck structure and page-level source notes.
2. Produce a chapter plan and figure plan.
3. Draft the textbook in staged runs.
4. Merge staged drafts into one manuscript.
5. Generate source-backed or accurate synthetic figures.
6. Build a polished Markdown manuscript.
7. Export a final PDF using Pandoc/XeLaTeX.
8. Run QA checks for text, figures, structure, and reproducibility.

## Figure Requirements

- Use title, figure, explanation ordering.
- Keep meaningful labels, arrows, edge tags, legends, and annotations inside figure images.
- Use source-specific explanations after figures. Do not repeat generic boilerplate after each figure, and do not invent broad scanner-implication prose unless it is directly supported by the surrounding source material.
- Use no more than two panels side by side.
- Split dense figure sequences into continued figure blocks.
- Put at most one generated continued-figure asset on a PDF page by default when slides contain small labels, tables, or dense brain-image grids.
- Synthetic figures are allowed only when accurate and more readable.
- Source-backed figures are required when source-specific labels or callouts would otherwise be lost.
- Do not turn every slide into one figure.
- Do not use a slide-screenshot dump as a finished textbook.
- Do not hide visual source pages in prose. If a slide contains substantive images, brain-image grids, arrows, edge tags, tables, diagrams, or source-specific visual evidence, it normally belongs in a source-backed figure or appendix/table/resource entry.
- A visual source page may be classified as `prose` only when the visual itself is duplicate, decorative, or has no unique teaching content. Generic explanations such as "represented nearby", "nearby named figures", or "fully restated in prose" are not acceptable.

## Depth Requirements

For validation against the practical fMRI source deck, target the golden reference quality class: substantial textbook prose, reader-facing appendices where the source supports them, a useful glossary, and figure-adjacent explanations that teach the material. A compact slide-note summary is not acceptable for that validation case.

For other course decks, do not copy the practical fMRI outline, chapter count, page count, appendix count, or figure count. Match the quality standard while scaling the product to the source deck's length, density, and teaching goals.

## Grounding Requirements

- Stay grounded in the source slide deck.
- Do not fabricate unsupported claims.
- If you add standard background knowledge, keep it conservative and mark it for review.

## Required Outputs

Create outputs for extraction notes, chapter plan, `figure_plan.md`, staged drafts, merged manuscript, polished manuscript, figure assets, figure manifest, figure text extracts, Pandoc/XeLaTeX export log, quality-gate report, and the final polished PDF.

Also create `outputs/source_coverage_audit.md` with one entry per source PDF page. Follow `docs/SOURCE_COVERAGE_AUDIT.md`. Each entry must include page number, short source summary, classification, and final textbook location or omission reason. Allowed classifications are `figure`, `prose`, `appendix/table/resource`, `duplicate/transition`, `blank/admin`, `external resource`, and `needs review`. Resolve all `needs review` entries before promotion.

For visual-rich pages, do not use vague `Visual handling:` language. If a visual page is represented in the book, classify it as `figure` or `appendix/table/resource`. If it is classified as `prose`, explain the exact reason the visual itself has no unique teaching content.
