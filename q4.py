import pandas as pd
import matplotlib
myfile = pd.read_csv('Salaries.csv')
import numpy as np

myfile.hist(column="TotalPay")
myfile.plot.bar(column="BasePay")

POLICEsum=0
FIREsum=0
for x in myfile.index:
   if myfile.loc[x,"department"]=='POLICE DEPARTMENT':
      POLICEsum+=myfile[x]['TotalPay']

for x in myfile.index:
   if myfile.loc[x,"department"]=='FIRE DEPARTMENT':
      FIREsum+=myfile[x]['TotalPay']

myfile.groupby(['EmployeeName']).sum().plot(kind='pie', y='TotalPay')


