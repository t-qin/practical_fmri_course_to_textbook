# Practical fMRI: From NMR Foundations to EPI Artifacts, Advanced Acquisition, and Biological Confounds
## Textbook Manuscript — Front Matter, Chapters 13–14, and End Matter

---

# Title Page

# **Practical fMRI: From NMR Foundations to EPI Artifacts, Advanced Acquisition, and Biological Confounds**

### A textbook-style reconstruction and expansion of the Ben Inglis fMRI course slides for long-term self-study

Prepared as a pedagogical manuscript for advanced undergraduates, beginning graduate students, and research trainees who need a cumulative understanding of MRI/fMRI physics, acquisition logic, artifact behavior, and practical interpretation.

---

# Preface
This book was built from a practical teaching deck rather than from a conventional textbook manuscript. That origin matters. Slide decks are often excellent for live instruction because they compress ideas, foreground figures, and rely on the instructor’s spoken explanation to supply missing context. For self-study, however, that same compression becomes a barrier. Important transitions are omitted, shorthand replaces explanation, and figures that make sense during a lecture can become cryptic when viewed alone.

The purpose of this manuscript is therefore not to summarize the source slides, but to reconstruct them into a coherent, textbook-style learning sequence. Every major scientific topic in the source course has been preserved, but the structure has been reorganized so that a reader can build understanding progressively. Concepts that were only implied in the slides have been made explicit. Equations are explained in words. Figures appear in context rather than as isolated slide visuals. Practical acquisition consequences are highlighted throughout, because MRI and fMRI are not subjects in which theory can be separated cleanly from practice.

This is a book about both **how MRI works** and **how MRI fails in instructive ways**. That second theme is crucial. Functional MRI depends heavily on echo-planar imaging, a fast but fragile acquisition strategy. Many of the most important lessons in practical fMRI arise not from idealized image formation, but from the tension between desirable signal contrast and the artifact burden that accompanies it. Understanding MRI therefore means understanding not only magnetization, gradients, and Fourier reconstruction, but also ghosting, distortion, dropout, motion, receive-field heterogeneity, calibration mismatch, and biological confounds.

The intended reader is an intelligent learner who may not yet have deep MRI physics background but is willing to engage carefully with the material. The text is written for advanced undergraduate students, beginning graduate students, and new imaging researchers. It aims to make the reader capable not just of recognizing terminology, but of reasoning through acquisition tradeoffs and diagnosing real data problems.

---

# How to Use This Book
This manuscript is designed to be read in layers.

## If you are new to MRI
Read Chapters 1–7 in order. Those chapters establish the essential foundations:
- spins and magnetization,
- excitation and relaxation,
- scanner hardware,
- Fourier logic,
- gradients,
- slice selection,
- and k-space.

Without those chapters, later EPI and artifact discussions are much harder to interpret correctly.

## If you already know basic MRI but struggle with fMRI practice
Start at Chapter 8 and continue through Chapters 12–14, but refer back to Chapters 5–7 whenever k-space, bandwidth, or gradient-area reasoning feels unclear.

## If you mainly need troubleshooting guidance
Chapter 12 and Appendix B provide the most direct practical diagnostic material. However, their explanations depend heavily on Chapters 8–11.

## If you mainly need confound interpretation
Chapter 13 is the main conceptual destination, but it should be read together with Chapters 10 and 12 because physiological confounds, motion-linked signal changes, and artifact behavior overlap strongly in practice.

## How the pedagogical elements are used
Throughout the manuscript, several recurring teaching devices are used:
- **Why this matters** boxes explain why a concept changes scanner behavior or interpretation.
- **Common confusion** boxes identify typical misunderstandings.
- **Practical scanner implication** boxes translate theory into protocol or QC choices.
- **Artifact recognition** boxes connect physics origin to image appearance.
- **Review questions** are included at the end of chapters to support self-study.

The figure plan is intentionally integrated into the text structure. In the final formatted version, the most important source diagrams and image examples should be inserted at the figure locations already identified in the chapter drafts.

---

# Table of Contents

## Front Matter
- Title Page
- Preface
- How to Use This Book
- Table of Contents

## Chapters
1. **Why MRI and fMRI Work: A Practical Orientation**
2. **Nuclear Magnetization, Precession, and the Rotating Frame**
3. **Relaxation, Dephasing, T1, T2, and T2***
4. **MRI Hardware and the Physical Scanner Environment**
5. **Fourier Transform Intuition for MRI**
6. **Gradients, Slice Selection, and Basic MRI Image Formation**
7. **K-Space: The Organizing Language of MRI**
8. **Echo-Planar Imaging (EPI): Why fMRI Is Fast**
9. **The Classic EPI Artifacts: Ghosting, Distortion, and Dropout**
10. **Susceptibility, Motion History, Inflow, and Receive-Field Confounds**
11. **Accelerated and Advanced EPI Methods**
12. **Artifact Recognition, Quality Control, and Troubleshooting**
13. **Biological Confounds and Human Factors in fMRI**
14. **Integrative Practical Framework for Running and Interpreting fMRI**

## End Matter
- Appendix A. Equation Guide and Symbol Reference
- Appendix B. Artifact Troubleshooting Tables
- Appendix C. Acquisition Tradeoff Summary Tables
- Glossary
- Index-like Keyword Guide

---

# Chapter 13. Biological Confounds and Human Factors in fMRI

## 13.1 Why confounds belong at the end of the physics story
The source deck’s final day is devoted to **confounds in fMRI**, and that placement is pedagogically wise. Biological confounds are easiest to understand only after the reader already understands BOLD contrast, T2* sensitivity, EPI artifacts, motion, receive-bias effects, and accelerated acquisition tradeoffs.

If confounds are introduced too early, they sound like a miscellaneous list of things that can go wrong. If they are introduced after the acquisition and artifact chapters, they become intelligible as the final layer of an already complex system.

Functional MRI is not merely an image-acquisition problem. It is an inference problem. The signal of interest is usually a small time-varying effect embedded within a larger mixture of nuisance sources. Some nuisance sources are scanner-related. Some are motion-related. Some are genuine biological responses that are real, measurable, and even BOLD-like, but not the neural process the experimenter hoped to isolate.

That last category is especially important. Biological confounds are not “fake” in the sense of being nonexistent. Many are real physiologic processes that alter MR signal lawfully. They are confounds because they threaten the mapping from measured signal to intended neural interpretation.

## 13.2 Biological mechanisms that modify fMRI signal
The source slides begin this final block with “Biological mechanisms,” and that broad framing is exactly right. A useful way to organize the topic is by asking: **what biological processes can change the MR signal, even if neural activity of interest has not changed in the intended way?**

Several broad classes matter repeatedly in practical fMRI.

### Baseline vascular state
The BOLD response depends not only on neural activity but on vascular reactivity and baseline physiology. Two subjects with the same neural activation can show different BOLD amplitudes if their vascular systems respond differently.

### Blood gases and respiration-related physiology
Arterial carbon dioxide, oxygenation status, and respiratory pattern can alter cerebral blood flow, blood volume, and blood oxygenation. These changes can produce signal fluctuations that are spatially structured and physiologically meaningful, yet unrelated to the psychological process under study.

### Cardiac pulsation and pulsatile vascular motion
The cardiac cycle can produce local signal fluctuations through vessel motion, cerebrospinal fluid pulsatility, and subtle tissue displacement. These effects may be modest in mean images but important in temporal variability.

### Arousal, fatigue, vigilance, and behavioral state
Alertness and task engagement can change over the course of a scan. These changes may alter both neural activity and physiology, making them especially difficult to classify cleanly.

### Endogenous motion-linked physiology
Breathing, swallowing, jaw tension, posture adjustment, and subtle body movement can alter both physiology and image quality simultaneously.

These mechanisms are not independent; they often interact. For example, anxiety can change breathing and vascular tone, which changes signal. Fatigue can change compliance, eye behavior, and task performance. Caffeine can alter both vascular dynamics and subjective alertness.

## 13.3 Why nuisance importance depends on experiment type
One of the source slides explicitly addresses the **relative importance of nuisance variables to different classes of fMRI experiment**. This is one of the most valuable high-level ideas in the entire confounds section.

There is no single universal ranking of confounds. Their importance depends on the experiment.

For example:
- In a **visual task**, eye movements and vigilance shifts may matter greatly.
- In a **motor task**, subtle motion and muscle-associated physiology may dominate.
- In a **resting-state study**, breathing, cardiac fluctuations, sleepiness, and slow drifts can strongly influence the apparent network structure.
- In a **single-trial event-related design**, time-varying arousal, habituation, and rapid physiologic fluctuations can be especially damaging because the effects of interest are already small and temporally sparse.
- In studies of **clinical or pharmacologic populations**, baseline vascular differences may change the amplitude or timing of BOLD independent of neural mechanism.

This means good fMRI practice does not ask only, “What confounds exist?” It asks, “Which confounds matter most for this specific design, population, target region, and interpretation?”

## 13.4 Human factors as modifiers rather than mere nuisances
The source deck then reframes the issue as **human factors as modifiers**. This wording is important. Human behavior and state do not merely add noise. They often alter the size, timing, or spatial distribution of the measured response.

Examples include:
- alertness and sleepiness,
- anxiety or discomfort,
- task comprehension,
- compliance and effort,
- respiration pattern,
- caffeine or medication use,
- hydration,
- recent exercise,
- and whether the subject talks, fidgets, or moves subtly between runs.

A confound is therefore not always something external to the experiment. Sometimes the experimental session itself changes the biologic conditions under which the imaging is performed.

This perspective is especially helpful because it prevents a false separation between “scanner issues” and “subject issues.” In real fMRI, the subject is part of the measurement system.

## 13.5 Caffeine as a concrete case study
The source slides single out **caffeine** with the memorable phrase “Damned if you do…?” and refer to changes in visual-task responses before and after a 200 mg dose. This is a good case study because caffeine is common, biologically active, behaviorally relevant, and not straightforward to handle.

Caffeine can:
- alter cerebral blood flow,
- change vascular tone and reactivity,
- affect alertness and performance,
- modify baseline state,
- and therefore change the measured BOLD response in more than one way.

This produces a practical dilemma. If participants consume caffeine, vascular and performance effects may change the fMRI signal. If they abstain abruptly, withdrawal or altered arousal may also change the signal. Thus the best practice is not a naive universal ban or universal allowance, but **consistency plus documentation**.

The broader principle is that many common lifestyle factors—sleep, stress, food timing, medication, exercise, nicotine, caffeine—behave similarly. They are not always dominant, but they can become important depending on study design.

## 13.6 Human factors modify the main confounding mechanisms
The source slides explicitly discuss the **relative importance of human factors modifying the main confounding mechanisms**. This suggests a useful conceptual framework.

Human factors modify confounds through several pathways:

### Pathway 1: physiology
Arousal, caffeine, fatigue, and stress change vascular and autonomic physiology.

### Pathway 2: motion and compliance
Discomfort, anxiety, poor task understanding, or boredom increase motion, fidgeting, and inconsistent performance.

### Pathway 3: neural state variation
Subjects may not remain in a stable cognitive state across a run. Mind wandering, habituation, and drowsiness alter the neural background itself.

### Pathway 4: interaction with acquisition choices
Some human-factor effects become more visible under certain protocols. For example, inflow-sensitive acquisitions may accentuate some vascular differences, while high-SMS short-TR protocols may reveal subtle physiologic periodicities more clearly.

This is why the most useful confound model is not a flat list but an interaction map.

## 13.7 Which MRI scans are most useful for capturing biological confounds?
The source deck includes a slide on the **relative utility of MRI scans to capture biological confounds**. This is a particularly practical question because it turns confound awareness into acquisition planning.

Different MRI measurements can be useful for different confound classes:
- **Field maps or reverse-phase-encoded EPI pairs** help characterize distortion-related off-resonance structure.
- **Structural scans** help identify anatomy, susceptibility-prone regions, and motion-degraded morphology.
- **Temporal stability measures** such as tSNR maps help identify unstable regions.
- **Multi-echo acquisitions** can help separate some TE-dependent BOLD-like signal from certain non-BOLD components.
- **Additional physiology-sensitive scans** may be useful depending on the research question, such as vascular reactivity or perfusion-related acquisitions, although these are not always part of routine protocols.

The broader lesson is that some confounds are better addressed with extra imaging, while others are better addressed with auxiliary non-imaging measurements or with better session control.

## 13.8 The role of simultaneous auxiliary data
The source slides also refer to the **relative utility of simultaneous auxiliary data**. This is a crucial point because many confounds are physiologic time-series phenomena, not just image-space phenomena.

Auxiliary data can include:
- respiration traces,
- cardiac pulse recordings,
- end-tidal CO₂ when available,
- eye tracking,
- behavioral performance logs,
- button-response timing,
- and task-compliance measures.

These are valuable because they provide direct or indirect access to nuisance processes that are otherwise only inferred from the imaging data. In many studies, such recordings are not optional luxuries. They are the only way to model or at least recognize certain confound sources with confidence.

## 13.9 What should be collected before and after the scan?
The source deck closes with the **relative importance of auxiliary data to collect pre/post scan**. This is perhaps the most operationally important question of the confounds chapter.

Useful pre/post-scan information may include:
- recent caffeine use,
- sleep quality or sleep duration,
- medication status,
- nicotine or stimulant use,
- hydration and meal timing,
- exercise prior to scan,
- anxiety/discomfort notes,
- task understanding and compliance,
- and any unusual scanner-room events.

These data are often omitted because they feel secondary to the MRI itself. In reality, they can be essential for interpretation, especially when a dataset looks unusual and the imaging alone cannot explain why.

## 13.10 A practical confounds hierarchy
Combining the source slides with the earlier chapters, a practical confounds hierarchy in fMRI can be framed like this:

### Level 1: acquisition and hardware confounds
- ghosting,
- distortion,
- dropout,
- residual aliasing,
- coil instability,
- spikes and drift.

### Level 2: motion-linked and setup-linked confounds
- head motion,
- eye motion,
- breathing-linked pseudo-motion,
- receive-bias modulation,
- spin-history effects.

### Level 3: physiological confounds
- vascular baseline variation,
- breathing and CO₂ changes,
- cardiac effects,
- inflow,
- arousal and fatigue.

### Level 4: human-factor modifiers
- caffeine,
- sleep,
- stress,
- discomfort,
- effort,
- compliance,
- medication.

The levels interact, but this hierarchy helps the user reason systematically about what class of explanation is most plausible when a dataset or response pattern looks abnormal.

## 13.11 Interpretation rules for practical fMRI
A cautious but useful set of interpretation rules follows from this chapter.

1. **Do not equate statistically significant with neurally specific.** A strong signal can still reflect a confound.
2. **Do not equate BOLD-like with task-specific.** Real BOLD physiology can still reflect nuisance vascular or systemic influences.
3. **Always ask what state the subject was in.** Subject state is not background; it is part of the measurement context.
4. **Confounds matter differently by design.** There is no universal ranking.
5. **Consistency is often more valuable than theoretical purity.** Standardized participant preparation and good metadata can sometimes do more for interpretability than minor protocol tweaks.

---

**Figure 13.1 (planned).** Concept map of biological confound mechanisms and how they interact with acquisition and interpretation. Adapt from source slides 219–224.

**Figure 13.2 (planned).** Caffeine case study showing response differences before and after dose. Adapt from source slide 223.

**Figure 13.3 (planned).** Decision chart for MRI-based versus auxiliary-data-based confound assessment. Adapt from source slides 225–226.

---

### Why This Matters
The biggest mistake in fMRI interpretation is not missing a rare scanner failure. It is failing to ask whether the signal you trust is actually the signal you think you are measuring.

### Practical Scanner Implication
For many studies, improved confound handling begins before the first RF pulse: standardize participant preparation, record relevant human-factor information, and decide in advance which auxiliary measurements are worth collecting.

---

## Chapter 13 Summary
- Biological confounds are real physiologic processes that alter measured fMRI signal without necessarily reflecting the neural process of interest.
- The importance of different confounds depends strongly on experiment type, region of interest, and participant population.
- Human factors such as caffeine, sleep, stress, and compliance often modify the main physiological confound pathways rather than merely adding generic noise.
- Extra MRI scans and simultaneous auxiliary recordings can help characterize different confound classes, but they solve different problems.
- Good fMRI interpretation requires both acquisition awareness and session-context awareness.

## Key Terms
- Biological confound
- Vascular reactivity
- Inflow
- Auxiliary data
- Vigilance
- Compliance
- Caffeine effect
- Baseline physiology
- Non-neural BOLD-like signal

## Review Questions
1. Why is the importance of a confound design-dependent rather than universal?
2. Why can caffeine be both scientifically relevant and methodologically problematic in fMRI?
3. What types of simultaneous auxiliary data are most useful for identifying physiological confounds?
4. Why is it misleading to treat all non-neural signal change as simple “noise”?
5. What types of pre/post-scan information are most useful to collect for interpretation?
6. How would you explain the difference between a hardware artifact and a biological confound?

---

# Chapter 14. Integrative Practical Framework for Running and Interpreting fMRI

## 14.1 Why a synthesis chapter is necessary
The source slides end with confound-prioritization tables, but the broader course as a whole teaches something even more valuable: practical fMRI is an exercise in **integrative judgment**.

A reader who finishes this book should not merely know isolated facts such as “ghosts occur at FOV/2” or “SMS requires a phased-array coil.” The reader should be able to connect acquisition choices to predictable artifact patterns, connect those artifact patterns to likely interpretive risks, and connect interpretive risks to choices about QC and auxiliary measurements.

That is the purpose of this final chapter. It converts the preceding chapters into a workflow of practical reasoning.

## 14.2 Connecting acquisition choices to artifact vulnerability
Every major acquisition decision changes the error landscape.

### Main field strength
Higher field often improves available signal but increases susceptibility burden and nonuniformity challenges.

### Echo time (TE)
Longer TE generally increases BOLD sensitivity but worsens dropout and signal loss in susceptibility-prone regions.

### Repetition time (TR)
Shorter TR improves temporal sampling but increases steady-state complexity, flip-angle dependence, and often acceleration pressure.

### Slice thickness
Thinner slices reduce intravoxel dephasing and therefore can reduce dropout, but they reduce per-voxel SNR and may force compromises in coverage or TR.

### Phase-encoding direction
Changes the direction in which distortion and ghost placement occur, which can change whether artifacts overlap the region of interest.

### Partial Fourier
Can increase coverage or shorten timing but may increase smoothing and vulnerability to dropout-related tradeoffs.

### GRAPPA
Can reduce distortion but increases reconstruction dependence and motion sensitivity.

### SMS
Can reduce TR or increase coverage but increases slice-leakage and calibration sensitivity when pushed too far.

### Multi-echo EPI
Can improve interpretive leverage but increases complexity and often requires further acceleration support.

The practical user should therefore think of protocol design as choosing not just what data to collect, but also what failure modes to tolerate.

## 14.3 Connecting artifacts to downstream analysis risk
An artifact is not important merely because it is visually ugly. It is important because it threatens a downstream inference.

Some examples:
- **Ghosting** is especially dangerous when it overlaps expected activation regions or varies with time.
- **Distortion** is especially dangerous when accurate anatomical localization matters.
- **Dropout** is especially dangerous when the study depends on orbitofrontal or inferior temporal signal.
- **Residual aliasing** is dangerous when accelerated-imaging leakage creates structured but subtle nuisance patterns.
- **Receive-bias motion effects** are dangerous when small motion appears as plausible regional time-series modulation.
- **Biological confounds** are dangerous when they mimic expected timing or correlate with task structure indirectly.

Thus, QC should not be aesthetic alone. It should be hypothesis-aware.

## 14.4 Choosing compromises for different study goals
Different studies justify different compromises.

### Whole-brain task fMRI
Coverage and robust temporal sampling may dominate. Moderate distortion may be acceptable if the target regions are not in severe susceptibility zones.

### Orbitofrontal or anterior temporal studies
Dropout and distortion burden become central. Phase-encoding direction, slice thickness, TE, and perhaps multi-echo strategy deserve extra attention.

### High-resolution laminar or small-structure work
SNR, distortion, and motion sensitivity become much more severe constraints. Aggressive acceleration may help some aspects while worsening others.

### Resting-state studies
Long-run stability, physiologic recording, vigilance control, and drift become especially important.

### Clinical or developmental studies
Motion tolerance, participant comfort, and standardized preparation may matter more than theoretical peak efficiency.

This is why no acquisition template is universally optimal.

## 14.5 A pre-scan checklist
Before the scan begins, a practical operator should ask:

### Subject preparation
- Has caffeine/medication/sleep status been documented if relevant?
- Does the participant understand the task?
- Is the participant comfortable enough to remain still?
- Is the importance of eye behavior, talking avoidance, and motion control clear?

### Hardware/setup
- Is the coil seated correctly and stably?
- Are cables, pads, and accessories positioned cleanly?
- Is the phase-encoding direction appropriate for the region of interest?
- Are acceleration settings justified rather than habitual?

### Protocol design
- Is TE appropriate for the target contrast and anatomical region?
- Is slice thickness acceptable given dropout concerns?
- Are auxiliary recordings planned if the study needs them?

## 14.6 An in-scan checklist
During the scan, the following questions matter:
- Do the mean images resemble known-good data?
- Is ghosting weak and where expected?
- Is distortion tolerable for the target anatomy?
- Is dropout catastrophic in the target region?
- Are there signs of unexpected spikes, leakage, or instability?
- Is the subject moving, talking, breathing irregularly, or fatiguing?
- Does a quick retest improve or reproduce the problem?

The value of rapid visual QC cannot be overstated. Detecting a correctable issue during the session is vastly better than discovering it after the subject has left.

## 14.7 A post-scan checklist
After the acquisition, interpretation should be guided by structured review.

### Image quality review
- mean image,
- standard-deviation image,
- temporal SNR,
- motion estimates,
- distortion profile,
- presence of residual aliasing or spikes.

### Session-context review
- unusual subject behavior,
- discomfort or noncompliance,
- caffeine or sleep irregularity,
- hardware/setup notes,
- any mid-session changes.

### Analysis-risk review
- Did the main confounds likely overlap the regions of interest?
- Are there design features that make specific confounds especially dangerous?
- Are auxiliary recordings adequate for nuisance modeling?

## 14.8 A decision tree for practical interpretation
When interpreting a result, a cautious practical workflow is:

1. **Is the data quality acceptable in principle?**  
   If not, stop before overinterpreting statistics.

2. **Do known artifacts overlap the effect location?**  
   If yes, interpret with strong caution.

3. **Could the effect be explained by motion, physiology, or human-factor variation?**  
   If yes, evaluate available nuisance evidence.

4. **Does the acquisition design make the region especially vulnerable to the observed pattern?**  
   If yes, do not treat the effect as generic evidence.

5. **Are additional supporting data available?**  
   Structural alignment, auxiliary physiology, task behavior, retests, or alternative contrasts can increase confidence.

This process is slower than naive interpretation, but it is much more scientifically honest.

## 14.9 The final synthesis: from signal physics to scientific validity
The deepest lesson of practical fMRI is that scientific validity emerges from a chain, not from a single good image.

The chain looks like this:

spin physics → excitation and relaxation → spatial encoding → EPI trajectory → artifact structure → motion and hardware interaction → physiologic modulation → human-factor modification → interpretation.

At any stage, simplifications can be useful. But if too many stages are ignored, the final inference becomes fragile.

This is why MRI education should not split into disconnected courses on “physics,” “sequences,” and “analysis.” Practical competence lives in the links between them.

A reader who can reason across the full chain is much less likely to make two common errors:
1. overtrusting a clean-looking but unstable dataset,
2. or dismissing a complex but still interpretable dataset without understanding what actually limits it.

## 14.10 What practical mastery looks like
Practical mastery in fMRI does not mean memorizing every pulse-sequence option or every published correction technique. It means being able to answer questions like these:
- Why does this region look distorted?
- Why does this task effect appear earlier at one flip angle than another?
- Why did motion correction not remove the fluctuation?
- Why did acceleration reduce one problem but create another?
- What extra data should I collect next time to distinguish competing explanations?

If this manuscript succeeds, the reader should be able to treat those questions not as isolated mysteries, but as reasoned consequences of the system described throughout the book.

---

**Figure 14.1 (planned).** Integrated concept map from acquisition choice to artifact burden to interpretive risk. Synthesized from the full course.

**Figure 14.2 (planned).** Pre-scan, in-scan, and post-scan practical checklist.

---

### Key takeaway box
Good fMRI is never just “good pictures.” It is the disciplined management of tradeoffs across physics, hardware, physiology, behavior, and interpretation.

---

## Chapter 14 Summary
- Practical fMRI requires connecting acquisition parameters to expected artifact behavior and downstream inferential risk.
- Different study goals justify different compromises; there is no universally optimal protocol.
- Good practice includes structured pre-scan preparation, in-scan QC, and post-scan interpretive review.
- Scientific confidence in fMRI depends on understanding the full chain from spins to confounds.

## Key Terms
- Protocol tradeoff
- Inferential risk
- Quality control
- Auxiliary recording
- Hypothesis-aware QC
- Session context

## Review Questions
1. Why is a visually acceptable image not sufficient evidence of scientifically acceptable fMRI data?
2. How do study goals change the appropriate acquisition tradeoffs?
3. Why should QC be hypothesis-aware rather than purely aesthetic?
4. What information should be gathered before, during, and after the scan to support interpretation?
5. What does it mean to say that scientific validity in fMRI emerges from a chain rather than from a single step?

---

# Appendix A. Equation Guide and Symbol Reference

## A.1 Core equations

### Larmor equation
\[
\omega_0 = \gamma B_0
\]
**Meaning:** precessional angular frequency is proportional to the magnetic field.  
**Why it matters:** sets resonance frequency, RF hardware frequency, and the sensitivity of imaging to field perturbations.

### Boltzmann population relation
\[
\frac{N_{\text{low}}}{N_{\text{high}}} = e^{\Delta E/kT}
\]
**Meaning:** lower-energy spin states are slightly more populated.  
**Why it matters:** explains why equilibrium magnetization exists but is intrinsically small.

### Flip-angle relation
\[
\theta = \gamma B_1 T_p
\]
**Meaning:** RF amplitude and pulse duration determine the tip angle.  
**Why it matters:** connects sequence timing to excitation strength, saturation behavior, inflow sensitivity, and steady-state contrast.

### Transverse decay
\[
M_{xy}(t) = M_{xy}(0)e^{-t/T_2}
\]
**Meaning:** coherent transverse magnetization decays exponentially.  
**Why it matters:** underlies T2 contrast and helps explain why echoes must be sampled promptly.

### Longitudinal recovery
\[
M_z(t) = M_0\left(1-e^{-t/T_1}\right)
\]
**Meaning:** longitudinal magnetization recovers toward equilibrium after excitation.  
**Why it matters:** determines saturation, T1 weighting, and repeated-excitation behavior.

### Signal under a readout gradient
\[
S(t) = \int M(x)e^{i\gamma G_x t x}\,dx
\]
**Meaning:** the measured signal is the sum of spatial contributions whose phase evolves according to gradient-imposed position dependence.  
**Why it matters:** provides the direct bridge from object space to encoded signal.

### k-space definition
\[
k(t) = \frac{\gamma}{2\pi}\int_0^t G(\tau)\,d\tau
\]
**Meaning:** k-space position depends on gradient area.  
**Why it matters:** allows pulse sequences to be understood as trajectories through spatial-frequency space.

### Image–k-space Fourier relationship
\[
S(k_x) = \int M(x)e^{i2\pi k_x x}\,dx
\]
**Meaning:** k-space data are the Fourier transform of the spatial object.  
**Why it matters:** explains reconstruction, aliasing, partial Fourier, and many artifact classes.

## A.2 Common symbols
- \(B_0\): static main magnetic field
- \(B_1\): RF excitation field
- \(\gamma\): gyromagnetic ratio
- \(\omega_0\): Larmor angular frequency
- \(M_0\): equilibrium magnetization
- \(M_z\): longitudinal magnetization
- \(M_{xy}\): transverse magnetization
- \(T_1\): longitudinal relaxation time
- \(T_2\): intrinsic transverse relaxation time
- \(T_2^*\): apparent transverse decay including field inhomogeneity
- \(G_x, G_y, G_z\): gradient amplitudes along x, y, z
- \(k_x, k_y\): spatial-frequency coordinates
- \(TE\): echo time
- \(TR\): repetition time
- \(FA\): flip angle
- \(\chi\): magnetic susceptibility

---

# Appendix B. Artifact Troubleshooting Tables

## B.1 Quick symptom-to-cause table

| Symptom | Likely mechanism | First thing to check | Common response |
|---|---|---|---|
| Replica image at ~FOV/2 in PE direction | Nyquist ghosting / odd-even mismatch | Is it stable or time-varying? | Check ghost correction, eye motion, fat suppression, timing stability |
| Warped anatomy near sinuses or ear regions | Off-resonance distortion | PE direction and local susceptibility zones | Reverse PE pair, adjust protocol, accept tradeoff with caution |
| Signal voids in orbitofrontal or inferior temporal cortex | Susceptibility dropout / intravoxel dephasing | TE, slice thickness, target anatomy | Consider thinner slices, shorter TE, alternative protocol choices |
| Bright shifted scalp signal or ghost-like contamination | Fat-related chemical shift / inadequate fat suppression | Was fatsat on and effective? | Improve fat suppression and review PE placement |
| Fine replicated structure after accelerated imaging | Residual aliasing from GRAPPA/SMS | Calibration/reference stability | Review ACS/SBRef quality, reduce acceleration if needed |
| Sudden spikes across time | RF interference / gradient or coil spikes | Does it appear across sequence types? | Run short retest, QC, phantom if needed |
| Structured fluctuation after motion correction | Receive-bias modulation / spin history / residual motion | Coil geometry, motion traces, receive nonuniformity | Interpret cautiously, review preprocessing and acquisition context |
| Global or slow drift over run | System drift, chronic motion, subject-state change | Long-run stability and session notes | Retest, review padding/setup, consider nuisance modeling |

## B.2 Practical diagnostic questions
1. Is the problem in one frame or across the whole run?
2. Is it present in multiple sequence types?
3. Does it align with the phase-encode direction?
4. Does it worsen with motion or calibration mismatch?
5. Does it overlap the region of interest?
6. Would a short retest or phantom test distinguish subject from hardware causes?

---

# Appendix C. Acquisition Tradeoff Summary Tables

## C.1 Parameter tradeoffs

| Parameter / method | Main benefit | Main cost | Best use case | Main caution |
|---|---|---|---|---|
| Longer TE | Stronger T2* / BOLD sensitivity | More dropout and lower raw signal | BOLD-sensitive studies in moderate artifact regions | Risky in orbitofrontal / inferior temporal cortex |
| Shorter TE | Less dropout, better signal retention | Reduced BOLD sensitivity | Artifact-prone regions or robustness-first protocols | May weaken functional contrast |
| Thinner slices | Less intravoxel dephasing | Lower per-voxel SNR, more slices needed | Susceptibility-prone regions | Coverage/TR tradeoff |
| Partial Fourier | More slices or shorter TR | Smoothing, SNR loss, some dropout tradeoff | Coverage-limited EPI | Choose early vs late omission deliberately |
| GRAPPA | Less distortion, higher nominal efficiency | Motion-sensitive calibration, noise amplification | Distortion-limited EPI | ACS quality is crucial |
| SMS | Shorter TR / more coverage | Slice leakage, calibration burden, low-SNR fragility | Fast whole-brain EPI | Avoid overaggressive MB factors |
| Multi-echo EPI | Better regional SNR and TE-dependent classification | More complexity and acceleration pressure | Studies where BOLD/non-BOLD separation matters | Does not solve all physiology |
| Higher flip angle | More signal in some settings | More saturation/inflow weighting changes | Specific steady-state designs | Temporal behavior can change |
| Reverse PE pair | Distortion characterization/correction | Extra acquisition time | Distortion-sensitive protocols | Still not a substitute for good base EPI |

## C.2 Study-priority framing
- **If coverage is limiting:** consider SMS or partial Fourier, but watch calibration and smoothing costs.
- **If distortion is limiting:** consider GRAPPA and PE-direction choice.
- **If dropout is limiting:** consider thinner slices, TE adjustment, and anatomy-aware compromises.
- **If interpretation is limiting:** consider multi-echo and better auxiliary recordings.

---

# Glossary

**Aliasing** — Wrap-around of signal caused by insufficient sampling or inadequate field of view representation.

**Autocalibration signal (ACS)** — Fully sampled reference data used to reconstruct missing lines in GRAPPA-style parallel imaging.

**B0** — Static main magnetic field of the MRI system.

**B1** — Oscillating RF magnetic field used for excitation.

**BOLD** — Blood-oxygen-level-dependent contrast; a T2*-weighted fMRI signal mechanism linked to hemodynamic consequences of neural activity.

**Chemical shift** — Frequency difference between chemically distinct proton environments caused by electronic shielding.

**Conjugate symmetry** — Relationship between opposite parts of k-space used in partial Fourier reconstruction under appropriate assumptions.

**Conjugate variables** — Paired domains related by Fourier transform, such as time/frequency and space/k-space.

**Distortion** — Off-resonance-driven misplacement of signal, especially along the phase-encoded direction in EPI.

**Dropout** — Local signal loss caused by strong dephasing, often from susceptibility variation.

**Echo-planar imaging (EPI)** — Rapid imaging method that samples many k-space lines after a single excitation using a train of gradient echoes.

**Echo time (TE)** — Time between excitation and echo sampling.

**Flip angle (FA)** — Rotation angle of magnetization produced by an RF pulse.

**Fourier transform** — Mathematical operation that converts a signal between conjugate domains, such as time and frequency or image space and k-space.

**Free induction decay (FID)** — Decaying transverse MR signal following excitation in the absence of full refocusing.

**Ghosting** — Replica-image artifact, commonly caused in EPI by odd/even line mismatch or related timing/phase errors.

**Gradient echo (GRE)** — Echo produced by reversing gradient-induced dephasing with balanced gradient moments rather than with a 180° RF pulse.

**Gradient spiking** — Artifact arising from abrupt transient gradient-related corruption.

**GRAPPA** — Parallel imaging method that reconstructs omitted k-space lines using multi-channel coil data and reference calibration.

**Gyromagnetic ratio** — Constant linking magnetic field strength to resonance frequency for a given nucleus.

**Inflow effect** — Signal change caused by fresh spins entering the imaging region with different saturation history than stationary tissue.

**K-space** — Spatial-frequency representation of the image.

**Larmor frequency** — Resonance frequency of precession in a magnetic field.

**Multi-echo EPI** — EPI acquisition collecting more than one echo per excitation for combined-SNR or TE-dependent analysis.

**Nyquist ghost** — Classic EPI ghosting artifact often displaced by half the field of view in the phase-encoded direction.

**Partial Fourier** — Acquisition strategy that omits part of k-space and reconstructs the missing portion approximately.

**Phase encoding** — Spatial encoding dimension in which gradient-induced phase steps are varied across repetitions.

**Prescan normalize** — Reconstruction or scanner option used to reduce apparent intensity nonuniformity from receive bias.

**Receive bias field** — Spatial variation in receive-coil sensitivity across the image.

**Receive field heterogeneity** — Nonuniform receive sensitivity pattern, especially important with coil arrays.

**Residual aliasing** — Incomplete unaliasing after acceleration methods such as GRAPPA or SMS.

**Repetition time (TR)** — Time between successive excitations in a repeated sequence.

**Rotating frame** — Reference frame rotating at or near the Larmor frequency, used to simplify spin dynamics.

**Signal-to-noise ratio (SNR)** — Ratio of measured signal amplitude to noise level.

**Simultaneous multi-slice (SMS)** — Method that excites multiple slices at once and uses coil sensitivity to separate them.

**Slice selection** — Excitation of a limited spatial slab using a selective RF pulse during a gradient.

**Spin echo** — Echo formed by applying a 180° RF pulse to refocus certain types of dephasing.

**Spin history** — Dependence of current magnetization on previous excitation history.

**Susceptibility** — Tendency of a material to magnetize in an external field, affecting local field structure.

**T1** — Longitudinal relaxation time describing recovery toward equilibrium magnetization.

**T2** — Intrinsic transverse relaxation time describing loss of coherence from microscopic interactions.

**T2*** — Apparent transverse decay that includes T2 plus additional dephasing from field inhomogeneity.

**Temporal SNR (tSNR)** — Mean signal over time divided by temporal standard deviation; a measure of time-series stability.

**Wrap-around** — Another term for aliasing.

---

# Index-like Keyword Guide

## Core physics
B0; B1; Larmor frequency; net magnetization; rotating frame; flip angle; T1; T2; T2*; spin echo; gradient echo.

## Image formation
Fourier transform; conjugate variables; gradients; slice selection; k-space; frequency encoding; phase encoding; readout.

## EPI and artifacts
EPI; ghosting; Nyquist ghost; distortion; dropout; fat suppression; chemical shift; bandwidth; phase-encoding direction.

## Advanced methods
Partial Fourier; GRAPPA; ACS; SMS; multiband; multi-echo EPI; FLEET.

## Troubleshooting and QC
tSNR; standard-deviation image; residual aliasing; coil instability; RF interference; gradient spiking; retest; phantom check.

## Confounds and interpretation
Inflow; spin history; receive bias field; biological confounds; human factors; caffeine; auxiliary data; interpretation risk.
