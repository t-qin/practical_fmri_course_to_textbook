# Project Introduction

This project captures a concrete “course PDF to textbook” conversion workflow for a practical fMRI teaching deck. The source material is a Ben Inglis course slide PDF. The output is not a slide summary or lecture notes; it is a textbook-style manuscript and PDF designed for long-term self-study, with expanded explanations, integrated figures, and a more coherent chapter structure than the original slide order.

The goal of this package is reproducibility and transfer, not archive-for-archive’s-sake completeness. It preserves the source inputs, the staged drafting artifacts, the active figure/polish and PDF export scripts, and the main handoff documents that explain how the book was assembled. It does not try to preserve every transient debug directory, every temporary build intermediate, or the back-and-forth operational chatter that happened during iterative cleanup.

If you want to understand the project quickly, start here:

1. [`README.md`](README.md) for the short project map.
2. [`docs/REBUILD_DOSSIER.md`](docs/REBUILD_DOSSIER.md) for the full pipeline and provenance.
3. [`initial_work/BUILD_HANDOFF.md`](initial_work/BUILD_HANDOFF.md) for the original long-form textbook task handoff.
4. [`initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.pdf`](initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.pdf) for the current output artifact.

The `initial_work` directory is intentionally a curated build bundle. It keeps enough material for another engineer to inspect the workflow and rebuild the book, while excluding noisy scratch artifacts such as temporary QA folders, page-render debug directories, and transient Pandoc/XeLaTeX intermediates.

This package also preserves build provenance. It documents the working environment, the initial prompt/specification, the repository/agent context, the active local skills used during the task, and the policy choices that shaped the figures and manuscript. It does not assume that future rebuilders will use the same agent tooling, but it records that context so the pipeline is transparent rather than implied.
