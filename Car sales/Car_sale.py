#Import all necessary libraries such as numpy, panda, and matplotlib.
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#Importing the data set to be analyzed.
file_path = r"C:\Users\EMMANUEL FAGBEMI\Desktop\PSP ANALYTICS\My Assessment\PSP\Car sales\Car_sales.csv"
df = pd.read_csv(file_path)
#Using pd.read_csv because raw file is a csv file.

print(df)

#Exploratory Analysis
# 1. No. of rows and columns in the dataset

rows_count = df.shape[0]
print(f"Number of rows: {(rows_count)}")

col_count = df.shape[1]
print(f"Number of columns: {(col_count)}")

#2. Data types of each column
print(df.dtypes)

# 3. Filling missing or null values

# a. counting the number of missing values
print(df.isna().sum())

# b. Filling the missing values in the year_resale_value
average_ysv = df['__year_resale_value'].mean()

print(average_ysv)

df['__year_resale_value'] = df['__year_resale_value'].fillna(df['__year_resale_value'].mean())


print(df)

#To drop null/missing values
df.dropna(inplace=True)

#4. Cleaning the the __year_resale_value column name
df.rename(columns={'__year_resale_value':'Year resale value'}, inplace=True)

print(df)

#4b. Descriptive statistics of the numerical columns
print(df.describe())

#Checking for duplicates
df.duplicated()
print(df.duplicated())


#Specific Analysis
# #5. Manufacturer with the highest and lowest average sales volume
#a. Highest
print(df.groupby('Manufacturer')['Sales_in_thousands'].mean().sort_values(ascending=False))


#b. Smallest
print(df.groupby('Manufacturer')['Sales_in_thousands'].mean().sort_values(ascending=True))

#distribution of car prices in the dataset
pivot1 = df.pivot_table(index='Manufacturer', values='Price_in_thousands', aggfunc='sum')
pivot1

pivot1.plot(kind='bar', figsize=(10, 5))
plt.xlabel('Manufacturer')
plt.ylabel('Sum of prices')
plt.title('Distribution of Car Prices')
plt.show()

#8. Correlation matrix of numerical variables in the dataset
data_correlation = df.corr(numeric_only=True)
print(data_correlation)


#Plotting the correlation
plt.figure(figsize=(10, 8))
plt.heatmap(data_correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

#Grouping cars by manufacturers and analyze their average price and fuel  efficiency
Car_analysis = df.groupby('Manufacturer',as_index=False).agg({'Price_in_thousands':'mean','Fuel_efficiency':'count'})



