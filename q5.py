import pandas as pd
import matplotlib
myfile = pd.read_csv('Salaries.csv')

df=myfile.groupby("Id")['TotalPay'].mean()

print(df)

