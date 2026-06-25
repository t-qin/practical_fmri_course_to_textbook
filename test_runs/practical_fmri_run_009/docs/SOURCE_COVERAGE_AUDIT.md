# Source Coverage Audit

`outputs/source_coverage_audit.md` is the run's page-level accounting file. It prevents a reusable course-to-textbook run from silently dropping source material when the input deck is different from the practical fMRI validation deck.

The audit is not reader-facing. Keep it under `outputs/` and do not include it in the textbook manuscript or PDF.

## Required Scope

Create exactly one entry for every page in the source PDF. If the source deck has 226 pages, the audit must have 226 source-page entries. Do not audit only the pages that became figures.

Each entry must include:

- `Source page N`
- `Summary:`
- `Classification:`
- either `Location:` for represented pages or `Reason:` for intentionally omitted pages
- `Visual handling:` when a source page contains meaningful diagrams, screenshots, arrows, tables, image grids, or other visual teaching content but is classified as `prose`

Allowed classifications:

- `figure`
- `prose`
- `appendix/table/resource`
- `duplicate/transition`
- `blank/admin`
- `external resource`
- `needs review`

`needs review` is allowed while drafting, but a run cannot be promoted while any page remains in that state.

For visual-rich source pages, prefer `figure` or `appendix/table/resource`. Use `prose` only when the visual carries no unique teaching information. Do not classify a slide as `prose` merely because the surrounding concept is discussed in the chapter.

`Visual handling:` must be concrete. Do not use ambiguous language such as "discussed in prose or represented by a nearby figure sequence", "nearby named figures", "fully restated in prose", or "no unique labels or arrows are omitted." If the page is represented by a figure, classify it as `figure` and give that figure location. If it is not represented visually, explain the exact reason the image can be omitted, such as decorative photograph, duplicate visual of a named source page, or text-only restatement with no unique diagram labels.

For source pages with brain-image grids, arrow-linked labels, edge tags, tables, sequence diagrams, screenshots with meaningful marks, or other source-specific visual evidence, the default is not prose. Those pages must appear in `figure_manifest.md` as source pages for a figure, appear as appendix/table/resource material, or be explicitly identified as duplicates of a named source page.

## Entry Format

```markdown
- Source page 20
  - Summary: Approximate T1 and T2 values for common tissue types.
  - Classification: appendix/table/resource
  - Location: Appendix A, relaxation values reference table.

- Source page 57
  - Summary: Diagram of RF excitation geometry used in Chapter 6.
  - Classification: figure
  - Location: Figure 6.1.

- Source page 88
  - Summary: Section divider for EPI examples.
  - Classification: duplicate/transition
  - Reason: Transition slide with no unique teaching content beyond the following section heading.

- Source page 89
  - Summary: Decorative scanner-room photograph used as a section opener.
  - Classification: prose
  - Location: Chapter 7 opening paragraph.
  - Visual handling: The photograph is decorative context only; no labels, arrows, measurements, or unique visual teaching content are omitted.
```

## Validation

Run the checker directly when debugging:

```powershell
python scripts/source_coverage_audit.py --root . --input-pdf inputs/your_course.pdf --audit outputs/source_coverage_audit.md
```

`scripts/quality_gate.py` runs the same validation automatically.
