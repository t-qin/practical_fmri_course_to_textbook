# Run Manifest

Run: `practical_fmri_run_009`

Date: 2026-05-13

Purpose: fresh from-scratch reproducibility run for the practical fMRI course-to-textbook build.

## Start State

- Created from a clean copy of `C:\practical_fmri_course_to_textbook\course_to_textbook_kit\template_project`.
- Copied only `FMRI_course.pdf` and `textbook_instruction.txt` from `C:\practical_fmri_course_to_textbook\Tianhao\initial_work\inputs`.
- Did not copy manuscripts, generated figures, export logs, PDFs, or other generated outputs from earlier test runs.
- Read before build: `AGENTS.md`, `CLAUDE.md`, `prompts/base_textbook_prompt.md`, `docs/GOLDEN_REFERENCE_STANDARD.md`, `docs/RUN_PROTOCOL.md`, `docs/SOURCE_COVERAGE_AUDIT.md`, `docs/QA_CHECKLIST.md`, and `inputs/textbook_instruction.txt`.

## Commands Run

```powershell
$src = 'C:\practical_fmri_course_to_textbook\course_to_textbook_kit\template_project'
$dst = 'C:\practical_fmri_course_to_textbook\test_runs\practical_fmri_run_009'
if (Test-Path -LiteralPath $dst) { throw "Destination already exists: $dst" }
Copy-Item -LiteralPath $src -Destination $dst -Recurse
Copy-Item -LiteralPath 'C:\practical_fmri_course_to_textbook\Tianhao\initial_work\inputs\FMRI_course.pdf' -Destination (Join-Path $dst 'inputs\FMRI_course.pdf')
Copy-Item -LiteralPath 'C:\practical_fmri_course_to_textbook\Tianhao\initial_work\inputs\textbook_instruction.txt' -Destination (Join-Path $dst 'inputs\textbook_instruction.txt')
```

Output summary: created the run folder with `docs`, `inputs`, `notes`, `outputs`, `prompts`, `scripts`, `skills`, `AGENTS.md`, and `CLAUDE.md`.

```powershell
python scripts\build_practical_fmri_textbook.py --phase plan
```

Output: `Wrote extraction notes, chapter plan, and figure plan for 226 source pages.`

```powershell
python scripts\build_practical_fmri_textbook.py --phase build
```

Output: `Generated fresh figures, staged drafts, polished manuscript, manifest, text extracts, and source coverage audit.`

```powershell
python scripts\source_coverage_audit.py --root . --input-pdf inputs\FMRI_course.pdf --audit outputs\source_coverage_audit.md
```

Output:

```text
PASS
slide_count=226; entries=226
```

```powershell
wsl bash -lc 'cd /mnt/c/practical_fmri_course_to_textbook/test_runs/practical_fmri_run_009 && python3 scripts/export_markdown_to_pdf.py --input-md outputs/practical_fmri_textbook_full_manuscript_polished.md --output-pdf outputs/practical_fmri_textbook_full_manuscript_polished.pdf --title "Practical fMRI" --subtitle "A textbook-style reconstruction for self-study" --author "Generated from source course materials"' | Tee-Object -FilePath 'outputs\pdf_export.log'
```

Output: `/mnt/c/practical_fmri_course_to_textbook/test_runs/practical_fmri_run_009/outputs/practical_fmri_textbook_full_manuscript_polished.pdf`

```powershell
python scripts\quality_gate.py --root . --input-pdf inputs\FMRI_course.pdf --polished-md outputs\practical_fmri_textbook_full_manuscript_polished.md --polished-pdf outputs\practical_fmri_textbook_full_manuscript_polished.pdf
```

Output: no stdout; process exited 0 and wrote `qa/QUALITY_GATE.md`.

```powershell
# Rendered representative PDF pages for visual spot check with PyMuPDF.
# Pages: 1, 5, 15, 22, 40, 75, 110, 150, 200, 250, 270.
```

Output: `qa/rendered_pages_contact_sheet.png` plus individual rendered pages under `qa/rendered_pages/`.

```powershell
# Rendered risk PDF pages at higher scale with PyMuPDF.
# Pages: 22, 75, 150, 190, 250.
```

Output: individual rendered pages under `qa/risk_pdf_pages/`.

## Generated Outputs

- `notes/page_titles.tsv`
- `notes/source_page_notes.md`
- `outputs/extraction_notes.md`
- `outputs/chapter_plan.md`
- `outputs/figure_plan.md`
- `outputs/figures/` with 207 fresh source-backed PNG assets, total 65,050,759 bytes.
- `outputs/figure_manifest.md`
- `outputs/figure_text_extracts.md`
- `outputs/source_coverage_audit.md`
- `outputs/staged_draft_01_chapter_1.md` through `outputs/staged_draft_11_chapter_11.md`
- `outputs/practical_fmri_textbook_full_manuscript_merged.md`
- `outputs/practical_fmri_textbook_full_manuscript_polished.md`
- `outputs/pandoc_export.log`
- `outputs/pdf_export.log`
- `outputs/LAST_REBUILD_STAMP.txt`
- `outputs/practical_fmri_textbook_full_manuscript_polished.pdf`
- `qa/QUALITY_GATE.md`
- `qa/rendered_pages_contact_sheet.png`
- `qa/rendered_pages/`
- `qa/risk_pdf_pages/`

## Output Metrics

- Source PDF pages: 226.
- Source coverage audit entries: 226.
- Figure blocks: 43.
- Figure assets: 207.
- Polished Markdown size: 247,095 bytes.
- Final PDF size: 51,414,998 bytes.
- Final PDF pages: 270.
- Final PDF outline entries: 135.
- Final PDF extracted text characters: 255,815.

## QA Status

Automated source coverage audit: PASS.

Quality gate: PASS, profile `practical-fmri`.

Key quality gate checks:

- Required files exist.
- Final renderer evidence is Pandoc/XeLaTeX.
- Source coverage audit covers all 226 source pages.
- The manuscript is not a one-rendered-slide-per-numbered-figure dump.
- Reader-facing Markdown and PDF exclude build/QA/template artifacts.
- Reader-facing Markdown and PDF do not repeat long boilerplate paragraphs.
- Continued figure blocks are explicitly paginated.
- PDF opens.
- PDF has outline/bookmark entries.
- Practical fMRI depth thresholds pass: 270 pages and more than 180,000 extracted text characters.
- Reader-facing appendices are present.

Visual spot check: PASS for inspected pages. The rendered contact sheet and higher-scale risk pages showed clean title/front matter, readable figure panels, source labels preserved in representative dense figures, no obvious overlap, and readable appendix/back matter. Continued figure sequences intentionally place one source-backed asset per page for label readability.

## Remaining Manual Steps

- Full human page-by-page PDF review is still required before promoting this run as the golden reproducible output.
- Scientific/editorial review should verify the conservative bridge explanations added around the source material.

## Risks

- The output is source-backed figure heavy: 207 assets in 43 curated figure blocks. This preserves labels, arrows, legends, edge tags, and diagnostic image evidence, but a human reviewer may prefer redrawing selected simple mechanism panels in a future kit revision.
- Some continued figure pages show a single source panel before the shared caption/explanation at the end of the figure block. This was chosen to keep dense source labels readable under the exporter default.
- The build script is deterministic and local to this run; if this run is accepted, the useful parts should be promoted into the kit rather than copied from this run's generated outputs.
