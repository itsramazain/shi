import pandas as pd

myfile1 = pd.read_csv('Salaries.csv')
myfile=pd.DataFrame(myfile1)
## get rid of dups

myfile.drop_duplicates(inplace=True)

##remove col i dont need
myfile.drop(columns=['Benefits','Notes','Status'],inplace=True)

##split the JobTitle into 2 col job/dep in the '('
myfile[['job', 'department']] = myfile['JobTitle'].str.split('(',n=1, expand=True)

##remove the 0 at the end
myfile['department']=myfile['department'].str.rstrip(")")
print(myfile)
