# Chapter 8. Simultaneous Multi-slice and Multi-echo EPI

This chapter covers source pages 169-182 and turns them into a self-study sequence about extend
epi acceleration and signal modeling to slice multiplexing and multiple echo times. The chapter
is organized by mechanism and scanning consequence, not by slide order alone, so figures appear
where they support the local explanation.

## SMS requirements and reference data

SMS requirements and reference data is the local bridge between the course vocabulary and a
self-study explanation. The relevant source ideas include Simultaneous multi-slice; (SMS) EPI;
a.k.a. multi-band (MB) EPI; Requires a phased-array coil; Need lots of coil loops along the
slice axis; Acquire a set of "single band" reference EPIs; without acceleration, i.e. one multi-
slice set at a; time (takes SMS x TR to acquire); Then acquire time series using simultaneous
slice; Coils along the slice axis?; From Kaza et al. JMRI (2011); From: D Feinberg & K
Setsompop, JMR (2013). Taken together, they should be read as one argument about show why slice-
axis coil diversity and SBRef data matter. The textbook version therefore slows the slide
sequence down: first define the measured or manipulated quantity, then state what changes it,
and only then connect the change to image appearance or fMRI interpretation.

In this part of simultaneous multi-slice and multi-echo epi, the central discipline is to
separate mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is
not merely a picture of a result; it encodes a chain of causes. For sms requirements and
reference data, that chain starts with the controlled scanner quantity, passes through spin
phase or signal weighting, and ends as a spatial pattern, time-series change, or acquisition
tradeoff. If the chain is left implicit, the same term can be memorized without being
understood.

A useful way to study sms requirements and reference data is to ask three questions for every
equation or panel. What quantity is deliberately controlled in Chapter 8's local sequence or
example? What uncontrolled physical or biological quantity can perturb it? What image-space or
time-series signature would reveal the problem? These questions keep the mathematics connected
to practical fMRI, where protocol choices are judged by SNR, temporal stability, distortion,
dropout, timing, and interpretability rather than by elegance alone.

The source pages named Simultaneous multi-slice, - Requires a phased-array coil, Coils along the
slice axis?, From: D Feinberg & K Setsompop, JMR (2013), SMS-EPI pulse sequence, and related
panels also show why MRI explanations often require several levels. At the microscopic level,
spins precess, relax, dephase, or refocus. At the sequence level, RF pulses and gradients impose
timing and spatial encoding. At the reconstruction level, Fourier relationships convert sampled
signals into images. At the experimental level, subject motion, physiology, hardware stability,
and human factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate sms requirements and reference data without
using slide shorthand. The restatement should include the relevant variables, the direction of
the effect, and the likely failure mode. A good explanation is specific enough to predict what
would happen if the field strength, gradient area, echo spacing, flip angle, coil sensitivity,
motion state, or nuisance measurement changed.

## Figure 8.1. SMS requirements, reference data, and pulse sequence

![Figure 8.1 panel](figures/fig_8_1_panel_01_source_169.png)

![Figure 8.1 panel](figures/fig_8_1_panel_02_source_170.png)

![Figure 8.1 panel](figures/fig_8_1_panel_03_source_171.png)

![Figure 8.1 panel](figures/fig_8_1_panel_04_source_172.png)

![Figure 8.1 panel](figures/fig_8_1_panel_05_source_173.png)

![Figure 8.1 panel](figures/fig_8_1_panel_06_source_174.png)

**Figure 8.1. SMS requirements, reference data, and pulse sequence.** Slice-axis coil diversity, SBRef data, and SMS pulse-sequence structure. Source pages 169-174 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Simultaneous multi-slice; (SMS) EPI; a.k.a. multi-band (MB) EPI; Requires a phased-array coil; Need lots of coil loops along the slice axis; Acquire a set of "single band" reference EPIs; without acceleration, i.e. one multi-slice set at a; time (takes SMS x TR to acquire).

This figure should be read as a sequence inside Chapter 8, not as an isolated picture. It begins
with simultaneous multi-slice and ends with from: d feinberg & k setsompop, jmr (2013), so the
reader can follow how the local idea changes across the source panels. The retained source-
backed panels are used here because the original annotations are part of the evidence: the
reader needs the labels, axes, arrows, image examples, and comparison tags to see why the
mechanism matters.

The practical lesson is slice-axis coil diversity, sbref data, and sms pulse-sequence structure.
In a scanner context, the important move is to translate what is drawn into an acquisition
consequence: which gradient is acting, which echo or reference data are being trusted, which
bandwidth or timing choice is limiting, or which image pattern would appear during quality
control.

For Figure 8.1, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label sms requirements,
reference data, and pulse sequence as a diagnosis before checking the visual evidence.

## SMS benefits and limits

SMS benefits and limits is the local bridge between the course vocabulary and a self-study
explanation. The relevant source ideas include EPI SMS=6; Some contrast differences due to
longer effective TR for EPI.; No intentional motion; Motion with SMS-EPI; TSNR images; MB=6, 2
mm voxels, TR=1300 ms; Motion during SBRef; Motion after SBRef; But even SMS has limits!; Voxels
below (2 mm)3 have low SNR; 1.5 mm resolution (partial brain coverage); is probably the
practical limit at 3 T. Taken together, they should be read as one argument about balance speed,
contrast, motion sensitivity, and practical resolution. The textbook version therefore slows the
slide sequence down: first define the measured or manipulated quantity, then state what changes
it, and only then connect the change to image appearance or fMRI interpretation.

In this part of simultaneous multi-slice and multi-echo epi, the central discipline is to
separate mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is
not merely a picture of a result; it encodes a chain of causes. For sms benefits and limits,
that chain starts with the controlled scanner quantity, passes through spin phase or signal
weighting, and ends as a spatial pattern, time-series change, or acquisition tradeoff. If the
chain is left implicit, the same term can be memorized without being understood.

A useful way to study sms benefits and limits is to ask three questions for every equation or
panel. What quantity is deliberately controlled in Chapter 8's local sequence or example? What
uncontrolled physical or biological quantity can perturb it? What image-space or time-series
signature would reveal the problem? These questions keep the mathematics connected to practical
fMRI, where protocol choices are judged by SNR, temporal stability, distortion, dropout, timing,
and interpretability rather than by elegance alone.

The source pages named EPI SMS=6, No intentional motion, But even SMS has limits! also show why
MRI explanations often require several levels. At the microscopic level, spins precess, relax,
dephase, or refocus. At the sequence level, RF pulses and gradients impose timing and spatial
encoding. At the reconstruction level, Fourier relationships convert sampled signals into
images. At the experimental level, subject motion, physiology, hardware stability, and human
factors determine whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate sms benefits and limits without using slide
shorthand. The restatement should include the relevant variables, the direction of the effect,
and the likely failure mode. A good explanation is specific enough to predict what would happen
if the field strength, gradient area, echo spacing, flip angle, coil sensitivity, motion state,
or nuisance measurement changed.

## Figure 8.2. SMS image examples and limits

![Figure 8.2 panel](figures/fig_8_2_panel_01_source_175.png)

![Figure 8.2 panel](figures/fig_8_2_panel_02_source_176.png)

![Figure 8.2 panel](figures/fig_8_2_panel_03_source_177.png)

**Figure 8.2. SMS image examples and limits.** Contrast differences, SBRef motion, voxel-size limits, and practical MB factors. Source pages 175-177 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: EPI SMS=6; Some contrast differences due to longer effective TR for EPI.; No intentional motion; Motion with SMS-EPI; TSNR images; MB=6, 2 mm voxels, TR=1300 ms; Motion during SBRef; Motion after SBRef.

This figure should be read as a sequence inside Chapter 8, not as an isolated picture. It begins
with epi sms=6 and ends with but even sms has limits!, so the reader can follow how the local
idea changes across the source panels. The retained source-backed panels are used here because
the original annotations are part of the evidence: the reader needs the labels, axes, arrows,
image examples, and comparison tags to see why the mechanism matters.

The practical lesson is contrast differences, sbref motion, voxel-size limits, and practical mb
factors. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 8.2, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label sms image examples and
limits as a diagnosis before checking the visual evidence.

## Multi-echo acquisition and classification

Multi-echo acquisition and classification is the local bridge between the course vocabulary and
a self-study explanation. The relevant source ideas include Multi-echo EPI; Combine 2+ echoes to
boost SNR; Or use a model to classify BOLD from; non-BOLD signal changes; tedana: TE Dependent
ANAlysis; Weighted sum of echoes; Classify BOLD vs non-BOLD; ME-EPI pros & cons; Can boost
regional SNR; Can sometimes differentiate artifacts; Doesn't deal with a lot of physiology;
(e.g. blood gases) which cause real. Taken together, they should be read as one argument about
explain weighted echo combination and BOLD/non-BOLD separation. The textbook version therefore
slows the slide sequence down: first define the measured or manipulated quantity, then state
what changes it, and only then connect the change to image appearance or fMRI interpretation.

In this part of simultaneous multi-slice and multi-echo epi, the central discipline is to
separate mechanism from display. A pulse sequence diagram, a k-space grid, or a brain image is
not merely a picture of a result; it encodes a chain of causes. For multi-echo acquisition and
classification, that chain starts with the controlled scanner quantity, passes through spin
phase or signal weighting, and ends as a spatial pattern, time-series change, or acquisition
tradeoff. If the chain is left implicit, the same term can be memorized without being
understood.

A useful way to study multi-echo acquisition and classification is to ask three questions for
every equation or panel. What quantity is deliberately controlled in Chapter 8's local sequence
or example? What uncontrolled physical or biological quantity can perturb it? What image-space
or time-series signature would reveal the problem? These questions keep the mathematics
connected to practical fMRI, where protocol choices are judged by SNR, temporal stability,
distortion, dropout, timing, and interpretability rather than by elegance alone.

The source pages named Multi-echo EPI, Weighted sum of echoes, Classify BOLD vs non-BOLD,
Classify BOLD vs non-BOLD, ME-EPI pros & cons also show why MRI explanations often require
several levels. At the microscopic level, spins precess, relax, dephase, or refocus. At the
sequence level, RF pulses and gradients impose timing and spatial encoding. At the
reconstruction level, Fourier relationships convert sampled signals into images. At the
experimental level, subject motion, physiology, hardware stability, and human factors determine
whether the image series supports a defensible fMRI interpretation.

For practice, the reader should be able to restate multi-echo acquisition and classification
without using slide shorthand. The restatement should include the relevant variables, the
direction of the effect, and the likely failure mode. A good explanation is specific enough to
predict what would happen if the field strength, gradient area, echo spacing, flip angle, coil
sensitivity, motion state, or nuisance measurement changed.

## Figure 8.3. Multi-echo EPI and BOLD classification

![Figure 8.3 panel](figures/fig_8_3_panel_01_source_178.png)

![Figure 8.3 panel](figures/fig_8_3_panel_02_source_179.png)

![Figure 8.3 panel](figures/fig_8_3_panel_03_source_180.png)

![Figure 8.3 panel](figures/fig_8_3_panel_04_source_181.png)

![Figure 8.3 panel](figures/fig_8_3_panel_05_source_182.png)

**Figure 8.3. Multi-echo EPI and BOLD classification.** Weighted echo summation, TE dependence, and BOLD/non-BOLD component classification. Source pages 178-182 are grouped because they teach one local mechanism or diagnostic comparison. Key source labels and terms include: Multi-echo EPI; Combine 2+ echoes to boost SNR; Or use a model to classify BOLD from; non-BOLD signal changes; tedana: TE Dependent ANAlysis; Weighted sum of echoes; Classify BOLD vs non-BOLD; ME-EPI pros & cons.

This figure should be read as a sequence inside Chapter 8, not as an isolated picture. It begins
with multi-echo epi and ends with me-epi pros & cons, so the reader can follow how the local
idea changes across the source panels. The retained source-backed panels are used here because
the original annotations are part of the evidence: the reader needs the labels, axes, arrows,
image examples, and comparison tags to see why the mechanism matters.

The practical lesson is weighted echo summation, te dependence, and bold/non-bold component
classification. In a scanner context, the important move is to translate what is drawn into an
acquisition consequence: which gradient is acting, which echo or reference data are being
trusted, which bandwidth or timing choice is limiting, or which image pattern would appear
during quality control.

For Figure 8.3, use the panels as a local reasoning test. If they show a temporal sequence, ask
what physical quantity is being conserved, reversed, accelerated, or lost. If they show images,
compare the same anatomical region across the named conditions before making a protocol
conclusion. That habit prevents a common fMRI error: treating the label multi-echo epi and bold
classification as a diagnosis before checking the visual evidence.

### Chapter Summary

Chapter 8 used pages 169-182 to develop extend epi acceleration and signal modeling to slice
multiplexing and multiple echo times. The main lesson is cumulative: the reader should move from
vocabulary to mechanism, from mechanism to protocol choice, and from protocol choice to image or
time-series consequences.

### Key Terms

requirements, reference, data, benefits, limits, Multi, echo, acquisition.

### Review Questions

1. Explain how sms requirements and reference data affects a practical fMRI decision.
2. Describe one way a visual panel in Chapter 8 changes the interpretation of the prose.
3. Name one acquisition parameter from this chapter and predict a tradeoff if it is changed.
4. Distinguish a mechanism-level explanation from an image-appearance description.
5. Identify one quality-control sign that would make you revisit this chapter before scanning more data.
