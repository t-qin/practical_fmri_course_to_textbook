# Chapter 4. EPI Fundamentals and Classic Artifacts

This chapter covers source pages 86-124 and turns them into a self-study sequence about explain
why epi is fast, why it is vulnerable, and how its characteristic artifacts arise. The chapter
is organized by mechanism and scanning consequence, not by slide order alone, so figures appear
where they support the local explanation.

## Echo-planar k-space traversal

Echo-planar k-space traversal is the local bridge between the course vocabulary and a self-study
explanation. The relevant source ideas include Day Three; Morning; Introduction to EPI; K-space
for EPI:; A multiple gradient echo; sequence; The first four-and-a-half echoes of; a 16-echo
"train," for the 16x16; k-space matrix above:; The three "classic" EPI artifacts:; Ghosting -
The appearance of (hopefully) faint replica; images in the phase encoding dimension.. Taken
together, they should be read as one argument about frame EPI as a multiple-gradient-echo
readout. The textbook version therefore slows the slide sequence down: first define the measured
or manipulated quantity, then state what changes it, and only then connect the change to image
appearance or fMRI interpretation.

In this part of epi fundamentals and classic artifacts, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For echo-planar k-space traversal, that
chain starts with the controlled scanner quantity, passes through spin phase or signal
weighting, and ends as a spatial pattern, time-series change, or acquisition tradeoff. If the
chain is left implicit, the same term can be memorized without being understood.

A useful way to study echo-planar k-space traversal is to ask three questions for every equation
or panel. What quantity is deliberately controlled in Chapter 4's local sequence or example?
What uncontrolled physical or biological quantity can perturb it? What image-space or time-
series signature would reveal the problem? These questions keep the mathematics connected to
practical fMRI, where protocol choices are judged by SNR, temporal stability, distortion,
dropout, timing, and interpretability rather than by elegance alone.

The source pages named Day Three, K-space for EPI:, The three "classic" EPI artifacts: also show
why MRI explanations often require several levels. At the microscopic level, spins precess,
relax, dephase, or refocus. At the sequence level, RF pulses and gradients impose timing and
spatial encoding. At the reconstruction level, Fourier relationships convert sampled signals
into images. At the experimental level, subject motion, physiology, hardware stability, and
human factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate echo-planar k-space traversal without using
slide shorthand. The restatement should include the relevant variables, the direction of the
effect, and the likely failure mode. A good explanation is specific enough to predict what would
happen if the field strength, gradient area, echo spacing, flip angle, coil sensitivity, motion
state, or nuisance measurement changed.

## Figure 4.1. EPI readout and Nyquist ghost formation

![Figure 4.1 panel](figures/fig_4_1_panel_01_source_087.png)

![Figure 4.1 panel](figures/fig_4_1_panel_02_source_088.png)

![Figure 4.1 panel](figures/fig_4_1_panel_03_source_090.png)

![Figure 4.1 panel](figures/fig_4_1_panel_04_source_091.png)

![Figure 4.1 panel](figures/fig_4_1_panel_05_source_092.png)

**Figure 4.1. EPI readout and Nyquist ghost formation.** Alternating readout polarity, timing delay, and the FOV/2 ghost. Source pages 87-88, 90-92 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: K-space for EPI:; A multiple gradient echo; sequence; The first four-and-a-half echoes of; a 16-echo "train," for the 16x16; k-space matrix above:; The three "classic" EPI artifacts:; Ghosting - The appearance of (hopefully) faint replica.

This figure should be read as a sequence inside Chapter 4, not as an isolated picture. It begins
with k-space for epi: and ends with ghosts appear at fov/2, so the reader can follow how the
local idea changes across the source panels. The retained source-backed panels are used here
because the original annotations are part of the evidence: the reader needs the labels, axes,
arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is alternating readout polarity, timing delay, and the fov/2 ghost. In a
scanner context, the important move is to translate what is drawn into an acquisition
consequence: which gradient is acting, which echo or reference data are being trusted, which
bandwidth or timing choice is limiting, or which image pattern would appear during quality
control.

For Figure 4.1, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label epi readout and nyquist
ghost formation as a diagnosis before checking the visual evidence.

## Ghosting mechanisms

Ghosting mechanisms is the local bridge between the course vocabulary and a self-study
explanation. The relevant source ideas include Ghosting; Left: A delay in signal digitization
relative to the read gradient periods; causes rightward k-space lines to be offset relative to
the leftward k-; space lines.; Right: Alternate kx lines after time-reversal (before 2D FT). Now
we have; a clear zigzag in k-space. The magnitude of the zigzag determines the; Actual k-space =
Ideal k-space + Error from delay; Actual EPI Ideal EPI Ghost image; 2Deltaky; Ghosts appear at
FOV/2; The error term has a ky increment twice as large as ky for the target image.; Doubling
Deltaky causes the ghost image to have half the FOV as the ideal. Taken together, they should be
read as one argument about derive the FOV/2 ghost and show common sources. The textbook version
therefore slows the slide sequence down: first define the measured or manipulated quantity, then
state what changes it, and only then connect the change to image appearance or fMRI
interpretation.

In this part of epi fundamentals and classic artifacts, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For ghosting mechanisms, that chain starts
with the controlled scanner quantity, passes through spin phase or signal weighting, and ends as
a spatial pattern, time-series change, or acquisition tradeoff. If the chain is left implicit,
the same term can be memorized without being understood.

A useful way to study ghosting mechanisms is to ask three questions for every equation or panel.
What quantity is deliberately controlled in Chapter 4's local sequence or example? What
uncontrolled physical or biological quantity can perturb it? What image-space or time-series
signature would reveal the problem? These questions keep the mathematics connected to practical
fMRI, where protocol choices are judged by SNR, temporal stability, distortion, dropout, timing,
and interpretability rather than by elegance alone.

The source pages named Ghosting, Ghosting, Actual k-space = Ideal k-space + Error from delay,
Ghosts appear at FOV/2, Where are the ghosts?, and related panels also show why MRI explanations
often require several levels. At the microscopic level, spins precess, relax, dephase, or
refocus. At the sequence level, RF pulses and gradients impose timing and spatial encoding. At
the reconstruction level, Fourier relationships convert sampled signals into images. At the
experimental level, subject motion, physiology, hardware stability, and human factors determine
whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate ghosting mechanisms without using slide
shorthand. The restatement should include the relevant variables, the direction of the effect,
and the likely failure mode. A good explanation is specific enough to predict what would happen
if the field strength, gradient area, echo spacing, flip angle, coil sensitivity, motion state,
or nuisance measurement changed.

## Figure 4.2. Ghost examples and fat-related ghost sources

![Figure 4.2 panel](figures/fig_4_2_panel_01_source_093.png)

![Figure 4.2 panel](figures/fig_4_2_panel_02_source_094.png)

![Figure 4.2 panel](figures/fig_4_2_panel_03_source_095.png)

![Figure 4.2 panel](figures/fig_4_2_panel_04_source_096.png)

![Figure 4.2 panel](figures/fig_4_2_panel_05_source_097.png)

**Figure 4.2. Ghost examples and fat-related ghost sources.** Where ghosts appear, why they are weak in good data, and why fat suppression matters. Source pages 93-97 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Where are the ghosts?; In a good experiment they're very weak!; But they do vary with time.; 150 volume; time series,; stdev image; Other common causes of; ghosts in EPI.

This figure should be read as a sequence inside Chapter 4, not as an isolated picture. It begins
with where are the ghosts? and ends with scalp fat suppression required, so the reader can
follow how the local idea changes across the source panels. The retained source-backed panels
are used here because the original annotations are part of the evidence: the reader needs the
labels, axes, arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is where ghosts appear, why they are weak in good data, and why fat
suppression matters. In a scanner context, the important move is to translate what is drawn into
an acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 4.2, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label ghost examples and fat-
related ghost sources as a diagnosis before checking the visual evidence.

## Chemical shift and ramp sampling

Chemical shift and ramp sampling is the local bridge between the course vocabulary and a self-
study explanation. The relevant source ideas include Origin of the chemical shift; (Shielding is
defined relative to tetramethysilane (TMS), a symmetric molecule.); Electrons in motion around
a; molecule generate a magnetic field; that opposes B0. This shielding; varies by position
around the; Chemical shifts; Lipids; 1 ppm = 123 Hz @ 2.9 T; Ramp sampling; Gread; Dkread. Taken
together, they should be read as one argument about connect resonance offsets and read-gradient
timing to ghost risk. The textbook version therefore slows the slide sequence down: first define
the measured or manipulated quantity, then state what changes it, and only then connect the
change to image appearance or fMRI interpretation.

In this part of epi fundamentals and classic artifacts, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For chemical shift and ramp sampling, that
chain starts with the controlled scanner quantity, passes through spin phase or signal
weighting, and ends as a spatial pattern, time-series change, or acquisition tradeoff. If the
chain is left implicit, the same term can be memorized without being understood.

A useful way to study chemical shift and ramp sampling is to ask three questions for every
equation or panel. What quantity is deliberately controlled in Chapter 4's local sequence or
example? What uncontrolled physical or biological quantity can perturb it? What image-space or
time-series signature would reveal the problem? These questions keep the mathematics connected
to practical fMRI, where protocol choices are judged by SNR, temporal stability, distortion,
dropout, timing, and interpretability rather than by elegance alone.

The source pages named Origin of the chemical shift, Chemical shifts, Ramp sampling, Ramp
sampling: going too fast also show why MRI explanations often require several levels. At the
microscopic level, spins precess, relax, dephase, or refocus. At the sequence level, RF pulses
and gradients impose timing and spatial encoding. At the reconstruction level, Fourier
relationships convert sampled signals into images. At the experimental level, subject motion,
physiology, hardware stability, and human factors determine whether the image series supports a
defensible fMRI interpretation.

For practice, the reader should be able to restate chemical shift and ramp sampling without
using slide shorthand. The restatement should include the relevant variables, the direction of
the effect, and the likely failure mode. A good explanation is specific enough to predict what
would happen if the field strength, gradient area, echo spacing, flip angle, coil sensitivity,
motion state, or nuisance measurement changed.

## Figure 4.3. Chemical shift and ramp-sampling timing

![Figure 4.3 panel](figures/fig_4_3_panel_01_source_098.png)

![Figure 4.3 panel](figures/fig_4_3_panel_02_source_099.png)

![Figure 4.3 panel](figures/fig_4_3_panel_03_source_100.png)

![Figure 4.3 panel](figures/fig_4_3_panel_04_source_101.png)

**Figure 4.3. Chemical shift and ramp-sampling timing.** Shielding, water-lipid frequency offsets, ADC timing, and echo-spacing pressure. Source pages 98-101 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Origin of the chemical shift; (Shielding is defined relative to tetramethysilane (TMS), a symmetric molecule.); Electrons in motion around a; molecule generate a magnetic field; that opposes B0. This shielding; varies by position around the; Chemical shifts; Lipids.

This figure should be read as a sequence inside Chapter 4, not as an isolated picture. It begins
with origin of the chemical shift and ends with ramp sampling: going too fast, so the reader can
follow how the local idea changes across the source panels. The retained source-backed panels
are used here because the original annotations are part of the evidence: the reader needs the
labels, axes, arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is shielding, water-lipid frequency offsets, adc timing, and echo-spacing
pressure. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 4.3, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label chemical shift and ramp-
sampling timing as a diagnosis before checking the visual evidence.

## Distortion and bandwidth

Distortion and bandwidth is the local bridge between the course vocabulary and a self-study
explanation. The relevant source ideas include Distortion; Arises in the phase-encoded
dimension, and is a result of; the relatively slow sampling in that dimension.; Dt = 8 micros;
Dtesp = 0.5 ms; Bandwith in EPI; Frequency encoding axis:; BW = (1/Dt)/Npixels; Typically
2000-2600 Hz/pixel; BW ~ 15 Hz/pixel; BW ~ 30 Hz/pixel; BW ~ 2000 Hz/pixel. Taken together, they
should be read as one argument about explain phase-encoding displacement and direction
reversals. The textbook version therefore slows the slide sequence down: first define the
measured or manipulated quantity, then state what changes it, and only then connect the change
to image appearance or fMRI interpretation.

In this part of epi fundamentals and classic artifacts, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For distortion and bandwidth, that chain
starts with the controlled scanner quantity, passes through spin phase or signal weighting, and
ends as a spatial pattern, time-series change, or acquisition tradeoff. If the chain is left
implicit, the same term can be memorized without being understood.

A useful way to study distortion and bandwidth is to ask three questions for every equation or
panel. What quantity is deliberately controlled in Chapter 4's local sequence or example? What
uncontrolled physical or biological quantity can perturb it? What image-space or time-series
signature would reveal the problem? These questions keep the mathematics connected to practical
fMRI, where protocol choices are judged by SNR, temporal stability, distortion, dropout, timing,
and interpretability rather than by elegance alone.

The source pages named Distortion, Distortion, Bandwith in EPI, Distortion, A-P versus P-A phase
encoding also show why MRI explanations often require several levels. At the microscopic level,
spins precess, relax, dephase, or refocus. At the sequence level, RF pulses and gradients impose
timing and spatial encoding. At the reconstruction level, Fourier relationships convert sampled
signals into images. At the experimental level, subject motion, physiology, hardware stability,
and human factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate distortion and bandwidth without using slide
shorthand. The restatement should include the relevant variables, the direction of the effect,
and the likely failure mode. A good explanation is specific enough to predict what would happen
if the field strength, gradient area, echo spacing, flip angle, coil sensitivity, motion state,
or nuisance measurement changed.

## Figure 4.4. EPI distortion and phase-encoding bandwidth

![Figure 4.4 panel](figures/fig_4_4_panel_01_source_102.png)

![Figure 4.4 panel](figures/fig_4_4_panel_02_source_103.png)

![Figure 4.4 panel](figures/fig_4_4_panel_03_source_104.png)

![Figure 4.4 panel](figures/fig_4_4_panel_04_source_105.png)

![Figure 4.4 panel](figures/fig_4_4_panel_05_source_106.png)

**Figure 4.4. EPI distortion and phase-encoding bandwidth.** Slow phase-encoding sampling, bandwidth, and the AP/PA diagnostic reversal. Source pages 102-106 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Distortion; Arises in the phase-encoded dimension, and is a result of; the relatively slow sampling in that dimension.; Dt = 8 micros; Dtesp = 0.5 ms; Bandwith in EPI; Frequency encoding axis:; BW = (1/Dt)/Npixels.

This figure should be read as a sequence inside Chapter 4, not as an isolated picture. It begins
with distortion and ends with a-p versus p-a phase encoding, so the reader can follow how the
local idea changes across the source panels. The retained source-backed panels are used here
because the original annotations are part of the evidence: the reader needs the labels, axes,
arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is slow phase-encoding sampling, bandwidth, and the ap/pa diagnostic
reversal. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 4.4, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label epi distortion and
phase-encoding bandwidth as a diagnosis before checking the visual evidence.

## Dropout and slice timing

Dropout and slice timing is the local bridge between the course vocabulary and a self-study
explanation. The relevant source ideas include Dropout; Signal dropout; Not strictly an EPI
issue,* there would be dropout for any; gradient echo sequence at the same TE.; * But signal
decay in-plane during EPI readout makes it worse.; Thinner slices produce less dropout; Two thin
slices > one thick slice; Multi-slice EPI: slice order; Ascending; Descending; Interleaved;
DESC. Taken together, they should be read as one argument about separate susceptibility dropout
from slice-order artifacts. The textbook version therefore slows the slide sequence down: first
define the measured or manipulated quantity, then state what changes it, and only then connect
the change to image appearance or fMRI interpretation.

In this part of epi fundamentals and classic artifacts, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For dropout and slice timing, that chain
starts with the controlled scanner quantity, passes through spin phase or signal weighting, and
ends as a spatial pattern, time-series change, or acquisition tradeoff. If the chain is left
implicit, the same term can be memorized without being understood.

A useful way to study dropout and slice timing is to ask three questions for every equation or
panel. What quantity is deliberately controlled in Chapter 4's local sequence or example? What
uncontrolled physical or biological quantity can perturb it? What image-space or time-series
signature would reveal the problem? These questions keep the mathematics connected to practical
fMRI, where protocol choices are judged by SNR, temporal stability, distortion, dropout, timing,
and interpretability rather than by elegance alone.

The source pages named Dropout, Signal dropout, Thinner slices produce less dropout, Two thin
slices > one thick slice, Multi-slice EPI: slice order, and related panels also show why MRI
explanations often require several levels. At the microscopic level, spins precess, relax,
dephase, or refocus. At the sequence level, RF pulses and gradients impose timing and spatial
encoding. At the reconstruction level, Fourier relationships convert sampled signals into
images. At the experimental level, subject motion, physiology, hardware stability, and human
factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate dropout and slice timing without using slide
shorthand. The restatement should include the relevant variables, the direction of the effect,
and the likely failure mode. A good explanation is specific enough to predict what would happen
if the field strength, gradient area, echo spacing, flip angle, coil sensitivity, motion state,
or nuisance measurement changed.

## Figure 4.5. Dropout, slice thickness, and slice order

![Figure 4.5 panel](figures/fig_4_5_panel_01_source_107.png)

![Figure 4.5 panel](figures/fig_4_5_panel_02_source_108.png)

![Figure 4.5 panel](figures/fig_4_5_panel_03_source_109.png)

![Figure 4.5 panel](figures/fig_4_5_panel_04_source_110.png)

![Figure 4.5 panel](figures/fig_4_5_panel_05_source_111.png)

![Figure 4.5 panel](figures/fig_4_5_panel_06_source_112.png)

**Figure 4.5. Dropout, slice thickness, and slice order.** Susceptibility-related signal loss and practical effects of slice acquisition order. Source pages 107-112 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Dropout; Signal dropout; Not strictly an EPI issue,* there would be dropout for any; gradient echo sequence at the same TE.; * But signal decay in-plane during EPI readout makes it worse.; Thinner slices produce less dropout; Two thin slices > one thick slice; Multi-slice EPI: slice order.

This figure should be read as a sequence inside Chapter 4, not as an isolated picture. It begins
with dropout and ends with descending (stdev) interleaved (stdev), so the reader can follow how
the local idea changes across the source panels. The retained source-backed panels are used here
because the original annotations are part of the evidence: the reader needs the labels, axes,
arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is susceptibility-related signal loss and practical effects of slice
acquisition order. In a scanner context, the important move is to translate what is drawn into
an acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 4.5, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label dropout, slice
thickness, and slice order as a diagnosis before checking the visual evidence.

## Real EPI sequence anatomy

Real EPI sequence anatomy is the local bridge between the course vocabulary and a self-study
explanation. The relevant source ideas include A real EPI pulse sequence; EPI: crusher
gradients; Fat signal crusher gradients; Spurious water crusher gradients; EPI: slice select,
k-space; N/2 ghost correction echoes; Gradient echo train; (to sample 2D k-space); Slice
selection; Good EPI; Good axial EPI; g-fmri-artifacts-good-axial.html. Taken together, they
should be read as one argument about read a practical sequence diagram and quality images. The
textbook version therefore slows the slide sequence down: first define the measured or
manipulated quantity, then state what changes it, and only then connect the change to image
appearance or fMRI interpretation.

In this part of epi fundamentals and classic artifacts, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For real epi sequence anatomy, that chain
starts with the controlled scanner quantity, passes through spin phase or signal weighting, and
ends as a spatial pattern, time-series change, or acquisition tradeoff. If the chain is left
implicit, the same term can be memorized without being understood.

A useful way to study real epi sequence anatomy is to ask three questions for every equation or
panel. What quantity is deliberately controlled in Chapter 4's local sequence or example? What
uncontrolled physical or biological quantity can perturb it? What image-space or time-series
signature would reveal the problem? These questions keep the mathematics connected to practical
fMRI, where protocol choices are judged by SNR, temporal stability, distortion, dropout, timing,
and interpretability rather than by elegance alone.

The source pages named https://practicalfmri.blogspot.com/2012/07/physics-for-understanding-
fmri.html, EPI: crusher gradients, EPI: slice select, k-space, Good EPI, TSNR image also show
why MRI explanations often require several levels. At the microscopic level, spins precess,
relax, dephase, or refocus. At the sequence level, RF pulses and gradients impose timing and
spatial encoding. At the reconstruction level, Fourier relationships convert sampled signals
into images. At the experimental level, subject motion, physiology, hardware stability, and
human factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate real epi sequence anatomy without using slide
shorthand. The restatement should include the relevant variables, the direction of the effect,
and the likely failure mode. A good explanation is specific enough to predict what would happen
if the field strength, gradient area, echo spacing, flip angle, coil sensitivity, motion state,
or nuisance measurement changed.

## Figure 4.6. Real EPI sequence anatomy and quality images

![Figure 4.6 panel](figures/fig_4_6_panel_01_source_114.png)

![Figure 4.6 panel](figures/fig_4_6_panel_02_source_115.png)

![Figure 4.6 panel](figures/fig_4_6_panel_03_source_116.png)

![Figure 4.6 panel](figures/fig_4_6_panel_04_source_117.png)

![Figure 4.6 panel](figures/fig_4_6_panel_05_source_118.png)

**Figure 4.6. Real EPI sequence anatomy and quality images.** Crusher gradients, slice selection, echo trains, TSNR, and standard deviation images. Source pages 114-118 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: A real EPI pulse sequence; EPI: crusher gradients; Fat signal crusher gradients; Spurious water crusher gradients; EPI: slice select, k-space; N/2 ghost correction echoes; Gradient echo train; (to sample 2D k-space).

This figure should be read as a sequence inside Chapter 4, not as an isolated picture. It begins
with https://practicalfmri.blogspot.com/2012/07/physics-for-understanding-fmri.html and ends
with tsnr image, so the reader can follow how the local idea changes across the source panels.
The retained source-backed panels are used here because the original annotations are part of the
evidence: the reader needs the labels, axes, arrows, image examples, and comparison tags to see
why the mechanism matters.

The practical lesson is crusher gradients, slice selection, echo trains, tsnr, and standard
deviation images. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 4.6, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label real epi sequence
anatomy and quality images as a diagnosis before checking the visual evidence.

## Motion, susceptibility, and phase

Motion, susceptibility, and phase is the local bridge between the course vocabulary and a self-
study explanation. The relevant source ideas include The brain is always moving!; Magnetic
susceptibility; Magnetic susceptibility, c; The tendency of a material to magnetize when
exposed; to a magnetic field; Interaction of electrons with the magnetic field; Variations in c
cause intrinsic, static magnetic field; gradients in parts of the brain; Interfaces, especially
air-bone-brain, create strong; magnetic field gradients across parts of the brain; A map of MR
image phase shows the problem; T2* relaxation. Taken together, they should be read as one
argument about connect moving anatomy and air-tissue interfaces to EPI behavior. The textbook
version therefore slows the slide sequence down: first define the measured or manipulated
quantity, then state what changes it, and only then connect the change to image appearance or
fMRI interpretation.

In this part of epi fundamentals and classic artifacts, the central discipline is to separate
mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely
a picture of a result; it encodes a chain of causes. For motion, susceptibility, and phase, that
chain starts with the controlled scanner quantity, passes through spin phase or signal
weighting, and ends as a spatial pattern, time-series change, or acquisition tradeoff. If the
chain is left implicit, the same term can be memorized without being understood.

A useful way to study motion, susceptibility, and phase is to ask three questions for every
equation or panel. What quantity is deliberately controlled in Chapter 4's local sequence or
example? What uncontrolled physical or biological quantity can perturb it? What image-space or
time-series signature would reveal the problem? These questions keep the mathematics connected
to practical fMRI, where protocol choices are judged by SNR, temporal stability, distortion,
dropout, timing, and interpretability rather than by elegance alone.

The source pages named The brain is always moving!, Magnetic susceptibility, Magnetic
susceptibility, c, Interfaces, especially air-bone-brain, create strong, A map of MR image phase
shows the problem, and related panels also show why MRI explanations often require several
levels. At the microscopic level, spins precess, relax, dephase, or refocus. At the sequence
level, RF pulses and gradients impose timing and spatial encoding. At the reconstruction level,
Fourier relationships convert sampled signals into images. At the experimental level, subject
motion, physiology, hardware stability, and human factors determine whether the image series
supports a defensible fMRI interpretation.

For practice, the reader should be able to restate motion, susceptibility, and phase without
using slide shorthand. The restatement should include the relevant variables, the direction of
the effect, and the likely failure mode. A good explanation is specific enough to predict what
would happen if the field strength, gradient area, echo spacing, flip angle, coil sensitivity,
motion state, or nuisance measurement changed.

## Figure 4.7. Movement, susceptibility, and phase in EPI

![Figure 4.7 panel](figures/fig_4_7_panel_01_source_119.png)

![Figure 4.7 panel](figures/fig_4_7_panel_02_source_120.png)

![Figure 4.7 panel](figures/fig_4_7_panel_03_source_121.png)

![Figure 4.7 panel](figures/fig_4_7_panel_04_source_122.png)

![Figure 4.7 panel](figures/fig_4_7_panel_05_source_123.png)

![Figure 4.7 panel](figures/fig_4_7_panel_06_source_124.png)

**Figure 4.7. Movement, susceptibility, and phase in EPI.** Always-moving brains, susceptibility interfaces, phase maps, and T2-star loss during readout. Source pages 119-124 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: The brain is always moving!; Magnetic susceptibility; Magnetic susceptibility, c; The tendency of a material to magnetize when exposed; to a magnetic field; Interaction of electrons with the magnetic field; Variations in c cause intrinsic, static magnetic field; gradients in parts of the brain.

This figure should be read as a sequence inside Chapter 4, not as an isolated picture. It begins
with the brain is always moving! and ends with t2* relaxation, so the reader can follow how the
local idea changes across the source panels. The retained source-backed panels are used here
because the original annotations are part of the evidence: the reader needs the labels, axes,
arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is always-moving brains, susceptibility interfaces, phase maps, and t2-star
loss during readout. In a scanner context, the important move is to translate what is drawn into
an acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 4.7, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label movement,
susceptibility, and phase in epi as a diagnosis before checking the visual evidence.

### Chapter Summary

Chapter 4 used pages 86-124 to develop explain why epi is fast, why it is vulnerable, and how
its characteristic artifacts arise. The main lesson is cumulative: the reader should move from
vocabulary to mechanism, from mechanism to protocol choice, and from protocol choice to image or
time-series consequences.

### Key Terms

Echo, planar, space, Ghosting, mechanisms, Chemical, shift, ramp, Distortion, bandwidth.

### Review Questions

1. Explain how echo-planar k-space traversal affects a practical fMRI decision.
2. Describe one way a visual panel in Chapter 4 changes the interpretation of the prose.
3. Name one acquisition parameter from this chapter and predict a tradeoff if it is changed.
4. Distinguish a mechanism-level explanation from an image-appearance description.
5. Identify one quality-control sign that would make you revisit this chapter before scanning more data.
