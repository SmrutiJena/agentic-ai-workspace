import pandas as pd
import numpy as np

dataFrame = pd.DataFrame(np.arange(0,20).reshape(4,5), 
                         columns=['Col1','Col2','Col3','Col4','Col5'], index=['Row1','Row2','Row3','Row4']) #
print(dataFrame)

dataFrame.to_csv('dataFrame.csv') # Save DataFrame to CSV
print('DataFrame saved to dataFrame.csv')
print('DataFrame loaded from dataFrame.csv:')
print("DataFrame Col1:",dataFrame['Col1']) #
print("DataFrame Row1:",dataFrame.loc['Row1'])
print("DataFrame.iloc[0]:",dataFrame.iloc[0])


print("DataFrame with Col1 > 5:")
print(dataFrame[dataFrame['Col1'] > 10]) #

print("DataFrame multiple columns:")
print(dataFrame[['Col1', 'Col2']]) #
print("DataFrame multiple rows:")
print(dataFrame.loc['Row1': 'Row2','Col1':'Col2']) #

print(type(dataFrame.loc['Row1'])) #Its a Series, because it contains a single row. Each column value becomes an element in the Series, and the column names become the index of the Series.
print(type(dataFrame.loc['Row1':'Row2'])) #Its a DataFrame, not a Series, because it contains multiple rows.


print(dataFrame.describe()) #Summary statistics of the DataFrame

print(dataFrame.values) #Returns a Numpy representation of the DataFrame, without the index and column labels.

print(dataFrame.iloc[0:2, 0:2].values) #Returns a Numpy representation of the DataFrame, without the index and column labels.

print(dataFrame.iloc[0:2, 0:2].to_numpy()) #Returns a Numpy representation of the DataFrame, without the index and column labels.

print(dataFrame.isnull()) #Returns a DataFrame of the same shape as the original, with True for each element that is null (NaN) and False for each element that is not null.

print(dataFrame[['Col1','Col2']]) #Returns the value at the intersection of Col1 and Col2

print(dataFrame['Col1'].unique()) #Returns the unique values in the specified columns. Since the values in Col1 and Col2 are all unique, it will return an array of unique values from those columns.


df = pd.read_csv('dataFrame.csv') # Load DataFrame from CSV, using the first column as the 
print('DataFrame loaded from dataFrame.csv:')
print(df)