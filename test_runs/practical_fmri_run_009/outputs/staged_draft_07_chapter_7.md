# Chapter 7. Parallel Imaging with GRAPPA

This chapter covers source pages 159-168 and turns them into a self-study sequence about explain
how coil arrays and calibration data support accelerated phase encoding, and why motion can
corrupt the result. The chapter is organized by mechanism and scanning consequence, not by slide
order alone, so figures appear where they support the local explanation.

## R=2 trajectories and calibration

R=2 trajectories and calibration is the local bridge between the course vocabulary and a self-
study explanation. The relevant source ideas include In-plane acceleration; (GRAPPA); R=2
k-space trajectory:; Image-only teaching panel 161; 32-channel coil; Bottom half only, from
underneath with cover removed; GRAPPA scheme (R=2); ACS1 … ACS2 … EPI1 … EPI2 … EPI3
..............… EPIN; The ACS make up a reference data set; The omitted k-space lines from each
accelerated (under-. Taken together, they should be read as one argument about connect skipped
k-space lines, coil arrays, and ACS data. The textbook version therefore slows the slide
sequence down: first define the measured or manipulated quantity, then state what changes it,
and only then connect the change to image appearance or fMRI interpretation.

In this part of parallel imaging with grappa, the central discipline is to separate mechanism
from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely a picture
of a result; it encodes a chain of causes. For r=2 trajectories and calibration, that chain
starts with the controlled scanner quantity, passes through spin phase or signal weighting, and
ends as a spatial pattern, time-series change, or acquisition tradeoff. If the chain is left
implicit, the same term can be memorized without being understood.

A useful way to study r=2 trajectories and calibration is to ask three questions for every
equation or panel. What quantity is deliberately controlled in Chapter 7's local sequence or
example? What uncontrolled physical or biological quantity can perturb it? What image-space or
time-series signature would reveal the problem? These questions keep the mathematics connected
to practical fMRI, where protocol choices are judged by SNR, temporal stability, distortion,
dropout, timing, and interpretability rather than by elegance alone.

The source pages named In-plane acceleration, R=2 k-space trajectory:, Image-only teaching panel
161, 32-channel coil, GRAPPA scheme (R=2) also show why MRI explanations often require several
levels. At the microscopic level, spins precess, relax, dephase, or refocus. At the sequence
level, RF pulses and gradients impose timing and spatial encoding. At the reconstruction level,
Fourier relationships convert sampled signals into images. At the experimental level, subject
motion, physiology, hardware stability, and human factors determine whether the image series
supports a defensible fMRI interpretation.

For practice, the reader should be able to restate r=2 trajectories and calibration without
using slide shorthand. The restatement should include the relevant variables, the direction of
the effect, and the likely failure mode. A good explanation is specific enough to predict what
would happen if the field strength, gradient area, echo spacing, flip angle, coil sensitivity,
motion state, or nuisance measurement changed.

## Figure 7.1. GRAPPA acceleration and calibration data

![Figure 7.1 panel](figures/fig_7_1_panel_01_source_159.png)

![Figure 7.1 panel](figures/fig_7_1_panel_02_source_160.png)

![Figure 7.1 panel](figures/fig_7_1_panel_03_source_161.png)

![Figure 7.1 panel](figures/fig_7_1_panel_04_source_162.png)

![Figure 7.1 panel](figures/fig_7_1_panel_05_source_163.png)

**Figure 7.1. GRAPPA acceleration and calibration data.** R=2 trajectories, receive-array requirements, and ACS-based reconstruction. Source pages 159-163 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: In-plane acceleration; (GRAPPA); R=2 k-space trajectory:; Image-only teaching panel 161; 32-channel coil; Bottom half only, from underneath with cover removed; GRAPPA scheme (R=2); ACS1 … ACS2 … EPI1 … EPI2 … EPI3 ..............… EPIN.

This figure should be read as a sequence inside Chapter 7, not as an isolated picture. It begins
with in-plane acceleration and ends with grappa scheme (r=2), so the reader can follow how the
local idea changes across the source panels. The retained source-backed panels are used here
because the original annotations are part of the evidence: the reader needs the labels, axes,
arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is r=2 trajectories, receive-array requirements, and acs-based
reconstruction. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 7.1, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label grappa acceleration and
calibration data as a diagnosis before checking the visual evidence.

## Motion sensitivity

Motion sensitivity is the local bridge between the course vocabulary and a self-study
explanation. The relevant source ideas include GRAPPA motion sensitivity; ACS used to
reconstruct all the under-sampled; time series; Motion during the ACS affects all data!!!;
Motion after the ACS generates a mismatch; between the ACS and the current EPI volume; ACS1 …
ACS2 … EPI1 … EPI2 … EPI3 ............ EPIN-1 … EPI N; Motion corruption of; reference data;
Mismatch of reference data; with the time series; No motion Motion during ACS Motion after ACS.
Taken together, they should be read as one argument about distinguish ACS corruption from later
reference mismatch. The textbook version therefore slows the slide sequence down: first define
the measured or manipulated quantity, then state what changes it, and only then connect the
change to image appearance or fMRI interpretation.

In this part of parallel imaging with grappa, the central discipline is to separate mechanism
from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely a picture
of a result; it encodes a chain of causes. For motion sensitivity, that chain starts with the
controlled scanner quantity, passes through spin phase or signal weighting, and ends as a
spatial pattern, time-series change, or acquisition tradeoff. If the chain is left implicit, the
same term can be memorized without being understood.

A useful way to study motion sensitivity is to ask three questions for every equation or panel.
What quantity is deliberately controlled in Chapter 7's local sequence or example? What
uncontrolled physical or biological quantity can perturb it? What image-space or time-series
signature would reveal the problem? These questions keep the mathematics connected to practical
fMRI, where protocol choices are judged by SNR, temporal stability, distortion, dropout, timing,
and interpretability rather than by elegance alone.

The source pages named GRAPPA motion sensitivity, ACS1 … ACS2 … EPI1 … EPI2 … EPI3 ............
EPIN-1 … EPI N, GRAPPA motion sensitivity also show why MRI explanations often require several
levels. At the microscopic level, spins precess, relax, dephase, or refocus. At the sequence
level, RF pulses and gradients impose timing and spatial encoding. At the reconstruction level,
Fourier relationships convert sampled signals into images. At the experimental level, subject
motion, physiology, hardware stability, and human factors determine whether the image series
supports a defensible fMRI interpretation.

For practice, the reader should be able to restate motion sensitivity without using slide
shorthand. The restatement should include the relevant variables, the direction of the effect,
and the likely failure mode. A good explanation is specific enough to predict what would happen
if the field strength, gradient area, echo spacing, flip angle, coil sensitivity, motion state,
or nuisance measurement changed.

## Figure 7.2. GRAPPA motion sensitivity and tradeoffs

![Figure 7.2 panel](figures/fig_7_2_panel_01_source_164.png)

![Figure 7.2 panel](figures/fig_7_2_panel_02_source_165.png)

![Figure 7.2 panel](figures/fig_7_2_panel_03_source_166.png)

![Figure 7.2 panel](figures/fig_7_2_panel_04_source_167.png)

**Figure 7.2. GRAPPA motion sensitivity and tradeoffs.** Motion during ACS versus after ACS and the practical gains and costs of GRAPPA. Source pages 164-167 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: GRAPPA motion sensitivity; ACS used to reconstruct all the under-sampled; time series; Motion during the ACS affects all data!!!; Motion after the ACS generates a mismatch; between the ACS and the current EPI volume; ACS1 … ACS2 … EPI1 … EPI2 … EPI3 ............ EPIN-1 … EPI N; Motion corruption of.

This figure should be read as a sequence inside Chapter 7, not as an isolated picture. It begins
with grappa motion sensitivity and ends with grappa pros & cons, so the reader can follow how
the local idea changes across the source panels. The retained source-backed panels are used here
because the original annotations are part of the evidence: the reader needs the labels, axes,
arrows, image examples, and comparison tags to see why the mechanism matters.

The practical lesson is motion during acs versus after acs and the practical gains and costs of
grappa. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 7.2, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label grappa motion
sensitivity and tradeoffs as a diagnosis before checking the visual evidence.

## Protocol consequences

Protocol consequences is the local bridge between the course vocabulary and a self-study
explanation. The relevant source ideas include GRAPPA pros & cons; Reduces PE distortion by
factor R; Reduced distortion can recover some; signal dropout; Can allow higher nominal
resolution; 10-15% more slices in TR; Further information; Partial Fourier versus GRAPPA for;
increasing EPI slice coverage; versus-grappa-for.html. Taken together, they should be read as
one argument about weigh reduced distortion against SNR and motion cost. The textbook version
therefore slows the slide sequence down: first define the measured or manipulated quantity, then
state what changes it, and only then connect the change to image appearance or fMRI
interpretation.

In this part of parallel imaging with grappa, the central discipline is to separate mechanism
from display. A pulse sequence diagram, a k-space grid, or a brain image is not merely a picture
of a result; it encodes a chain of causes. For protocol consequences, that chain starts with the
controlled scanner quantity, passes through spin phase or signal weighting, and ends as a
spatial pattern, time-series change, or acquisition tradeoff. If the chain is left implicit, the
same term can be memorized without being understood.

A useful way to study protocol consequences is to ask three questions for every equation or
panel. What quantity is deliberately controlled in Chapter 7's local sequence or example? What
uncontrolled physical or biological quantity can perturb it? What image-space or time-series
signature would reveal the problem? These questions keep the mathematics connected to practical
fMRI, where protocol choices are judged by SNR, temporal stability, distortion, dropout, timing,
and interpretability rather than by elegance alone.

The source pages named GRAPPA pros & cons, Further information also show why MRI explanations
often require several levels. At the microscopic level, spins precess, relax, dephase, or
refocus. At the sequence level, RF pulses and gradients impose timing and spatial encoding. At
the reconstruction level, Fourier relationships convert sampled signals into images. At the
experimental level, subject motion, physiology, hardware stability, and human factors determine
whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate protocol consequences without using slide
shorthand. The restatement should include the relevant variables, the direction of the effect,
and the likely failure mode. A good explanation is specific enough to predict what would happen
if the field strength, gradient area, echo spacing, flip angle, coil sensitivity, motion state,
or nuisance measurement changed.

### Chapter Summary

Chapter 7 used pages 159-168 to develop explain how coil arrays and calibration data support
accelerated phase encoding, and why motion can corrupt the result. The main lesson is
cumulative: the reader should move from vocabulary to mechanism, from mechanism to protocol
choice, and from protocol choice to image or time-series consequences.

### Key Terms

trajectories, calibration, Motion, sensitivity, Protocol, consequences.

### Review Questions

1. Explain how r=2 trajectories and calibration affects a practical fMRI decision.
2. Describe one way a visual panel in Chapter 7 changes the interpretation of the prose.
3. Name one acquisition parameter from this chapter and predict a tradeoff if it is changed.
4. Distinguish a mechanism-level explanation from an image-appearance description.
5. Identify one quality-control sign that would make you revisit this chapter before scanning more data.
