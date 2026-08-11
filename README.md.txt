# NextGenLearners Data Science Internship - Capstone

## Project Title
Predicting Internship Selection Outcomes

## Objective
This project combines data cleaning, exploratory data analysis, SQL 
querying, and a first introduction to machine learning to predict whether 
an applicant is likely to be selected for the NextGenLearners internship 
program, based on their application data.

## Dataset Description
The dataset is based on the cleaned applicant dataset from Week 1, extended 
with 4 additional features for this exercise: number of skills listed, 
whether the applicant provided a portfolio, prior hackathon participation, 
and a statement quality score. **Note: these 4 features are simulated, not 
real historical data**, since this information was not originally collected 
in the applications.

## Method
1. Cleaned and explored the raw applicant dataset (Weeks 1-2)
2. Queried and aggregated program data using SQL (Week 3)
3. Extended the dataset with simulated features
4. Converted categorical data (Yes/No fields, Domain) into numeric format
5. Split data into training (80%) and test (20%) sets
6. Trained a Logistic Regression model to predict selection outcomes
7. Evaluated the model using accuracy, precision, recall, and a confusion 
   matrix
8. Interpreted which features most influenced the model's predictions

## Key Results
- Accuracy: 54.55%
- Precision: 50.00%
- Recall: 100.00%
- The model caught all actually-selected applicants but also incorrectly 
  flagged several non-selected applicants as likely to be selected — 
  results should be treated as illustrative given the small dataset size 
  (52 applicants).
- Prior hackathon participation was the strongest positive predictor in 
  this dataset.

## How to Run
1. Open `Week4_Capstone_Shakti.ipynb` in Google Colab
2. Upload `applicants_cleaned.csv` when prompted
3. Go to Runtime → Run All to execute the full notebook top to bottom

## Walkthrough Video
[PASTE YOUR VIDEO LINK HERE]