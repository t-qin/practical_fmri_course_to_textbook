# Source Completeness Audit — 2026-04-13 (late pass)

## Goal of this audit
Check whether the current textbook is still missing any information from the original slide deck after the recent correction and source-completeness passes.

Standard used for this audit:
- Losing slide knowledge counts as failure.
- Correcting scientifically wrong slide content is allowed and preferred, but the correction should be explicit.
- Compressing a sequence of slides into cleaner textbook prose is acceptable **only if the underlying knowledge is still preserved**.

## What is now clearly preserved
The following previously flagged gaps are now explicitly preserved in the book:
- late confound decision-matrix slides:
  - slide 220 -> Table 13.1
  - slide 224 -> Table 13.2
  - slide 225 -> Tables 13.3 and 13.4
  - slide 226 -> Table 13.5
- resource appendix content already preserved:
  - slide 23 -> Bonus videos
  - slide 168 -> Partial Fourier versus GRAPPA link
  - slides 188 and 198 -> practicalfMRI artifact/example links
- previously identified textbook corrections now applied:
  - nominal 3.0 T proton frequency corrected to ~127.7 MHz
  - T2 / T2* wording corrected into explicit T2-star wording
  - Kaza attribution corrected to receive-coil / SMS context
  - Table 3.1 placeholder replaced with a real table

## Current verdict
- I do **not** see any remaining missing **major chapter-scale scientific block** from the original slide deck.
- I do see a small number of remaining **explicit source-preservation gaps**, mostly in the form of slide-provided external resources/links that are still not represented in the textbook.
- I also see some places where stepwise slide pedagogy has been compressed into prose or composite visuals, but those do **not** currently look like clear information loss.

## Remaining likely-missing source information
These are the source items I can defend as still missing **as source information**, because they appear in the deck but are not currently preserved explicitly in the manuscript/PDF.

### Missing resource / external-link slides or link-level source items
1. **Slide 83 — Aliasing**
   - Source link: `https://mriquestions.com/eliminate-wrap-around.html`
   - The aliasing concept itself is covered in the textbook.
   - The specific source-provided external resource link is not currently preserved.

2. **Slide 111 — Multi-slice EPI: slice order / spin history effects**
   - Source link: `https://imaging.mrc-cbu.cam.ac.uk/imaging/CommonArtefacts`
   - The spin-history concept is covered.
   - The source-provided external troubleshooting/resource link is not currently preserved.

3. **Slide 114 — A real EPI pulse sequence**
   - Source link: `https://practicalfmri.blogspot.com/2012/07/physics-for-understanding-fmri.html`
   - EPI pulse-sequence logic is covered in the book.
   - The explicit practicalfMRI resource link from the source slide is not currently preserved.

4. **Slide 120 — Magnetic susceptibility**
   - Source link: `https://mriquestions.com/what-is-susceptibility-chi.html`
   - Susceptibility physics is covered in the book.
   - The source-provided explanatory external link is not currently preserved.

5. **Slide 178 — Multi-echo EPI / tedana**
   - Source link: `https://tedana.readthedocs.io/en/stable/index.html`
   - Multi-echo EPI concepts are covered.
   - The explicit tedana resource link from the slide is not currently preserved.

6. **Slide 179 — Weighted sum of echoes**
   - Source link: `https://doi.org/10.3390/s23094329`
   - Weighted-sum / multi-echo discussion is present in substance.
   - The explicit DOI/resource from the source slide is not currently preserved.

## Things that are compressed rather than clearly missing
These do not currently look like true information loss, but they are worth naming accurately:
- some step-by-step pulse-sequence / GRE / k-space teaching slides are condensed into textbook prose rather than preserved slide-by-slide
- some slide visuals are still represented via slide-derived or source-derived figure forms rather than fully redrawn textbook diagrams
- some troubleshooting and artifact examples are summarized rather than reproduced at the granularity of every individual slide image

Current judgment:
- these are **presentation/compression issues**, not currently obvious missing-knowledge failures
- I would not call them missing unless a future closer slide-by-slide audit shows a specific omitted claim

## Resolution update (same day)
The previously identified remaining source-resource gaps were then patched into Appendix E of the textbook:
- slide 83 aliasing link
- slide 111 spin-history / common-artifacts link
- slide 114 real-EPI pulse-sequence link
- slide 120 magnetic-susceptibility link
- slide 178 tedana link
- slide 179 weighted-sum-of-echoes DOI

## Bottom line
If the standard is:
> “The textbook should contain all knowledge from the slides, corrected where necessary, with scientific supplements for textbook use,”
then the book is now **very close to that standard**.

After the Appendix E expansion, I do **not** currently see a remaining missing major scientific teaching block or an obvious remaining unpreserved source-resource block comparable to the already-fixed late confound tables.
