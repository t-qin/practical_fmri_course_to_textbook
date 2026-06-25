# Golden Reference Standard

The goal is not to produce any PDF. The goal is to produce a textbook PDF with the same kind of quality as the practical fMRI golden reference.

## Required Product Shape

- Long-form textbook prose, not slide notes.
- Pedagogical chapter structure derived from the deck, not one chapter per arbitrary page block.
- A curated figure plan before figure generation.
- Reader-facing Markdown plus a final PDF.
- Figure manifest and source-text extracts for audit.
- Reader-facing appendices when the source material supports equation guides, troubleshooting tables, tradeoff summaries, source resources, or glossary material.
- No build-review sections such as `Source Coverage Map`, `QA Notes`, `Quality Gate`, or run manifests in the final reader-facing manuscript.
- No placeholder or template artifacts such as `[visual or blank slide]`, `compact source wording can be restated as:`, or source-processing notes in the final reader-facing manuscript.
- No repeated generic figure-explanation boilerplate. Figure-adjacent prose must be local, source-grounded, and useful; it must not be a repeated paragraph telling the reader to inspect labels or connect the figure to protocol choice.
- Human PDF review before a run is accepted.

## Required Rendering Path

- Use Pandoc plus XeLaTeX for the final PDF.
- Preserve a PDF export log.
- Preserve a rebuild stamp or equivalent build metadata.
- Keep TOC/bookmarks usable.
- Render equations, tables, and captions as textbook material.
- Do not use ReportLab as the final product renderer.

## Required Figure Standard

- Do not render every source slide as one textbook figure.
- Do not treat slide screenshots as the default final figure form.
- Build a curated `outputs/figure_plan.md` that groups source pages into pedagogical figures.
- Use no more than two panels side by side.
- Split dense figure sequences into continued figure blocks.
- Put at most one generated continued-figure asset on a PDF page by default; table-heavy slides, brain-image grids, and small-label slides must not be stacked into dense multi-asset pages.
- Preserve labels, arrows, edge tags, legends, and annotations inside the figure.
- Use synthetic figures when they are accurate and more readable.
- Use source-backed figures when source-specific visual labels would be lost.

## Depth and Back Matter Standard

The practical fMRI test case is used to measure whether the kit can reproduce the golden reference quality class. For that test, a compact outline-level product is not enough. The result should be structurally comparable to the reference: deep textbook prose, useful appendices, a substantial glossary, and figure-adjacent explanation that teaches the material rather than merely labeling screenshots.

For other courses, the exact page count will differ, but the same principle applies: do not compress a full course deck into a thin slide-note summary if the source supports a full textbook treatment.

## Generalization Standard

The practical fMRI reference is a quality benchmark, not a fixed outline, chapter count, appendix count, page count, or figure count for unrelated courses. For a different source deck, scale the manuscript to that deck's actual length, density, and teaching goals. A short workshop deck may produce a short textbook; a semester-long course may produce a large one. The invariant requirements are source grounding, readable figures, complete coverage of informative slides, reader-facing polish, and reproducibility.

Use the practical-fMRI-specific quality-gate profile only for the bundled practical fMRI validation deck. Generic courses should use the generic profile unless they intentionally define their own course-specific thresholds.

## Source Coverage Standard

Every informative source slide must be represented somewhere in the final product, either as a source-backed/synthetic figure, as source-derived body prose, as a table, or as reader-facing appendix/resource material. Section dividers, blank slides, duplicated title slides, and non-essential transition slides may be omitted, but the run must record why they were omitted in a source coverage audit.

The required audit artifact is `outputs/source_coverage_audit.md`, with the exact format defined in `docs/SOURCE_COVERAGE_AUDIT.md`. It must contain one entry per source PDF page. Each entry must include the page number, a short source summary, one classification, and either a final textbook location or an omission reason. Allowed classifications are `figure`, `prose`, `appendix/table/resource`, `duplicate/transition`, `blank/admin`, `external resource`, and `needs review`. A run cannot be promoted while any page remains `needs review`.

The audit must not hide visual teaching material by classifying a diagram-heavy, screenshot-heavy, table-heavy, brain-grid, or arrow-labeled slide as ordinary prose. If a visual-rich page is classified as `prose`, the entry must include concrete `Visual handling:` explaining why no figure or appendix/table/resource representation is needed. Ambiguous phrases such as "discussed in prose or represented by a nearby figure sequence", "nearby named figures", or "fully restated in prose" are not acceptable. If the visual is represented by a figure, classify that source page as `figure` and include it in the figure manifest.

## Run 001 Failure To Avoid

The first practical fMRI scratch run produced a valid but unacceptable product by rendering 226 slide JPEGs and exporting through ReportLab. That run proved the kit was reproducible, but not quality-reproducible.

Future runs must fail the quality gate if they:

- use ReportLab for the final PDF,
- generate one figure per source slide,
- omit `figure_plan.md`,
- skip curated figure grouping,
- include build/QA notes in the reader-facing PDF,
- compress dense continued figures into unreadable multi-asset pages,
- omit informative source slides without a source coverage audit,
- or claim success before human PDF review.

## Run 002 Failure To Avoid

The second practical fMRI scratch run corrected the renderer and figure-plan failures, but remained too compressed. It produced a 93-page PDF compared with the 191-page golden reference, packed dense figure sequences onto single pages, and included `Source Coverage Map` and `QA Notes` in the final book. Future runs should fail the quality gate for those issues.
