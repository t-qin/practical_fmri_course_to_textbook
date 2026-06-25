# Chapter Plan

Generated: 2026-05-13T02:53:17

This plan reorganizes the practical fMRI slide deck into a cumulative textbook. The chapter
boundaries follow the course's teaching progression, but sections are written as textbook
concept arcs rather than as slide-by-slide notes.

## Chapter 1. NMR Signal Formation

Source pages: 1-23.

Build the physical vocabulary for precession, excitation, relaxation, spin echoes, and chemical
shift.

Sections:

- Pages 1-3: Magnetization, Larmor precession, and signal strength. Purpose: connect B0, spin populations, and detectable net magnetization.
- Pages 4-8: RF excitation in the rotating frame. Purpose: show how B1 tips magnetization and why transverse phase coherence is temporary.
- Pages 9-16: Signal detection and echo formation. Purpose: follow dephasing, refocusing, and the signal that a receive coil can measure.
- Pages 17-22: Relaxation mechanisms and tissue constants. Purpose: separate T1, T2, T2-star, diffusion, and chemical-shift contributions.
- Pages 23-23: External learning resources. Purpose: preserve the optional video resources as back-matter references.

## Chapter 2. Scanner Hardware and Receive Fields

Source pages: 24-30.

Translate the physics vocabulary into the scanner components that polarize, excite, encode, and
receive signal.

Sections:

- Pages 24-27: System components. Purpose: identify magnet, gradient, RF, and room hardware roles.
- Pages 28-30: Receive arrays and spatial sensitivity. Purpose: explain why multi-channel coils improve sensitivity but introduce receive-field structure.

## Chapter 3. Fourier Thinking, Gradients, and K-space

Source pages: 31-85.

Develop the mathematical and practical path from frequency analysis to two-dimensional MRI.

Sections:

- Pages 31-38: Fourier pairs and frequency analysis. Purpose: turn waves into spectra and introduce reciprocal variables.
- Pages 39-43: Gradients as spatial encoders. Purpose: use the Larmor equation to make position affect frequency.
- Pages 44-48: Slice selection. Purpose: combine a selective RF pulse with a gradient and refocusing lobe.
- Pages 49-53: Gradient echoes and reversible dephasing. Purpose: show how gradient area moves phase out and back.
- Pages 54-65: K-space definitions. Purpose: connect gradient time integrals to k-space coordinates.
- Pages 66-75: Phase encoding and two-dimensional imaging. Purpose: fill a matrix of k-space samples and reconstruct an image.
- Pages 76-81: Spatial-frequency interpretation. Purpose: interpret low- and high-frequency k-space content.
- Pages 82-85: Artifact previews and stimulation limits. Purpose: link aliasing, truncation, and gradient switching to practical limits.

## Chapter 4. EPI Fundamentals and Classic Artifacts

Source pages: 86-124.

Explain why EPI is fast, why it is vulnerable, and how its characteristic artifacts arise.

Sections:

- Pages 86-88: Echo-planar k-space traversal. Purpose: frame EPI as a multiple-gradient-echo readout.
- Pages 89-97: Ghosting mechanisms. Purpose: derive the FOV/2 ghost and show common sources.
- Pages 98-101: Chemical shift and ramp sampling. Purpose: connect resonance offsets and read-gradient timing to ghost risk.
- Pages 102-106: Distortion and bandwidth. Purpose: explain phase-encoding displacement and direction reversals.
- Pages 107-113: Dropout and slice timing. Purpose: separate susceptibility dropout from slice-order artifacts.
- Pages 114-118: Real EPI sequence anatomy. Purpose: read a practical sequence diagram and quality images.
- Pages 119-124: Motion, susceptibility, and phase. Purpose: connect moving anatomy and air-tissue interfaces to EPI behavior.

## Chapter 5. Flip Angle, Inflow, and Receive-field Motion Effects

Source pages: 125-139.

Show how choices and hardware sensitivity fields convert physiology and motion into time-series
structure.

Sections:

- Pages 125-130: Spin history and inflow. Purpose: interpret flip-angle effects on BOLD amplitude, timing, SNR, and temporal SNR.
- Pages 131-136: Receive bias and motion correction. Purpose: explain why perfect rigid realignment can still leave signal modulation.
- Pages 137-139: Magnitude and mitigation of receive-field effects. Purpose: compare coil dependence and anchoring strategies.

## Chapter 6. Partial Fourier EPI

Source pages: 140-158.

Evaluate partial Fourier as an acceleration strategy with asymmetric consequences for TE,
slices, smoothing, and dropout.

Sections:

- Pages 140-145: Conjugate symmetry and reconstruction. Purpose: establish why a portion of k-space can be omitted.
- Pages 146-150: Early versus late echo omission. Purpose: compare the consequences of omitting early or late echoes.
- Pages 151-158: Image consequences and protocol tradeoffs. Purpose: integrate dropout, smoothing, phase-encoding direction, and pros/cons.

## Chapter 7. Parallel Imaging with GRAPPA

Source pages: 159-168.

Explain how coil arrays and calibration data support accelerated phase encoding, and why motion
can corrupt the result.

Sections:

- Pages 159-163: R=2 trajectories and calibration. Purpose: connect skipped k-space lines, coil arrays, and ACS data.
- Pages 164-166: Motion sensitivity. Purpose: distinguish ACS corruption from later reference mismatch.
- Pages 167-168: Protocol consequences. Purpose: weigh reduced distortion against SNR and motion cost.

## Chapter 8. Simultaneous Multi-slice and Multi-echo EPI

Source pages: 169-182.

Extend EPI acceleration and signal modeling to slice multiplexing and multiple echo times.

Sections:

- Pages 169-174: SMS requirements and reference data. Purpose: show why slice-axis coil diversity and SBRef data matter.
- Pages 175-177: SMS benefits and limits. Purpose: balance speed, contrast, motion sensitivity, and practical resolution.
- Pages 178-182: Multi-echo acquisition and classification. Purpose: explain weighted echo combination and BOLD/non-BOLD separation.

## Chapter 9. Artifact Recognition and Practical Troubleshooting

Source pages: 183-214.

Convert artifact examples into a practical diagnostic vocabulary for fMRI data inspection.

Sections:

- Pages 183-188: FLEET and artifact-recognition mindset. Purpose: connect calibration timing with the discipline of knowing good data.
- Pages 189-199: Ghosting, background, and aliasing examples. Purpose: recognize normal ghosts, scalp ghosts, PSN changes, GRAPPA aliasing, and SMS aliasing.
- Pages 200-208: Motion sources and mechanical instability. Purpose: distinguish head, eye, body, coil, animal, and anatomical-scan motion.
- Pages 209-214: Foreign objects, RF interference, and spiking. Purpose: separate metallic artifacts, RF pickup, gradient spikes, and coil spikes.

## Chapter 10. System Drift and Diagnostic Strategy

Source pages: 215-217.

Turn troubleshooting examples into a reproducible sequence of temporal checks, retests,
hypotheses, and system adjustments.

Sections:

- Pages 215-216: System drifts and chronic motion. Purpose: interpret slow changes in shim, sensitivity maps, and participant behavior.
- Pages 217-217: A practical diagnostic loop. Purpose: formalize short retests, hypothesis lists, and follow-up decisions.

## Chapter 11. Biological and Human Confounds in fMRI

Source pages: 218-226.

Map nuisance mechanisms to experiment classes and to the auxiliary measurements that can make
them interpretable.

Sections:

- Pages 218-220: Biological nuisance mechanisms. Purpose: organize vascular, respiratory, cardiac, and metabolic confounds.
- Pages 221-224: Human factors as modifiers. Purpose: connect caffeine and participant state to BOLD interpretation.
- Pages 225-226: MRI and auxiliary data for confounds. Purpose: decide which scans and pre/post measures help diagnose confounds.
