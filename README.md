# Loan Default Prediction Project

## Project Overview
The project is to check whether the research paer named "Research on loan default prediction based on logistic regression, randomforest, xgboost and adaboost" is reproducible. This paper aims to predict loan default risks using machine learning algorithms such as Logistic Regression, Random Forest, XGBoost, and AdaBoost. The dataset link is shown as follows: https://www.kaggle.com/datasets/laotse/credit-risk-dataset/data


## Environment Setup
1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
Code Execution Instructions
After running the project.py file, the cleaned dataset will be saved as credit_risk_dataset_cleaned.csv.

The code performs data cleaning and preprocessing as follows:

Missing values for person_emp_length are filled with the median.

Missing values for loan_int_rate are filled with the mean.

Records where person_age exceeds 100 or person_income exceeds 500,000 are removed.

Data entries where the person_emp_length is greater than person_age or where the person_age is greater than 60 are also removed.

Categorical features (person_home_ownership, loan_intent, loan_grade, cb_person_default_on_file) are converted to category data type.

Numerical features (person_income, loan_amnt, loan_int_rate, loan_percent_income) are standardized (z-score normalization).

Data Description
The dataset contains the following columns:

person_emp_length: Number of years the borrower has been employed.

loan_int_rate: The interest rate of the loan.

person_age: Age of the borrower.

person_income: The income of the borrower.

person_home_ownership: Home ownership status (categorical).

loan_intent: Purpose of the loan (categorical).

loan_grade: Loan grade (categorical).

cb_person_default_on_file: Indicates if the person has a default record on file (categorical).

loan_amnt: Amount of the loan.

loan_percent_income: Percentage of income taken by the loan.

Data Cleaning Operations
The following data cleaning operations have been performed:

Missing values handling:

person_emp_length: Filled with the median value.

loan_int_rate: Filled with the mean value.

Outlier handling:

Removed records where person_age exceeds 100 or person_income exceeds 500,000.

Removed records where person_emp_length is greater than person_age.

Removed records where person_age is greater than 60.

Categorical data transformation:

Converted categorical features (person_home_ownership, loan_intent, loan_grade, cb_person_default_on_file) to category data type.

Feature standardization:

Standardized numerical features (person_income, loan_amnt, loan_int_rate, loan_percent_income) using z-score normalization.

Contribution
Guanhong Chen: Data cleaning and preprocessing.

Piotr Lichota: Logistic regression and RandomForest.

Mikołaj Sydow: AdaBoost.

Yun Wu: XGBoost.








