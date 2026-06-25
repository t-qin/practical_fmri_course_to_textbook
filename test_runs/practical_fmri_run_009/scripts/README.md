# Scripts

This folder is for project-specific build scripts created or adapted during a run.

Typical scripts:

- `build_figures_and_polish.py`
- `export_markdown_to_pdf.py`
- `quality_gate.py`
- `source_coverage_audit.py`
- small QA helpers for PDF text extraction or page rendering

Scripts should be deterministic once the agent has designed the manuscript and figure policy for the course. Do not copy scripts from a prior project without checking source paths, output paths, figure numbering, and course-specific overrides.

The included `export_markdown_to_pdf.py` and `quality_gate.py` are reusable kit infrastructure. Prefer extending them over replacing them. The final product PDF should use the Pandoc/XeLaTeX exporter unless there is a documented technical blocker.

`quality_gate.py` auto-detects a single source PDF in `inputs/` and a single polished Markdown/PDF pair in `outputs/`. If a run has multiple candidates, pass explicit paths with `--input-pdf`, `--polished-md`, and `--polished-pdf`.

`export_markdown_to_pdf.py` defaults to one generated continued-figure asset per PDF page. Keep that default for dense slides; override `--continued-images-per-page` only after visual review shows that labels and tables remain readable.

`quality_gate.py` auto-detects the practical fMRI validation profile and applies stricter depth/back-matter checks for that bundled test case. Use `--profile generic` only for a different course where those exact practical fMRI thresholds do not apply.

`source_coverage_audit.py` validates `outputs/source_coverage_audit.md`. The audit format is defined in `docs/SOURCE_COVERAGE_AUDIT.md`. The audit must have one entry per source PDF page, one source summary per entry, no duplicate pages, no `needs review` entries before promotion, and valid classifications. Represented pages require `Location:`; intentionally omitted pages require `Reason:`. Visual-rich source pages classified as `prose` require concrete `Visual handling:`; vague "represented nearby" language is rejected. Use the same checker directly when debugging coverage failures:

```powershell
python scripts/source_coverage_audit.py --root . --input-pdf inputs/your_course.pdf --audit outputs/source_coverage_audit.md
```
