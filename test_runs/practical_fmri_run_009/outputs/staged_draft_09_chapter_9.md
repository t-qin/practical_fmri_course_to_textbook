# Chapter 9. Artifact Recognition and Practical Troubleshooting

This chapter covers source pages 183-214 and turns them into a self-study sequence about convert
artifact examples into a practical diagnostic vocabulary for fmri data inspection. The chapter
is organized by mechanism and scanning consequence, not by slide order alone, so figures appear
where they support the local explanation.

## FLEET and artifact-recognition mindset

FLEET and artifact-recognition mindset is the local bridge between the course vocabulary and a
self-study explanation. The relevant source ideas include Day Four; Afternoon; Advanced EPI;
FLEET: Fast Low-angle Excitation Echo-planar Technique; Polimeni et al. Magn Reson Med.
2016;75(2):665-679; Minimize time between ACS segments for each slice; Loop the ACS, then the
slices, using low FA to reduce spin history; Day Five; Morning; Artifacts and troubleshooting;
"There is no situation so bad that; you can't make it worse.". Taken together, they should be
read as one argument about connect calibration timing with the discipline of knowing good data.
The textbook version therefore slows the slide sequence down: first define the measured or
manipulated quantity, then state what changes it, and only then connect the change to image
appearance or fMRI interpretation.

In this part of artifact recognition and practical troubleshooting, the central discipline is to
separate mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is
not merely a picture of a result; it encodes a chain of causes. For fleet and artifact-
recognition mindset, that chain starts with the controlled scanner quantity, passes through spin
phase or signal weighting, and ends as a spatial pattern, time-series change, or acquisition
tradeoff. If the chain is left implicit, the same term can be memorized without being
understood.

A useful way to study fleet and artifact-recognition mindset is to ask three questions for every
equation or panel. What quantity is deliberately controlled in Chapter 9's local sequence or
example? What uncontrolled physical or biological quantity can perturb it? What image-space or
time-series signature would reveal the problem? These questions keep the mathematics connected
to practical fMRI, where protocol choices are judged by SNR, temporal stability, distortion,
dropout, timing, and interpretability rather than by elegance alone.

The source pages named Day Four, FLEET: Fast Low-angle Excitation Echo-planar Technique, Day
Five, "There is no situation so bad that, Artifact recognition, and related panels also show why
MRI explanations often require several levels. At the microscopic level, spins precess, relax,
dephase, or refocus. At the sequence level, RF pulses and gradients impose timing and spatial
encoding. At the reconstruction level, Fourier relationships convert sampled signals into
images. At the experimental level, subject motion, physiology, hardware stability, and human
factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate fleet and artifact-recognition mindset
without using slide shorthand. The restatement should include the relevant variables, the
direction of the effect, and the likely failure mode. A good explanation is specific enough to
predict what would happen if the field strength, gradient area, echo spacing, flip angle, coil
sensitivity, motion state, or nuisance measurement changed.

## Figure 9.1. FLEET calibration timing

![Figure 9.1 panel](figures/fig_9_1_panel_01_source_184.png)

**Figure 9.1. FLEET calibration timing.** Low-angle excitation timing intended to reduce calibration inconsistency. Source pages 184 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: FLEET: Fast Low-angle Excitation Echo-planar Technique; Polimeni et al. Magn Reson Med. 2016;75(2):665-679; Minimize time between ACS segments for each slice; Loop the ACS, then the slices, using low FA to reduce spin history.

This figure should be read as a sequence inside Chapter 9, not as an isolated picture. It begins
with fleet: fast low-angle excitation echo-planar technique and ends with fleet: fast low-angle
excitation echo-planar technique, so the reader can follow how the local idea changes across the
source panels. The retained source-backed panels are used here because the original annotations
are part of the evidence: the reader needs the labels, axes, arrows, image examples, and
comparison tags to see why the mechanism matters.

The practical lesson is low-angle excitation timing intended to reduce calibration
inconsistency. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 9.1, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label fleet calibration timing
as a diagnosis before checking the visual evidence.

## Figure 9.2. Ghosting, background, and prescan-normalization examples

![Figure 9.2 panel](figures/fig_9_2_panel_01_source_187.png)

![Figure 9.2 panel](figures/fig_9_2_panel_02_source_189.png)

![Figure 9.2 panel](figures/fig_9_2_panel_03_source_190.png)

![Figure 9.2 panel](figures/fig_9_2_panel_04_source_191.png)

![Figure 9.2 panel](figures/fig_9_2_panel_05_source_192.png)

![Figure 9.2 panel](figures/fig_9_2_panel_06_source_193.png)

**Figure 9.2. Ghosting, background, and prescan-normalization examples.** Recognition strategy for normal ghosts, scalp ghosts, eye-motion ghosts, stdev images, and PSN effects. Source pages 187, 189-193 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Artifact recognition; Learn what "good data" looks like for your scan; Get to know the background! Most of the problems; lurk down at the noise level; Proper identification of normal artifacts (ghosting,; distortion, dropout, residual aliasing) is the first step; Normal ghosting; Scalp ghosts.

This figure should be read as a sequence inside Chapter 9, not as an isolated picture. It begins
with artifact recognition and ends with prescan normalize affects, so the reader can follow how
the local idea changes across the source panels. The retained source-backed panels are used here
because the original annotations are part of the evidence: the reader needs the labels, axes,
arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is recognition strategy for normal ghosts, scalp ghosts, eye-motion ghosts,
stdev images, and psn effects. In a scanner context, the important move is to translate what is
drawn into an acquisition consequence: which gradient is acting, which echo or reference data
are being trusted, which bandwidth or timing choice is limiting, or which image pattern would
appear during quality control.

For Figure 9.2, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label ghosting, background,
and prescan-normalization examples as a diagnosis before checking the visual evidence.

## Ghosting, background, and aliasing examples

Ghosting, background, and aliasing examples is the local bridge between the course vocabulary
and a self-study explanation. The relevant source ideas include Normal ghosting; Scalp ghosts;
Make sure Nyquist ghosts from eye movements; don't fall on something you're interested in!;
Stdev image; Prescan normalize affects; background intensity; PSN on PSN off; Residual aliasing
for GRAPPA; GRAPPA R=2 No GRAPPA; Residual aliasing for SMS; SMS = 3 No SMS. Taken together,
they should be read as one argument about recognize normal ghosts, scalp ghosts, PSN changes,
GRAPPA aliasing, and SMS aliasing. The textbook version therefore slows the slide sequence down:
first define the measured or manipulated quantity, then state what changes it, and only then
connect the change to image appearance or fMRI interpretation.

In this part of artifact recognition and practical troubleshooting, the central discipline is to
separate mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is
not merely a picture of a result; it encodes a chain of causes. For ghosting, background, and
aliasing examples, that chain starts with the controlled scanner quantity, passes through spin
phase or signal weighting, and ends as a spatial pattern, time-series change, or acquisition
tradeoff. If the chain is left implicit, the same term can be memorized without being
understood.

A useful way to study ghosting, background, and aliasing examples is to ask three questions for
every equation or panel. What quantity is deliberately controlled in Chapter 9's local sequence
or example? What uncontrolled physical or biological quantity can perturb it? What image-space
or time-series signature would reveal the problem? These questions keep the mathematics
connected to practical fMRI, where protocol choices are judged by SNR, temporal stability,
distortion, dropout, timing, and interpretability rather than by elegance alone.

The source pages named Normal ghosting, Scalp ghosts, Make sure Nyquist ghosts from eye
movements, Stdev image, Prescan normalize affects, and related panels also show why MRI
explanations often require several levels. At the microscopic level, spins precess, relax,
dephase, or refocus. At the sequence level, RF pulses and gradients impose timing and spatial
encoding. At the reconstruction level, Fourier relationships convert sampled signals into
images. At the experimental level, subject motion, physiology, hardware stability, and human
factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate ghosting, background, and aliasing examples
without using slide shorthand. The restatement should include the relevant variables, the
direction of the effect, and the likely failure mode. A good explanation is specific enough to
predict what would happen if the field strength, gradient area, echo spacing, flip angle, coil
sensitivity, motion state, or nuisance measurement changed.

## Figure 9.3. Residual aliasing in accelerated EPI

![Figure 9.3 panel](figures/fig_9_3_panel_01_source_194.png)

![Figure 9.3 panel](figures/fig_9_3_panel_02_source_195.png)

![Figure 9.3 panel](figures/fig_9_3_panel_03_source_196.png)

![Figure 9.3 panel](figures/fig_9_3_panel_04_source_197.png)

![Figure 9.3 panel](figures/fig_9_3_panel_05_source_199.png)

**Figure 9.3. Residual aliasing in accelerated EPI.** GRAPPA and SMS aliasing patterns, including TSNR and standard-deviation context. Source pages 194-197, 199 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Residual aliasing for GRAPPA; GRAPPA R=2 No GRAPPA; Residual aliasing for SMS; SMS = 3 No SMS; Residual aliasing for SMS = 3; Residual aliasing: SMS+GRAPPA; TSNR image; SDEV image.

This figure should be read as a sequence inside Chapter 9, not as an isolated picture. It begins
with residual aliasing for grappa and ends with tsnr image, so the reader can follow how the
local idea changes across the source panels. The retained source-backed panels are used here
because the original annotations are part of the evidence: the reader needs the labels, axes,
arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is grappa and sms aliasing patterns, including tsnr and standard-deviation
context. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 9.3, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label residual aliasing in
accelerated epi as a diagnosis before checking the visual evidence.

## Motion sources and mechanical instability

Motion sources and mechanical instability is the local bridge between the course vocabulary and
a self-study explanation. The relevant source ideas include Movement; Real head motion; Pseudo-
motion from breathing; Movement of other body parts; Unstable hardware; Eye movements; Head
movements; Talking; Moving feet; Coil instability; Siemens Trio 32ch coil: ~3 cm "play" along z,
a few mm L-R; Coil instability?. Taken together, they should be read as one argument about
distinguish head, eye, body, coil, animal, and anatomical-scan motion. The textbook version
therefore slows the slide sequence down: first define the measured or manipulated quantity, then
state what changes it, and only then connect the change to image appearance or fMRI
interpretation.

In this part of artifact recognition and practical troubleshooting, the central discipline is to
separate mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is
not merely a picture of a result; it encodes a chain of causes. For motion sources and
mechanical instability, that chain starts with the controlled scanner quantity, passes through
spin phase or signal weighting, and ends as a spatial pattern, time-series change, or
acquisition tradeoff. If the chain is left implicit, the same term can be memorized without
being understood.

A useful way to study motion sources and mechanical instability is to ask three questions for
every equation or panel. What quantity is deliberately controlled in Chapter 9's local sequence
or example? What uncontrolled physical or biological quantity can perturb it? What image-space
or time-series signature would reveal the problem? These questions keep the mathematics
connected to practical fMRI, where protocol choices are judged by SNR, temporal stability,
distortion, dropout, timing, and interpretability rather than by elegance alone.

The source pages named Movement, Eye movements, Head movements, Talking, Moving feet, and
related panels also show why MRI explanations often require several levels. At the microscopic
level, spins precess, relax, dephase, or refocus. At the sequence level, RF pulses and gradients
impose timing and spatial encoding. At the reconstruction level, Fourier relationships convert
sampled signals into images. At the experimental level, subject motion, physiology, hardware
stability, and human factors determine whether the image series supports a defensible fMRI
interpretation.

For practice, the reader should be able to restate motion sources and mechanical instability
without using slide shorthand. The restatement should include the relevant variables, the
direction of the effect, and the likely failure mode. A good explanation is specific enough to
predict what would happen if the field strength, gradient area, echo spacing, flip angle, coil
sensitivity, motion state, or nuisance measurement changed.

## Figure 9.4. Motion sources and mechanical instability

![Figure 9.4 panel](figures/fig_9_4_panel_01_source_201.png)

![Figure 9.4 panel](figures/fig_9_4_panel_02_source_202.png)

![Figure 9.4 panel](figures/fig_9_4_panel_03_source_203.png)

![Figure 9.4 panel](figures/fig_9_4_panel_04_source_204.png)

![Figure 9.4 panel](figures/fig_9_4_panel_05_source_205.png)

![Figure 9.4 panel](figures/fig_9_4_panel_06_source_206.png)

![Figure 9.4 panel](figures/fig_9_4_panel_07_source_207.png)

![Figure 9.4 panel](figures/fig_9_4_panel_08_source_208.png)

**Figure 9.4. Motion sources and mechanical instability.** Eye, head, speech, feet, coil, third-party, and anatomical-scan motion examples. Source pages 201-208 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Eye movements; Head movements; Talking; Moving feet; Coil instability; Siemens Trio 32ch coil: ~3 cm "play" along z, a few mm L-R; Coil instability?; Prisma: 20-ch and 64-ch coils have a hard plug at the rear of the table.

This figure should be read as a sequence inside Chapter 9, not as an isolated picture. It begins
with eye movements and ends with motion in mp-rage, so the reader can follow how the local idea
changes across the source panels. The retained source-backed panels are used here because the
original annotations are part of the evidence: the reader needs the labels, axes, arrows, image
examples, and comparison tags to see why the mechanism matters.

The practical lesson is eye, head, speech, feet, coil, third-party, and anatomical-scan motion
examples. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 9.4, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label motion sources and
mechanical instability as a diagnosis before checking the visual evidence.

## Foreign objects, RF interference, and spiking

Foreign objects, RF interference, and spiking is the local bridge between the course vocabulary
and a self-study explanation. The relevant source ideas include Foreign objects - metal pin; RF
interference; Gradient spiking; Gradient spiking: phantom check; RF coil spikes; Localizer; MP-
RAGE. Taken together, they should be read as one argument about separate metallic artifacts, RF
pickup, gradient spikes, and coil spikes. The textbook version therefore slows the slide
sequence down: first define the measured or manipulated quantity, then state what changes it,
and only then connect the change to image appearance or fMRI interpretation.

In this part of artifact recognition and practical troubleshooting, the central discipline is to
separate mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is
not merely a picture of a result; it encodes a chain of causes. For foreign objects, rf
interference, and spiking, that chain starts with the controlled scanner quantity, passes
through spin phase or signal weighting, and ends as a spatial pattern, time-series change, or
acquisition tradeoff. If the chain is left implicit, the same term can be memorized without
being understood.

A useful way to study foreign objects, rf interference, and spiking is to ask three questions
for every equation or panel. What quantity is deliberately controlled in Chapter 9's local
sequence or example? What uncontrolled physical or biological quantity can perturb it? What
image-space or time-series signature would reveal the problem? These questions keep the
mathematics connected to practical fMRI, where protocol choices are judged by SNR, temporal
stability, distortion, dropout, timing, and interpretability rather than by elegance alone.

The source pages named Foreign objects - metal pin, RF interference, Gradient spiking, Gradient
spiking, Gradient spiking: phantom check, and related panels also show why MRI explanations
often require several levels. At the microscopic level, spins precess, relax, dephase, or
refocus. At the sequence level, RF pulses and gradients impose timing and spatial encoding. At
the reconstruction level, Fourier relationships convert sampled signals into images. At the
experimental level, subject motion, physiology, hardware stability, and human factors determine
whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate foreign objects, rf interference, and spiking
without using slide shorthand. The restatement should include the relevant variables, the
direction of the effect, and the likely failure mode. A good explanation is specific enough to
predict what would happen if the field strength, gradient area, echo spacing, flip angle, coil
sensitivity, motion state, or nuisance measurement changed.

## Figure 9.5. Foreign objects, RF interference, and spike artifacts

![Figure 9.5 panel](figures/fig_9_5_panel_01_source_209.png)

![Figure 9.5 panel](figures/fig_9_5_panel_02_source_210.png)

![Figure 9.5 panel](figures/fig_9_5_panel_03_source_211.png)

![Figure 9.5 panel](figures/fig_9_5_panel_04_source_212.png)

![Figure 9.5 panel](figures/fig_9_5_panel_05_source_213.png)

![Figure 9.5 panel](figures/fig_9_5_panel_06_source_214.png)

**Figure 9.5. Foreign objects, RF interference, and spike artifacts.** Metal pins, RF pickup, gradient spiking, phantom checks, and coil spikes. Source pages 209-214 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Foreign objects - metal pin; RF interference; Gradient spiking; Gradient spiking: phantom check; RF coil spikes; Localizer; MP-RAGE.

This figure should be read as a sequence inside Chapter 9, not as an isolated picture. It begins
with foreign objects - metal pin and ends with rf coil spikes, so the reader can follow how the
local idea changes across the source panels. The retained source-backed panels are used here
because the original annotations are part of the evidence: the reader needs the labels, axes,
arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is metal pins, rf pickup, gradient spiking, phantom checks, and coil
spikes. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 9.5, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label foreign objects, rf
interference, and spike artifacts as a diagnosis before checking the visual evidence.

### Chapter Summary

Chapter 9 used pages 183-214 to develop convert artifact examples into a practical diagnostic
vocabulary for fmri data inspection. The main lesson is cumulative: the reader should move from
vocabulary to mechanism, from mechanism to protocol choice, and from protocol choice to image or
time-series consequences.

### Key Terms

FLEET, artifact, recognition, Ghosting, background, aliasing, Motion, sources, mechanical, Foreign.

### Review Questions

1. Explain how fleet and artifact-recognition mindset affects a practical fMRI decision.
2. Describe one way a visual panel in Chapter 9 changes the interpretation of the prose.
3. Name one acquisition parameter from this chapter and predict a tradeoff if it is changed.
4. Distinguish a mechanism-level explanation from an image-appearance description.
5. Identify one quality-control sign that would make you revisit this chapter before scanning more data.
