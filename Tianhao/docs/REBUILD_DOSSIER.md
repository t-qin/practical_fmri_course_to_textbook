# Practical fMRI Textbook Rebuild Dossier

## 1. Project Identity

This package documents how a Ben Inglis fMRI course slide deck was converted into a textbook-style manuscript and PDF.

- Working project title: **practiCal fMRI: From NMR Foundations to EPI Artifacts, Advanced Acquisition, and Biological Confounds**
- Source deck: [`../initial_work/inputs/FMRI_course.pdf`](../initial_work/inputs/FMRI_course.pdf)
- Canonical initial prompt/specification: [`../initial_work/inputs/textbook_instruction.txt`](../initial_work/inputs/textbook_instruction.txt)
- Current polished manuscript: [`../initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.md`](../initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.md)
- Current canonical PDF: [`../initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.pdf`](../initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.pdf)

## 2. Agent and Tooling Context

### Agent roles captured in this task

- **Codex** acted as the repository executor and implementation agent.
- A local agent orchestration environment was the surrounding operating context in which the task was managed.

### Execution environment

- Windows host filesystem
- WSL2 Ubuntu as the canonical execution environment for rebuilds
- Python scripts operating on local files under the task root
- Pandoc + XeLaTeX for final PDF export

### Active local skills relevant to this task

- a repository-grounding skill
  - used for task-policy grounding inside the original workspace context
- `pdf`
  - used for PDF/page rendering and figure-layout verification where visual output mattered

These skills are part of the provenance of the work. They are not required to rebuild the output if the scripts and prerequisites are available.

### Repo/task policy surfaces used

- the original task-level `AGENTS.md`
- [`../initial_work/README.md`](../initial_work/README.md)
- [`../initial_work/BUILD_HANDOFF.md`](../initial_work/BUILD_HANDOFF.md)
- [`../initial_work/outputs/run1_textbook_plan.md`](../initial_work/outputs/run1_textbook_plan.md)

## 3. Initial Prompt

The task specification is the full contents of [`../initial_work/inputs/textbook_instruction.txt`](../initial_work/inputs/textbook_instruction.txt).

At a high level, that prompt required:

- textbook transformation rather than slide summarization
- preservation of all meaningful source concepts and visuals
- deeper explanatory prose suitable for self-study
- pedagogical reorganization into chapters and sections
- figure integration with textbook-style captions and discussion
- careful scientific grounding and avoidance of unsupported invention
- a final PDF-quality deliverable

The prompt also established the staged workflow:

1. extract the conceptual structure of the PDF
2. design a textbook TOC/chapter map
3. draft in multiple runs
4. integrate figures
5. polish and export

## 4. End-to-End Pipeline

### Stage 1. Source ingestion

Inputs:

- [`../initial_work/inputs/FMRI_course.pdf`](../initial_work/inputs/FMRI_course.pdf)
- [`../initial_work/inputs/textbook_instruction.txt`](../initial_work/inputs/textbook_instruction.txt)

Purpose:

- establish the source deck and the explicit authorship/transformation specification

### Stage 2. Extraction notes

Artifacts in [`../initial_work/notes/`](../initial_work/notes/):

- `page_titles.tsv`
- `run1_source_extraction.md`
- `run2_pages_1_30_extraction.txt`
- `run3_pages_31_120_extraction.txt`
- `run4_pages_121_217_extraction.txt`
- `run5_pages_218_226_extraction.txt`

Purpose:

- capture the source deck structure and raw textual material in manageable slices
- preserve source analysis separate from the final manuscript

### Stage 3. TOC and chapter planning

Artifact:

- [`../initial_work/outputs/run1_textbook_plan.md`](../initial_work/outputs/run1_textbook_plan.md)

Purpose:

- translate slide structure into textbook architecture
- define chapter boundaries, figure integration intent, and staged drafting plan

### Stage 4. Staged drafting runs

Artifacts:

- `run2_chapters_1_4_draft.md`
- `run3_chapters_5_9_draft.md`
- `run4_chapters_10_12_draft.md`
- `run5_chapters_13_14_front_back_matter.md`

Purpose:

- expand the source into long-form chapter prose in manageable blocks
- preserve intermediate drafting structure before merge/polish

### Stage 5. Merged manuscript

Artifact:

- [`../initial_work/outputs/practical_fmri_textbook_full_manuscript.md`](../initial_work/outputs/practical_fmri_textbook_full_manuscript.md)

Purpose:

- serve as the merged working manuscript that feeds the figure/polish step

### Stage 6. Figure integration and polishing

Primary script:

- [`../initial_work/scripts/build_figures_and_polish.py`](../initial_work/scripts/build_figures_and_polish.py)

Primary outputs:

- [`../initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.md`](../initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.md)
- [`../initial_work/outputs/figure_manifest.md`](../initial_work/outputs/figure_manifest.md)
- [`../initial_work/outputs/figure_text_extracts.md`](../initial_work/outputs/figure_text_extracts.md)
- [`../initial_work/outputs/figures/`](../initial_work/outputs/figures/)

Purpose:

- generate source-backed and synthetic figure assets
- place figure titles/captions/explanations into the polished manuscript
- maintain a manifest of what each figure came from
- keep extracted figure text available for audit without dumping it directly into the reader-facing book body

### Stage 7. Pandoc/XeLaTeX export

Primary script:

- [`../initial_work/scripts/export_markdown_to_pdf.py`](../initial_work/scripts/export_markdown_to_pdf.py)

Primary outputs:

- [`../initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.pdf`](../initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.pdf)
- [`../initial_work/outputs/pandoc_export.log`](../initial_work/outputs/pandoc_export.log)
- [`../initial_work/outputs/LAST_REBUILD_STAMP.txt`](../initial_work/outputs/LAST_REBUILD_STAMP.txt)

Purpose:

- convert the polished Markdown manuscript into a textbook-style PDF
- generate linked TOC/bookmarks through the LaTeX toolchain
- preserve a build log and a last-successful export stamp

### Stage 8. QA and audit passes

Artifacts:

- `full_book_audit_2026-04-13.md`
- `full_book_visual_qa_2026-04-13.md`
- `full_book_visual_qa_all_pages_2026-04-13.md`
- `source_completeness_audit_2026-04-13_late.md`

Purpose:

- document whole-book structural review, visual QA, and source-completeness checks

## 5. Important Artifact Map

### Root task docs in `initial_work/`

- `README.md`
  - compact summary of the original textbook task workspace
- `BUILD_HANDOFF.md`
  - the main long-form handoff/history note from the original task

### Inputs

- `inputs/FMRI_course.pdf`
  - authoritative source slide deck
- `inputs/textbook_instruction.txt`
  - authoritative initial prompt/specification

### Notes

- `notes/*`
  - extraction and source-analysis artifacts

### Scripts

- `scripts/build_figures_and_polish.py`
  - manuscript/figure build step
- `scripts/export_markdown_to_pdf.py`
  - PDF export step

### Outputs

- `outputs/run1_textbook_plan.md`
  - chapter map and writing plan
- `outputs/run2_*`, `run3_*`, `run4_*`, `run5_*`
  - staged drafting outputs
- `outputs/practical_fmri_textbook_full_manuscript.md`
  - merged working manuscript
- `outputs/practical_fmri_textbook_full_manuscript_polished.md`
  - reader-facing polished Markdown manuscript
- `outputs/practical_fmri_textbook_full_manuscript_polished.pdf`
  - canonical PDF deliverable
- `outputs/figure_manifest.md`
  - figure inventory and source-page mapping
- `outputs/figure_text_extracts.md`
  - extracted text grouped by figure for validation
- `outputs/figures/`
  - current figure PNG set
- `outputs/pandoc_export.log`
  - last export log
- `outputs/LAST_REBUILD_STAMP.txt`
  - last successful export stamp
- `outputs/full_book_*` and `source_completeness_*`
  - QA and audit documentation

### Reference

- `reference/fmri_textbook_chapter_book_fixed.pdf`
  - non-authoritative comparison artifact
  - included for context only, not as a source of truth

## 6. Rebuild Procedure

### Prerequisites

- Windows machine with WSL2 Ubuntu available
- Python 3 available in WSL
- Python packages required by the included scripts:
  - `pymupdf`
  - `Pillow`
- `pandoc` available in PATH or via the fallback logic in `export_markdown_to_pdf.py`
- `xelatex` available in WSL PATH

Example Python dependency install:

```bash
python3 -m pip install pymupdf Pillow
```

### Rebuild commands

From Windows:

```bash
wsl bash -lc "cd /mnt/c/practical_fmri_course_to_textbook/Tianhao/initial_work && python3 scripts/build_figures_and_polish.py"
wsl bash -lc "cd /mnt/c/practical_fmri_course_to_textbook/Tianhao/initial_work && python3 scripts/export_markdown_to_pdf.py"
```

### Expected outputs after rebuild

- `outputs/practical_fmri_textbook_full_manuscript_polished.md`
- `outputs/figure_manifest.md`
- `outputs/figure_text_extracts.md`
- `outputs/figures/`
- `outputs/practical_fmri_textbook_full_manuscript_polished.pdf`
- `outputs/pandoc_export.log`
- `outputs/LAST_REBUILD_STAMP.txt`

### Verify after rebuild

Confirm:

- the polished Markdown exists
- the polished PDF exists
- the stamp file points to a successful recent export
- the figure manifest and figure text extracts were refreshed

## 7. Known Policy Choices in the Current Build

- **Title, figure, explanation ordering**
  - title/pretitle text should appear before the figure
  - figure comes next
  - explanatory text belongs after the figure
- **Source-backed vs synthetic figures**
  - both are allowed
  - synthetic figures are acceptable when they are accurate and materially more readable
  - source-backed figures are preferred when tags, arrows, or labeled anatomy would be lost by synthetic compression
- **Two-up maximum side-by-side rule**
  - the current build policy caps side-by-side figure grids at 2 panels across
- **Annotation preservation**
  - arrow-linked labels, edge tags, and meaningful in-figure markers should stay inside the figure image
- **No unsupported invention**
  - the manuscript may expand and explain
  - it should not fabricate scientific claims absent support from the source or well-grounded supplements
- **Reproducibility over chatter**
  - canonical artifacts and stable policy choices are preserved
  - back-and-forth tweak noise is intentionally not part of the package narrative

## 8. What Was Intentionally Excluded

This package excludes:

- interactive conversational tweak history
- orchestration-tool failure chatter or troubleshooting noise
- temporary debug page renders
- scratch QA directories such as `debug_*`, `tmp_qc_*`, and `audit_pages/`
- transient Pandoc/XeLaTeX intermediates such as `_pandoc_build_*`, `.aux`, `.toc`, and one-off scratch PDFs
- unrelated repo/system material outside the textbook task
- secrets, auth stores, environment files, and non-textbook system internals

## 9. Rebuild Notes for Future Maintainers

- This package is a curated snapshot, not the entire original repo.
- If you need more task history, start with [`../initial_work/BUILD_HANDOFF.md`](../initial_work/BUILD_HANDOFF.md).
- If you need the exact source task specification, use [`../initial_work/inputs/textbook_instruction.txt`](../initial_work/inputs/textbook_instruction.txt) as the authoritative prompt.
- If a future rebuild changes figure policy or output naming, update this dossier so the package remains truthful rather than aspirational.
