# Run 1 Source Extraction: `FMRI_course.pdf`

## Source overview
- **Source file:** `inputs/FMRI_course.pdf`
- **Author metadata:** Ben Inglis
- **Length:** 226 pages/slides
- **Overall character:** advanced practical MRI/fMRI teaching deck organized roughly by day blocks, moving from NMR foundations to MRI encoding, EPI physics/artifacts, accelerated EPI methods, troubleshooting/QC, and biological/human confounds.

## High-level topic blocks identified from the source PDF

### Block A. NMR and relaxation foundations (pp. 1-23)
Core topics visible in this block:
- Net magnetization and Larmor frequency
- Boltzmann population differences and field-strength dependence
- Rotating frame intuition
- RF excitation and flip angle logic
- Post-excitation dephasing and transverse magnetization
- Signal detection and induction
- T2 decay
- Spin echo formation step by step
- T1 relaxation and molecular origins of relaxation
- Approximate tissue T1/T2 values
- Diffusion, T2, and T2*
- Chemical shift

### Block B. MRI system components and hardware context (pp. 24-30)
Core topics visible in this block:
- Main MRI components
- Gradient coil role
- Receive coil arrays
- 32-channel coil example
- Receive field heterogeneity

### Block C. Fourier transform, gradients, slice selection, and k-space foundations (pp. 31-85)
Core topics visible in this block:
- Fourier transform and conjugate variables
- One-dimensional MRI intuition
- Historical first MRI projection logic
- Slice selection and sinc-RF relationship
- Slice thickness and slice-refocusing gradient
- Gradient echo readout buildup
- 2D k-space meaning
- Frequency encoding and phase encoding
- k-space trajectories under gradients
- Reconstructing 2D MRI from full k-space
- Interpreting k-space content
- Resolution limits, reduced resolution, high spatial frequencies only
- Aliasing, truncation artifact, stimulus limits

### Block D. EPI fundamentals and classic artifact physics (pp. 86-120)
Core topics visible in this block:
- EPI k-space traversal
- The three classic EPI artifacts
- Nyquist ghosting: mechanism, appearance, FOV/2 ghosts, temporal variation
- Other ghost sources
- Scalp fat suppression requirement
- Chemical shift origin and image manifestation
- Ramp sampling and echo-spacing tradeoffs
- Distortion in the phase-encode dimension
- EPI bandwidth logic
- A-P versus P-A phase encoding
- Signal dropout and why gradient-echo EPI is vulnerable
- Thin-slice tradeoffs for dropout mitigation
- Multi-slice EPI slice order
- EPI pros/cons
- Crusher gradients
- Good EPI and tSNR examples
- Motion reminder transition into instability topics

### Block E. Susceptibility, motion history, inflow, receive-bias motion interaction (pp. 121-139)
Core topics visible in this block:
- Magnetic susceptibility and intrinsic field gradients
- Air-bone-brain interfaces
- Phase maps and local field variation
- T2* relaxation consequences
- Flip angle/spin-history effects
- Inflow effects in fMRI
- Flip angle impact on SNR and temporal SNR
- Receive bias field effects / RFC-MoCo effect
- Perfect motion correction does not fully remove receive-field modulation
- Magnitude of motion-linked bias effects
- Anchoring during volume realignment

### Block F. Partial Fourier, parallel imaging, SMS, multi-echo, and advanced EPI methods (pp. 140-184)
Core topics visible in this block:
- Full k-space versus partial Fourier EPI
- Conjugate symmetry intuition for omitted k-space
- Early vs late partial Fourier
- Speed gains and dropout tradeoffs
- Smoothing consequences of partial Fourier
- In-plane acceleration / GRAPPA
- GRAPPA trajectory, coil dependence, ACS lines
- GRAPPA motion sensitivity
- GRAPPA pros/cons
- Simultaneous multi-slice (SMS)
- Need for phased-array coil structure along slice axis
- SMS pulse sequence concept
- SMS examples and failure limits
- Multi-echo EPI and weighted echo combination
- BOLD vs non-BOLD classification logic
- Multi-echo pros/cons
- FLEET (Fast Low-angle Excitation Echo-planar Technique)

### Block G. Artifact recognition, troubleshooting, QC, and scanner stability (pp. 185-217)
Core topics visible in this block:
- Practical diagnostic mindset
- Artifact recognition by image appearance
- Good axial EPI references/examples
- Normal ghosting vs scalp ghosts
- Eye-movement ghosts
- Standard-deviation image interpretation
- Prescan normalize effects
- Residual aliasing in GRAPPA and SMS
- SMS+GRAPPA combined artifacts
- Good EPI and tSNR examples revisited
- Movement classes: eyes, head, talking, feet, third-party movement
- Coil instability
- Motion in MP-RAGE
- Foreign objects / metal
- RF interference
- Gradient spiking and phantom checks
- RF coil spikes
- System drifts and chronic motion
- Tactics for diagnosis

### Block H. Biological confounds and human factors in fMRI interpretation (pp. 218-226)
Core topics visible in this block:
- Biological mechanisms
- Relative importance of nuisance variables across experiment classes
- Human factors as modifiers
- Caffeine effects
- Relative importance of human-factor modifiers of confounds
- Relative utility of MRI scans to capture biological confounds
- Relative importance of auxiliary pre/post-scan data collection

## Notes on source style
- The PDF is **highly visual** and often uses short labels, figure sequences, and image examples rather than full prose.
- Many pages are conceptually dense but text-light; these will require **substantial expansion** in textbook form.
- Several slide sequences function as animations in static form (for example, spin echo buildup, gradient action in k-space, partial Fourier reconstruction, GRAPPA/SMS logic, and artifact comparison sets). These should become multi-panel figure explanations in the book.

## Immediate textbook implications
The final book should not follow the slide order literally. A better pedagogical ordering is:
1. NMR and relaxation fundamentals
2. MRI hardware context
3. Fourier intuition and spatial encoding
4. Slice selection, gradients, and basic image formation
5. EPI readout and why it is fast but fragile
6. Artifact mechanisms and image signatures
7. Advanced EPI acceleration methods
8. Motion, instability, and QC troubleshooting
9. Biological confounds and experiment-level interpretation

## Supporting extraction file
- `notes/page_titles.tsv` contains a page-by-page first-line extraction to support later detailed mapping.
