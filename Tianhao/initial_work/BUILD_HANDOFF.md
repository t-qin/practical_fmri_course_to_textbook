# Practical fMRI Textbook — Build Handoff

_Last updated: 2026-04-13 (America/Los_Angeles)_

## 1. Project objective
Convert the Ben Inglis fMRI course slide PDF into a long-form textbook-style chapter book that:
- preserves all substantive content from the slide deck,
- expands terse slide content into self-study prose,
- integrates figures/graphs/equations responsibly,
- avoids unsupported invention,
- and exports to a navigable PDF.

This document is the **main handoff note** for revisiting the textbook later. It records what the project is, how it was built, what changed across revisions, what rules now govern the manuscript, where the important files live, and what still needs judgment if work resumes.

---

## 2. Canonical project location
Root task folder:
- `/mnt/c/practical_fmri_course_to_textbook/Tianhao/initial_work`

### Inputs
- Source instruction file:
  - `inputs/textbook_instruction.txt`
- Source slide deck:
  - `inputs/FMRI_course.pdf`

### Reference / comparison artifact
Borrowed ChatGPT-made reference version (used only as a comparison artifact, not as a source of truth):
- `reference/fmri_textbook_chapter_book_fixed.pdf`

### Main outputs
- `outputs/practical_fmri_textbook_full_manuscript.md`
  - merged working manuscript
- `outputs/practical_fmri_textbook_full_manuscript_polished.md`
  - current polished working manuscript used for PDF export
- `outputs/practical_fmri_textbook_full_manuscript_polished.pdf`
  - current export target / readable book artifact
- `outputs/figure_manifest.md`
  - figure inventory
- `outputs/figure_text_extracts.md`
  - extracted slide text grouped by figure for validation and revisits
- `outputs/figures/`
  - generated figure assets
- `outputs/_pandoc_build_input.md`
  - generated Pandoc/XeLaTeX build input used to create the canonical PDF
- `outputs/_pandoc_build_output.tex`
  - generated LaTeX file emitted by Pandoc before XeLaTeX compilation
- `outputs/_pandoc_build_output.pdf`
  - intermediate PDF produced by the current XeLaTeX compile step before copying to the canonical file
- `outputs/pandoc_export.log`
  - Pandoc/XeLaTeX export log for debugging
- `outputs/LAST_REBUILD_STAMP.txt`
  - latest successful canonical rebuild stamp
- `outputs/full_book_audit_2026-04-13.md`
  - automated whole-book structural audit
- `outputs/full_book_visual_qa_all_pages_2026-04-13.md`
  - whole-book page-by-page visual QA note

### Supporting run outputs
- `outputs/run1_textbook_plan.md`
- `outputs/run2_chapters_1_4_draft.md`
- `outputs/run3_chapters_5_9_draft.md`
- `outputs/run4_chapters_10_12_draft.md`
- `outputs/run5_chapters_13_14_front_back_matter.md`

### Extraction notes
- `notes/run1_source_extraction.md`
- `notes/page_titles.tsv`
- `notes/run2_pages_1_30_extraction.txt`
- `notes/run3_pages_31_120_extraction.txt`
- `notes/run4_pages_121_217_extraction.txt`
- `notes/run5_pages_218_226_extraction.txt`

### Build scripts
- `scripts/build_figures_and_polish.py`
- `scripts/export_markdown_to_pdf.py`

---

## 3. Source PDF facts
- Source file: `inputs/FMRI_course.pdf`
- Source metadata observed during setup:
  - title: `FMRI_course`
  - author: `Ben Inglis`
  - length: **226 pages/slides**

High-level source coverage extracted during Run 1:
1. NMR and relaxation foundations
2. MRI hardware
3. Fourier transform / gradients / slice selection / k-space
4. EPI fundamentals
5. Classic EPI artifacts
6. Susceptibility, motion history, inflow, receive-field effects
7. Partial Fourier / GRAPPA / SMS / multi-echo / FLEET
8. Artifact recognition and troubleshooting
9. Biological confounds and human factors

---

## 4. Final manuscript scope
Current manuscript structure:
- Title page
- Preface
- How to use this book
- Table of contents
- Chapters 1–14
- Appendix A. Equation Guide and Symbol Reference
- Appendix B. Artifact Troubleshooting Tables
- Appendix C. Acquisition Tradeoff Summary Tables
- Appendix D. Grounding and Scientific Supplements
- Glossary
- Index-like keyword guide

The current PDF is designed to be:
- readable,
- internally navigable,
- reasonably figure-integrated,
- and grounded to the slide deck plus named scientific supplements.

---

## 5. What happened across the build

### Phase 1 — Task initialization
Created the task workspace and staged the instruction file and source PDF inside it.

### Phase 2 — Run 1: source extraction and textbook plan
Generated:
- source-topic extraction,
- textbook TOC,
- chapter mapping,
- figure integration plan,
- five-run drafting plan.

### Phase 3 — Run 2: early chapters
Drafted Chapters 1–4:
- MRI/fMRI orientation
- magnetization / Larmor / rotating frame
- relaxation / T1 / T2 / T2* / chemical shift
- hardware and receive coils

### Phase 4 — Run 3: core image-formation chapters
Drafted Chapters 5–9:
- Fourier transform intuition
- gradients / slice selection / GRE
- k-space
- EPI fundamentals
- ghosting / distortion / dropout

### Phase 5 — Run 4: advanced acquisition and troubleshooting
Drafted Chapters 10–12:
- susceptibility / inflow / receive-bias-motion effects
- partial Fourier / GRAPPA / SMS / multi-echo / FLEET
- artifact recognition / QC / troubleshooting

### Phase 6 — Run 5: confounds and end matter
Drafted:
- Chapter 13 biological confounds / human factors
- Chapter 14 integrative framework
- front matter and appendices
- glossary and keyword guide

### Phase 7 — Merged manuscript
Combined run outputs into a single Markdown manuscript.

### Phase 8 — First figure integration attempt (superseded)
Initial figure integration used slide-page composites / broad crops. This was **not good enough** and is no longer the target method.

Main problems discovered:
- figures treated whole slides as figures,
- captions/labels sometimes got cut off,
- some figures combined too many panels,
- some text-only slides were incorrectly preserved as images,
- appendix tables rendered poorly,
- equations were messy in PDF export.

### Phase 9 — Extracted-asset rebuild
Shifted to a better figure pipeline:
- prefer actual image/visual regions,
- extract source text separately,
- treat text-only slides as text sources rather than figures,
- keep figure count readable.

### Phase 10 — User-driven figure and layout corrections
User review led to these concrete rules:
- do **not** treat slide screenshots as textbook figures by default,
- preserve captions / explanatory labels,
- if a slide contains **two graphs**, split them rather than merging them into one bad crop,
- keep figures at **one panel or two panels max**, never dense multi-panel sheets,
- discard low-information slide images instead of forcing them in,
- fix appendix table rendering,
- add clickable TOC navigation,
- do not make up knowledge beyond the slide deck unless supported by valid scientific supplements.

### Phase 11 — Manual replacements
Some bad figures were replaced with synthetic textbook-style diagrams instead of keeping weak crops. At minimum, these were explicitly replaced during cleanup:
- Figure 3.2
- Figure 6.1
- Figure 7.3
- Figure 12.6
- Figure 13.3

### Phase 12 — Navigation improvements
The PDF now has:
- a clickable table of contents page,
- and a bookmark / outline tree in the PDF sidebar.

### Phase 13 — Grounding hardening
Added Appendix D to make the grounding rule explicit:
- core content should be anchored to the slide deck,
- expansions should remain within standard MRI/fMRI scientific supplements,
- unsupported elaboration should be revised or removed.

### Phase 14 — Equation formatting cleanup (superseded)
Performed an additional equation-format pass on the old ReportLab exporter to reduce raw LaTeX leakage. That path improved some failures but remained too brittle for textbook-quality equation typesetting.

### Phase 15 — Pandoc/XeLaTeX export pipeline
Switched the canonical PDF export path from the custom ReportLab renderer to a real Pandoc + XeLaTeX pipeline so equations render as proper textbook-style math instead of fragile plain-text approximations.

Key changes in the live build path:
- `scripts/export_markdown_to_pdf.py` now preprocesses the polished Markdown into a Pandoc-ready build input,
- strips the manual in-manuscript TOC block and lets Pandoc generate the linked TOC,
- converts Markdown image + explicit caption pairs into fixed-position LaTeX figure blocks so the image stays with its caption,
- preserves the manuscript's explicit figure numbering (for example `Figure 4.1`) instead of letting LaTeX renumber them generically,
- uses XeLaTeX with `book` class for a more textbook-like PDF structure,
- uses `TeX Gyre Pagella` / `TeX Gyre Pagella Math` for body text and math,
- keeps PDF bookmarks/navigation through the LaTeX bookmark stack,
- writes `_pandoc_build_output.tex` as the explicit LaTeX handoff artifact,
- and compiles that LaTeX file from a clean temporary directory before copying the intermediate PDF back to the canonical output path; this avoids the in-place XeLaTeX flakiness seen on `/mnt/c/`.

This was triggered by the user explicitly asking for proper textbook-style equations and authorizing package installation as needed. The older ReportLab path should now be treated as legacy/superseded rather than the preferred route.

### Phase 16 — Source-completeness patch for late confound slides and resource slides
After a source-alignment review, the following missing-or-diluted slide content was restored explicitly:
- source slide 220 retyped as a full textbook table on relative importance of nuisance variables by study type,
- source slide 224 retyped as a full textbook table on human factors modifying the main confounding mechanisms,
- source slide 225 split into two textbook tables: relative utility of MRI scans and relative utility of simultaneous auxiliary data,
- source slide 226 retyped as a full textbook table on pre/post-scan auxiliary data importance,
- source slide 23 plus resource/link slides 168, 188, and 198 preserved in a new `Appendix E. Source Resource Slides and External Links`,
- and the later completeness pass expanded Appendix E to also preserve the source-provided external links from slides 83, 111, 114, 120, 178, and 179.

This phase also corrected specific slide-to-textbook mismatches instead of preserving them blindly:
- the nominal proton frequency at 3.0 T was corrected to ~127.7 MHz while noting the slide's 123 MHz shorthand,
- the T2/T2* wording was clarified in textbook language,
- Kaza et al. was remapped to the receive-coil/SMS context where it actually appears in the deck,
- and the stale `Table 3.1 (planned)` marker was replaced with a real table.

---

## 6. Current manuscript rules
These are the live rules that should govern future edits.

### 6.1 Grounding rule
Do not freely embellish MRI/fMRI explanations just because the prose sounds textbook-like.

Any substantive claim in the manuscript should satisfy at least one of these:
1. clearly present or implied in the source slides, or
2. standard enough to be supported by a named MRI/fMRI supplement or a slide-cited paper.

If neither is true, rewrite or remove it.

### 6.2 Figure rule
Do **not** use full-slide screenshots as textbook figures by default.

Preferred order:
1. extract the true visual asset or diagram region,
2. pull slide title/subtitle text out of the crop and place it above the extracted panel when possible,
3. place paragraph-style explanatory text after the figure instead of duplicating it both inside and outside the crop,
4. if the slide bundles multiple visuals, split them,
5. if the source visual is too messy, redraw it cleanly.

### 6.3 Figure panel rule
- one panel is preferred
- two panels max
- do not build dense 3–6 panel composite figures just because the source deck used a sequence of slides

### 6.4 Caption/callout rule
If a graph/diagram depends on nearby slide text to make sense, preserve that text without duplicating it.

Preferred handling:
- slide title above the extracted panel,
- subtitle directly under the title when present,
- paragraph or bullet-style explanation after the figure,
- and only keep text inside the crop when it is truly part of the visual itself.

### 6.5 Appendix rendering rule
Appendix markdown tables should render as **actual PDF tables**, not monospace code blocks.

### 6.6 Navigation rule
The PDF should keep:
- clickable TOC page entries,
- and a usable outline/bookmark tree.

---

## 7. Scientific supplements currently named in the manuscript
Appendix D currently names these supplements / anchors:
- Lauterbur (1973), Nature — early MRI / projection imaging
- Feinberg & Setsompop (2013), JMR — simultaneous multi-slice imaging
- Polimeni et al. (2016), MRM — FLEET / calibration robustness
- Wald — receive-field / motion-correction context (slide-cited context)
- Duyn / Frahm / Gao & Liu / Liu et al. — inflow / physiology / confounds (slide-cited context)
- Kaza et al. — distortion / susceptibility context (slide-cited context)
- Buxton (2009)
- Bernstein, King, Zhou (2004)
- Brown et al. (2014)

Important: this appendix is a **grounding guardrail**, not a full scholarly citation audit of every paragraph.

---

## 8. Build scripts and what they do

### `scripts/build_figures_and_polish.py`
Purpose:
- rebuild figure assets,
- crop/extract source-backed visuals,
- separate slide heading/explanation text from the crop when possible,
- regenerate the polished Markdown manuscript.

Current behavior includes:
- skips title-only / text-only slides as figure panels,
- limits source-derived figures to one or two panels max,
- keeps cropped figure assets to the visual/graph itself instead of baking slide heading text into the image,
- places extracted slide titles/subtitles in the manuscript before the figure when available,
- moves preserved explanatory text into normal manuscript paragraphs after the figure instead of using a stock callout label,
- uses curated/manual explanation overrides for figures where raw extraction still reads like OCR fragments,
- writes `figure_manifest.md`,
- writes `figure_text_extracts.md` for validation.

### `scripts/export_markdown_to_pdf.py`
Purpose:
- export the polished Markdown manuscript to the final PDF.

Current behavior includes:
- preprocesses the polished Markdown into `_pandoc_build_input.md`,
- removes the manual in-manuscript TOC block and lets Pandoc generate the linked TOC,
- rewrites Markdown image + caption pairs into fixed-position LaTeX figure blocks so figures do not disappear behind orphaned caption paragraphs,
- preserves the manuscript's explicit figure numbering in the rendered PDF,
- uses Pandoc + XeLaTeX with the `book` document class,
- renders equations as real LaTeX math,
- emits `_pandoc_build_output.tex` and compiles it from a clean temporary directory for reliability,
- produces PDF bookmarks/navigation through the LaTeX bookmark stack,
- and writes `pandoc_export.log` for debugging.

---

## 9. How to rebuild the current book
From anywhere with access to the repo/runtime:

```bash
python3 /mnt/c/practical_fmri_course_to_textbook/Tianhao/initial_work/scripts/build_figures_and_polish.py
python3 /mnt/c/practical_fmri_course_to_textbook/Tianhao/initial_work/scripts/export_markdown_to_pdf.py
```

Main output after rebuild:
- `/mnt/c/practical_fmri_course_to_textbook/Tianhao/initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.pdf`

---

## 10. Current known limitations
The project is in a strong usable state, but not fully perfect.

### Remaining limitations
1. Some source-derived figures are still based on slide visuals rather than clean redrawn textbook art.
2. Some complex slide layouts may still be better handled manually than by automated crop logic.
3. The grounding appendix establishes policy and references, but the manuscript still benefits from future paragraph-by-paragraph scientific audit against the slide deck.
4. `figure_text_extracts.md` is a validation artifact, not polished book prose.
5. The PDF export now uses a real Pandoc/XeLaTeX path for much better equations, but the overall layout is still a pragmatic academic/book-style export rather than a fully custom press-quality book design.

### Best future improvement path
If work resumes later, the highest-value next steps are:
1. paragraph-level grounding audit,
2. figure-by-figure manual curation / redraw,
3. higher-end book layout / typesetting on top of the new TeX-capable export path.

---

## 11. Specific user review lessons that must not be forgotten
These came directly from user review and should be treated as canonical process memory for this textbook project.

- “Don’t just put the slides on there as graphs.”
- Extract pictures, equations, and graphs properly.
- Slide text also needs to be extracted when it carries the meaning.
- If a figure caption got cut off, that is a bad crop.
- If two graphs were put together and part of the paragraph got cut off, that is still just a bad crop.
- A bad crop includes both:
  - extra irrelevant slide junk left in, and
  - missing meaningful figure/caption content.
- Figures should be shown one by one, or at most two together, because larger composites become unreadable.
- Appendix sheets should not render as ugly text dumps.
- The book should not make up knowledge; it must stay grounded in the slides and valid scientific supplements.

---

## 12. What to review first next time
If this project is reopened later, review in this order:
1. `BUILD_HANDOFF.md` (this file)
2. `README.md`
3. current PDF output
4. `figure_manifest.md`
5. `figure_text_extracts.md`
6. source PDF and any newly reported bad figures

This order should make it possible to resume work without reconstructing the whole process from chat history.
