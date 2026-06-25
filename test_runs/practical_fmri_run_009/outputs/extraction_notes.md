# Extraction Notes

Generated: 2026-05-13T02:53:17
Source PDF: `inputs/FMRI_course.pdf`
Source page count: 226

The source is the practical fMRI course deck. Text extraction shows day-based course blocks
covering NMR signal formation, scanner hardware, Fourier and k-space fundamentals, EPI
artifacts, advanced EPI acceleration, troubleshooting, and biological confounds. Many pages
are image-heavy or image-only, so the run uses source-backed figures for the visual teaching
evidence and prose expansion for the conceptual scaffolding.

## Major Blocks

- Pages 1-23: Chapter 1, NMR Signal Formation. Build the physical vocabulary for precession, excitation, relaxation, spin echoes, and chemical shift.
- Pages 24-30: Chapter 2, Scanner Hardware and Receive Fields. Translate the physics vocabulary into the scanner components that polarize, excite, encode, and receive signal.
- Pages 31-85: Chapter 3, Fourier Thinking, Gradients, and K-space. Develop the mathematical and practical path from frequency analysis to two-dimensional MRI.
- Pages 86-124: Chapter 4, EPI Fundamentals and Classic Artifacts. Explain why EPI is fast, why it is vulnerable, and how its characteristic artifacts arise.
- Pages 125-139: Chapter 5, Flip Angle, Inflow, and Receive-field Motion Effects. Show how choices and hardware sensitivity fields convert physiology and motion into time-series structure.
- Pages 140-158: Chapter 6, Partial Fourier EPI. Evaluate partial Fourier as an acceleration strategy with asymmetric consequences for TE, slices, smoothing, and dropout.
- Pages 159-168: Chapter 7, Parallel Imaging with GRAPPA. Explain how coil arrays and calibration data support accelerated phase encoding, and why motion can corrupt the result.
- Pages 169-182: Chapter 8, Simultaneous Multi-slice and Multi-echo EPI. Extend EPI acceleration and signal modeling to slice multiplexing and multiple echo times.
- Pages 183-214: Chapter 9, Artifact Recognition and Practical Troubleshooting. Convert artifact examples into a practical diagnostic vocabulary for fMRI data inspection.
- Pages 215-217: Chapter 10, System Drift and Diagnostic Strategy. Turn troubleshooting examples into a reproducible sequence of temporal checks, retests, hypotheses, and system adjustments.
- Pages 218-226: Chapter 11, Biological and Human Confounds in fMRI. Map nuisance mechanisms to experiment classes and to the auxiliary measurements that can make them interpretable.

## Figure Policy Applied

The figure plan was written before asset generation. The plan groups source pages into
pedagogical figures rather than treating each slide as an independent numbered figure.
Dense sequences are continued figures, and every generated asset contains no more than one
source panel by default so labels, arrows, legends, edge tags, and image-grid details remain readable.
