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

Now for the idea that error budget/magnitude of a surrogate models each output dimension is a function of the input space. And the error margin/magnitude changes predictably with the change of the input design point with respect to the design space including all the input dimensions across all ranges of these variables. Now to test that out we first make a vanilla neural network to predict FEA simulation outputs form the parametric inputs which are geometric parameters. Then we train it to predict the output or target set. And we keep the epochs very low, intentionally so there is some amount of error in the primary neural network model so once we train the error mapper model on these data, we can see the difference and range of error the secondary model can predict with some level of precision to differentiate. And then we use the primary model to predict targets from the error_df.csv set of data. This created the training data for error mapper neural network. After training we run The primary model frezzed on the held out test set data and get predictions and compute error quantity for each output dimension. Then use run the Error Mapper model on the held out test set to predict errors per output dimention without shuffling. Then we compute Pearson and Spearman Correlation for finding the linear and rank correlation between the predicted and absolute error. And The results Are here.

| Ouput Dimension | Pearson Correlation | Spearman Correlation |
|---|---|---|
| max stress von mises error | 0.89 | 0.88 |
| max deformation error | 0.53 | 0.41 |
| mode 1 frequency error | 0.97 | 0.90 |
| mode 2 frequency error | 0.99 | 0.92 |
| mode 3 frequency error | 0.95 | 0.94 |
| mode 4 frequency error | 0.97 | 0.95 |


## Mappings
### Cloning
```bash
git clone https://github.com/Aniruddh5502/assisted-nn-error-mapping.git
cd assisted-nn-error-mapping
```
### Installing prerequisites
```bash
pip install -r requirements.txt
```
### Test Commands
1. To Run the simulation pipelines
```bash
python -m src.main
```


### Files and Folders
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