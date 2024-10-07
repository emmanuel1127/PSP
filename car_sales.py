#Importing Libraries 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Loading Dataset
df = pd.read_csv('Car_sales.csv')

#Exploring Dataset
print(df.head())

#To find number of rows and columns
No_of_rows = len(df.index)
No_of_columns = len(df.columns)

#Output
print(f'No_of_rows:{No_of_rows}')
print(f'No_of_columns:{No_of_columns}')

#Identifying data types of each columns.
df.dtypes
print(df.dtypes)

#To ascribe datatype to a column
#df['Column'] = df['Column'].astype(int,float, object...) or
#df = df.astype({'column_name':int, 'column_name1':float})
#Column meaning name of designated/desired columns

#Finding and replacing missing dataset
#Finding and printing out result
df.isna().sum()
print(df.isna().sum())
#Replacing missing dataset with their averages.
#Finding average of the dataset in entire column
avg1 = df['__year_resale_value'].mean()
#Replacing missing items in column by the column's average
df['__year_resale_value'] = df['__year_resale_value'].fillna(df['__year_resale_value'].mean())
#printing out entire dataset to see difference with column __year_resale_value
df.isna().sum()
print(df.isna().sum())

#To drop rows with missing datasets
df.dropna(inplace=True)
print(df.isna().sum())

#To rename column
df.rename(columns={'__year_resale_value':'year_resale_value'}, inplace=True)
df.head()
print(df.head())

#Descriptive Analysis
df.describe()
print(df.describe())

#Checking for duplicates
df.duplicated()
print(df.duplicated())
#To see numerical information of duplicates
df.duplicated().sum()
print(df.duplicated().sum())

#To ascribe datatype
df = df.astype({'Sales_in_thousands': int})

#SPECIFIC ANALYSIS
#HIghest average sales volume
Highest = df.groupby('Manufacturer')['Sales_in_thousands'].mean().sort_values(ascending=False)
print(Highest)
