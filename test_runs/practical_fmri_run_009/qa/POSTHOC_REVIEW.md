# Posthoc Review

## Automated Result

`scripts/quality_gate.py` passed with the practical-fMRI profile. The report is in `qa/QUALITY_GATE.md`.

## Visual Spot Check

Rendered PDF pages inspected:

- Representative contact sheet: `qa/rendered_pages_contact_sheet.png`
- Individual pages: `qa/rendered_pages/page_001.png`, `page_005.png`, `page_015.png`, `page_022.png`, `page_040.png`, `page_075.png`, `page_110.png`, `page_150.png`, `page_200.png`, `page_250.png`, and `page_270.png`
- Higher-scale risk pages: `qa/risk_pdf_pages/pdf_page_022.png`, `pdf_page_075.png`, `pdf_page_150.png`, `pdf_page_190.png`, and `pdf_page_250.png`

Observed status: the inspected pages render cleanly, source labels are readable in representative dense figures, and no obvious overlap, missing image, or build-review leakage was visible in the spot check.

## Caveat

This is not a full page-by-page human review. The run should not be promoted as a final golden reproducible output until a human reviewer checks the complete 270-page PDF.
