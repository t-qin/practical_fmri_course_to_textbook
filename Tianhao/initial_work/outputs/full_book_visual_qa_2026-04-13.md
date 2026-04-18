# Full Book Visual QA — Figure-Heavy Pages (2026-04-13)

## Scope
Visual pass over figure-heavy PDF pages in:
- `outputs/practical_fmri_textbook_full_manuscript_polished.pdf`

Method:
- Rendered all pages containing figure labels.
- Checked for missing figures, orphaned captions, clipped crops, obviously broken layout, and obvious caption/content mismatch.

## Pages checked
20, 26, 31, 32, 39, 40, 45, 46, 52, 53, 54, 59, 60, 66, 67, 68, 75, 76, 84, 85, 92, 93, 94, 95, 102, 103, 109, 110

## Result summary
- Most figure-heavy pages passed visual QA after the Pandoc/XeLaTeX figure-block fix.
- One concrete content-level issue remains.

## Flagged issue
### PDF page 26 — Figure 3.2 mismatch
Caption in book:
- `Figure 3.2. Longitudinal recovery and transverse decay curves with T1, T2, and T2* annotated.`

Observed visual problem:
- The rendered figure content does not match that caption.
- One panel shows **Chemical shift** content rather than the expected T1/T2/T2* decay-curve figure.

Likely root cause:
- `outputs/figures/figure_3_2.png` appears to be misassigned during figure generation.
- Figure manifest currently maps Figure 3.2 to source pages `17, 20, 21, 22`, but the generated asset includes chemical-shift material.

Cross-check:
- A direct comparison suggests `figure_3_2.png` is mislabeled and contains content closer to chemical-shift material than to the intended longitudinal/transverse relaxation-curve summary.

## Pass result
No obvious visual/layout problems were detected on the other checked figure-heavy pages.
That includes:
- figures present
- captions present
- no obvious orphaned-caption problem after the figure-block fix
- no obvious clipped/missing image problem in the checked pages

## Resolution update (same day)
- `Figure 3.2` was replaced with a synthetic textbook-style T1 / T2 / T2* figure.
- The canonical PDF was rebuilt successfully afterward.
- Targeted recheck of the repaired page passed.
