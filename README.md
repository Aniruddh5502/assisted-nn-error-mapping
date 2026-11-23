---
Topic: Research on making higher correlation error/variance prediction system for better Absolute Error prediction.
Description: In this research I am working with finding uncertainity prediciton methods that has better correlation with absolute error and can give a better estimate of the Actual Error in the prediction of a Surrogate model specially in SDOF Compliant Mechanicsms in Macro Scale dataset from FEA as a regression problem.
Date: 11/11/2026
Draft: true
---
# Can I trust the UQ of Surrogate?

## 1. The Question
As we have UQ for Surrogate mdoels in various cases, here I am concerned about the regression type problems with FEA simulations. Every UQ estimation we do is either from Epistemic Uncertainity quantification or Analyzing the training data to estimate the alhetoric uncertainity in the data. But the problem with them is they are propabilistic in nature, and are statistical measures. And a probability means nothing in real life, if we are not going to use it in context of the Law Of the Large Number. But a the question I want to ask if a error in any dimension of the prediction from the surrogate model if its Uncertain or NOT. And here I have a Hypothesis that the error quantity of the model is not random/probabilistic in nature, it is input space dependent. And the error quantity in each output dimension of a surrogate model is some function of the input space, given that we have a smooth enough response manifold. And that this manifold of response error for each output dimension can be learned as an objective.

## Architecture Choice
First we tested some fancy architectures to see if they hold up with the expectations. I tested Ensemble Surrogates, SNGP on multi output regression type problem where we use FEA data from a SDOF compliant mechanicsms Static Structural and Modal Analysis information. And from the results we have seen that there is minimal relation/correlation between the error prediction from member varaince in Ensemble and GP prediction from SNGP that doesn't strongly relate the error prediction with absolute error. Both of those test cases had $<0.5$ in both absolute Spearman and Pearson Correlation.

Now I am testing vanilla NN on this 1200+ datapoint training data from FEA simulations to train a Vanilla NN to predict its outputs, and then we shall see the error measurements after we test it with the test set and try to see the pattern in which the error varies.

Then we take another unseen portion of the dataset from the same experiment and compute the error on those datapoints. Then use that map of error behaviour of that model train a new model for only error prediction. Once this error prediction model is accurate enough that we can have a correlation $>0.5$ then we can say we have a good predictor which will be tested with the held out test set obviously.

So total dataset division will be training set, error map generation set, test set. I think these 3 sets will be enough. 


## Mappings

```text 
root
    ├─── config/             # Configuration settings
    ├─── data/               # All the datasets and Ansys Simulation files
    ├─── plots/              # plots from experiments
    ├─── scaler/             # Dataset Scaling data
    ├─── scripts/            # All scripts includes Ansys, simulations etc
    ├─── src/                # Constains core coders, scripts to run the pipeline
    ├─── tests/              # Ansys, Sim, Loop, etc tests
    |       ├─── ensemble_test/
    |       ├─── sn_ablation_study/
    |       └─── aw_arch/
    ├─── writings/           # writing the papers and its drafts, nots etc
    ├─── .gitignore          # git settings
    ├─── README.md           # This file.
    └─── requirements.txt    # Requirements or dependencies to run the experiments in pyhton
``` 

## Running

### Running Simulation Pipeline

### Model Training and Post Steps

### Conclusion