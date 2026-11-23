- [ ] Show the error map. Plot $|e(x)|$ and the predicted error over the input space (for example, against beam_height and beam_width, which you said drive the results). If the two maps look alike, that is direct visual evidence for the claim.
- [ ] Report the baselines on the same definition. Ensemble and SNGP should be scored against the same $e(x)$ with the same recalibration step, so the comparison is fair.


# Paper Framing
## Target Journal
[Applied Soft Computing](https://www.sciencedirect.com/journal/applied-soft-computing)

## To Inlclude in Analysis
- Spearman & Pearson correlation reports
- MAE/RMSE Error magnitude accuracy.
- Calibration: Weather predicted uncertainity

## Formatting


## Scratch
### Abstract
#### Core Parts
The core parts of a good abstract

```markdown

**Background/Motivation(Why)**: This is the opening.Briefly state the problem, the gap in current knowledge, and why this research is important.

**Objective/Purpose(What)**: Clearly state the aim or your study or the hypothesis you are testing. This should be direct statement to what you set out to do.

**Methods(How)**: Describe your approach. Mention the study design, and the key techniques to analyze what the experiment exposed.

**Results(What you found)**: This is the most critical part. Present your main findings directly. Use specific data(numbers, percentages). Every result mentioned should relate to the objective stated.

**Conclusion(What it means)**: State the main take home message. Explain the implications of the findings. And how they contribute to the field.

[1 sentence background/gap] Antibiotic resistance in urinary tract infections is rising, yet empirical treatment guidelines vary widely across regions. [1 sentence objective] This study evaluated resistance patterns among 500 clinical isolates collected in Dhaka between 2021–2023. [1–2 sentences methods] Isolates were identified by culture and susceptibility tested by disk diffusion per CLSI standards. [2–3 sentences results] Resistance to ciprofloxacin was 62%, to ceftriaxone 41%, and to nitrofurantoin 8%. Multidrug resistance was found in 34% of isolates, significantly higher than the 2018 regional baseline (p < 0.01). [1–2 sentences conclusion] These findings suggest nitrofurantoin remains a viable first-line option locally, while fluoroquinolones should be avoided empirically.

```

#### Draft
UQ in surrogate modelings for FEA and other types of areas of reliablity needs. Current methods of UQ or predictive error modeling are crude and do not have much correlation with actual error as they mostly provide probabilistic intervals for error. Although in this paper keeping the UQ aside, we focus on the nature of the error for a multi-dimensional FEA regression problem setup.