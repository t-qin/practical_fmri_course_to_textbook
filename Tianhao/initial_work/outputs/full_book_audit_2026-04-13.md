# Full Book Audit — 2026-04-13

- generated_at: 2026-04-13T11:29-07:00
- pdf: `/mnt/c/practical_fmri_course_to_textbook/Tianhao/initial_work/outputs/practical_fmri_textbook_full_manuscript_polished.pdf`
- pages_extracted: 124
- audit_mode: automated whole-book pass over PDF text, outline, chapter starts, figure labels, and obvious rendering leaks

## Real chapter start check
- OK: `Chapter 1. Why MRI and fMRI Work: A Practical Orientation` -> page 12
- OK: `Chapter 2. Nuclear Magnetization, Precession, and the Rotating Frame` -> page 16
- OK: `Chapter 3. Relaxation, Dephasing, T1, T2, and T2*` -> page 22
- OK: `Chapter 4. MRI Hardware and the Physical Scanner Environment` -> page 28
- OK: `Chapter 5. Fourier Transform Intuition for MRI` -> page 35
- OK: `Chapter 6. Gradients, Slice Selection, and Basic MRI Image Formation` -> page 42
- OK: `Chapter 7. K-Space: The Organizing Language of MRI` -> page 48
- OK: `Chapter 8. Echo-Planar Imaging (EPI): Why fMRI Is Fast` -> page 56
- OK: `Chapter 9. The Classic EPI Artifacts: Ghosting, Distortion, and Dropout` -> page 62
- OK: `Chapter 10. Susceptibility, Motion History, Inflow, and Receive-Field Confounds` -> page 70
- OK: `Chapter 11. Accelerated and Advanced EPI Methods` -> page 78
- OK: `Chapter 12. Artifact Recognition, Quality Control, and Troubleshooting` -> page 87
- OK: `Chapter 13. Biological Confounds and Human Factors in fMRI` -> page 100
- OK: `Chapter 14. Integrative Practical Framework for Running and Interpreting fMRI` -> page 105

## Appendix / front matter check
- OK: `Preface` -> page 10
- OK: `How to Use This Book` -> page 11
- OK: `Contents` -> page 2
- OK: `Appendix A. Equation Guide and Symbol Reference` -> page 112
- OK: `Appendix B. Artifact Troubleshooting Tables` -> page 114
- OK: `Appendix C. Acquisition Tradeoff Summary Tables` -> page 116
- OK: `Appendix D. Grounding and Scientific Supplements` -> page 118
- OK: `Glossary` -> page 120
- OK: `Index-like Keyword Guide` -> page 123

## Figure label check
- expected_figure_labels_from_manuscript: 46
- figure_labels_found_in_pdf_text: 46
- missing_figure_labels: 0
- figure distribution by chapter label:
  - Chapter 2: 2
  - Chapter 3: 2
  - Chapter 4: 3
  - Chapter 5: 3
  - Chapter 6: 3
  - Chapter 7: 5
  - Chapter 8: 3
  - Chapter 9: 5
  - Chapter 10: 4
  - Chapter 11: 5
  - Chapter 12: 6
  - Chapter 13: 3
  - Chapter 14: 2

## Rendering leak checks
- raw_latex_commands: 0
- raw_frac_literal: 0
- inline_math_markers: 0
- latex_text_command: 0
- latex_left_right: 0
- caret_delta: 0
- replacement_char: 0

## Bookmark / outline check
- all chapter and appendix headings were found in the PDF outline

## Figure numbering drift check
- no generic auto-caption drift like `Figure 5:` / `Figure 6:` was detected in extracted PDF text after the latest figure-block fix

## Summary
- automated audit did not detect missing chapters, missing appendices, missing figure labels, raw LaTeX leakage, or outline gaps
- the whole-book chapter pass is clean at the automated text/structure level
- remaining risk is purely visual/layout-level polish that a text extraction audit cannot fully prove
