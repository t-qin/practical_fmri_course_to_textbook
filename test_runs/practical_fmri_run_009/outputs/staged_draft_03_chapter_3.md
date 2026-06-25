# Chapter 3. Fourier Thinking, Gradients, and K-space

This chapter covers source pages 31-85 and turns them into a self-study sequence about develop
the mathematical and practical path from frequency analysis to two-dimensional mri. The chapter
is organized by mechanism and scanning consequence, not by slide order alone, so figures appear
where they support the local explanation.

## Fourier pairs and frequency analysis

Fourier pairs and frequency analysis is the local bridge between the course vocabulary and a
self-study explanation. The relevant source ideas include Day Two; Morning; Fundamentals of MRI;
Conjugate variables:; Conjugate variables are related through; a Fourier transform:; Frequency
(Hz, or s-1) Û time (s); Space (cm) Û k-space (cm-1); F.T.; Fourier transform:; The analysis of
frequency content; The FT can determine the frequency content of. Taken together, they should be
read as one argument about turn waves into spectra and introduce reciprocal variables. The
textbook version therefore slows the slide sequence down: first define the measured or
manipulated quantity, then state what changes it, and only then connect the change to image
appearance or fMRI interpretation.

In this part of fourier thinking, gradients, and k-space, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For fourier pairs and frequency analysis,
that chain starts with the controlled scanner quantity, passes through spin phase or signal
weighting, and ends as a spatial pattern, time-series change, or acquisition tradeoff. If the
chain is left implicit, the same term can be memorized without being understood.

A useful way to study fourier pairs and frequency analysis is to ask three questions for every
equation or panel. What quantity is deliberately controlled in Chapter 3's local sequence or
example? What uncontrolled physical or biological quantity can perturb it? What image-space or
time-series signature would reveal the problem? These questions keep the mathematics connected
to practical fMRI, where protocol choices are judged by SNR, temporal stability, distortion,
dropout, timing, and interpretability rather than by elegance alone.

The source pages named Day Two, Conjugate variables:, Fourier transform:, The FT can determine
the frequency content of, Image-only teaching panel 35, and related panels also show why MRI
explanations often require several levels. At the microscopic level, spins precess, relax,
dephase, or refocus. At the sequence level, RF pulses and gradients impose timing and spatial
encoding. At the reconstruction level, Fourier relationships convert sampled signals into
images. At the experimental level, subject motion, physiology, hardware stability, and human
factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate fourier pairs and frequency analysis without
using slide shorthand. The restatement should include the relevant variables, the direction of
the effect, and the likely failure mode. A good explanation is specific enough to predict what
would happen if the field strength, gradient area, echo spacing, flip angle, coil sensitivity,
motion state, or nuisance measurement changed.

## Figure 3.1. Fourier transform intuition and useful pairs

![Figure 3.1 panel](figures/fig_3_1_panel_01_source_032.png)

![Figure 3.1 panel](figures/fig_3_1_panel_02_source_033.png)

![Figure 3.1 panel](figures/fig_3_1_panel_03_source_034.png)

![Figure 3.1 panel](figures/fig_3_1_panel_04_source_035.png)

![Figure 3.1 panel](figures/fig_3_1_panel_05_source_036.png)

![Figure 3.1 panel](figures/fig_3_1_panel_06_source_037.png)

![Figure 3.1 panel](figures/fig_3_1_panel_07_source_038.png)

**Figure 3.1. Fourier transform intuition and useful pairs.** Frequency analysis, conjugate variables, and visual Fourier pairs used later for k-space. Source pages 32-38 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Conjugate variables:; Conjugate variables are related through; a Fourier transform:; Frequency (Hz, or s-1) Û time (s); Space (cm) Û k-space (cm-1); F.T.; Fourier transform:; The analysis of frequency content.

This figure should be read as a sequence inside Chapter 3, not as an isolated picture. It begins
with conjugate variables: and ends with some useful, so the reader can follow how the local idea
changes across the source panels. The retained source-backed panels are used here because the
original annotations are part of the evidence: the reader needs the labels, axes, arrows, image
examples, and comparison tags to see why the mechanism matters.

The practical lesson is frequency analysis, conjugate variables, and visual fourier pairs used
later for k-space. In a scanner context, the important move is to translate what is drawn into
an acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 3.1, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label fourier transform
intuition and useful pairs as a diagnosis before checking the visual evidence.

## Gradients as spatial encoders

Gradients as spatial encoders is the local bridge between the course vocabulary and a self-study
explanation. The relevant source ideas include Magnetic field gradient:; Start with the Larmor
equation:; w0 = gB0; Add a gradient Gx along the x; direction:; wx = g (B0 + Gx x); One-
dimensional MRI:; x1x2 ……............ xn; omega1omega2 ……........... omegan; Fourier transform
of the signal:; x1x2 ……….….. xn; s(w). Taken together, they should be read as one argument about
use the Larmor equation to make position affect frequency. The textbook version therefore slows
the slide sequence down: first define the measured or manipulated quantity, then state what
changes it, and only then connect the change to image appearance or fMRI interpretation.

In this part of fourier thinking, gradients, and k-space, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For gradients as spatial encoders, that
chain starts with the controlled scanner quantity, passes through spin phase or signal
weighting, and ends as a spatial pattern, time-series change, or acquisition tradeoff. If the
chain is left implicit, the same term can be memorized without being understood.

A useful way to study gradients as spatial encoders is to ask three questions for every equation
or panel. What quantity is deliberately controlled in Chapter 3's local sequence or example?
What uncontrolled physical or biological quantity can perturb it? What image-space or time-
series signature would reveal the problem? These questions keep the mathematics connected to
practical fMRI, where protocol choices are judged by SNR, temporal stability, distortion,
dropout, timing, and interpretability rather than by elegance alone.

The source pages named Magnetic field gradient:, One-dimensional MRI:, Fourier transform of the
signal:, Other 1D Projections:, The first MRI also show why MRI explanations often require
several levels. At the microscopic level, spins precess, relax, dephase, or refocus. At the
sequence level, RF pulses and gradients impose timing and spatial encoding. At the
reconstruction level, Fourier relationships convert sampled signals into images. At the
experimental level, subject motion, physiology, hardware stability, and human factors determine
whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate gradients as spatial encoders without using
slide shorthand. The restatement should include the relevant variables, the direction of the
effect, and the likely failure mode. A good explanation is specific enough to predict what would
happen if the field strength, gradient area, echo spacing, flip angle, coil sensitivity, motion
state, or nuisance measurement changed.

## Figure 3.2. Gradients as one-dimensional spatial encoders

![Figure 3.2 panel](figures/fig_3_2_panel_01_source_039.png)

![Figure 3.2 panel](figures/fig_3_2_panel_02_source_040.png)

![Figure 3.2 panel](figures/fig_3_2_panel_03_source_041.png)

![Figure 3.2 panel](figures/fig_3_2_panel_04_source_042.png)

![Figure 3.2 panel](figures/fig_3_2_panel_05_source_043.png)

**Figure 3.2. Gradients as one-dimensional spatial encoders.** The Larmor equation with a gradient and the historical bridge to projection imaging. Source pages 39-43 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Magnetic field gradient:; Start with the Larmor equation:; w0 = gB0; Add a gradient Gx along the x; direction:; wx = g (B0 + Gx x); One-dimensional MRI:; x1x2 ……............ xn.

This figure should be read as a sequence inside Chapter 3, not as an isolated picture. It begins
with magnetic field gradient: and ends with the first mri, so the reader can follow how the
local idea changes across the source panels. The retained source-backed panels are used here
because the original annotations are part of the evidence: the reader needs the labels, axes,
arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is the larmor equation with a gradient and the historical bridge to
projection imaging. In a scanner context, the important move is to translate what is drawn into
an acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 3.2, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label gradients as one-
dimensional spatial encoders as a diagnosis before checking the visual evidence.

## Slice selection

Slice selection is the local bridge between the course vocabulary and a self-study explanation.
The relevant source ideas include Slice selection; Recall that the Fourier transform of a sinc;
function is a square (or top hat) and vice versa; Instead of using an on-off (square) RF pulse;
for excitation, if we use a sinc-shaped RF; pulse then we can select a square "notch" of;
frequencies centered about the frequency of; If the sinc-modulated RF pulse is; played out while
a gradient is on along; z, the notch of frequencies Deltan; corresponds to a spatial notch of
width; Dz. This is a slice, of thickness Dz.. Taken together, they should be read as one
argument about combine a selective RF pulse with a gradient and refocusing lobe. The textbook
version therefore slows the slide sequence down: first define the measured or manipulated
quantity, then state what changes it, and only then connect the change to image appearance or
fMRI interpretation.

In this part of fourier thinking, gradients, and k-space, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For slice selection, that chain starts with
the controlled scanner quantity, passes through spin phase or signal weighting, and ends as a
spatial pattern, time-series change, or acquisition tradeoff. If the chain is left implicit, the
same term can be memorized without being understood.

A useful way to study slice selection is to ask three questions for every equation or panel.
What quantity is deliberately controlled in Chapter 3's local sequence or example? What
uncontrolled physical or biological quantity can perturb it? What image-space or time-series
signature would reveal the problem? These questions keep the mathematics connected to practical
fMRI, where protocol choices are judged by SNR, temporal stability, distortion, dropout, timing,
and interpretability rather than by elegance alone.

The source pages named Slice selection, - Recall that the Fourier transform of a sinc, If the
sinc-modulated RF pulse is, Slice thickness:, Slice selection also needs a refocusing also show
why MRI explanations often require several levels. At the microscopic level, spins precess,
relax, dephase, or refocus. At the sequence level, RF pulses and gradients impose timing and
spatial encoding. At the reconstruction level, Fourier relationships convert sampled signals
into images. At the experimental level, subject motion, physiology, hardware stability, and
human factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate slice selection without using slide
shorthand. The restatement should include the relevant variables, the direction of the effect,
and the likely failure mode. A good explanation is specific enough to predict what would happen
if the field strength, gradient area, echo spacing, flip angle, coil sensitivity, motion state,
or nuisance measurement changed.

## Figure 3.3. Slice selection with a sinc RF pulse

![Figure 3.3 panel](figures/fig_3_3_panel_01_source_044.png)

![Figure 3.3 panel](figures/fig_3_3_panel_02_source_045.png)

![Figure 3.3 panel](figures/fig_3_3_panel_03_source_046.png)

![Figure 3.3 panel](figures/fig_3_3_panel_04_source_047.png)

![Figure 3.3 panel](figures/fig_3_3_panel_05_source_048.png)

**Figure 3.3. Slice selection with a sinc RF pulse.** How RF bandwidth and z-gradient strength define slice thickness and require refocusing. Source pages 44-48 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Slice selection; Recall that the Fourier transform of a sinc; function is a square (or top hat) and vice versa; Instead of using an on-off (square) RF pulse; for excitation, if we use a sinc-shaped RF; pulse then we can select a square "notch" of; frequencies centered about the frequency of; If the sinc-modulated RF pulse is.

This figure should be read as a sequence inside Chapter 3, not as an isolated picture. It begins
with slice selection and ends with slice selection also needs a refocusing, so the reader can
follow how the local idea changes across the source panels. The retained source-backed panels
are used here because the original annotations are part of the evidence: the reader needs the
labels, axes, arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is how rf bandwidth and z-gradient strength define slice thickness and
require refocusing. In a scanner context, the important move is to translate what is drawn into
an acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 3.3, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label slice selection with a
sinc rf pulse as a diagnosis before checking the visual evidence.

## Gradient echoes and reversible dephasing

Gradient echoes and reversible dephasing is the local bridge between the course vocabulary and a
self-study explanation. The relevant source ideas include Gradient echo for readout:; The
dephasing effect of; gradient 1 can be undone by; reversing the direction of the; gradient 2;
After 1:; w0 = 0; wx1 = - g Gx x1; wx2 = g Gx x2; GRE considerations:; Acquiring the rephasing
plus the dephasing; magnetization (segments 2 + 3) provides ~sqrt(2). Taken together, they
should be read as one argument about show how gradient area moves phase out and back. The
textbook version therefore slows the slide sequence down: first define the measured or
manipulated quantity, then state what changes it, and only then connect the change to image
appearance or fMRI interpretation.

In this part of fourier thinking, gradients, and k-space, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For gradient echoes and reversible
dephasing, that chain starts with the controlled scanner quantity, passes through spin phase or
signal weighting, and ends as a spatial pattern, time-series change, or acquisition tradeoff. If
the chain is left implicit, the same term can be memorized without being understood.

A useful way to study gradient echoes and reversible dephasing is to ask three questions for
every equation or panel. What quantity is deliberately controlled in Chapter 3's local sequence
or example? What uncontrolled physical or biological quantity can perturb it? What image-space
or time-series signature would reveal the problem? These questions keep the mathematics
connected to practical fMRI, where protocol choices are judged by SNR, temporal stability,
distortion, dropout, timing, and interpretability rather than by elegance alone.

The source pages named Gradient echo for readout:, After 1:, After 1:, After 1:, GRE
considerations: also show why MRI explanations often require several levels. At the microscopic
level, spins precess, relax, dephase, or refocus. At the sequence level, RF pulses and gradients
impose timing and spatial encoding. At the reconstruction level, Fourier relationships convert
sampled signals into images. At the experimental level, subject motion, physiology, hardware
stability, and human factors determine whether the image series supports a defensible fMRI
interpretation.

For practice, the reader should be able to restate gradient echoes and reversible dephasing
without using slide shorthand. The restatement should include the relevant variables, the
direction of the effect, and the likely failure mode. A good explanation is specific enough to
predict what would happen if the field strength, gradient area, echo spacing, flip angle, coil
sensitivity, motion state, or nuisance measurement changed.

## Figure 3.4. Gradient echoes and reversible phase dispersion

![Figure 3.4 panel](figures/fig_3_4_panel_01_source_049.png)

![Figure 3.4 panel](figures/fig_3_4_panel_02_source_050.png)

![Figure 3.4 panel](figures/fig_3_4_panel_03_source_051.png)

![Figure 3.4 panel](figures/fig_3_4_panel_04_source_052.png)

![Figure 3.4 panel](figures/fig_3_4_panel_05_source_053.png)

**Figure 3.4. Gradient echoes and reversible phase dispersion.** The timing logic that dephases and rephases spins under a readout gradient. Source pages 49-53 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Gradient echo for readout:; The dephasing effect of; gradient 1 can be undone by; reversing the direction of the; gradient 2; After 1:; w0 = 0; wx1 = - g Gx x1.

This figure should be read as a sequence inside Chapter 3, not as an isolated picture. It begins
with gradient echo for readout: and ends with gre considerations:, so the reader can follow how
the local idea changes across the source panels. The retained source-backed panels are used here
because the original annotations are part of the evidence: the reader needs the labels, axes,
arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is the timing logic that dephases and rephases spins under a readout
gradient. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 3.4, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label gradient echoes and
reversible phase dispersion as a diagnosis before checking the visual evidence.

## K-space definitions

K-space definitions is the local bridge between the course vocabulary and a self-study
explanation. The relevant source ideas include K-space:; A useful pictorial representation of;
imaging pulse sequences; Take the 2D FT of a random image, we get its; representation in
reciprocal (k) space:; Fourier transforms for the x and kx dimensions:; y and ky can be
transformed analogously.; We will return to this seemingly arbitrary set of equations in a
moment.; But first…..; "Signal"; Image; Reconsider a frequency encoding gradient:. Taken
together, they should be read as one argument about connect gradient time integrals to k-space
coordinates. The textbook version therefore slows the slide sequence down: first define the
measured or manipulated quantity, then state what changes it, and only then connect the change
to image appearance or fMRI interpretation.

In this part of fourier thinking, gradients, and k-space, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For k-space definitions, that chain starts
with the controlled scanner quantity, passes through spin phase or signal weighting, and ends as
a spatial pattern, time-series change, or acquisition tradeoff. If the chain is left implicit,
the same term can be memorized without being understood.

A useful way to study k-space definitions is to ask three questions for every equation or panel.
What quantity is deliberately controlled in Chapter 3's local sequence or example? What
uncontrolled physical or biological quantity can perturb it? What image-space or time-series
signature would reveal the problem? These questions keep the mathematics connected to practical
fMRI, where protocol choices are judged by SNR, temporal stability, distortion, dropout, timing,
and interpretability rather than by elegance alone.

The source pages named K-space:, Take the 2D FT of a random image, we get its, Fourier
transforms for the x and kx dimensions:, Reconsider a frequency encoding gradient:, The MR
signal under Gx:, and related panels also show why MRI explanations often require several
levels. At the microscopic level, spins precess, relax, dephase, or refocus. At the sequence
level, RF pulses and gradients impose timing and spatial encoding. At the reconstruction level,
Fourier relationships convert sampled signals into images. At the experimental level, subject
motion, physiology, hardware stability, and human factors determine whether the image series
supports a defensible fMRI interpretation.

For practice, the reader should be able to restate k-space definitions without using slide
shorthand. The restatement should include the relevant variables, the direction of the effect,
and the likely failure mode. A good explanation is specific enough to predict what would happen
if the field strength, gradient area, echo spacing, flip angle, coil sensitivity, motion state,
or nuisance measurement changed.

## Figure 3.5. K-space as the Fourier representation of the image

![Figure 3.5 panel](figures/fig_3_5_panel_01_source_054.png)

![Figure 3.5 panel](figures/fig_3_5_panel_02_source_055.png)

![Figure 3.5 panel](figures/fig_3_5_panel_03_source_056.png)

![Figure 3.5 panel](figures/fig_3_5_panel_04_source_057.png)

![Figure 3.5 panel](figures/fig_3_5_panel_05_source_058.png)

![Figure 3.5 panel](figures/fig_3_5_panel_06_source_059.png)

![Figure 3.5 panel](figures/fig_3_5_panel_07_source_060.png)

**Figure 3.5. K-space as the Fourier representation of the image.** From the image Fourier transform to kx as gamma times gradient area. Source pages 54-60 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: K-space:; A useful pictorial representation of; imaging pulse sequences; Take the 2D FT of a random image, we get its; representation in reciprocal (k) space:; Fourier transforms for the x and kx dimensions:; y and ky can be transformed analogously.; We will return to this seemingly arbitrary set of equations in a moment..

This figure should be read as a sequence inside Chapter 3, not as an isolated picture. It begins
with k-space: and ends with for the x dimension only, so the reader can follow how the local
idea changes across the source panels. The retained source-backed panels are used here because
the original annotations are part of the evidence: the reader needs the labels, axes, arrows,
image examples, and comparison tags to see why the mechanism matters.

The practical lesson is from the image fourier transform to kx as gamma times gradient area. In
a scanner context, the important move is to translate what is drawn into an acquisition
consequence: which gradient is acting, which echo or reference data are being trusted, which
bandwidth or timing choice is limiting, or which image pattern would appear during quality
control.

For Figure 3.5, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label k-space as the fourier
representation of the image as a diagnosis before checking the visual evidence.

## Figure 3.6. Gradient area as a k-space trajectory

![Figure 3.6 panel](figures/fig_3_6_panel_01_source_061.png)

![Figure 3.6 panel](figures/fig_3_6_panel_02_source_062.png)

![Figure 3.6 panel](figures/fig_3_6_panel_03_source_063.png)

![Figure 3.6 panel](figures/fig_3_6_panel_04_source_064.png)

![Figure 3.6 panel](figures/fig_3_6_panel_05_source_065.png)

**Figure 3.6. Gradient area as a k-space trajectory.** Mental integration of pulse-sequence gradients into motion through k-space. Source pages 61-65 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Note that kx changes with time depending on Gx; because we defined: kx = g Gx t; When Gx is off then kx is static.; When Gx is on, the value of kx changes with the; magnitude of Gx and the time Gx has been on.; We can make kx change more rapidly or more; The action of Gx is to trace a path through the; FT of the image:.

This figure should be read as a sequence inside Chapter 3, not as an isolated picture. It begins
with note that kx changes with time depending on gx and ends with -, so the reader can follow
how the local idea changes across the source panels. The retained source-backed panels are used
here because the original annotations are part of the evidence: the reader needs the labels,
axes, arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is mental integration of pulse-sequence gradients into motion through
k-space. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 3.6, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label gradient area as a
k-space trajectory as a diagnosis before checking the visual evidence.

## Phase encoding and two-dimensional imaging

Phase encoding and two-dimensional imaging is the local bridge between the course vocabulary and
a self-study explanation. The relevant source ideas include Phase encoding as seen in 2D
k-space; Consider a second gradient episode, Gy in the pulse sequence; below. We call this the
phase encoding gradient because we will; encode spatial information as phase in y.; S(t) =
integral M(y) e i g Gy t y.dy; becomes; S(ky) = integral M(y) e i ky y.dy; where; ky = g Gy t;
90 degrees; How would we do this?; The green lines hit 16x16 points on this 2D k-space grid,.
Taken together, they should be read as one argument about fill a matrix of k-space samples and
reconstruct an image. The textbook version therefore slows the slide sequence down: first define
the measured or manipulated quantity, then state what changes it, and only then connect the
change to image appearance or fMRI interpretation.

In this part of fourier thinking, gradients, and k-space, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For phase encoding and two-dimensional
imaging, that chain starts with the controlled scanner quantity, passes through spin phase or
signal weighting, and ends as a spatial pattern, time-series change, or acquisition tradeoff. If
the chain is left implicit, the same term can be memorized without being understood.

A useful way to study phase encoding and two-dimensional imaging is to ask three questions for
every equation or panel. What quantity is deliberately controlled in Chapter 3's local sequence
or example? What uncontrolled physical or biological quantity can perturb it? What image-space
or time-series signature would reveal the problem? These questions keep the mathematics
connected to practical fMRI, where protocol choices are judged by SNR, temporal stability,
distortion, dropout, timing, and interpretability rather than by elegance alone.

The source pages named Phase encoding as seen in 2D k-space, S(t) = integral M(y) e i g Gy t
y.dy, RF, How would we do this?, Image-only teaching panel 70, and related panels also show why
MRI explanations often require several levels. At the microscopic level, spins precess, relax,
dephase, or refocus. At the sequence level, RF pulses and gradients impose timing and spatial
encoding. At the reconstruction level, Fourier relationships convert sampled signals into
images. At the experimental level, subject motion, physiology, hardware stability, and human
factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate phase encoding and two-dimensional imaging
without using slide shorthand. The restatement should include the relevant variables, the
direction of the effect, and the likely failure mode. A good explanation is specific enough to
predict what would happen if the field strength, gradient area, echo spacing, flip angle, coil
sensitivity, motion state, or nuisance measurement changed.

## Figure 3.7. Phase encoding and two-dimensional k-space filling

![Figure 3.7 panel](figures/fig_3_7_panel_01_source_066.png)

![Figure 3.7 panel](figures/fig_3_7_panel_02_source_067.png)

![Figure 3.7 panel](figures/fig_3_7_panel_03_source_068.png)

![Figure 3.7 panel](figures/fig_3_7_panel_04_source_069.png)

**Figure 3.7. Phase encoding and two-dimensional k-space filling.** How Gy selects a ky line and Gx reads across kx. Source pages 66-69 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Phase encoding as seen in 2D k-space; Consider a second gradient episode, Gy in the pulse sequence; below. We call this the phase encoding gradient because we will; encode spatial information as phase in y.; S(t) = integral M(y) e i g Gy t y.dy; becomes; S(ky) = integral M(y) e i ky y.dy; where.

This figure should be read as a sequence inside Chapter 3, not as an isolated picture. It begins
with phase encoding as seen in 2d k-space and ends with how would we do this?, so the reader can
follow how the local idea changes across the source panels. The retained source-backed panels
are used here because the original annotations are part of the evidence: the reader needs the
labels, axes, arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is how gy selects a ky line and gx reads across kx. In a scanner context,
the important move is to translate what is drawn into an acquisition consequence: which gradient
is acting, which echo or reference data are being trusted, which bandwidth or timing choice is
limiting, or which image pattern would appear during quality control.

For Figure 3.7, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label phase encoding and two-
dimensional k-space filling as a diagnosis before checking the visual evidence.

## Figure 3.8. A full gradient-echo sequence samples a 2D matrix

![Figure 3.8 panel](figures/fig_3_8_panel_01_source_070.png)

![Figure 3.8 panel](figures/fig_3_8_panel_02_source_071.png)

![Figure 3.8 panel](figures/fig_3_8_panel_03_source_072.png)

![Figure 3.8 panel](figures/fig_3_8_panel_04_source_073.png)

![Figure 3.8 panel](figures/fig_3_8_panel_05_source_074.png)

![Figure 3.8 panel](figures/fig_3_8_panel_06_source_075.png)

**Figure 3.8. A full gradient-echo sequence samples a 2D matrix.** The repeated phase-encoding steps that fill k-space before a 2D Fourier transform. Source pages 70-75 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Image-only teaching panel 70; Image-only teaching panel 71; Image-only teaching panel 72; Image-only teaching panel 73; 2D FT of this full k-space matrix produces a 2D MRI; 2D MRI: The steps; 1. Select a slice; 2. Fill the k-space.

This figure should be read as a sequence inside Chapter 3, not as an isolated picture. It begins
with image-only teaching panel 70 and ends with 2d mri: the steps, so the reader can follow how
the local idea changes across the source panels. The retained source-backed panels are used here
because the original annotations are part of the evidence: the reader needs the labels, axes,
arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is the repeated phase-encoding steps that fill k-space before a 2d fourier
transform. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 3.8, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label a full gradient-echo
sequence samples a 2d matrix as a diagnosis before checking the visual evidence.

## Spatial-frequency interpretation

Spatial-frequency interpretation is the local bridge between the course vocabulary and a self-
study explanation. The relevant source ideas include The k parameter is simply the time-integral
of a gradient; multiplied by a coefficient, g/2p :; We can now see that in MRI, the conjugate
variable for; space is the gradient area. So, if we know what gradients; are being applied, we
can easily relate them to the image; we will obtain!; Space; K-space; Putting it all together:
2D MRI; What can we tell from k-space?; We need a full k-space; matrix for the complete. Taken
together, they should be read as one argument about interpret low- and high-frequency k-space
content. The textbook version therefore slows the slide sequence down: first define the measured
or manipulated quantity, then state what changes it, and only then connect the change to image
appearance or fMRI interpretation.

In this part of fourier thinking, gradients, and k-space, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For spatial-frequency interpretation, that
chain starts with the controlled scanner quantity, passes through spin phase or signal
weighting, and ends as a spatial pattern, time-series change, or acquisition tradeoff. If the
chain is left implicit, the same term can be memorized without being understood.

A useful way to study spatial-frequency interpretation is to ask three questions for every
equation or panel. What quantity is deliberately controlled in Chapter 3's local sequence or
example? What uncontrolled physical or biological quantity can perturb it? What image-space or
time-series signature would reveal the problem? These questions keep the mathematics connected
to practical fMRI, where protocol choices are judged by SNR, temporal stability, distortion,
dropout, timing, and interpretability rather than by elegance alone.

The source pages named The k parameter is simply the time-integral of a gradient, Space, What
can we tell from k-space?, Image-only teaching panel 79, Reduced resolution, and related panels
also show why MRI explanations often require several levels. At the microscopic level, spins
precess, relax, dephase, or refocus. At the sequence level, RF pulses and gradients impose
timing and spatial encoding. At the reconstruction level, Fourier relationships convert sampled
signals into images. At the experimental level, subject motion, physiology, hardware stability,
and human factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate spatial-frequency interpretation without
using slide shorthand. The restatement should include the relevant variables, the direction of
the effect, and the likely failure mode. A good explanation is specific enough to predict what
would happen if the field strength, gradient area, echo spacing, flip angle, coil sensitivity,
motion state, or nuisance measurement changed.

## Figure 3.9. Spatial frequency, resolution, and k-space content

![Figure 3.9 panel](figures/fig_3_9_panel_01_source_076.png)

![Figure 3.9 panel](figures/fig_3_9_panel_02_source_077.png)

![Figure 3.9 panel](figures/fig_3_9_panel_03_source_078.png)

![Figure 3.9 panel](figures/fig_3_9_panel_04_source_079.png)

![Figure 3.9 panel](figures/fig_3_9_panel_05_source_080.png)

![Figure 3.9 panel](figures/fig_3_9_panel_06_source_081.png)

**Figure 3.9. Spatial frequency, resolution, and k-space content.** The image consequences of central versus peripheral k-space. Source pages 76-81 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: The k parameter is simply the time-integral of a gradient; multiplied by a coefficient, g/2p :; We can now see that in MRI, the conjugate variable for; space is the gradient area. So, if we know what gradients; are being applied, we can easily relate them to the image; we will obtain!; Space; K-space.

This figure should be read as a sequence inside Chapter 3, not as an isolated picture. It begins
with the k parameter is simply the time-integral of a gradient and ends with only high spatial
frequencies, so the reader can follow how the local idea changes across the source panels. The
retained source-backed panels are used here because the original annotations are part of the
evidence: the reader needs the labels, axes, arrows, image examples, and comparison tags to see
why the mechanism matters.

The practical lesson is the image consequences of central versus peripheral k-space. In a
scanner context, the important move is to translate what is drawn into an acquisition
consequence: which gradient is acting, which echo or reference data are being trusted, which
bandwidth or timing choice is limiting, or which image pattern would appear during quality
control.

For Figure 3.9, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label spatial frequency,
resolution, and k-space content as a diagnosis before checking the visual evidence.

## Artifact previews and stimulation limits

Artifact previews and stimulation limits is the local bridge between the course vocabulary and a
self-study explanation. The relevant source ideas include Day Two; Afternoon; MRI basics;
Aliasing; Truncation artifact; (Gibbs ringing); Stimulus limits; Relative areas of effective
current loops produced by gradient switching.; An effective current loop is induced in the plane
perpendicular to the; switched gradient axis.. Taken together, they should be read as one
argument about link aliasing, truncation, and gradient switching to practical limits. The
textbook version therefore slows the slide sequence down: first define the measured or
manipulated quantity, then state what changes it, and only then connect the change to image
appearance or fMRI interpretation.

In this part of fourier thinking, gradients, and k-space, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For artifact previews and stimulation
limits, that chain starts with the controlled scanner quantity, passes through spin phase or
signal weighting, and ends as a spatial pattern, time-series change, or acquisition tradeoff. If
the chain is left implicit, the same term can be memorized without being understood.

A useful way to study artifact previews and stimulation limits is to ask three questions for
every equation or panel. What quantity is deliberately controlled in Chapter 3's local sequence
or example? What uncontrolled physical or biological quantity can perturb it? What image-space
or time-series signature would reveal the problem? These questions keep the mathematics
connected to practical fMRI, where protocol choices are judged by SNR, temporal stability,
distortion, dropout, timing, and interpretability rather than by elegance alone.

The source pages named Day Two, Aliasing, Truncation artifact, Stimulus limits also show why MRI
explanations often require several levels. At the microscopic level, spins precess, relax,
dephase, or refocus. At the sequence level, RF pulses and gradients impose timing and spatial
encoding. At the reconstruction level, Fourier relationships convert sampled signals into
images. At the experimental level, subject motion, physiology, hardware stability, and human
factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate artifact previews and stimulation limits
without using slide shorthand. The restatement should include the relevant variables, the
direction of the effect, and the likely failure mode. A good explanation is specific enough to
predict what would happen if the field strength, gradient area, echo spacing, flip angle, coil
sensitivity, motion state, or nuisance measurement changed.

## Figure 3.10. Early MRI artifact concepts and stimulation limits

![Figure 3.10 panel](figures/fig_3_10_panel_01_source_083.png)

![Figure 3.10 panel](figures/fig_3_10_panel_02_source_084.png)

![Figure 3.10 panel](figures/fig_3_10_panel_03_source_085.png)

**Figure 3.10. Early MRI artifact concepts and stimulation limits.** Wrap-around, Gibbs ringing, and gradient-switching current-loop limits. Source pages 83-85 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Aliasing; Truncation artifact; (Gibbs ringing); Stimulus limits; Relative areas of effective current loops produced by gradient switching.; An effective current loop is induced in the plane perpendicular to the; switched gradient axis..

This figure should be read as a sequence inside Chapter 3, not as an isolated picture. It begins
with aliasing and ends with stimulus limits, so the reader can follow how the local idea changes
across the source panels. The retained source-backed panels are used here because the original
annotations are part of the evidence: the reader needs the labels, axes, arrows, image examples,
and comparison tags to see why the mechanism matters.

The practical lesson is wrap-around, gibbs ringing, and gradient-switching current-loop limits.
In a scanner context, the important move is to translate what is drawn into an acquisition
consequence: which gradient is acting, which echo or reference data are being trusted, which
bandwidth or timing choice is limiting, or which image pattern would appear during quality
control.

For Figure 3.10, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label early mri artifact
concepts and stimulation limits as a diagnosis before checking the visual evidence.

### Chapter Summary

Chapter 3 used pages 31-85 to develop develop the mathematical and practical path from frequency
analysis to two-dimensional mri. The main lesson is cumulative: the reader should move from
vocabulary to mechanism, from mechanism to protocol choice, and from protocol choice to image or
time-series consequences.

### Key Terms

Fourier, pairs, frequency, Gradients, spatial, encoders, Slice, selection, Gradient, echoes.

### Review Questions

1. Explain how fourier pairs and frequency analysis affects a practical fMRI decision.
2. Describe one way a visual panel in Chapter 3 changes the interpretation of the prose.
3. Name one acquisition parameter from this chapter and predict a tradeoff if it is changed.
4. Distinguish a mechanism-level explanation from an image-appearance description.
5. Identify one quality-control sign that would make you revisit this chapter before scanning more data.
