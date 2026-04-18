# Practical fMRI: From NMR Foundations to EPI Artifacts, Advanced Acquisition, and Biological Confounds
## Run 4 Draft — Chapters 10–12

**Scope of this draft.** This run extends the textbook from classic EPI artifact physics into the next layer of practical fMRI competence: susceptibility and T2* behavior in real tissue, flip-angle and inflow effects, receive-bias-motion interactions, accelerated EPI strategies (partial Fourier, GRAPPA, SMS, multi-echo, FLEET), and a full practical chapter on artifact recognition and troubleshooting.

The source deck becomes especially practical in this range. Many slides are not about abstract sequence theory, but about what actually goes wrong in scanner rooms and how to reason about it. That practical tone is preserved here, but expanded into textbook prose.

---

# Chapter 10. Susceptibility, Motion History, Inflow, and Receive-Field Confounds

## 10.1 Magnetic susceptibility as a spatially varying perturbation
The source slides define **magnetic susceptibility**, usually written \(\chi\), as the tendency of a material to become magnetized when exposed to an external magnetic field. In MRI, susceptibility matters because it determines how different tissues, air spaces, bone, blood products, and foreign materials perturb the local magnetic field.

This is not a minor refinement to basic MRI physics. It is one of the most important reasons that real MRI differs from the idealized scanner model. In the ideal model, the main field \(B_0\) is spatially uniform except where deliberately modified by the imaging gradients. In real brains, however, variations in susceptibility create **intrinsic, static magnetic field gradients**. These act like additional unwanted gradients superimposed on the acquisition.

The source slides make exactly this point: susceptibility-induced gradients dephase spins “just like the imaging gradients, except that we can’t turn the intrinsic gradients off.” That is one of the best practical descriptions of the problem. Susceptibility effects are powerful precisely because they are always present. One may shim them, minimize their consequences, or design around them—but one does not simply turn them off the way one turns off a readout gradient.

## 10.2 Why air-bone-brain interfaces are especially problematic
The source deck highlights **air-bone-brain interfaces**, especially around the paranasal sinuses and temporal bone, as major generators of local field heterogeneity. This is a foundational fact of practical fMRI.

Air and tissue differ greatly in magnetic susceptibility. Whenever such materials meet, the magnetic field is perturbed strongly in the surrounding region. The result is a local spatial gradient in off-resonance frequency. These gradients are often strongest in precisely the regions that many fMRI researchers care about most, including:
- orbitofrontal cortex,
- ventromedial prefrontal regions,
- inferior temporal areas,
- medial temporal lobe structures in some orientations,
- and regions near ear canals or mastoid air cells.

This explains why susceptibility artifact is not evenly distributed throughout the brain. It clusters in anatomically predictable locations.

## 10.3 Phase maps reveal the hidden field problem
The source slides include a map of MR phase to show the problem directly. This is pedagogically valuable because image magnitude alone can hide the underlying mechanism.

Phase images can reveal structured spatial variation in local field. If neighboring voxels exhibit strong phase gradients, that is evidence that off-resonance conditions differ substantially across space. In practice, those same regions are often where one later sees distortion, dropout, or unstable signal behavior in gradient-echo EPI.

This is a useful diagnostic principle: **magnitude artifacts are often consequences of field structure that is easier to appreciate in phase or field maps**.

## 10.4 T2* relaxation revisited in the context of EPI
The source slides explicitly state that **T2* relaxation occurs during the EPI readout**, and that in BOLD fMRI we usually try to set **TE ~ T2*** to maximize contrast sensitivity.

This deserves a more formal textbook unpacking.

As established earlier, T2* is the effective transverse decay constant that includes both intrinsic T2 processes and additional dephasing caused by static field inhomogeneity. In gradient-echo EPI, there is no 180° refocusing pulse to recover that added dephasing. Therefore signal evolution during the readout remains highly sensitive to local field nonuniformity.

Why set TE near T2* for BOLD? Because BOLD contrast is strongest when the acquisition samples the signal at a time where small changes in T2* produce appreciable changes in signal amplitude. If TE is too short, BOLD sensitivity is reduced. If TE is too long, signal may be too weak, distortion worsens, and dropout becomes more severe.

This is a quintessential MRI tradeoff:
- shorter TE reduces dropout and improves raw signal retention,
- but longer TE increases T2*-weighting and therefore BOLD sensitivity.

A competent fMRI acquisition is therefore not just “as short as possible” or “as BOLD-sensitive as possible.” It is a compromise between sensitivity and robustness.

## 10.5 Flip angle effects and spin history
The source deck next turns to **flip angle effects**, especially in the presence of flow and repeated excitation. This is an area where many new fMRI users underestimate how sequence behavior can interact with physiology.

In repeated imaging, spins do not begin each excitation in a fully reset state. Their current magnetization depends on what happened during prior excitations. This dependence is often called **spin history**.

If a subject moves between slices or if flowing blood enters the imaging volume after experiencing a different number of previous excitations than stationary tissue, its magnetization history differs. That can change signal intensity in ways that are not directly attributable to local neural activity.

Thus, spin history is not merely a sequence-design subtlety. It is a mechanism by which acquisition timing, motion, and physiology become entangled.

## 10.6 Inflow effects in GRE-based fMRI
The source slides cite work by Duyn, Frahm, and others showing that **blood inflow plays a major role in GRE-based functional brain maps**. This is a crucial reminder that not every signal change in gradient-echo fMRI is pure deoxyhemoglobin-mediated BOLD.

**Inflow effects** occur because spins flowing into a slice or imaging volume may be less saturated than the stationary tissue already being repeatedly excited. Fresh inflowing blood can therefore produce elevated signal simply because its longitudinal magnetization has recovered more completely. In addition, blood volume changes and inflow timing can alter the temporal shape of the observed response.

The source slide specifically notes that with flow, the **apparent T1 of blood decreases**. Operationally, this means the inflowing signal behaves as though it recovers more quickly than static tissue under repeated excitation.

This matters for fMRI because inflow can:
- increase signal changes with certain flip-angle choices,
- shift apparent response timing,
- add non-neural vascular contributions,
- and complicate interpretation of what is “BOLD” versus what is simply flow-sensitive gradient-echo signal.

## 10.7 Flip angle, inflow, and hemodynamic response shape
The source slides show that higher flip angles at 3 T and TR = 1000 ms produce slightly higher signal change and an earlier apparent time-to-peak of the hemodynamic response, consistent with inflow plus CBV-BOLD effects.

This is a very important practical lesson. Sequence parameters do not merely scale signal uniformly—they can bias what physiological mixture contributes to the measured response.

Higher flip angle generally does at least three things in this context:
1. changes the steady-state magnetization of stationary tissue,
2. changes the contrast between inflowing fresh spins and repeatedly excited tissue,
3. and therefore changes not only signal magnitude but potentially the temporal profile of the response.

Thus, if two studies use different TR/flip-angle combinations, their functional time courses may differ not only because of neural or task factors but because the acquisition itself weights physiological mechanisms differently.

## 10.8 Flip angle effects on SNR and temporal SNR
The source deck includes slides on flip angle, SNR, and temporal SNR, with explicit comparisons such as **FA = 20° versus FA = 65°**. These comparisons are especially important because they correct a common beginner mistake: assuming that the largest instantaneous signal automatically produces the best fMRI data.

That is not always true. In fMRI, **temporal SNR** is often more important than static image brightness. A higher flip angle may increase mean signal in some regions or conditions, but if it also changes variability structure, saturation behavior, or inflow sensitivity, the net effect on functional interpretability can be complex.

This is why one must separate several related but nonidentical questions:
- Which flip angle maximizes signal magnitude?
- Which maximizes steady-state SNR for the tissue of interest?
- Which maximizes temporal SNR?
- Which yields the most interpretable BOLD-weighted response rather than a contaminated physiological mixture?

In many practical contexts, the **Ernst-angle intuition** is useful but incomplete. For fMRI, temporal stability and confound sensitivity matter just as much as mean signal.

## 10.9 Receive bias field effects
The source slides then pivot from physiology to hardware-linked confounds with **receive bias field effects**. This is a key bridge between hardware chapters and artifact chapters.

A receive array does not measure the same sensitivity everywhere in the head. The result is a spatial sensitivity pattern, sometimes called receive contrast “staining.” In static structural images, this appears as brightness nonuniformity. But in fMRI, the issue becomes more serious because the head is not perfectly stationary.

If tissue moves through a steep receive sensitivity gradient, then even if the tissue itself is unchanged biologically, its measured signal changes. This means the time series can contain structured fluctuations that arise from motion through the receive field rather than from neural or vascular effects.

## 10.10 RFC-MoCo: why perfect rigid-body realignment is not enough
The source slides specifically name this effect as **RFC-MoCo** and quote Larry Wald’s formulation: even after perfect rigid-body alignment, the signal time course in a given brain structure will be modulated by motion through the steep sensitivity gradient.

This is one of the most important conceptual corrections in practical fMRI. Many users believe that if motion estimates are small and rigid-body realignment is applied well, then motion-related intensity problems are largely solved. That is false.

Rigid-body motion correction aligns anatomy geometrically. It does **not** change the fact that each time point may have been acquired under a different receive sensitivity profile for a given tissue location. After realignment, the anatomy may sit still in reconstructed space while its intensity still fluctuates because the original coil sensitivity weighting was different at acquisition time.

Thus, motion correction can solve positional mismatch while leaving receive-field modulation intact.

## 10.11 Homogeneous versus heterogeneous receive coils
The source slides contrast motion correction under homogeneous and heterogeneous receive fields. This is pedagogically ideal. If receive sensitivity were perfectly uniform, rigid-body realignment could in principle restore geometric correspondence without creating residual intensity error from this mechanism. But with realistic heterogeneous receive fields, motion correction aligns position while preserving a motion-induced amplitude modulation.

This comparison should be emphasized in textbook form because it makes the causal chain explicit:

head moves → tissue samples different coil sensitivity → time-varying intensity bias → realignment restores geometry but not original sensitivity weighting.

That is why later nuisance regression or bias-field-aware processing may be needed even when motion correction appears visually successful.

## 10.12 How large can the effect be?
The source slides include simulation results showing percentage signal change for 1 mm translation under different coil types (birdcage, 12-channel, 32-channel). This is important because it demonstrates that the effect is not merely theoretical.

The exact magnitude depends on coil geometry, motion direction, anatomical location, and acquisition details, but the principle is clear:
- more spatially varying receive profiles can create larger motion-linked intensity modulation,
- small motion can create non-negligible apparent signal change,
- and higher-channel arrays can be especially powerful and especially nonuniform.

This is not an argument against modern arrays—they are essential for high-SNR and accelerated imaging—but it is an argument for intellectually honest interpretation. Improved hardware can amplify certain confound pathways even while improving overall acquisition capability.

## 10.13 Anchoring during volume realignment
The source slides conclude this section with **anchoring during volume realignment**. The idea is subtle but important: if receive-field contrast becomes strong enough, it can dominate the apparent image similarity structure used by volume registration algorithms. In that case, the cost function may partially anchor to receive bias patterns rather than to underlying anatomy.

The source slide suggests normalization by the receive bias field as a mitigation strategy. This is a practical lesson that should be generalized:
- motion correction is not just an optimization problem over anatomy,
- the image intensity landscape being optimized may itself be corrupted by hardware sensitivity patterns,
- and preprocessing choices can influence whether registration follows anatomy or follows bias-field structure.

## 10.14 Putting the confounds together
This chapter’s source material is valuable because it shows that not all “extra” fMRI signal comes from the same place.

Three broad classes are interacting here:
1. **Susceptibility-related field structure**, which drives T2*, distortion, and dropout.
2. **Physiological inflow and spin-history effects**, which alter signal amplitude and timing.
3. **Receive-field heterogeneity plus motion**, which creates time-varying intensity modulation even after geometric alignment.

A practical researcher must be able to distinguish among them. They may coexist in the same run, but they imply different remedies and different interpretive caution.

---

**Figure 10.1 (planned).** Susceptibility gradients near air-bone-brain interfaces, with phase-map illustration. Adapt from source slides 121–123.

**Figure 10.2 (planned).** TE near T2* for BOLD contrast, with tradeoff schematic for sensitivity versus dropout. Adapt from source slide 124 and expanded pedagogically.

**Figure 10.3 (planned).** Flip-angle / inflow effects on response magnitude and timing. Adapt from source slides 126–130.

**Figure 10.4 (planned).** Receive-bias-motion interaction before and after perfect motion correction under homogeneous versus heterogeneous receive fields. Adapt from source slides 131–139.

---

### Common Confusion: motion correction does not remove all motion effects
Motion correction aligns images in space. It does **not** guarantee that voxel intensities are comparable across time for all reasons. If motion changes receive sensitivity weighting, inflow state, or spin history, those effects can survive even excellent realignment.

### Practical Scanner Implication
If a dataset shows unexpected temporal fluctuations after apparently good motion correction, do not assume the remaining problem is “just noise.” Ask whether receive-field heterogeneity, inflow, or spin-history effects are contributing.

---

## Chapter 10 Summary
- Magnetic susceptibility differences create intrinsic local field gradients that cannot simply be switched off.
- Air-bone-brain interfaces are major sources of off-resonance problems in practical fMRI.
- T2* relaxation during EPI readout is both the basis of BOLD contrast and a source of artifact vulnerability.
- Flip angle changes not only signal magnitude but also inflow weighting, temporal behavior, and temporal SNR.
- Receive field heterogeneity can convert small motion into structured signal modulation.
- Rigid-body motion correction does not remove receive-bias-induced intensity fluctuations.
- Realignment itself can be affected by receive-field contrast if that contrast dominates the registration cost function.

## Key Terms
- Magnetic susceptibility
- Off-resonance
- T2*
- Inflow effect
- Spin history
- Receive bias field
- RFC-MoCo
- Realignment
- Temporal SNR

## Review Questions
1. Why do susceptibility variations act like gradients that the user cannot turn off?
2. Why are frontal and inferior brain regions particularly vulnerable to susceptibility-related problems?
3. Why is TE usually chosen near T2* for BOLD fMRI?
4. How can higher flip angle affect not only signal amplitude but also response timing?
5. Why can receive-field-related intensity modulation survive perfect rigid-body realignment?
6. What does “anchoring” mean in the context of volume realignment?

---

# Chapter 11. Accelerated and Advanced EPI Methods

## 11.1 Why acceleration methods are attractive in fMRI
The source slides open Day Four with advanced EPI methods. The reason these methods matter is straightforward: standard EPI is useful, but it is always under pressure from competing demands.

Researchers want:
- more slices,
- shorter TR,
- higher spatial resolution,
- less distortion,
- less dropout,
- and acceptable SNR,

all at the same time.

Acceleration methods are attempts to improve this tradeoff surface. But they do not create free performance. They exchange one type of cost for another. The central educational goal in this chapter is therefore not to catalog methods as if they were upgrades, but to explain their **tradeoff logic**.

## 11.2 Partial Fourier EPI and conjugate symmetry
The first advanced method in the source deck is **partial Fourier EPI**. The key mathematical idea is **conjugate symmetry in k-space**. If an image is real-valued under appropriate assumptions, then one side of k-space contains information related to the complex conjugate of the opposite side.

The source slides illustrate this with the familiar relation between \(a-ib\) and \(a+ib\). This is the basis for the idea that not all of k-space necessarily needs to be acquired directly. One may omit part of k-space and reconstruct the missing portion approximately.

This is a powerful strategy because it can reduce acquisition time, but it is only safe insofar as the assumptions behind the reconstruction are sufficiently satisfied in practice.

## 11.3 Reconstructing omitted k-space
The source deck notes that several reconstruction approaches exist and that one practical implementation is to **zero-fill the missing portion before the 2D Fourier transform**. In modern practice, additional phase-estimation strategies may also be used, but the source’s operational point is still important: omitted data are not magically unnecessary. They are being inferred, estimated, or replaced using assumptions.

This means partial Fourier is not just “faster EPI.” It is **less directly sampled EPI with compensatory reconstruction**.

## 11.4 Early versus late echo omission
A particularly useful contribution of the source slides is the comparison between omitting **early echoes** versus omitting **late echoes**.

- Omitting **early echoes** allows a shorter **TE**.
- Omitting **late echoes** allows a shorter **TR** or more slices for the same TR.

The source slides argue that for BOLD fMRI, omitting late echoes is generally preferable, because BOLD contrast usually benefits from keeping TE near T2* rather than shortening it excessively.

This is a practical example of physics informing protocol design. If TE is shortened too much, one may gain efficiency but lose the desired BOLD sensitivity.

## 11.5 Coverage gains and BOLD logic in partial Fourier
The source slides provide a concrete example on a Siemens 3 T Trio with TR = 2000 ms:
- full Fourier: 37 slices at TE = 22 ms,
- early 6/8 partial Fourier: 40 slices at TE = 18 ms,
- late 6/8 partial Fourier: 44 slices at TE = 22 ms.

The conclusion is practical and important: **late echo omission can yield greater coverage without sacrificing a TE favorable for BOLD**.

This is precisely the kind of scanner-facing judgment that distinguishes practical fMRI from abstract sequence theory. The “best” option depends on whether BOLD contrast, coverage, TR, or robustness is the priority.

## 11.6 Partial Fourier and dropout tradeoffs
The source slides raise a subtle but important concern: partial Fourier can increase dropout. Why? Because local susceptibility gradients can make the actual local k-space trajectory deviate from the idealized assumption. If the missing k-space portion corresponds to information that is already fragile in certain regions, the reconstruction may exacerbate signal loss or smoothing.

The source slides further note that signal dropping out under early omission may differ from signal behavior under late omission, and that some practical control exists through the choice of omission direction and phase-encoding direction.

This is a particularly sophisticated acquisition point. Partial Fourier is not simply about how many lines are omitted. It is also about **which part of k-space** is omitted, **which way the EPI train runs**, and **which anatomy is already vulnerable to susceptibility loss**.

## 11.7 Partial Fourier, smoothing, and phase-encode direction
The source slides emphasize two practical effects:
1. dropout may be enhanced slightly,
2. smoothing is implicit.

This makes sense. When part of k-space is estimated rather than measured, the reconstruction is generally less faithful to the highest-fidelity full-k-space representation. That often behaves like a smoothing or resolution-loss mechanism.

The slides also note that the interaction with phase-encode direction gives the user some control over which regions are most affected. This is a practical design space, not an all-purpose solution.

## 11.8 Partial Fourier: pros and cons
Summarizing the source material in textbook form:

### Advantages
- more slices or shorter TR,
- no fundamentally new motion sensitivity compared with full EPI,
- potentially better BOLD-compatible coverage if late echoes are omitted.

### Disadvantages
- some SNR loss,
- implicit smoothing,
- possible enhancement of dropout in vulnerable regions,
- full k-space still remains the fidelity ceiling.

## 11.9 In-plane acceleration with GRAPPA
The next method in the source deck is **in-plane acceleration**, specifically **GRAPPA**. This method under-samples k-space lines during acquisition and uses coil-sensitivity information plus calibration data to reconstruct the missing lines.

The source slides show an R = 2 trajectory, illustrating that every other line may be skipped and later inferred. The method depends critically on a multi-channel receive array, because each coil sees the anatomy with a different sensitivity profile. Those differing profiles provide the extra encoding information needed to reconstruct the omitted lines.

GRAPPA should therefore be understood as a way of exchanging hardware-supported parallel information for reduced acquisition burden in the phase-encoded direction.

## 11.10 ACS lines and reconstruction logic
The source deck describes the role of **ACS (autocalibration signal) lines** very clearly. These fully sampled reference lines are used to fit the reconstruction relationship between acquired and missing k-space lines. The fit is performed for each receive coil separately, and the coil images are later combined.

This means GRAPPA has two informational components:
1. the under-sampled time-series data,
2. the calibration reference data set.

This dual dependence is what gives GRAPPA both its power and one of its major vulnerabilities.

## 11.11 GRAPPA motion sensitivity
The source slides emphasize motion sensitivity repeatedly, and this is one of their most important practical teachings.

If motion occurs **during ACS acquisition**, the reference data themselves are corrupted. Since those ACS data are used to reconstruct the entire under-sampled time series, the corruption propagates broadly.

If motion occurs **after ACS acquisition**, then the ACS still represent a different head position from the current EPI volumes. A mismatch remains even if the subject becomes still afterward.

The source slides illustrate both cases and show resulting temporal-SNR degradation.

This is a crucial real-world lesson: GRAPPA can reduce distortion, improve nominal resolution, and increase coverage, but it comes at the price of substantial sensitivity to calibration mismatch.

## 11.12 GRAPPA: pros and cons
The source deck summarizes the tradeoff well.

### Advantages
- reduces phase-encode distortion roughly by factor \(R\),
- can recover some dropout indirectly by reducing distortion burden,
- can support higher nominal resolution,
- can yield modest slice-count gains in a fixed TR.

### Disadvantages
- large increase in motion sensitivity,
- dependence on high-quality reference data,
- residual aliasing if reconstruction is imperfect,
- SNR penalties and noise amplification in practical use.

The key teaching point is this: GRAPPA is not just a distortion-reduction tool. It is also a calibration-sensitive reconstruction strategy.

## 11.13 Simultaneous multi-slice (SMS) / multiband EPI
The next acceleration method is **simultaneous multi-slice (SMS)**, also called **multiband (MB)** EPI. Instead of accelerating within a slice, SMS excites multiple slices at once and then uses coil sensitivity differences to unalias them.

The source slides make several critical practical points:
- SMS requires a phased-array coil.
- It specifically benefits from many coil loops distributed along the slice axis.
- It requires a reference set of **single-band** images (SBRef-like information) for calibration.
- Reconstruction is conceptually similar to GRAPPA-like unaliasing.

Thus, SMS is another example of trading acquisition efficiency for reconstruction dependence on coil geometry and reference stability.

## 11.14 Coil requirements for SMS separation
The source deck rightly pauses to ask whether there are enough coils along the slice axis. This is not a trivial hardware question. SMS only works well if simultaneously excited slices produce distinguishable patterns across the receive array.

If coil sensitivity variation along the slice axis is insufficient, unaliasing becomes poor and slice leakage or residual aliasing increases.

This is why channel geometry matters, not just channel count in the abstract.

## 11.15 SMS pulse sequence logic and benefits
The source slides use classic diagrams from Feinberg and Setsompop to illustrate SMS pulse-sequence logic. In textbook form, the main point is that multiple slices are excited simultaneously, the readout acquires their combined signal, and the reconstruction uses spatial sensitivity information to separate them.

The benefit is obvious: one can acquire many more slices per unit time without simply making the readout longer in the usual line-by-line sense.

For fMRI, this often means:
- shorter TR,
- more whole-brain coverage,
- or better spatial resolution at similar temporal resolution.

## 11.16 SMS limits and motion sensitivity
The source slides also stress that SMS has limits. They note, for example, that:
- voxels below approximately \((2\text{ mm})^3\) have low SNR,
- 1.5 mm resolution at 3 T is probably a practical limit for partial-brain coverage,
- SMS factors greater than 5 are generally not advised,
- and one must think carefully about combining **R × SMS** when using GRAPPA too.

This is important because SMS is sometimes discussed as though more multiband is always better. The source slides reject that simplification. More aggressive SMS can increase leakage, motion sensitivity, reconstruction burden, and SNR penalties.

The slide set also shows motion effects tied to SBRef mismatch. This parallels the GRAPPA ACS problem: calibration mismatch can persist even when the subject is currently still.

## 11.17 Multi-echo EPI
The source deck then turns to **multi-echo EPI (ME-EPI)**. Here, more than one echo is collected after a single excitation, allowing the signal to be analyzed across multiple echo times.

The source slides identify two major uses:
1. combine echoes to boost SNR,
2. or use TE dependence to classify **BOLD** versus **non-BOLD** signal changes.

This is one of the conceptually richest methods in the deck because it turns contrast evolution itself into a diagnostic tool. If a signal behaves like BOLD, it should vary with TE in a characteristic way. If it is TE-independent or behaves inconsistently with BOLD expectations, it is more likely to reflect a non-BOLD source.

## 11.18 Weighted echo combination and BOLD classification
The source slides mention **weighted sum of echoes** and explicit classification of BOLD versus non-BOLD. In textbook form, the core idea is that multi-echo data provide a small contrast trajectory rather than a single snapshot.

A BOLD-like effect should scale with TE because it is linked to T2* changes. A non-BOLD signal source—such as some motion-linked or hardware-linked amplitude modulations—may not show the same TE dependence.

This does not mean ME-EPI magically distinguishes all nuisance variation. The source deck is careful here, noting that some physiology (such as blood-gas-related changes) may be real BOLD but non-neural, and subtle motion issues can remain.

Thus, ME-EPI improves interpretive leverage, not perfect truth access.

## 11.19 Multi-echo pros and cons
The source slides summarize ME-EPI as follows.

### Advantages
- can improve regional SNR,
- can help distinguish some artifact classes,
- can support more nuanced BOLD/non-BOLD separation.

### Disadvantages
- does not solve all physiology-related confounds,
- may leave subtle motion problems,
- often needs in-plane GRAPPA for three or more echoes,
- adds complexity to acquisition, reconstruction, and analysis.

This is a good example of an advanced method that improves model richness more than it improves basic raw acquisition simplicity.

## 11.20 FLEET as a stabilization strategy
The last advanced method in the source block is **FLEET** (Fast Low-angle Excitation Echo-planar Technique), cited to Polimeni et al. The source slides describe it as minimizing time between ACS segments for each slice and looping ACS then slices using low flip angle to reduce spin history.

This is best understood as a strategy for making calibration data more robust. If reference segments are acquired close together in time and with lower flip-angle perturbation, one reduces the opportunities for motion mismatch and spin-history inconsistency. In other words, FLEET is not just “another acceleration trick.” It is a practical response to calibration fragility in accelerated EPI.

## 11.21 The deeper lesson of advanced EPI
The advanced methods in this chapter are often marketed as efficiency tools, but the deeper lesson is broader: every acceleration or enhancement method rebalances four pressures:
1. distortion,
2. SNR,
3. motion sensitivity,
4. reconstruction dependence.

The practical user should therefore not ask “Which advanced method is best?” in the abstract. The right question is “Which compromise best matches my study’s tolerance for distortion, instability, coverage limits, and analysis complexity?”

---

**Figure 11.1 (planned).** Conjugate symmetry and partial Fourier omission of early versus late echoes. Adapt from source slides 141–158.

**Figure 11.2 (planned).** GRAPPA R = 2 trajectory, ACS logic, and motion mismatch scenarios. Adapt from source slides 159–167.

**Figure 11.3 (planned).** SMS acquisition and coil-based slice unaliasing. Adapt from source slides 169–177.

**Figure 11.4 (planned).** Multi-echo TE dependence for BOLD versus non-BOLD signal components. Adapt from source slides 178–182.

**Figure 11.5 (planned).** FLEET calibration logic. Adapt from source slide 184.

---

### Tradeoff box: partial Fourier versus GRAPPA
A useful practical comparison from the source material is this:
- **Partial Fourier** mainly trades fidelity for shorter acquisition or greater coverage, with modest smoothing and possible dropout tradeoffs.
- **GRAPPA** mainly trades calibration dependence and motion sensitivity for reduced distortion and higher effective acceleration.

Neither is universally superior. The right choice depends on whether distortion reduction or calibration robustness matters more for the specific study.

### Practical Scanner Implication
Before enabling multiple accelerations together, ask what failure mode you are stacking. For example, combining high SMS with GRAPPA may reduce TR and distortion but can also amplify residual aliasing, calibration mismatch sensitivity, and low-SNR fragility.

---

## Chapter 11 Summary
- Advanced EPI methods exist to improve coverage, speed, distortion burden, or contrast separability—but every one introduces new tradeoffs.
- Partial Fourier uses conjugate symmetry to omit part of k-space, with choices about early versus late echo omission that matter for BOLD and coverage.
- GRAPPA reduces distortion and supports higher resolution but is highly sensitive to ACS quality and motion mismatch.
- SMS accelerates slice acquisition using coil-based unaliasing and depends strongly on coil geometry and calibration stability.
- Multi-echo EPI uses TE dependence to improve SNR and help distinguish BOLD-like from some non-BOLD signal changes.
- FLEET is a practical method for improving the robustness of calibration in accelerated EPI.

## Key Terms
- Partial Fourier
- Conjugate symmetry
- Early echo omission
- Late echo omission
- GRAPPA
- ACS lines
- Simultaneous multi-slice (SMS)
- Multiband EPI
- SBRef
- Multi-echo EPI
- TE dependence
- FLEET

## Review Questions
1. Why can late echo omission in partial Fourier be more attractive than early echo omission for BOLD fMRI?
2. Why can partial Fourier slightly increase dropout or smoothing?
3. What makes GRAPPA especially sensitive to subject motion?
4. Why does SMS require strong coil sensitivity variation along the slice axis?
5. What kind of signal behavior allows ME-EPI to help separate some BOLD from non-BOLD changes?
6. Why is combining multiple acceleration methods not automatically beneficial?

---

# Chapter 12. Artifact Recognition, Quality Control, and Troubleshooting

## 12.1 The diagnostic mindset
The source slides begin the troubleshooting block with an excellent practical principle: **learn what good data look like for your scan**. This is perhaps the most important operational lesson in the entire course.

Troubleshooting in MRI is not mostly about memorizing rare catastrophic failures. It is about learning to distinguish:
- normal artifact from abnormal artifact,
- expected imperfection from harmful instability,
- subject-related problems from hardware-related problems,
- and acquisition tradeoffs from actual scanner failure.

The source slides also state bluntly that **motion is the biggest issue**, **user error is the next biggest**, and **scanner failures are rare but do happen**. That ordering should be preserved, because it is practical wisdom. In everyday scanning, the most likely explanation is not mysterious machine collapse; it is usually movement, setup error, parameter choice, or a predictable interaction between subject and acquisition.

## 12.2 Good data must be recognized before bad data can be classified
A recurring theme in the source deck is the need to know what **good axial EPI**, **good coronal EPI**, and **good sagittal EPI** look like. This deserves more emphasis than it often gets.

Artifact recognition is impossible without an internal reference standard. A new scanner user who has never really studied good EPI will overcall some normal features and undercall important failures.

What counts as “good” does not mean perfect. Good EPI may still include:
- some expected frontal susceptibility loss,
- faint normal Nyquist ghosting,
- receive field shading,
- and modest residual distortion.

The question is not whether the image is pristine, but whether the observed imperfections are:
- expected for the protocol,
- stable over time,
- spatially tolerable for the scientific target,
- and unlikely to dominate interpretation.

## 12.3 Normal ghosting versus abnormal ghosting
The source slides explicitly distinguish **normal ghosting** from more problematic ghost patterns. This is an important teaching move because it avoids a false binary. Not every ghost is evidence of a failed scan.

Small, stable Nyquist ghosts are common in EPI. The practical issue is whether they are:
- weak or strong,
- stable or time-varying,
- outside regions of interest or overlapping them,
- and anatomically predictable or newly abnormal.

A user who treats all ghosting as a disaster may overreact. A user who ignores ghosting entirely may miss task-correlated or motion-correlated nuisance structure. The correct posture is calibrated attention.

## 12.4 Scalp ghosts and eye-movement ghosts
The source deck includes scalp ghosts and specifically warns that Nyquist ghosts from **eye movements** should not fall on something scientifically important. This is highly practical advice.

Eye movements are a classic example of nuisance signal that is both biologically real and scientifically irrelevant to many experiments. Because the eyes are bright, mobile, and anterior, their movement can generate structured ghosting along the phase-encode axis. If those ghosts project into orbitofrontal or medial frontal regions, interpretation becomes especially hazardous.

This is one reason phase-encode direction and artifact placement matter. A good acquisition does not merely minimize artifacts in the abstract; it tries to place unavoidable artifacts somewhere less damaging.

## 12.5 Standard-deviation images and temporal instability
The source slides repeatedly use **standard-deviation images** and **tSNR maps**. This is one of the most valuable practical habits they teach. Some artifacts are easiest to see not in the mean image, but in temporal-variability summaries.

A standard-deviation image can reveal:
- unstable ghosts,
- motion-affected edges,
- pulsation-sensitive regions,
- calibration mismatch effects,
- or structured scanner instability.

A tSNR map converts the same idea into a normalized stability metric. Together, these tools help separate visually acceptable anatomy from functionally unacceptable time-series behavior.

## 12.6 Prescan normalize and background appearance
The source slides show that **prescan normalize** affects background intensity. This is a good reminder that some apparent changes in image quality are not due to anatomy or pathology but to preprocessing or scanner reconstruction options.

Prescan normalization can be useful, especially for reducing receive bias-field prominence. But it also changes background appearance and sometimes alters the visual salience of certain artifacts.

The practical lesson is simple: know your scanner’s reconstruction settings. Otherwise, you may confuse a processing choice with a physics problem.

## 12.7 Residual aliasing in accelerated acquisitions
The source deck shows **residual aliasing** for GRAPPA, SMS, and SMS + GRAPPA combinations. This is an important continuation of the advanced EPI chapter, but here the emphasis is on recognition rather than mechanism.

Residual aliasing often appears as faint replicated or leaked structure that follows the logic of the acceleration scheme rather than the classic Nyquist ghost pattern. It may be spatially structured, sometimes subtle, and can worsen when calibration is poor or SNR is low.

The practical challenge is that accelerated-imaging residual aliasing can be mistaken for motion, poor anatomy, or normal ghosting. Recognition requires knowing the expected aliasing geometry of the acquisition.

## 12.8 Movement is more than head motion
One of the strongest practical sections in the source deck is the decomposition of “movement” into multiple categories:
- real head motion,
- pseudo-motion from breathing,
- movement of other body parts,
- unstable hardware.

This is important because “motion artifact” is often used too loosely. Head motion is only one mechanism. Breathing can modulate the head position or B0 field. Feet moving can transmit mechanical disturbances. Talking changes head posture, jaw position, and physiology. Even third-party movement, as the source deck amusingly illustrates with sea-lion fMRI, can couple into the data.

The diagnostic point is that movement-like image instability does not uniquely identify one cause.

## 12.9 Eye movements, head movements, talking, and moving feet
The source slides devote separate examples to eye movements, head movements, talking, and moving feet. This is worth preserving because each has a different pattern.

- **Eye movements** often produce strong anterior ghosting.
- **Head movements** cause broad spatial misalignment plus spin-history and receive-bias interaction effects.
- **Talking** can create jaw and face motion, respiratory changes, and broader head perturbation.
- **Moving feet** may seem remote, but can transmit motion through the body and scanner support.

The important practical principle is that the body is mechanically and physiologically connected. Motion is rarely as localized as the subject believes.

## 12.10 Coil instability as a distinct failure class
The source slides pay unusual and valuable attention to **coil instability**, including the practical reality that some head coils may have physical play or tilt potential. This is exactly the kind of issue that often escapes purely theoretical MRI teaching.

Coil instability matters because if the coil moves relative to the head, then receive sensitivity can change even if the head itself is relatively still. The resulting artifact can resemble subject motion, receive-bias fluctuation, or inexplicable temporal instability.

This is an excellent example of why troubleshooting should include physical inspection and setup awareness, not only image review.

## 12.11 Third-party movement and environmental contributions
The source deck’s example of third-party movement is humorous, but the lesson is real. Not all instability originates inside the subject’s skull. Environmental disturbances, bed motion, cable tugging, or interactions with external equipment can all perturb the acquisition.

A good troubleshooter therefore asks not only “Did the subject move?” but also “What in the setup may have moved?”

## 12.12 Motion in structural imaging
The inclusion of **motion in MP-RAGE** is important because it broadens the student’s perspective beyond EPI. Motion is not only a functional-series problem. Structural scans can be severely degraded by motion, producing blurred anatomy, ringing, or segmentation problems that later compromise registration and analysis.

This matters because poor structural data can contaminate the entire downstream pipeline even if the EPI itself looks acceptable.

## 12.13 Foreign objects, RF interference, and spike artifacts
The source deck next shows several classic scanner-room or hardware issues:
- foreign objects such as a metal pin,
- RF interference,
- gradient spiking,
- RF coil spikes.

These belong in a textbook because they teach the user to keep an open diagnostic mind. Not every artifact is a subject-behavior problem.

### Foreign objects
Metallic objects distort the local magnetic field, induce severe susceptibility artifacts, and may create signal voids or geometric deformation.

### RF interference
External RF noise can introduce structured stripes, bands, or spikes, depending on its frequency and coupling.

### Gradient spiking
Gradient-related transient faults can produce abrupt structured corruption, sometimes best confirmed using phantom checks.

### RF coil spikes
Coil-electronics instability can create sudden localized or temporally sparse corruption that may also appear in localizers or structural images.

These examples reinforce a central diagnostic rule: if a problem appears across multiple sequence types, hardware causes rise in likelihood.

## 12.14 System drifts and chronic motion
The source slides conclude with **system drifts and chronic motion**. This is another important reminder that not all problems are transient acute failures. Some are slow, persistent, or cumulative.

Possible contributors include:
- inadequate foam padding,
- talking,
- long-run discomfort,
- slow changes in coil sensitivity map,
- B0 shim drift,
- and other evolving session-level factors.

These are especially dangerous in long runs because they may not produce a single obvious catastrophic frame. Instead, they gradually erode temporal stability.

## 12.15 Tactics for diagnosis
The source deck ends with a practical diagnostic checklist. This should be preserved almost as a canonical scanner-room decision process.

### Step 1: assess temporal stability
Do not begin with a single snapshot. Look across time. Use mean images, standard-deviation images, tSNR, and motion traces if available.

### Step 2: acquire a short retest
A short repeat acquisition can distinguish persistent setup problems from transient anomalies.

### Step 3: make a brief list of possible explanations
Do not jump immediately to a single cause. Enumerate a small differential diagnosis.

### Step 4: develop the most likely hypothesis
Then test it by asking questions such as:
- Does the problem appear in a different scan type?
- Can the problem be made worse deliberately or by changing conditions?
- Does removing and resetting the subject change the outcome?
- Would a short QC test or phantom run help separate subject from hardware causes?

This is excellent troubleshooting advice because it treats MRI diagnosis as a hypothesis-testing process rather than a reflex.

## 12.16 A practical troubleshooting hierarchy
Combining the source deck’s lessons, a practical troubleshooting hierarchy might look like this:

1. **Check whether the artifact is actually abnormal.** Compare against known-good reference images.
2. **Assess whether it is stable or time-varying.** Mean image alone is not enough.
3. **Ask whether the pattern matches a known acquisition artifact.** Ghosting, distortion, dropout, residual aliasing, receive-bias effects.
4. **Assess subject behavior.** Eyes, head, speech, breathing, feet, discomfort.
5. **Assess setup and hardware.** Coil seating, cable position, prescan options, interference risk, physical play, shim state.
6. **Retest briefly.** If needed, remove and reposition.
7. **Escalate to QC or phantom tests** if hardware causes remain plausible.

This is exactly the kind of structured thinking that turns a scanner user into a competent practical operator.

---

**Figure 12.1 (planned).** Good EPI reference images and normal ghosting examples. Adapt from source slides 188–189 and 198.

**Figure 12.2 (planned).** Scalp ghosts and eye-movement ghost placement. Adapt from source slides 190–191.

**Figure 12.3 (planned).** tSNR and standard-deviation images as temporal-stability tools. Adapt from source slides 192 and 199.

**Figure 12.4 (planned).** Residual aliasing examples for GRAPPA, SMS, and SMS + GRAPPA. Adapt from source slides 194–197.

**Figure 12.5 (planned).** Movement and hardware failure atlas: eyes, head, talking, feet, coil instability, metal, RF interference, gradient spikes, RF coil spikes. Adapt from source slides 200–214.

**Figure 12.6 (planned).** Troubleshooting decision checklist. Adapt from source slides 216–217.

---

### Artifact Recognition: ask three questions first
For any suspicious pattern, ask:
1. **Where is it?** (phase-encode axis? frontal region? background only? global?)
2. **How does it vary over time?** (stable? drifting? intermittent? task-locked?)
3. **What class of mechanism fits it best?** (trajectory mismatch, off-resonance, motion, receive bias, hardware instability, interference)

### Practical Scanner Implication
When in doubt, a short retest is often more informative than a long argument. MRI troubleshooting improves dramatically when hypotheses are tested quickly with small, purposeful acquisitions.

---

## Chapter 12 Summary
- Artifact recognition begins with knowing what good data look like.
- Many “normal” artifacts exist in EPI; the challenge is to judge whether they are stable, tolerable, and away from regions of interest.
- Ghosts from scalp or eye motion can be especially misleading if they fall on brain regions of interest.
- Standard-deviation images and tSNR maps are essential tools for detecting instability.
- Prescan normalization and other reconstruction settings can change image appearance without changing the underlying acquisition problem.
- Residual aliasing from GRAPPA and SMS must be recognized as distinct from classic Nyquist ghosting.
- Movement includes more than head motion; setup, breathing, talking, feet, coil instability, and environmental factors all matter.
- Hardware problems such as RF interference, gradient spiking, and coil spikes are uncommon but real and should be considered when artifacts cross sequence types.
- Good troubleshooting is hypothesis-driven and testable.

## Key Terms
- Artifact recognition
- Standard-deviation image
- Temporal SNR
- Prescan normalize
- Residual aliasing
- Coil instability
- RF interference
- Gradient spike
- QC retest
- Phantom check

## Review Questions
1. Why is learning what good EPI looks like a prerequisite for troubleshooting?
2. How can eye-movement ghosts interfere with interpretation of frontal-lobe data?
3. Why are standard-deviation images often more useful than mean images for troubleshooting?
4. How would you distinguish residual aliasing from classic Nyquist ghosting?
5. Why can coil instability mimic subject motion?
6. What sequence of steps would you follow when a new artifact appears during an fMRI session?

---

# Drafting Notes for Later Runs
- Chapter 12 should later connect directly to the final confounds chapter, since some physiologic and behavioral issues overlap both artifact recognition and interpretation.
- In the final polished version, the artifact-recognition chapter should become visually rich, with grouped figure plates and concise figure-side diagnostic notes.
- The final book should likely include a troubleshooting appendix that condenses Chapter 12 into quick lookup tables.
