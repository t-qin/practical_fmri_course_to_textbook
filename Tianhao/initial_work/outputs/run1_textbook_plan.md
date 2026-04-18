# Practical fMRI Textbook Project — Run 1

## Goal of this run
This first run converts the source slide deck into a **textbook architecture** rather than prose slides. It provides:
1. a full conceptual table of contents,
2. a chapter-level slide-to-book mapping,
3. a figure integration strategy,
4. a staged writing plan for the next runs.

---

# Proposed textbook title
# **Practical fMRI: From NMR Foundations to EPI Artifacts, Advanced Acquisition, and Biological Confounds**

## Subtitle
A textbook-style reconstruction and expansion of the Ben Inglis fMRI course slides for long-term self-study.

---

# Front matter plan
1. **Title page**
2. **Preface**
   - What this book is
   - Who it is for
   - How to read it if you are new to MRI/fMRI
   - How figures, boxes, and troubleshooting sections are organized
3. **How to use this book**
   - Recommended reading order
   - How to use the troubleshooting and artifact sections
4. **Table of contents**

---

# Proposed textbook table of contents

## Chapter 1. Why MRI and fMRI Work: A Practical Orientation
### 1.1 Why start with spins?
### 1.2 What MRI measures versus what fMRI infers
### 1.3 Why EPI dominates fMRI despite its weaknesses
### 1.4 How this book connects physics, images, and practice
### 1.5 A roadmap from signal physics to confounds

## Chapter 2. Nuclear Magnetization, Precession, and the Rotating Frame
### 2.1 Net magnetization and spin population imbalance
### 2.2 The Larmor frequency and field strength
### 2.3 Boltzmann distribution and why MRI signal is intrinsically small
### 2.4 The rotating frame as a conceptual simplifier
### 2.5 Equilibrium magnetization before excitation
### 2.6 RF excitation and the B1 field
### 2.7 Flip angle and pulse duration
### 2.8 Magnetization immediately after excitation
### 2.9 Transverse magnetization and signal detection

## Chapter 3. Relaxation, Dephasing, T1, T2, and T2*
### 3.1 Why transverse magnetization decays
### 3.2 T2 as spin-spin dephasing
### 3.3 Signal induction and the observed NMR signal
### 3.4 The spin echo: refocusing reversible dephasing
### 3.5 Echo formation step by step
### 3.6 Longitudinal recovery and T1
### 3.7 Molecular origins of relaxation
### 3.8 Typical tissue T1 and T2 values at 3 T
### 3.9 Diffusion effects and their relation to T2 and T2*
### 3.10 Chemical shift as a consequence of electronic shielding

## Chapter 4. MRI Hardware and the Physical Scanner Environment
### 4.1 Main scanner components
### 4.2 The role of the main field B0
### 4.3 Gradient coils and spatial encoding power
### 4.4 RF transmit versus receive hardware
### 4.5 Receive coil arrays and why channel count matters
### 4.6 Receive field heterogeneity and its downstream consequences

## Chapter 5. Fourier Transform Intuition for MRI
### 5.1 Conjugate variables in MRI
### 5.2 What the Fourier transform does physically
### 5.3 Frequency content and signal decomposition
### 5.4 One-dimensional MRI as the cleanest entry point
### 5.5 Historical projection imaging intuition
### 5.6 From time-domain signal to spatial information
### 5.7 Why reciprocal space exists at all

## Chapter 6. Gradients, Slice Selection, and Basic MRI Image Formation
### 6.1 Magnetic field gradients as controlled spatial frequency encoders
### 6.2 Slice selection with sinc-modulated RF pulses
### 6.3 Slice thickness and RF/gradient tradeoffs
### 6.4 Slice-select rephasing
### 6.5 Gradient-echo readout basics
### 6.6 Readout evolution step by step
### 6.7 Core gradient-echo design considerations

## Chapter 7. K-Space: The Organizing Language of MRI
### 7.1 What k-space is and what it is not
### 7.2 Frequency encoding and movement through kx
### 7.3 Phase encoding and movement through ky
### 7.4 The MR signal under gradients
### 7.5 Why gradients trace trajectories through the Fourier domain
### 7.6 Building a full 2D k-space matrix
### 7.7 The 2D Fourier transform back to image space
### 7.8 What low and high spatial frequencies contribute
### 7.9 Resolution, blur, edge detail, and sampling limits
### 7.10 Aliasing and truncation artifact

## Chapter 8. Echo-Planar Imaging (EPI): Why fMRI Is Fast
### 8.1 EPI k-space traversal
### 8.2 Why EPI is efficient enough for fMRI
### 8.3 Echo spacing and temporal constraints during readout
### 8.4 The structural weakness of EPI: long readout, narrow effective bandwidth
### 8.5 Slice order and multislice EPI practicalities
### 8.6 EPI strengths and weaknesses in real experiments
### 8.7 Crusher gradients and slice-select details in EPI
### 8.8 What a good EPI dataset looks like
### 8.9 Temporal SNR as a practical quality metric

## Chapter 9. The Classic EPI Artifacts: Ghosting, Distortion, and Dropout
### 9.1 Why these three artifacts dominate practical fMRI
### 9.2 Nyquist ghosting: source, k-space origin, and image appearance
### 9.3 Why ghosts often appear at half the field of view
### 9.4 Time-varying ghosting and experimental consequences
### 9.5 Other causes of ghost-like signal contamination
### 9.6 Chemical shift and the need for scalp fat suppression
### 9.7 Ramp sampling and when readout acceleration goes too far
### 9.8 Distortion in the phase-encoded direction
### 9.9 Effective bandwidth in EPI
### 9.10 Phase-encoding direction choice: A-P versus P-A
### 9.11 Signal dropout: susceptibility-driven intravoxel dephasing
### 9.12 Why thin slices can reduce dropout
### 9.13 Tradeoffs among TE, resolution, coverage, and artifact burden

## Chapter 10. Susceptibility, Motion History, Inflow, and Receive-Field Confounds
### 10.1 Magnetic susceptibility as a spatially varying perturbation
### 10.2 Air-bone-brain interfaces and local gradients
### 10.3 Phase maps as evidence of field inhomogeneity
### 10.4 T2* and why fMRI depends on it
### 10.5 Spin history and flip-angle dependence
### 10.6 Inflow effects and non-BOLD signal changes
### 10.7 Flip angle effects on SNR and temporal SNR
### 10.8 Receive bias field effects and RFC-MoCo
### 10.9 Why rigid-body realignment is not a complete fix
### 10.10 Anchoring artifacts during motion correction

## Chapter 11. Accelerated and Advanced EPI Methods
### 11.1 Why acceleration methods are attractive in fMRI
### 11.2 Partial Fourier EPI and conjugate-symmetry logic
### 11.3 Early versus late partial Fourier
### 11.4 Speed gains, smoothing, and dropout tradeoffs
### 11.5 In-plane acceleration and GRAPPA
### 11.6 ACS lines and reconstruction logic
### 11.7 Motion sensitivity of GRAPPA
### 11.8 GRAPPA strengths and weaknesses
### 11.9 Simultaneous multi-slice (SMS) acquisition
### 11.10 Coil requirements for SMS separation
### 11.11 SMS pulse-sequence logic and limits
### 11.12 Multi-echo EPI
### 11.13 Weighted echo combination
### 11.14 Distinguishing BOLD from non-BOLD signal using TE dependence
### 11.15 Multi-echo pros and cons
### 11.16 FLEET and related stabilization strategies

## Chapter 12. Artifact Recognition, Quality Control, and Troubleshooting
### 12.1 The diagnostic mindset: physics + appearance + time course
### 12.2 Good axial EPI as a reference standard
### 12.3 Normal ghosting versus abnormal ghosting
### 12.4 Eye-movement and scalp-related ghosts
### 12.5 Standard-deviation images and instability mapping
### 12.6 Prescan normalize side effects
### 12.7 Residual aliasing in GRAPPA
### 12.8 Residual aliasing in SMS
### 12.9 Combined SMS + GRAPPA failures
### 12.10 Motion classes: eyes, head, speech, feet, external motion
### 12.11 Coil instability and how it presents
### 12.12 Motion in structural imaging (for example MP-RAGE)
### 12.13 Foreign objects and metallic contamination
### 12.14 RF interference and spike artifacts
### 12.15 Gradient spiking and phantom checks
### 12.16 RF coil spikes
### 12.17 System drift and chronic motion
### 12.18 A practical diagnostic checklist

## Chapter 13. Biological Confounds and Human Factors in fMRI
### 13.1 Biological mechanisms that mimic or modulate BOLD
### 13.2 Why nuisance importance depends on experiment type
### 13.3 Human factors as modifiers of confounds
### 13.4 Caffeine as a concrete case study
### 13.5 What physiological and behavioral variables matter most
### 13.6 Which auxiliary scans best capture confounds
### 13.7 What auxiliary non-imaging data are worth collecting pre/post scan
### 13.8 Practical interpretation rules for real studies

## Chapter 14. Integrative Practical Framework for Running and Interpreting fMRI
### 14.1 Connecting acquisition choices to artifact vulnerability
### 14.2 Connecting artifacts to downstream analysis risk
### 14.3 Choosing compromises for different study goals
### 14.4 A pre-scan, in-scan, and post-scan checklist
### 14.5 Final synthesis: from signal physics to experimental validity

---

# End matter plan
## Appendix A. Equation guide and symbol glossary
## Appendix B. Artifact troubleshooting tables
## Appendix C. Acquisition tradeoff summary tables
## Glossary
## Chapter review questions
## Index-like keyword list

---

# Source-to-chapter mapping

## Chapter 1. Why MRI and fMRI Work
**Primary source basis:** distributed framing material across pp. 1, 31, 86, 113-120, 185-226
**Function in the book:** create a coherent narrative bridge that the slides only imply.

## Chapters 2-3. NMR, relaxation, spin echo, T1/T2/T2*, chemical shift
**Primary source basis:** pp. 1-23
**Key source clusters:**
- pp. 2-10: net magnetization, Larmor, excitation, dephasing, signal detection
- pp. 11-16: spin-echo sequence logic
- pp. 17-20: T1, molecular origins, tissue values
- pp. 21-22: diffusion, T2, T2*, chemical shift

## Chapter 4. Hardware
**Primary source basis:** pp. 24-30

## Chapters 5-7. Fourier, gradients, slice selection, GRE, and k-space
**Primary source basis:** pp. 31-85
**Key source clusters:**
- pp. 32-43: FT and one-dimensional MRI intuition
- pp. 44-49: slice selection
- pp. 49-53: GRE formation
- pp. 54-78: k-space and encoding trajectories
- pp. 79-85: resolution, aliasing, truncation

## Chapters 8-9. EPI fundamentals and classic artifacts
**Primary source basis:** pp. 86-120
**Key source clusters:**
- pp. 87-96: EPI k-space and ghosting
- pp. 97-101: fat suppression, chemical shift, ramp sampling
- pp. 102-110: distortion, dropout, slice thickness
- pp. 111-120: slice order, EPI pros/cons, crusher gradients, good EPI, tSNR, transition to motion/susceptibility

## Chapter 10. Susceptibility, inflow, receive bias, motion-history effects
**Primary source basis:** pp. 121-139

## Chapter 11. Advanced EPI methods
**Primary source basis:** pp. 140-184
**Key source clusters:**
- pp. 141-158: partial Fourier
- pp. 159-168: GRAPPA / in-plane acceleration
- pp. 169-177: SMS
- pp. 178-182: multi-echo EPI
- p. 184: FLEET

## Chapter 12. Artifact recognition and QC troubleshooting
**Primary source basis:** pp. 185-217

## Chapters 13-14. Biological confounds, human factors, and integrative practical framework
**Primary source basis:** pp. 218-226, with backward links to pp. 119-139 and 185-217

---

# Figure integration plan

## Figure Cluster 1. Rotating-frame magnetization and excitation sequence
**Source pages:** 4-9
**Textbook treatment:**
- Multi-panel figure showing equilibrium magnetization, B1 application, flip-angle rotation, post-excitation transverse magnetization, and signal detection.
- Main text should explain what the rotating frame hides and what it reveals.

## Figure Cluster 2. Spin-echo formation sequence
**Source pages:** 11-16
**Textbook treatment:**
- One figure sequence with panels for excitation, free evolution, 180° pulse, refocusing, and echo formation.
- Use this to explicitly distinguish reversible dephasing from irreversible T2 decay.

## Figure Cluster 3. Relaxation and tissue-property comparison
**Source pages:** 17-22
**Textbook treatment:**
- Relaxation schematic plus table of approximate T1/T2 values.
- Expand into a prose explanation of why tissue contrasts emerge.

## Figure Cluster 4. MRI hardware and coil architecture
**Source pages:** 25-30
**Textbook treatment:**
- Scanner component overview figure.
- Separate figure for receive arrays and receive-field heterogeneity.
- Tie directly to later motion/bias-field confounds.

## Figure Cluster 5. Fourier and one-dimensional MRI intuition
**Source pages:** 32-43
**Textbook treatment:**
- Redrawn or cleaned conceptual figure sequence if necessary.
- Explain the transformation between spatial pattern and frequency-domain representation.

## Figure Cluster 6. Slice selection and gradient-echo formation
**Source pages:** 44-53
**Textbook treatment:**
- Multi-step figure with RF pulse, slice-selection gradient, refocusing lobe, and GRE timing logic.
- Consider converting sequence fragments into a single pedagogical diagram.

## Figure Cluster 7. K-space geometry and reconstruction logic
**Source pages:** 54-85
**Textbook treatment:**
- Several textbook figures:
  1. image space vs k-space,
  2. gradient-driven trajectory through k-space,
  3. effect of removing low or high spatial frequencies,
  4. aliasing/truncation examples.

## Figure Cluster 8. EPI traversal and ghosting
**Source pages:** 87-96
**Textbook treatment:**
- EPI zig-zag trajectory figure.
- Ghosting figure sequence showing ideal vs delayed lines and FOV/2 ghost outcome.
- Explicit caption about odd/even line mismatch.

## Figure Cluster 9. Chemical shift, ramp sampling, distortion, dropout
**Source pages:** 97-110
**Textbook treatment:**
- A compact artifact chapter figure set or subfigures.
- For each artifact, explain both **physics origin** and **image appearance**.

## Figure Cluster 10. Susceptibility and motion-linked signal instability
**Source pages:** 119-139
**Textbook treatment:**
- Phase-map/susceptibility examples.
- Flip-angle and inflow comparison figures.
- Receive-bias motion interaction figure set before/after motion correction.

## Figure Cluster 11. Partial Fourier reconstruction logic
**Source pages:** 141-158
**Textbook treatment:**
- Full vs partial k-space diagrams.
- Early vs late partial Fourier comparison.
- Figure or table on tradeoffs: speed, smoothing, dropout, phase-encode direction dependence.

## Figure Cluster 12. GRAPPA and parallel imaging
**Source pages:** 159-168
**Textbook treatment:**
- Coil-array dependence figure.
- R=2 trajectory and ACS-line calibration diagram.
- Motion sensitivity figure or box.

## Figure Cluster 13. SMS acquisition and limits
**Source pages:** 169-177
**Textbook treatment:**
- Simultaneous slice excitation and coil-based unaliasing figure.
- Example image panels demonstrating benefit and failure mode.

## Figure Cluster 14. Multi-echo EPI and BOLD discrimination
**Source pages:** 178-182
**Textbook treatment:**
- Echo combination schematic.
- Classification box for BOLD vs non-BOLD based on TE dependence.

## Figure Cluster 15. Artifact recognition atlas
**Source pages:** 187-214
**Textbook treatment:**
- A major textbook section with labeled example plates.
- Best handled as grouped figures by category: ghosting, aliasing, motion, coil/system instability, RF/gradient spikes, metal contamination.

## Figure Cluster 16. Confound summary tables and decision aids
**Source pages:** 219-226
**Textbook treatment:**
- Preserve as textbook tables where possible.
- Expand them into decision frameworks and practical checklists.

---

# Special textbook boxes to add during drafting
- **Why this matters** boxes for every chapter opening
- **Scanner implication** boxes for TE, PE direction, slice thickness, partial Fourier, GRAPPA, SMS, and multi-echo choices
- **Common confusion** boxes for T2 vs T2*, ghosting vs aliasing, dropout vs distortion, and motion correction misconceptions
- **Artifact recognition** boxes with symptom → likely cause → first diagnostic test
- **Tradeoff tables** for EPI, partial Fourier, GRAPPA, SMS, and ME-EPI
- **Key takeaway** panels at chapter ends

---

# Recommended 5-run writing plan

## Run 1 (current)
- Extract full source structure
- Propose textbook TOC
- Build figure integration plan
- Map slide ranges into chapters

## Run 2
- Draft Chapters 1-4
- Cover NMR foundations, relaxation, chemical shift, and hardware
- Include glossary seeds and first review-question set

## Run 3
- Draft Chapters 5-9
- Cover Fourier intuition, slice selection, k-space, EPI logic, and classic artifacts
- Integrate the largest core figure clusters

## Run 4
- Draft Chapters 10-12
- Cover susceptibility, motion-linked bias, advanced EPI methods, artifact recognition, QC, and troubleshooting

## Run 5
- Draft Chapters 13-14 plus front/back matter
- Add biological confounds, human factors, practical synthesis, glossary, review questions, tradeoff tables, and consistency cleanup

## Final polishing pass (can be merged into Run 5 if needed)
- Terminology consistency
- Figure numbering consistency
- Equation notation consistency
- Cross-references and chapter summaries
- PDF-ready formatting/export

---

# Coverage check
This structure is designed to retain all substantive source domains visible in the PDF:
- NMR fundamentals
- Relaxation and echo logic
- Hardware
- Fourier transform and gradients
- Slice selection and GRE
- k-space
- EPI physics
- Ghosting, chemical shift, distortion, dropout
- Motion, susceptibility, receive bias effects
- Partial Fourier, GRAPPA, SMS, multi-echo, FLEET
- Artifact recognition and QC
- Biological confounds and human factors

No major source block identified in the PDF is intentionally excluded.
