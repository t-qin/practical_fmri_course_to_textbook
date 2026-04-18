# practiCal fMRI Course to Textbook

This repository-ready package preserves a clean rebuild bundle for a project that converts the Ben Inglis fMRI course slide deck into a long-form textbook-style manuscript and PDF. It keeps the source inputs, staged manuscript artifacts, active build scripts, and reproducibility documentation without the conversational tweak history or temporary debug clutter from the original workspace.

## Source and Deliverable

- Source slide deck: [`initial_work/inputs/FMRI_course.pdf`](initial_work/inputs/FMRI_course.pdf)
- Canonical task prompt: [`initial_work/inputs/textbook_instruction.txt`](initial_work/inputs/textbook_instruction.txt)
- Current polished manuscript: [`initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.md`](initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.md)
- Current canonical PDF: [`initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.pdf`](initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.pdf)

## Package Layout

- [`INTRO.md`](INTRO.md): project introduction and intended use of this package
- [`docs/REBUILD_DOSSIER.md`](docs/REBUILD_DOSSIER.md): full provenance, agent/tooling context, and rebuild pipeline
- [`initial_work/`](initial_work): curated snapshot of the textbook task materials

## Canonical Rebuild Commands

Canonical environment: Windows host with WSL2 Ubuntu, Python with `pymupdf` and `Pillow`, plus `pandoc` and `xelatex` available in WSL.

```bash
wsl bash -lc "cd /mnt/c/practical_fmri_course_to_textbook/Tianhao/initial_work && python3 scripts/build_figures_and_polish.py"
wsl bash -lc "cd /mnt/c/practical_fmri_course_to_textbook/Tianhao/initial_work && python3 scripts/export_markdown_to_pdf.py"
```

The full rebuild context, expected outputs, and policy choices are documented in [`docs/REBUILD_DOSSIER.md`](docs/REBUILD_DOSSIER.md).
