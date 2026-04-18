# Practical fMRI Textbook Task

## Start Here
- `BUILD_HANDOFF.md` — full process/history/handoff note for revisiting this textbook later

## Status
Post-draft follow-through completed: the textbook now has an extracted-asset figure-integrated Markdown manuscript plus an exported PDF handoff. The canonical PDF export now uses a real Pandoc/XeLaTeX pipeline for textbook-style equation rendering. The latest source-completeness passes restored the late Chapter 13 decision-matrix slides as real tables and expanded Appendix E to preserve the source deck's resource/external-link slides and later reference links.

## Objective
Transform the source slide PDF into a polished textbook-style PDF chapter set for long-term self-study, preserving all meaningful scientific content while expanding explanations, integrating figures, and reorganizing the material pedagogically.

## Current Inputs
- `inputs/textbook_instruction.txt` — full textbook-conversion specification
- `inputs/FMRI_course.pdf` — source slide deck (`Ben Inglis`, 226 pages)

## Planned Workflow
1. Extract full topic/figure structure from the slide PDF ✅
2. Propose textbook table of contents and chapter map ✅
3. Map slide content into the textbook structure ✅
4. Draft the textbook in staged passes
5. Integrate and explain useful figures
6. Produce the final polished manuscript/PDF

## Current Outputs
- `notes/run1_source_extraction.md` — source-domain extraction
- `notes/page_titles.tsv` — page-by-page title extraction
- `notes/run2_pages_1_30_extraction.txt` — raw text extraction for the early source block
- `notes/run3_pages_31_120_extraction.txt` — raw text extraction for the middle physics/acquisition block
- `notes/run4_pages_121_217_extraction.txt` — raw text extraction for susceptibility, advanced EPI, and troubleshooting blocks
- `notes/run5_pages_218_226_extraction.txt` — raw text extraction for confounds and human-factors block
- `outputs/run1_textbook_plan.md` — proposed textbook TOC, chapter map, and figure integration plan
- `outputs/run2_chapters_1_4_draft.md` — first-pass textbook manuscript for Chapters 1-4
- `outputs/run3_chapters_5_9_draft.md` — first-pass textbook manuscript for Chapters 5-9
- `outputs/run4_chapters_10_12_draft.md` — first-pass textbook manuscript for Chapters 10-12
- `outputs/run5_chapters_13_14_front_back_matter.md` — front matter, Chapters 13-14, appendices, glossary, and end matter
- `outputs/practical_fmri_textbook_full_manuscript.md` — merged full manuscript handoff
- `outputs/practical_fmri_textbook_full_manuscript_polished.md` — extracted-asset figure-integrated Markdown manuscript (clean textbook body; raw figure text kept in companion notes)
- `outputs/practical_fmri_textbook_full_manuscript_polished.pdf` — exported PDF handoff
- `outputs/figure_manifest.md` — figure inventory mapped to generated assets
- `outputs/figure_text_extracts.md` — extracted slide text grouped by figure for validation / cleanup outside the main textbook body
- `outputs/figures/` — generated extracted/cropped figure set (46 PNG files)

## Build Helpers
- `scripts/build_figures_and_polish.py` — extracts/crops source-backed figure assets, skips title-only / text-only slides as figure panels, limits figures to one panel or two panels max for readability, keeps the image crop focused on the visual/graph itself, emits slide title/subtitle text as manuscript text before the figure when possible, preserves explanatory text as normal post-figure manuscript text instead of a stock callout label, applies curated cleanup overrides where raw extraction still reads poorly, records extracted slide text in a companion artifact, and rebuilds the polished Markdown manuscript
- `scripts/export_markdown_to_pdf.py` — exports the polished manuscript to PDF using Pandoc + XeLaTeX, generates the linked TOC/bookmarks through the LaTeX stack, renders equations as real textbook-style math, rewrites Markdown image+caption pairs into fixed-position TeX figure blocks so figures stay with their captions, and now compiles from a clean temporary directory for more reliable XeLaTeX output on `/mnt/c/`

## Suggested Output Locations
- `notes/` — extraction notes, topic map, figure map
- `outputs/` — manuscript drafts, final PDF, supporting assets
