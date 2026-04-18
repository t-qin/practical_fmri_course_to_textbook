# Practical fMRI: From NMR Foundations to EPI Artifacts, Advanced Acquisition, and Biological Confounds
## Run 3 Draft — Chapters 5–9

**Scope of this draft.** This run develops the middle physics-and-acquisition core of the book. It expands the slide material covering Fourier intuition, gradient encoding, slice selection, gradient echoes, k-space, echo-planar imaging (EPI), and the three classic EPI artifact classes: ghosting, distortion, and dropout. The goal is not to summarize the slides, but to turn them into a cumulative textbook explanation that makes later troubleshooting chapters possible.

---

# Chapter 5. Fourier Transform Intuition for MRI

## 5.1 Why MRI needs the Fourier transform at all
Once the existence of a detectable transverse MR signal is understood, the next practical question is obvious: how can that signal be turned into an image? The answer is that MRI does not measure spatial location directly in the ordinary photographic sense. Instead, it encodes spatial information into signal frequency and phase, then uses a **Fourier transform** to recover the underlying spatial pattern.

That is why the source slides begin this section with a pair of conjugate-variable relationships:
- **time <-> frequency**
- **space <-> k-space**

The Fourier transform is the mathematical bridge that connects each pair.

MRI learners often find this stage psychologically harder than the earlier NMR material. Magnetization and excitation can be imagined as arrows and rotations. Fourier analysis feels more abstract. But the physical idea is simpler than it first appears: if a measured waveform is built from many oscillatory contributions, the Fourier transform tells us what frequencies are present and how much of each is present. In MRI, gradients deliberately make spins at different positions behave like different frequency or phase contributors, so that the Fourier transform becomes a spatial decoder.

## 5.2 Conjugate variables in MRI
Two conjugate-variable relationships matter constantly in MRI.

### Time and frequency
A signal recorded as a function of **time** can be transformed into a representation as a function of **frequency**. This is the familiar use of Fourier analysis in signal processing.

### Space and k-space
A signal represented as a function of **position** can be transformed into a representation as a function of **spatial frequency**, commonly called **k-space** in MRI.

Spatial frequency does not mean “how fast tissue moves.” It means how rapidly image intensity changes across space.
- Low spatial frequencies correspond to broad, slowly varying image structure and overall contrast.
- High spatial frequencies correspond to sharp edges, fine detail, and rapid intensity transitions.

MRI works because magnetic field gradients convert position into phase/frequency variation in a controlled way, allowing the scanner to sample spatial-frequency information directly.

## 5.3 What the Fourier transform does physically
The source slides introduce the Fourier transform as an analysis of frequency content. That is the correct practical entry point. A complex waveform that looks confusing in the time domain may be understood as the sum of simpler oscillatory components. The Fourier transform decomposes it into those components.

In symbolic form, the time-to-frequency transform can be written as

\[
s(\omega) = \int_{-\infty}^{\infty} S(t)e^{-i\omega t}\,dt,
\]

where:
- \(S(t)\) is the signal as a function of time,
- \(s(\omega)\) is the signal represented as a function of angular frequency,
- \(\omega\) is angular frequency,
- and \(i\) is the imaginary unit.

The source slides also remind the reader of Euler’s relation,

\[
e^{i\phi} = \cos\phi + i\sin\phi,
\]

which matters because rotating vectors, oscillating sinusoids, and phase evolution are all different views of the same underlying complex representation.

A rotating vector in the complex plane generates a sinusoidal projection along any axis. This is exactly why precessing transverse magnetization can be treated naturally with complex exponentials.

## 5.4 Why complex notation is not optional ornament
Complex notation in MRI is sometimes treated as a technical nuisance, but it is actually one of the cleanest ways to represent signal phase and amplitude simultaneously. The measured MR signal is not only about “how much signal” exists. It is also about **how the phase evolves** across time and across space.

This matters immediately for MRI because gradients do not just scale the signal. They impose position-dependent phase evolution. The Fourier transform then converts that phase pattern into spatial localization.

## 5.5 Magnetic field gradients as frequency encoders
The source slides return to the Larmor equation and then add a gradient along the x direction:

\[
\omega_0 = \gamma B_0,
\]

and with a gradient,

\[
\omega(x) = \gamma\big(B_0 + G_x x\big).
\]

This equation is one of the decisive transitions in MRI. It says that when a gradient is applied, spins at different positions experience different magnetic fields and therefore precess at different frequencies.

That is the essence of spatial encoding. Without a gradient, all positions would precess at the same base frequency \(\omega_0\). With a gradient, location along x becomes frequency-labeled.

Several practical consequences follow.

1. When the gradient is off, all points again precess at the same base rate determined by \(B_0\).
2. When the gradient is on, spins on one side of isocenter precess faster and spins on the other side precess slower.
3. The total field is what matters. The gradient does not replace \(B_0\); it perturbs it linearly across space.
4. The sign and magnitude of the gradient determine the direction and steepness of spatial frequency encoding.

## 5.6 One-dimensional MRI as the cleanest starting model
The slides wisely introduce **one-dimensional MRI** before two-dimensional imaging. If a gradient is applied along x, and the sample is thought of as a set of small spatial elements along x, then each element contributes signal with its own gradient-imposed precessional frequency.

In that picture,
- positions \(x_1, x_2, \ldots, x_n\) map to frequencies \(\omega_1, \omega_2, \ldots, \omega_n\),
- the total signal is the sum of all these contributions,
- and the Fourier transform of the measured waveform reveals the spatial distribution along x.

This is not yet full MRI, but it contains the central intuition: gradients translate position into spectral structure.

## 5.7 Projection imaging and the historical first MRI
The source deck references Paul Lauterbur’s first MRI work, which is historically important because it shows that image formation did not begin with fully modern k-space formalism. Early MRI development relied heavily on projection logic: acquire signals under different gradient directions and infer spatial structure from those projections.

This historical reminder matters pedagogically. MRI is not mysterious because it uses Fourier transforms; it is a natural extension of the idea that if different spatial locations are made to contribute distinguishable signal components, an image can be reconstructed.

## 5.8 From time-domain signal to spatial-domain description
The source slides set up the central MRI derivation by imagining the sample divided into small signal-producing chunks along x. Before a gradient is turned on, each chunk contributes simply according to its local magnetization.

With the gradient off,

\[
S(t) = \int M(x)\,dx,
\]

if one ignores relaxation and explicit phase evolution. Once the frequency-encoding gradient is turned on, each little chunk accumulates a phase proportional to position and time, and the signal becomes

\[
S(t) = \int M(x)e^{i\gamma G_x t x}\,dx.
\]

This is the central bridge equation. It says that the measured signal is the integral of the object weighted by a position-dependent phase factor imposed by the gradient.

If we then define a spatial-frequency coordinate,

\[
k_x = \frac{\gamma}{2\pi}\int G_x(t)\,dt,
\]

or, in the simple constant-gradient case used in the slides,

\[
k_x \propto \gamma G_x t,
\]

then the signal can be rewritten in the form

\[
S(k_x) = \int M(x)e^{i2\pi k_x x}\,dx,
\]

which is precisely a Fourier transform relationship between object space and k-space.

### A note on conventions
MRI literature uses slightly different Fourier conventions. Some write the exponent with \(i kx\), others with \(i2\pi kx\), depending on whether angular or cyclic frequency conventions are being used. The important point is not the bookkeeping constant. The important point is that **gradient area determines the sampled spatial frequency**.

## 5.9 Space and k-space are Fourier pairs
The slides state directly that space and k-space are Fourier pairs. This should be taken literally.

- **Image space** is where anatomy appears.
- **K-space** is a representation of the same object in spatial-frequency coordinates.

K-space is not a weird alternate image. It is not “halfway reconstructed anatomy.” It is the domain in which the scanner naturally collects encoded information.

One of the most useful conceptual shifts in MRI education occurs when a reader realizes that pulse sequences can be understood as **recipes for moving through k-space**.

## 5.10 Why this matters for the rest of MRI
Once the Fourier viewpoint is accepted, many later topics become much easier:
- slice selection becomes frequency selection under a gradient,
- gradient echo readout becomes a journey through k-space,
- phase encoding becomes a controlled displacement in ky,
- EPI becomes a rapid multi-echo raster through two-dimensional k-space,
- reduced resolution becomes omission of high spatial frequencies,
- and artifacts become errors in how k-space was sampled, shifted, or phase-corrupted.

This is why Fourier intuition is not just a mathematical prelude. It is the conceptual language of MRI pulse sequences.

---

**Figure 5.1 (planned).** Time-frequency and space-k-space conjugate-variable relationships. Adapt from source slides 32–33.

**Figure 5.2 (planned).** One-dimensional gradient encoding and how position maps to frequency components. Adapt from source slides 39–42.

**Figure 5.3 (planned).** Historical projection imaging and Lauterbur’s early MRI logic. Adapt from source slide 43.

---

### Why This Matters
If you do not understand why the Fourier transform belongs in MRI, later topics like k-space, EPI ghosting, partial Fourier, and parallel imaging will feel like disconnected tricks. If you do understand it, those later topics become variations on one idea: **the scanner encodes space into measurable phase and frequency patterns, then reconstructs the object by Fourier inversion**.

---

## Chapter 5 Summary
- MRI relies on Fourier relationships between time and frequency, and between space and k-space.
- Gradients make resonance frequency or phase depend on position.
- The measured MR signal under a gradient is the sum of many spatial contributions with position-dependent phase.
- That signal naturally takes the mathematical form of a Fourier transform of the underlying object.
- K-space is the spatial-frequency representation of the image, not a partial image in ordinary space.

## Key Terms
- Fourier transform
- Conjugate variables
- Spatial frequency
- K-space
- Frequency encoding
- Complex signal
- Euler relation
- Projection imaging

## Review Questions
1. What does it mean to say that time and frequency are conjugate variables?
2. Why does adding a gradient make MRI spatially informative?
3. What is the physical meaning of k-space?
4. Why is complex notation especially useful in MRI?
5. In plain language, what does the Fourier transform do for MRI reconstruction?

---

# Chapter 6. Gradients, Slice Selection, and Basic MRI Image Formation

## 6.1 Magnetic field gradients as controlled spatial encoders
Gradients are the practical devices that make MRI an imaging method rather than a bulk spectroscopy experiment. A gradient superimposes a linearly varying magnetic field on top of the main field. Because resonance frequency depends on total field, a gradient converts location into a predictable shift in phase or frequency.

But gradients do more than “label space.” Their time course controls how much phase accumulates. This makes them exquisitely flexible. The same gradient hardware can select a slice, generate a readout echo, encode phase, rewind unwanted dephasing, and steer a trajectory through k-space.

In practical MRI, gradients are therefore best understood not as background hardware but as dynamic sequence components that create the mapping between magnetization and image coordinates.

## 6.2 Slice selection with sinc-shaped RF pulses
The source slides introduce slice selection using one of the classic Fourier facts: the Fourier transform of a **sinc** is a **rectangular frequency profile** (and conversely, the transform of a rectangular profile is a sinc-like time-domain function).

This matters because a standard square RF pulse excites a broad frequency content with poor selectivity. If, instead, a **sinc-modulated RF pulse** is used, then its frequency-domain profile becomes much more sharply bounded. That makes it possible to excite only a controlled frequency band.

Now combine this selective RF pulse with a gradient applied along z. Under the gradient, resonance frequency depends on z position. Therefore a selected frequency band corresponds to a selected spatial band. That spatial band is the **slice**.

This is one of the most elegant uses of Fourier thinking in MRI: a shape in time is chosen so that its transform has the right frequency selectivity, and the gradient converts that frequency selection into spatial selection.

## 6.3 How slice thickness is determined
The source slides explain slice thickness in a practical way: if the RF pulse defines an excited frequency bandwidth \(\Delta \nu\), and a slice-selection gradient \(G_z\) maps frequency to position, then the selected thickness \(\Delta z\) is proportional to the ratio of RF bandwidth to gradient strength.

In conceptual form,

\[
\Delta z \propto \frac{\Delta \nu}{\gamma G_z}.
\]

This means slice thickness can be changed in two main ways:
1. change the gradient strength, or
2. change the RF pulse bandwidth.

The source slides point out an important practical preference. If one wants to halve slice thickness, one could double \(G_z\), or alternatively lengthen the RF pulse so that its bandwidth narrows appropriately. In many practical settings, it is preferable to adjust the gradient and keep RF pulse duration fixed if possible, because changing pulse duration has broader consequences for sequence timing and efficiency.

This is a good example of how sequence design balances theory with operational convenience. Theoretically, multiple knobs can achieve the same slice thickness. Practically, some knobs are more convenient than others.

## 6.4 Why slice selection needs a refocusing gradient
The source slides emphasize that slice selection requires more than simultaneous RF excitation and a gradient. During the RF pulse, the slice-selection gradient also introduces **phase dispersion** across the slice. If nothing were done about this, the slice would be selected, but the magnetization within it would already be partially dephased.

To compensate, a slice-select **refocusing gradient lobe** is applied. Its purpose is to reverse the phase accumulation caused by the slice-selection gradient so that the net phase of the selected magnetization is re-centered.

The practical lesson is important: many gradients in MRI serve dual roles. The same gradient that enables a desired encoding operation may also create unwanted dephasing that must later be undone.

## 6.5 Gradient echoes: reversible gradient-induced dephasing
The source deck next turns to the **gradient echo (GRE)** as a readout mechanism. This is another sequence that makes sense immediately once gradients are understood as phase-imposing devices.

If a gradient is applied in one direction, spins at different positions dephase relative to each other. But unlike intrinsic microscopic T2 processes, this gradient-induced dephasing is controlled and reversible. If a later gradient of opposite sign is applied with the right area, the phase dispersion can be canceled, bringing the magnetization back into coherence and producing a **gradient echo**.

This is the gradient analogue of refocusing, but the key distinction is that it does **not** use a 180° RF pulse. It uses balanced gradient moments instead.

## 6.6 Gradient echo formation step by step
The source slides break gradient echo formation into three periods. That staged explanation is worth preserving.

1. **Initial dephasing period.** A readout gradient drives magnetization away from coherence by making position-dependent phase accumulate.
2. **Rephasing period.** A gradient of opposite sign drives the system back toward zero net phase.
3. **Second dephasing/readout period.** After the echo center is reached, continued gradient evolution dephases the signal again while the readout samples it.

The source slides also emphasize the point of zero phase coherence: the moment when all the reversible gradient-induced dispersion has been undone. That instant is the gradient echo center.

This stepwise view is especially useful because it later becomes the language of k-space traversal. Periods 1, 2, and 3 are not just phase manipulations in image space; they are directed movements through k-space.

## 6.7 Why a gradient echo is not a spin echo
The source material explicitly warns that a gradient echo is very different from a spin echo. This deserves strong emphasis.

A **spin echo** uses a 180° RF pulse to reverse certain types of dephasing caused by static field offsets. A **gradient echo** only reverses dephasing caused by the applied gradient moments themselves. It does **not** refocus dephasing associated with \(T_2'\) or other susceptibility-related field inhomogeneity effects.

That is why gradient echoes are intrinsically sensitive to **T2*** rather than pure T2. This is exactly why gradient-echo EPI is so useful for BOLD fMRI—and also why it is so vulnerable to susceptibility artifact.

## 6.8 Signal gain and readout timing in GRE
The source slides make a subtle but practically interesting point: acquiring both the rephasing and dephasing sides of the gradient echo yields about \(\sqrt{2}\) more signal than acquiring only one side. This reflects the benefit of collecting more of the coherent echo waveform rather than discarding half of it.

The slides also note that a gradient echo introduces time between excitation and signal detection. This matters because signal continues to decay during that interval. Echo formation is useful, but it is not free. Longer echo times increase T2* weighting and can improve BOLD sensitivity, but they also reduce signal amplitude and worsen dropout or distortion vulnerabilities.

## 6.9 From slice selection to basic image formation
By this stage the basic pieces of an MRI image are in place:
1. use RF plus a gradient to select a slice,
2. control phase and frequency with gradients,
3. generate a detectable echo,
4. record the signal during a controlled trajectory through spatial-frequency space,
5. and reconstruct the image with a Fourier transform.

The remaining conceptual step is to describe that trajectory explicitly. That is the job of k-space.

---

**Figure 6.1 (planned).** Sinc-shaped RF pulse and rectangular excitation bandwidth, showing frequency-selective slice selection under \(G_z\). Adapt from source slides 44–47.

**Figure 6.2 (planned).** Slice-selection gradient plus refocusing lobe. Adapt from source slide 48.

**Figure 6.3 (planned).** Three-stage gradient-echo formation sequence. Adapt from source slides 49–53.

---

### Common Confusion: dephasing is not always permanent
Students often learn “dephasing means signal loss” and stop there. The more accurate statement is that **some dephasing is reversible and some is not**. Gradient-induced phase dispersion is deliberately reversible. T2* losses from field inhomogeneity are not fully reversed by a gradient echo. This distinction is one of the foundations of later fMRI artifact physics.

---

## Chapter 6 Summary
- Slice selection uses a frequency-selective RF pulse during a gradient, converting a selected frequency band into a selected spatial slice.
- Slice thickness depends on RF bandwidth and gradient strength.
- Slice selection also creates unwanted phase dispersion, so a refocusing gradient is required.
- Gradient echoes are formed by reversing gradient-induced dephasing with balanced gradient moments.
- Gradient echoes are not spin echoes; they do not refocus susceptibility-related T2* effects.
- GRE timing choices affect signal, contrast, and later artifact burden.

## Key Terms
- Slice selection
- Sinc pulse
- Slice thickness
- Refocusing gradient
- Gradient echo
- T2′
- Readout gradient
- Echo center

## Review Questions
1. Why is a sinc-shaped RF pulse useful for slice selection?
2. How can slice thickness be changed in practice?
3. Why does slice selection require a refocusing lobe?
4. Why is a gradient echo sensitive to T2* effects?
5. What is the difference between reversible gradient dephasing and spin-echo refocusing?

---

# Chapter 7. K-Space: The Organizing Language of MRI

## 7.1 What k-space is and what it is not
K-space is often introduced visually before it is explained conceptually, which is why students sometimes mistake it for a strange “pre-image.” The source slides correctly describe it as a useful pictorial representation of imaging pulse sequences. That is an excellent starting definition.

K-space is the domain in which MRI stores **spatial-frequency information**. Every point in k-space represents a particular Fourier component of the image. The final image is obtained by taking the inverse Fourier transform of the fully sampled k-space data.

K-space is therefore not:
- a distorted image waiting to be fixed,
- a direct map of anatomy,
- or a separate physical space inside the scanner.

It is a coordinate system for describing what spatial frequencies of the object have been sampled.

## 7.2 The Fourier transform of an image
The source slides show that if one takes the two-dimensional Fourier transform of an ordinary image, one gets its reciprocal-space representation. That is the cleanest way to see why k-space exists. The image and k-space contain the same information, but expressed differently.

The image tells us where structures are.
K-space tells us what spatial frequencies are present.

In practical MRI, we typically acquire the k-space representation first and reconstruct the image second.

## 7.3 Frequency encoding as movement through kx
The source slides derive the key x-dimension signal relationship under a readout gradient:

\[
S(t) = \int M(x)e^{i\gamma G_x t x}\,dx,
\]

which can be rewritten as

\[
S(k_x) = \int M(x)e^{i2\pi k_x x}\,dx
\]

once one defines kx appropriately from gradient area.

This means that turning on the read gradient causes the system to **move through kx**. When the gradient is off, kx is static. When the gradient is on, kx changes according to gradient amplitude and time.

The source slides put this beautifully: the action of the gradient is to **trace a path through the Fourier transform of the image**. That sentence is worth keeping almost verbatim because it captures the physical meaning of readout better than many formal derivations do.

## 7.4 Gradient area is the real k-space control variable
The source slides summarize the k parameter as the time integral of a gradient. In its standard form,

\[
k(t) = \frac{\gamma}{2\pi}\int_0^t G(\tau)\,d\tau.
\]

This is one of the most operationally useful equations in MRI.

It tells us that k-space position is determined not by gradient amplitude alone and not by duration alone, but by **gradient area**. That means:
- a strong short gradient and a weaker longer gradient can reach the same k-space point if their areas match,
- rewinder gradients move the trajectory backward by contributing opposite area,
- and complicated sequences can be understood by mentally integrating gradient waveforms over time.

This is why the source slides urge the reader to do a “mental integration” of the pulse sequence. That mental habit is central to MRI fluency.

## 7.5 The gradient echo as a k-space journey
In the source deck, the gradient echo is reinterpreted as a path through k-space.

- Before period 1, the system begins at the origin: \((k_x, k_y) = (0,0)\).
- Period 1 moves the trajectory away from the origin.
- Period 2 returns the trajectory toward the center.
- Period 3 carries it past the origin in the opposite direction while the echo is sampled.

This is a profound conceptual simplification. Instead of thinking of readout only in terms of spins being more or less dephased, one thinks in terms of where in k-space the sequence is at each moment.

That perspective generalizes immediately to phase encoding and to EPI.

## 7.6 Phase encoding as movement through ky
The source slides next introduce a second gradient episode, \(G_y\), which encodes position in the y direction as phase. Just as frequency encoding made x-position contribute a distinct oscillatory term, phase encoding makes y-position contribute a distinct accumulated phase.

The y-dimension signal relationship is analogous:

\[
S(k_y) = \int M(y)e^{i2\pi k_y y}\,dy,
\]

with

\[
k_y = \frac{\gamma}{2\pi}\int G_y(t)\,dt.
\]

Importantly, the phase-encoding gradient is usually applied in a short episode before readout, not during acquisition of the readout itself. Otherwise the simultaneous presence of both gradients would create an oblique effective encoding direction during data collection.

In practical terms, phase encoding shifts the trajectory to a chosen ky value, and then the readout gradient sweeps through kx at that ky level.

## 7.7 Filling a two-dimensional k-space matrix
The source slides show how repeated acquisitions with different phase-encoding amplitudes can fill a 2D grid of k-space points. A small example using a 16 × 16 grid makes the basic logic visible.

Each repetition of the pulse sequence:
1. selects the slice,
2. applies a chosen phase-encoding step to set the ky position,
3. reads across kx during the readout,
4. and stores one line of k-space.

Repeat that process across all required ky values, and the full 2D k-space matrix is obtained.

A two-dimensional Fourier transform of that matrix then yields the 2D image.

The source slides summarize 2D MRI in exactly this way:
1. select a slice,
2. fill the k-space matrix,
3. take the 2D Fourier transform.

That is as good a minimal description of MRI image formation as one can give.

## 7.8 What low and high spatial frequencies contribute
One of the most important intuitive lessons in k-space comes from seeing what happens when parts of k-space are removed.

The central region of k-space contains **low spatial frequencies**. These contribute broad contrast, gross shape, and coarse intensity variation.

The outer regions contain **high spatial frequencies**. These contribute edges, sharp transitions, and fine detail.

The source slides illustrate this with examples of reduced resolution and high-spatial-frequency-only content. These are textbook-worthy because they cure one of the most common misunderstandings: many students incorrectly assume the center of k-space corresponds to the center of the image. It does not. It corresponds to low spatial frequencies across the whole image.

## 7.9 Reduced resolution and selective loss of k-space content
If one omits high spatial frequencies, the image becomes blurred and reduced in resolution. Boundaries soften because fine detail is missing.

If one keeps only high spatial frequencies, broad intensity structure is lost and the image becomes edge-like, emphasizing transitions but not overall anatomy.

This perspective is essential for later understanding of acceleration methods and reconstruction artifacts. Many practical acquisition compromises effectively reshape or incompletely sample k-space, and the resulting image changes should be interpreted as changes in spatial-frequency content rather than mysterious visual side effects.

## 7.10 Aliasing (wrap-around)
The source slides then turn to **aliasing**, also called **wrap-around**. Aliasing occurs when the object extends beyond the field of view in an encoded dimension, or equivalently when sampling is insufficient to represent the full spatial extent without ambiguity.

In image space, anatomy from outside the nominal field of view appears wrapped into the image.

In Fourier terms, aliasing is not a random artifact. It is the expected consequence of insufficient sampling. This matters later in EPI as well, because some ghost images and accelerated-imaging artifacts can be understood as special forms of aliasing or controlled unaliasing failure.

## 7.11 Truncation artifact (Gibbs ringing)
The source slides explicitly identify **truncation artifact**, also known as **Gibbs ringing**. This artifact occurs when k-space is abruptly truncated, especially when a sharp edge in image space is represented by an insufficient number of Fourier components.

The result is oscillatory overshoot and undershoot near sharp intensity boundaries.

This is a beautiful illustration of the fact that Fourier reconstruction is exact only for fully and appropriately represented spatial frequencies. Sharp edges require broad frequency support. If that support is cut off, oscillatory ringing appears.

In practice, Gibbs ringing is often visible near high-contrast boundaries, such as tissue-fluid interfaces or edges of structures in high-resolution imaging.

## 7.12 Gradient switching and stimulation limits
The last slide in this source block mentions **stimulus limits** and effective current loops induced by gradient switching. This is a practical point that belongs in a textbook even though it is easy to overlook.

Rapidly switched magnetic field gradients induce electric fields in conductive tissue. If switching is strong enough, these induced fields can stimulate peripheral nerves or produce uncomfortable sensations. Thus, gradient performance is constrained not only by hardware capability but also by physiologic tolerance and safety limits.

This is a useful reminder that sequence design is not governed only by image quality. It is also bounded by human safety and comfort.

---

**Figure 7.1 (planned).** Image space versus k-space, showing that they are Fourier pairs rather than different anatomical spaces. Adapt from source slides 54–56.

**Figure 7.2 (planned).** Gradient-echo trajectory through kx and phase-encoding shifts through ky. Adapt from source slides 61–68.

**Figure 7.3 (planned).** Building a 2D k-space matrix line by line. Adapt from source slides 69–77.

**Figure 7.4 (planned).** Effects of preserving only low or high spatial frequencies; reduced resolution and edge-enhanced images. Adapt from source slides 78–81.

**Figure 7.5 (planned).** Aliasing and truncation artifact examples. Adapt from source slides 83–84.

---

### Practical Scanner Implication
Whenever you change resolution, field of view, bandwidth, or acceleration, ask yourself: **what part of k-space sampling am I changing?** This question is often more useful than asking, “what parameter menu option did I modify?”

---

## Chapter 7 Summary
- K-space is the spatial-frequency representation of the image.
- Gradient area, not just gradient amplitude, determines k-space position.
- Frequency encoding sweeps through kx; phase encoding selects ky positions.
- MRI images are formed by filling a k-space matrix and applying a 2D Fourier transform.
- Central k-space contains low spatial frequencies; outer k-space contains high spatial frequencies.
- Reduced resolution, aliasing, and Gibbs ringing all follow naturally from how k-space is sampled or truncated.
- Gradient switching is limited not only by engineering but also by physiologic stimulation constraints.

## Key Terms
- K-space
- Spatial frequency
- Gradient area
- Frequency encoding
- Phase encoding
- Field of view
- Aliasing
- Gibbs ringing
- Peripheral nerve stimulation

## Review Questions
1. Why is gradient area the natural control variable for k-space position?
2. What is the difference between the roles of kx and ky in a standard 2D acquisition?
3. Why does loss of high spatial frequencies reduce resolution?
4. Why does aliasing occur?
5. What is the physical basis of Gibbs ringing?
6. Why can gradient switching not simply be made arbitrarily fast?

---

# Chapter 8. Echo-Planar Imaging (EPI): Why fMRI Is Fast

## 8.1 What makes EPI different
The source slides describe EPI k-space as a **multiple gradient echo sequence**. That is an excellent operational definition. Unlike conventional imaging, where each excitation typically fills only one line of k-space, EPI acquires a long train of echoes after a single excitation and uses them to sample many lines of k-space rapidly.

This is the practical reason EPI became the backbone of fMRI. Whole-brain functional imaging requires repeated sampling over time. If each image required many separate excitations and long delays, temporal resolution would be poor. EPI solves this by being extraordinarily efficient in k-space coverage.

## 8.2 The EPI trajectory
The classic EPI trajectory is a rapid raster or zig-zag across two-dimensional k-space. A strong readout gradient alternates polarity, sweeping left-to-right on one line and right-to-left on the next. Between readouts, small phase-encoding “blips” step the trajectory to the next ky line.

The source slides illustrate this with the first several echoes of a 16-echo train. Although that small matrix is pedagogical, the logic scales directly to modern EPI.

The key point is that EPI converts one excitation into a long, densely packed sampling trajectory through k-space. That is what makes it fast. It is also what makes it fragile.

## 8.3 Why EPI is efficient enough for fMRI
Several features make EPI attractive for fMRI:
- it covers large portions of k-space very quickly,
- it supports whole-brain repeated imaging,
- it provides natural T2* sensitivity when implemented as gradient-echo EPI,
- and it can be combined with multislice, multiband, and acceleration methods.

Because BOLD contrast is a T2*-weighted phenomenon, EPI’s susceptibility sensitivity is not merely a nuisance. It is part of why the method works for functional imaging at all.

This is one of the central tradeoffs of the field: the very mechanism that gives EPI BOLD sensitivity also amplifies its vulnerability to susceptibility artifact.

## 8.4 Echo spacing and why long readouts are dangerous
The source slides later quantify why EPI becomes artifact-prone: one axis of the acquisition is sampled very rapidly, while the phase-encoded axis is effectively updated much more slowly. Echo spacing matters because during the long EPI train, the magnetization continues to evolve under T2* decay and local field inhomogeneity.

The longer the total readout:
- the more time there is for geometric warping,
- the more severe susceptibility-related misregistration becomes,
- the greater the phase mismatch risk between odd and even lines,
- and the more likely signal dropout or blur becomes.

EPI is therefore best thought of as a time-pressured acquisition. It wins speed, but every extra moment during the readout is costly.

## 8.5 The three classic EPI artifacts as a structural consequence
The source slides identify three classic EPI artifact categories:
1. **ghosting**,
2. **distortion**,
3. **dropout**.

This classification is pedagogically useful because it reflects three different failure modes of the same fast readout strategy.

- Ghosting arises when the intended k-space trajectory is sampled inconsistently, especially between alternating readout lines.
- Distortion arises because local off-resonance displaces signal along the slowly encoded direction.
- Dropout arises because transverse coherence is lost so strongly in some regions that little usable signal remains.

All three stem from the fact that EPI trades readout stability for speed.

## 8.6 Multislice EPI and slice ordering
The source slides also cover **slice order** in multislice EPI: ascending, descending, and interleaved. This may sound like a housekeeping detail, but it can matter practically.

If adjacent slices are acquired in immediate succession, imperfect slice profiles and repeated excitations can lead to cross-talk or spin-history effects. Interleaving is often used to reduce such interactions. However, motion complicates the situation. As the source slides note, slice-order choice can interact with motion and spin history.

This means slice timing is not just an analysis nuisance. It is also an acquisition-level phenomenon that can affect what signal is present in the first place.

## 8.7 EPI pros and cons
The source slides summarize the central compromise of EPI nicely:
- T2* relaxation during the readout causes image artifacts.
- But EPI is fast, and when speed is imperative, one accepts the artifacts and manages them.
- BOLD contrast depends on T2* changes when using gradient-echo sequences like EPI.

This can be sharpened into a more complete practical statement.

### Advantages of EPI
- very rapid acquisition,
- compatible with whole-brain repeated imaging,
- strong T2* sensitivity for BOLD,
- supports advanced acceleration strategies.

### Disadvantages of EPI
- high sensitivity to susceptibility variation,
- strong vulnerability to distortion and dropout,
- odd/even line mismatch and ghosting risk,
- sensitivity to motion and instability,
- and more difficult reconstruction than slower, simpler readouts.

## 8.8 Crusher gradients and real EPI pulse sequences
The source slides include a “real EPI pulse sequence” and mention **crusher gradients**, including fat-signal crushers and spurious-water crushers. In textbook form, this belongs in a practical section on making the idealized sequence actually work.

Real pulse sequences include additional gradient moments and correction components for several reasons:
- suppress unwanted residual transverse coherences,
- manage fat contamination,
- handle ghost correction,
- establish correct slice selection,
- and produce the intended k-space echo train.

This is a useful caution against overlearning simplified diagrams. Educational sequence schematics often show only the core logic; actual scanner implementations contain many additional components needed for robustness.

## 8.9 What a good EPI dataset looks like
The source slides include “Good EPI” examples and a temporal-SNR image. This is important because practical MRI competence is not only about knowing artifacts when they are obvious. It is also about knowing what normal, acceptable data look like.

A good EPI dataset should typically show:
- consistent anatomy across slices,
- manageable and expected susceptibility losses rather than catastrophic dropout,
- minimal visible Nyquist ghosting,
- no strong residual wrap-around or aliasing,
- stable temporal behavior across the run,
- and a temporal SNR pattern consistent with coil geometry and known physiology.

## 8.10 Temporal SNR as a quality metric
Temporal SNR (tSNR) is often estimated as the mean signal over time divided by the standard deviation over time. The source slide pairing of a tSNR image with a standard-deviation image is valuable because it teaches the reader to look not only at anatomy but at stability.

An image can look acceptable structurally and still be functionally poor if temporal fluctuations are large. That matters especially in fMRI, where the signal of interest is usually only a few percent or less.

Thus, a practical EPI evaluation should always ask two questions:
1. does the image look anatomically plausible?
2. is the signal stable enough over time for meaningful functional analysis?

## 8.11 The brain is always moving
The last slide in this block announces a theme that becomes central later: **the brain is always moving**. Even before full motion and confound chapters are introduced, this statement belongs here because it reveals a hidden fragility of EPI. Fast acquisition does not mean motion-immune acquisition. In fact, EPI often captures motion consequences vividly because it depends on consistent k-space sampling across time.

This serves as the bridge to both artifact chapters and later confound chapters.

---

**Figure 8.1 (planned).** Zig-zag EPI k-space trajectory with alternating read gradients and phase-encoding blips. Adapt from source slides 87 and 116.

**Figure 8.2 (planned).** Real EPI pulse sequence with slice select, echo train, and correction components. Adapt from source slides 114–116.

**Figure 8.3 (planned).** Example of good EPI and corresponding temporal SNR / standard-deviation images. Adapt from source slides 117–118.

---

### Why This Matters
EPI is not the dominant fMRI method because it is clean. It is dominant because it is fast enough to be useful. Every practical fMRI user must therefore learn to think like an engineer of compromises: **what speed am I buying, and what artifacts am I accepting in return?**

---

## Chapter 8 Summary
- EPI fills large portions of k-space after a single excitation by using a train of gradient echoes.
- Its speed makes whole-brain repeated fMRI feasible.
- Its long readout and alternating trajectory make it structurally vulnerable to ghosting, distortion, and dropout.
- Slice ordering, crusher gradients, and ghost-correction elements matter in real pulse-sequence implementations.
- Image quality must be judged both anatomically and temporally, for example using tSNR.

## Key Terms
- Echo-planar imaging (EPI)
- Echo train
- Echo spacing
- Phase-encoding blip
- Multislice acquisition
- Interleaved slices
- Temporal SNR (tSNR)
- Crusher gradient

## Review Questions
1. Why is EPI so much faster than conventional line-by-line acquisition?
2. Why does the same feature that makes EPI fast also make it fragile?
3. Why is EPI especially well suited to BOLD fMRI?
4. What practical role does slice ordering play in multislice EPI?
5. Why should a dataset with good anatomy still be checked with tSNR or standard-deviation maps?

---

# Chapter 9. The Classic EPI Artifacts: Ghosting, Distortion, and Dropout

## 9.1 Why these three artifacts dominate practical fMRI
The source slides identify ghosting, distortion, and dropout as the three classic EPI artifacts. This classification is extremely useful because these are not merely three random visual defects. They correspond to three different physical consequences of fast T2*-weighted sampling.

- **Ghosting** is mainly a trajectory consistency problem.
- **Distortion** is mainly an off-resonance displacement problem.
- **Dropout** is mainly an intravoxel dephasing problem.

A practical reader should learn to associate each artifact with both its image appearance and its physics origin. If only the appearance is memorized, diagnosis becomes brittle. If only the physics is memorized, real datasets remain hard to interpret. The skill lies in connecting the two.

## 9.2 Nyquist ghosting: the core mechanism
The source slides explain Nyquist ghosting using one of the canonical EPI problems: a delay in signal digitization relative to the alternating read-gradient periods. In EPI, adjacent k-space lines are acquired with opposite read-gradient polarity. If the timing or phase relationship between these odd and even lines is mismatched, their positions no longer align perfectly after reversal into a common k-space orientation.

The source slides show this as a zigzag in reconstructed k-space: rightward lines and leftward lines are shifted relative to each other. The larger the mismatch, the stronger the ghosting.

This is a beautiful example of an artifact that is best understood in k-space first and image space second. The ghost image is not “coming from nowhere.” It is the Fourier consequence of structured line-to-line error.

## 9.3 Why ghosts appear at half the field of view
The source slides make the key point that Nyquist ghosts commonly appear at **FOV/2** in the phase-encoding direction. Their explanation is elegant: if the line-to-line error effectively doubles the ky increment of the error term, then the corresponding ghost image has half the field of view and therefore wraps around in the final image.

The practical rule is easy to remember:
- classic Nyquist ghosts are centered about the midpoint of the phase-encode dimension.

This makes them diagnostically distinctive. If a repeated replica appears in the expected half-FOV displacement, Nyquist-related odd/even mismatch is a prime suspect.

## 9.4 Why weak ghosts can still be serious
The source slides note that in a good experiment ghosts are often faint. That is true—but it is not reassuring enough. Faint ghosts can still matter if they overlap brain tissue, vary over time, or correlate with task or motion.

In fMRI, weak structured instability can be more dangerous than an obvious catastrophic artifact, because the dataset may appear acceptable while still containing systematic nuisance variation.

This is why the source slides also emphasize that ghosts vary with time and show standard-deviation images. Time variation is often more important than static visibility.

## 9.5 Other common causes of ghosting
The source deck includes a slide on other common causes of EPI ghosts. Even when digitization delay is the textbook model, practical ghosting can arise from multiple sources, including:
- eddy currents,
- gradient timing asymmetry,
- phase errors,
- hardware instability,
- motion, especially periodic motion,
- physiological sources like eye movements,
- and fat signal contamination.

This broader view matters because not every ghost-like pattern should be blamed on the same correction strategy.

## 9.6 Scalp fat suppression and chemical-shift contamination
The source slides explicitly state that **scalp fat suppression is required**. This is a highly practical point.

Fat and water resonate at slightly different frequencies because of chemical shift. In EPI, where bandwidth along the phase-encoded axis is very low, even modest off-resonance differences can produce substantial misregistration. Strong fat signal from the scalp can therefore appear shifted into the brain or create ghost-like contamination.

That is why fat suppression is not just a cosmetic preference in EPI. It is often essential to prevent signal from outside the brain from being mis-mapped into functionally relevant locations.

## 9.7 Chemical shift in imaging practice
The source slides revisit chemical shift here with a more imaging-specific emphasis. They note that shielding differences create the frequency shift and give a ppm-to-hertz scaling example at approximately 3 T.

In practical MRI, the exact ppm convention matters less than the consequence: **fat and water precess at different frequencies**, and low-bandwidth dimensions are especially sensitive to this difference.

Thus, chemical shift becomes important not only in spectroscopy but in routine EPI artifact control. The later artifact signature—especially when fat suppression fails—can look like displaced bright signal or ghost-like contamination.

## 9.8 Ramp sampling and pushing readout speed too far
The source slides then discuss **ramp sampling**, in which data acquisition occurs not only during the flat part of the read gradient but also during its ramps. This can improve efficiency because more k-space is sampled per unit time.

But the source slides also warn that ramp sampling can go too far. Shortening echo spacing from, for example, 0.50 ms to 0.43 ms may look attractive, but if gradient behavior and digital correction are not accurate enough, ghosting or other artifacts can worsen.

This is an important acquisition-design lesson: every speed gain has a fidelity cost. A sequence that samples more aggressively may reduce one burden while increasing another.

## 9.9 Distortion: why geometry fails in EPI
The source slides define distortion as misplacement of voxels along the phase-encoded dimension. They further note that this arises because the phase-encoded dimension is sampled relatively slowly.

This can be explained physically as follows. Local field inhomogeneity changes the resonance frequency of the signal. In the frequency-encoding direction, bandwidth per pixel is high, so a given off-resonance shift causes only a small positional error. In the phase-encoded direction, effective bandwidth per pixel is extremely low, so the same off-resonance shift causes a much larger displacement.

Thus, EPI distortion is largely an **off-resonance-to-position-misregistration conversion problem** concentrated in the phase-encoded axis.

## 9.10 Bandwidth and why one axis distorts much more than the other
The source slides make this quantitative using per-pixel bandwidth estimates.

For the frequency-encoding axis,

\[
\text{BW}_{\text{read}} \approx \frac{1/\Delta t}{N_{\text{pixels}}},
\]

with typical values around **2000–2600 Hz/pixel**.

For the phase-encoded axis,

\[
\text{BW}_{\text{phase}} \approx \frac{1/\Delta t_{\text{esp}}}{N_{\text{pixels}}},
\]

with typical values around **20–35 Hz/pixel**.

That difference is enormous. If local field heterogeneity near the sinuses is on the order of **200–300 Hz**, then a region can be misplaced by several pixels in the phase-encode direction but hardly shifted in the read direction.

This is one of the most important practical numbers in EPI. It explains why distortion is not a vague nuisance but a predictable directional effect.

## 9.11 A-P versus P-A phase encoding
The source slides show anterior-to-posterior (A-P) versus posterior-to-anterior (P-A) phase encoding. This is not a trivial orientation choice. Reversing phase-encoding direction reverses the direction in which off-resonance displacement occurs.

That means:
- the same field inhomogeneity can produce different apparent geometric warping depending on phase-encoding direction,
- distortion can be redistributed rather than eliminated,
- and paired reverse-phase-encoded images can be used for distortion correction strategies in modern workflows.

For the practical user, this means phase-encoding direction is a deliberate design choice with anatomical and analysis consequences.

## 9.12 Dropout: when signal is not merely displaced but lost
Unlike distortion, **dropout** is not mainly about signal being moved. It is about signal being lost because within a voxel, spins dephase so strongly that little coherent transverse magnetization remains by the time the echo is sampled.

The source slides correctly note that dropout is not strictly an EPI-only issue. Any gradient-echo acquisition at the same TE could show dropout in a sufficiently inhomogeneous region. However, EPI often makes the problem worse because signal continues to decay during the long in-plane readout.

This is the practical meaning of susceptibility-driven signal dropout in fMRI: there may not be enough coherent signal left to represent the local tissue reliably at all.

## 9.13 Why thin slices reduce dropout
The source slides make a particularly important practical point: **thinner slices produce less dropout**. The reason is that intravoxel field variation is reduced when the voxel spans less depth. If less field variation exists within each voxel, less intravoxel dephasing occurs.

This is also why the source slides emphasize that **two thin slices are better than one thick slice** in this context. The tradeoff, of course, is that thinner slices often reduce raw SNR, increase the number of slices needed for coverage, or complicate timing.

But in dropout-prone regions, reduced intravoxel dephasing can outweigh those costs.

## 9.14 Tradeoffs among TE, slice thickness, coverage, and artifact burden
By this stage the reader can see that many EPI parameters are coupled.

- Longer **TE** increases T2* weighting and often improves BOLD sensitivity, but worsens dropout and reduces signal amplitude.
- Thinner slices reduce dropout but usually reduce per-voxel SNR and may reduce coverage or lengthen acquisition.
- Faster readout or higher acceleration may reduce distortion but increase noise amplification or reconstruction sensitivity.
- Narrower effective bandwidth makes distortion worse but may be tied to other timing constraints.

This is exactly why practical EPI is best taught as a tradeoff system rather than a menu of independent artifact fixes.

## 9.15 Artifact recognition rules of thumb
A practical recognition guide, distilled from the source slides, would include the following:

### Ghosting
- replicated structures in the phase-encode direction,
- often near FOV/2 displacement,
- may vary over time,
- often linked to odd/even mismatch, motion, eyes, or fat.

### Distortion
- stretched, compressed, or displaced anatomy,
- predominantly in the phase-encoded direction,
- strongest near frontal sinuses, ear canals, and other susceptibility boundaries,
- reverses direction when PE polarity is reversed.

### Dropout
- dark signal voids rather than shifted bright anatomy,
- common in orbitofrontal cortex and inferior temporal regions,
- worsens with longer TE and thicker slices,
- reflects irrecoverable local dephasing rather than mere voxel displacement.

---

**Figure 9.1 (planned).** Nyquist ghosting mechanism: odd/even line mismatch, zigzag k-space, and half-FOV ghost formation. Adapt from source slides 89–92.

**Figure 9.2 (planned).** Time-varying ghosting shown with standard-deviation imagery. Adapt from source slides 93–95.

**Figure 9.3 (planned).** Fat suppression on/off and chemical-shift contamination in EPI. Adapt from source slides 97–99.

**Figure 9.4 (planned).** Distortion and bandwidth comparison between read and phase directions. Adapt from source slides 102–106.

**Figure 9.5 (planned).** Signal dropout and slice-thickness dependence. Adapt from source slides 107–110.

---

### Artifact Recognition: physics origin versus image appearance
A useful discipline is to describe each artifact in two sentences: one sentence for **physics origin**, one for **image appearance**.

- **Ghosting origin:** inconsistent odd/even line sampling or related trajectory phase error.  
  **Appearance:** faint replicated anatomy in the phase-encode direction, often near FOV/2.

- **Distortion origin:** off-resonance displacement in the low-bandwidth phase-encode direction.  
  **Appearance:** warped, shifted, stretched, or compressed anatomy near susceptibility boundaries.

- **Dropout origin:** strong intravoxel dephasing from local field gradients.  
  **Appearance:** localized signal voids, often in orbitofrontal and inferior temporal areas.

### Practical Scanner Implication
When someone says an EPI image “looks bad,” the correct next question is: **bad in what way?** The remedy for ghosting is not the remedy for distortion, and the remedy for distortion is not the remedy for dropout.

---

## Chapter 9 Summary
- Ghosting, distortion, and dropout are the three classic EPI artifact families because they arise directly from the physics of fast T2*-weighted readout.
- Nyquist ghosting often comes from odd/even line mismatch and commonly appears at half the field of view in the phase-encode direction.
- Chemical shift and unsuppressed scalp fat can exacerbate ghost-like contamination.
- Ramp sampling can improve efficiency but can also worsen instability if pushed too hard.
- Distortion occurs mainly in the phase-encoded dimension because its effective bandwidth per pixel is much lower than in the read direction.
- Phase-encoding direction determines the direction of off-resonance displacement.
- Dropout reflects local intravoxel dephasing and is worsened by long TE and thick slices.
- Many EPI design choices are best understood as tradeoffs among speed, SNR, distortion, dropout, and stability.

## Key Terms
- Nyquist ghost
- Odd/even line mismatch
- Ramp sampling
- Distortion
- Bandwidth per pixel
- Phase-encoding direction
- Signal dropout
- Intravoxel dephasing
- Fat suppression

## Review Questions
1. Why do Nyquist ghosts commonly appear at half the field of view?
2. Why is distortion much more severe in the phase-encoded direction than in the read direction?
3. Why can fat suppression be essential in EPI rather than merely helpful?
4. Why does thinner slicing reduce dropout?
5. How does changing phase-encoding direction affect distortion appearance?
6. Why is it dangerous to describe all EPI artifacts simply as “motion” or “noise”?

---

# Drafting Notes for Later Runs
- Chapter 9 should cross-link forward to the susceptibility chapter, where the microscopic origin of distortion and dropout is expanded more formally.
- The “brain is always moving” slide is intentionally treated as a bridge to later chapters on motion, instability, and biological confounds.
- Final figure integration should include cleaned versions of the k-space and artifact diagrams, since many source slides are sequence-like or low-context rather than publication-ready textbook figures.
