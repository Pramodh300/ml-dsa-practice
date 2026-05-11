import pandas as pd
data = {
    "Age" : [20,21,22,22,100],
    "Marks" : [80,85,90,22,95]
}
df = pd.DataFrame(data)

'''#Basic Information
print(df.info())


#Use describe
print(df.describe())


#Find null values
print(df.isnull().sum())
'''

#Find duplicates
print(df.duplicated().sum())