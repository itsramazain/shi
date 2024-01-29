import pandas as pd

myfile = pd.read_csv('Salaries.csv')
print(f"number of rows:\t{myfile.shape[0]}")

print(f"number of cols:\t{myfile.shape[1]}")
print("\n\n")

result = myfile.dtypes
print("\n\n")
print("each col and its data type:")
print(result)
print("\n\n")

print("missing vlues in each col:")
df = pd.DataFrame(myfile) 
  
df.isnull() 
