---
title: Assisted neural network architecture test
description: In this test I use an additional vanilla neural network to try to map the error landscape of the primary Surrogate model. Now if the error fields of the outputs are a function of the input meaning if the error changes correlating to where the design point is, then this NN should be able to learn the manifold given the model has enough capacity to learn it.
draft: true
---
# Assisted Neural Networks Input Driven Error Estimation
## Introduction
In this experiment we first train our primary model to predict the outputs for the regression problem dataset for the SDOF Macro Scale Compliant Mechanism. Then train another model named Error Mapper to predict the error quantities of the Primary surrogate model form the input vector data.

## Methodology


## Usage
To prepare the data, run
```bash
cd tests
python -m assisted_nn.utils.data_loader
```
To train the Primary Model
```bash
python -m assisted_nn.core.train
```
To train the Error Mapper Model
```bash
python -m assisted_nn.core.trainer_errormapper
```
To run the experiment, execute
```bash
cd tests 
python -m assisted_nn.src.main
```
Now check the report in root/reports/correlation-report.md