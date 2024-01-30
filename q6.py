import pandas as pd
myfile = pd.read_csv('Salaries.csv')

corr_matrix=myfile.corr()
#salary with the other pay
corr_matrix['TotalPay'].corr(corr_matrix['OtherPay'])

print(corr_matrix)
