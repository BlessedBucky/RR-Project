import pandas as pd

df = pd.read_csv(r'C:\Users\Razer\Desktop\RR Project\credit_risk_dataset.csv')

print(df.isnull().sum())

df.dropna(subset=['person_emp_length', 'loan_int_rate'], inplace=True)  # 删除有缺失的行

df = df[(df['person_age'] <= 100) & (df['person_income'] <= 500000)]

df = df[df['person_emp_length'] <= df['person_age']]

df = df[df['person_age'] <= 60]

df['person_home_ownership'] = df['person_home_ownership'].astype('category')
df['loan_intent'] = df['loan_intent'].astype('category')
df['loan_grade'] = df['loan_grade'].astype('category')
df['cb_person_default_on_file'] = df['cb_person_default_on_file'].astype('category')

df['person_income'] = (df['person_income'] - df['person_income'].mean()) / df['person_income'].std()
df['loan_amnt'] = (df['loan_amnt'] - df['loan_amnt'].mean()) / df['loan_amnt'].std()
df['loan_int_rate'] = (df['loan_int_rate'] - df['loan_int_rate'].mean()) / df['loan_int_rate'].std()
df['loan_percent_income'] = (df['loan_percent_income'] - df['loan_percent_income'].mean()) / df['loan_percent_income'].std()

df.to_csv('credit_risk_dataset_cleaned.csv', index=False)

print("Data cleaning complete. Cleaned dataset saved as 'credit_risk_dataset_cleaned.csv'.")

