# Quality Gate

Generated: 2026-05-13T03:17:20
Overall status: PASS
Profile: practical-fmri

## Checks

- PASS required file exists: inputs/FMRI_course.pdf
- PASS required file exists: outputs/practical_fmri_textbook_full_manuscript_polished.md
- PASS required file exists: outputs/practical_fmri_textbook_full_manuscript_polished.pdf
- PASS required file exists: outputs/figure_plan.md
- PASS required file exists: outputs/figure_manifest.md
- PASS required file exists: outputs/source_coverage_audit.md
- PASS source PDF selection is unambiguous
- PASS polished Markdown selection is unambiguous
- PASS polished PDF selection is unambiguous
- PASS final renderer is Pandoc/XeLaTeX - ReportLab final output is below the golden-reference standard.
- PASS run is not one rendered slide image per figure - figure_refs=207, slide_count=226, slide_asset_refs=0
- PASS Markdown does not construct side-by-side figure tables - Use continued figure blocks instead.
- PASS reader-facing Markdown excludes build/QA/template artifacts
- PASS reader-facing Markdown does not repeat long boilerplate paragraphs
- PASS source coverage audit covers every source page - slide_count=226; entries=226
- PASS continued figure blocks are explicitly paginated - Figure 1.1. Magnetization and field-dependent signal strength (3 assets); Figure 1.2. RF excitation and transverse dephasing (4 assets); Figure 1.3. Signal detection and the spin-echo sequence (8 assets); Figure 1.4. Relaxation mechanisms, tissue constants, and chemical shift (6 assets); Figure 2.1. Scanner components and gradient hardware (3 assets); Figure 2.2. Receive arrays and receive-field heterogeneity (3 assets); Figure 3.1. Fourier transform intuition and useful pairs (7 assets); Figure 3.2. Gradients as one-dimensional spatial encoders (5 assets); plus 31 more
- PASS PDF opens - page_count=270
- PASS PDF has bookmarks or outline entries - outline_count=135
- PASS reader-facing PDF excludes build/QA/template artifacts
- PASS reader-facing PDF does not repeat long boilerplate paragraphs
- PASS practical fMRI PDF has golden-reference depth - page_count=270, minimum=150
- PASS practical fMRI text depth is substantial - pdf_text_chars=256084, minimum=180000
- PASS practical fMRI output includes reader-facing appendices - Expected Appendix A or equivalent reader-facing back matter.

## Policy

A failed quality gate means the reusable kit must be improved and the next numbered test run must start from scratch.
