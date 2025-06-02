# Loan Default Prediction Project

## Project Overview
The project is to check whether the research paer named "Research on loan default prediction based on logistic regression, randomforest, xgboost and adaboost" is reproducible. The dataset link is shown as follows: https://www.kaggle.com/datasets/laotse/credit-risk-dataset/data

This paper aims to predict loan default risks using machine learning algorithms such as Logistic Regression, Random Forest, XGBoost, and AdaBoost. The data has been cleaned, including handling missing values, removing outliers, and standardizing the data for modeling. 

## Environment Setup
1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
## Code Execution Instructions
After running the code, the cleaned dataset will be saved as `credit_risk_dataset_cleaned.csv`.

## Data Description
The dataset contains the following columns:
- `person_emp_length`: Number of years the borrower has been employed.
- `loan_int_rate`: The interest rate of the loan.
- `person_age`: Age of the borrower.
- `person_income`: The income of the borrower.
- And other related features.

The following data cleaning operations have been performed:
- Filled missing values for `person_emp_length` with the median and for `loan_int_rate` with the mean.
- Removed records where `person_age` exceeds 100 and `person_income` exceeds 500,000.
- Converted categorical features (`person_home_ownership`, `loan_intent`, `loan_grade`, `cb_person_default_on_file`) to category data type.
- Standardized numerical features (`person_income`, `loan_amnt`, `loan_int_rate`, `loan_percent_income`).

## Contribution
- **Guanhong Chen**: Data cleaning and preprocessing.
- **Piotr Lichota**: Logistic regression and RandomForest.
- **Mikołaj Sydow**: AdaBoost.
- **Yun Wu**: XGBoost.









