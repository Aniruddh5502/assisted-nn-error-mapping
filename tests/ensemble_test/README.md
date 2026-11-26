# Ensemble Test Guide

## Purpose
Tests whether **ensemble variance** (spread across 10 independently trained neural networks) correlates with **absolute prediction error** on parametric FEA surrogates. This evaluates if ensemble spread is a factual reliability indicator for engineering surrogate models.

## Folder Structure
The pipeline operates using the following root-level directory structure:
```
├── core/                # Ensemble logic and trainer
├── scripts/             # Execution scripts (train, evaluate, run_all)
├── utils/               # Data processing utilities
├── checkpoints/         # Model weights (.pt) and training history
├── results/             # Correlation analysis, plots, and summary.md
├── data/                # Processed train/val/test CSV files
└── tests/ensemble_test/ # Test module organization (internal scripts/logic)
```

## What the Code Tests
| Hypothesis | Test |
|------------|------|
| Ensemble variance correlates with absolute error | Spearman & Pearson correlation per target |
| Variance identifies "confident but wrong" predictions (Q3: low var, high error) | Reliability diagram quadrant analysis |
| Ensemble generalizes on parametric FEA manifold | Test MAE/RMSE on held-out 15% |

**Targets (6):**
- `max_stress_von_mises`
- `max_deformation`
- `mode_1_freq` — `mode_4_freq`

**Architecture:** 10 independent MLPs (4 → 32 → 32 → 6), ReLU hidden, no output activation.  
**Optimizer:** Adam (lr=1e-3).  
**Data:** 1897 samples from `data/raw/inputs.csv` → 70/15/15 split.

## Where is the Report
All outputs are saved in the **root directory**:
- **Auto-generated summary:** `results/summary.md` (created by `run_all.py`)
- **Correlation statistics:** `results/correlation_analysis.csv`
- **Visual reports:** 6 reliability diagrams + training curves + heatmap + error distributions (saved in `results/`)
- **Raw predictions:** `results/test_predictions.csv`, `results/individual_predictions.csv`

## Latest Results (from most recent run)

### Correlation: Variance vs Absolute Error

| Target | Spearman ρ | Pearson r |
|--------|-----------|-----------|
| max_stress_von_mises | 0.226 | 0.596 |
| max_deformation | 0.648 | 0.396 |
| mode_1_freq | 0.476 | 0.508 |
| mode_2_freq | 0.353 | 0.318 |
| mode_3_freq | 0.405 | 0.389 |
| mode_4_freq | 0.341 | 0.382 |

### Interpretation
- **Spearman ρ (0.23–0.65)**: Moderate monotonic relationship — variance somewhat tracks error rank
- **Pearson r (0.32–0.60)**: Moderate linear correlation — stronger for stress/deformation
- **Key finding**: Ensemble variance provides *some* signal but is **not a strong factual error bound** for FEA manifolds
- **Danger zone (Q3)**: Low variance + high error cases exist — ensemble can be confidently wrong

### Training
- Best validation loss: **0.000076** (MSE, normalized scale)
- 10 models × 14,140 params each
- Early stopping at epoch ~180 (patience=50)

*Full details in `results/summary.md`*

## How to Run

To generate the report, run the orchestration script from the project root:
```bash
python scripts/run_all.py
```
Or to specifically generate a report from existing results:
```bash
python tests/ensemble_test/scripts/generate-report.py
```