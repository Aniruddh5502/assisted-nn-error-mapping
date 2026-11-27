---
title: Assisted neural network architecture test
description: In this test I use an additional vanilla neural network to try to map the error landscape of the primary Surrogate model. If the error fields of the outputs are a function of the input, then this NN should be able to learn the manifold given the model has enough capacity.
draft: false
---
# Assisted Neural Networks: Input Driven Error Estimation

## Introduction
In this experiment, we evaluate whether the error landscape of a primary surrogate model can be predicted using an auxiliary neural network (the "Error Mapper"). 

The workflow consists of two stages:
1. **Primary Model Training:** A standard neural network is trained to predict physical outputs (e.g., stress, deformation, frequency modes) from a design space (SDOF Macro Scale Compliant Mechanism).
2. **Error Mapping:** An `ErrorMapper` network is trained to take the original input design vectors and predict the absolute error ($\text{Error} = |Y_{true} - Y_{pred}|$) produced by the Primary model.

If high correlations (Pearson/Spearman) are found between the predicted error and the actual error, it proves that the model's inaccuracy is a predictable function of its input coordinates.

## Methodology
1. **Data Preparation:** Load the dataset and split into training, validation, and testing sets.
2. **Stage 1 (Primary):** Train the `Primary` model on the training split to minimize MSE.
3. **Stage 2 (Error Mapper):** 
    - Pass the validation/test set through the trained `Primary` model to calculate actual errors.
    - Train the `ErrorMapper` to map inputs $\mathbf{X}$ to these calculated errors $\mathbf{E}$.
4. **Validation:** Perform a correlation analysis on the test set to compare the `ErrorMapper` predictions against the actual residuals.

## Usage

### 1. Prepare the Data
Ensure you are in the project root or the `tests` directory.
```bash
python -m assisted_nn.utils.data_loader
```

### 2. Train the Primary Model
```bash
python -m assisted_nn.core.train
```

### 3. Train the Error Mapper Model
```bash
python -m assisted_nn.core.trainer_errormapper
```

### 4. Run Correlation Analysis
To execute the final validation and generate the correlation report:
```bash
python -m assisted_nn.src.main
```

## Results & Reporting
After running the experiment, a detailed report is generated at:
`reports/correlation-report.md`

The report contains Pearson and Spearman correlation coefficients for each target variable, indicating the reliability of the error estimation.
