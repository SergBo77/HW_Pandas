import pandas as pd

df = pd.read_csv('kc_house_data.csv')

print(df.head())

print(df.info())

print(df.describe())

df_salary = pd.read_csv('dz.csv')

df_salary.info()

group = df_salary.groupby('City')['Salary'].mean()

print(group)

