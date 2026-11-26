# Ensemble Test Guide

## Purpose
This project investigates whether **ensemble variance** (the spread across 10 independently trained neural networks) correlates with **absolute prediction error** on parametric Finite Element Analysis (FEA) surrogate models. The goal is to determine if ensemble spread serves as a reliable indicator of prediction uncertainty in engineering manifolds.

## Project Structure
```
├── core/                # Model architecture and trainer logic
├── scripts/             # Orchestration and execution (train, evaluate, run_all)
├── utils/              # Data processing and scaling utilities
├── checkpoints/         # Trained model weights (.pt) and training history
├── results/             # Summary reports, statistical CSVs, and visualizations
├── data/               # Split datasets (train, val, test)
└── README.md            # Documentation
```

## Core Hypotheses
- **Correlation**: Does ensemble variance correlate with absolute error? (Measured via Spearman & Pearson coefficients).
- **Reliability**: Can variance identify "confident but wrong" predictions? (Analyzed via reliability diagram quadrants).
- **Generalization**: How well does the ensemble generalize to the held-out 15% test set?

**Target Variables (6):**
- `max_stress_von_mises`, `max_deformation`, `mode_1_freq`, `mode_2_freq`, `mode_3_freq`, `mode_4_freq`.

**Model Configuration:**
- **Architecture**: 10 independent MLPs (4 $\to$ 32 $\to$ 32 $\to$ 6), ReLU hidden, no output activation.
- **Optimizer**: Adam ($\alpha = 10^{-3}$).
- **Data**: 1,897 samples from `data/raw/inputs.csv` (70/15/15 split).

## Latest Experiment Results

### Correlation: Variance vs. Absolute Error
The following table shows the correlation between ensemble variance and absolute error for each target.

| Target | Spearman $\rho$ | Pearson $r$ |
| :--- | :---: | :---: |
| `max_stress_von_mises` | 0.3674 | 0.3431 |
| `max_deformation` | 0.0198 | 0.5780 |
| `mode_1_freq` | 0.4359 | 0.5520 |
| `mode_2_freq` | 0.4231 | 0.3729 |
| `mode_3_freq` | 0.4280 | 0.4146 |
| `mode_4_freq` | 0.4643 | 0.4458 |

### Key Findings
- **Moderate Correlation**: Spearman $\rho$ values (0.3–0.4) indicate a moderate monotonic relationship.
- **Signal Strength**: While variance provides some signal for error magnitude, it is not a strong or perfect factual indicator.
- **Consistency**: Results suggest that ensemble spread is not a highly reliable bound for FEA manifolds.

*For detailed analysis and full statistics, see `results/summary.md`.*

## Usage

To execute the full pipeline (training, evaluation, and report generation), run:
```bash
python scripts/run_all.py
```

### Output Artifacts
All results are stored in the `results/` directory:
- `summary.md`: Detailed experiment summary.
- `correlation_analysis.csv`: Raw correlation statistics.
- `*.png / *.svg`: Reliability diagrams, training curves, and error distributions.
- `test_predictions.csv`: Predictions on the test set.
