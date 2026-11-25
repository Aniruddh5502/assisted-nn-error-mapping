# Ensemble Vanilla NN - Experiment Summary

## Configuration
- **Architecture**: 4 -> 32 -> 32 -> 6 (ReLU hidden, no output activation)
- **Ensemble Size**: 10 models
- **Optimizer**: Adam (lr=0.001)
- **Epochs**: 200 (early stopping patience=50)
- **Batch Size**: 32
- **Train/Val/Test Split**: 70/15/15

## Data
- **Source**: `data/raw/inputs.csv`
- **Loaded 1897 samples after cleaning**
- **Split: train=1327, val=284, test=286**

## Training
- **Ensemble: 10 models, 14140 total params**
- **Training complete. Best val loss: 0.000078**

## Evaluation: Variance vs Absolute Error Correlation

| Target | Spearman rho | Pearson r |
|--------|------------|-----------|
| max_stress_von_mises | 0.333610 | 0.522766 |
| max_deformation | 0.297680 | 0.643453 |
| mode_1_freq | 0.411296 | 0.450947 |
| mode_2_freq | 0.252674 | 0.353766 |
| mode_3_freq | 0.332495 | 0.396955 |
| mode_4_freq | 0.295437 | 0.230615 |

## Interpretation
- **Spearman rho (0.3-0.4)**: Moderate monotonic relationship between ensemble variance and absolute error
- **Pearson r (0.3-0.5)**: Moderate linear correlation
- Variance provides **some signal** for error magnitude but is not a strong factual indicator
- Consistent with prior findings: ensemble spread != reliable error bound for FEA manifolds

## Artifacts Generated
- `checkpoints/best_ensemble.pt` - Trained ensemble weights
- `checkpoints/training_history.json` - Per-epoch train/val loss
- `results/correlation_analysis.csv` - Full correlation statistics
- `results/reliability_diagram.png` - 4-quadrant variance vs error plots
- `results/training_curves.png` - Train/val loss curves
- `results/test_predictions.csv` - Predictions (original scale)
- `results/individual_predictions.csv` - All 10 member predictions
