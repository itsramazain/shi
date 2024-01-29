
import pandas as pd

def _range(series):
 return series.max() -series.min()

myfile = pd.read_csv('Salaries.csv')
df = pd.DataFrame(myfile)

df2 = df[['BasePay', 'OvertimePay','OtherPay','TotalPay','TotalPayBenefits']].copy()

print("the mean for each col:")
print(df2.mean(axis='index'))
print("\n")

print("the meadian for each col:")
print(df2.median(axis=0))
print("\n")

print("the mode for each col:")
print(df2.mode())
print("\n")

print("the max for each col:")
print(df2.max())
print("\n")
print("the min for each col:")
print(df2.min())
print("\n")

print("the range for each col:")
print(_range(df2))
print("\n")

print("the standard diavtion for each col:")
print(df2.std())
print("\n")


