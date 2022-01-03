## House prices prediction 

This modelling is adapted from the Kaggle house prediction challenge.  it is a simple machine learning made for deployment.

## Setup

```bash
#  To run your local deployment
python run.py

# then open page http://localhost:8000/docs#/default/predict_predict_post to see your deployement
```

## Dataset

Dataset is consisting of one csv file, and model used was light gradient boosting, with Pycaret platform.

## using website

Enter the input of the house to get the predicted price of your house


## Reproducibility

The entire model should be completely reproducible - to score this the teacher will clone your repository and follow the instructions as per the readme.  All teams start out with a score of 10.  One point is deducted for each step not included in the repo.

## Advice

Commit early and often

Notebooks don't merge easily!

Visualize early

Look at the predictions your model is getting wrong - can you engineer a feature for those samples?

Models
- baseline (average sales per store from in training data)
- random forest
- XGBoost

Use your DSR instructor(s)
- you are not alone - they are here to help with both bugs and data science advice
- git issues, structuring the data on disk, models to try, notebook problems and conda problems are all things we have seen before
