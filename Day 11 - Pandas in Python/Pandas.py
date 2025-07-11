# Pandas - Use for Data Manipulation and Analysis
# Handles large datasets efficiently (Json, CSV, Excel, etc.)
# Memory efficient

import pandas as pd

# Read the data
data = pd.read_csv('E:\\Data Science\\Phase 0 - Python\\Day 11 - Pandas in Python\\dataset.csv')
print(data)
print(data.head())  # Display the first 5 rows
print(data.head(15))  # Display the first 15 rows
print(data.tail())  # Display the last 5 rows
print(data.tail(15))  # Display the last 15 rows
print(type(data))  # Display the type of the data - DataFrame

# Data Structure - way to Structure/Organize Data in a structured/efficient manner
# Types of Data Structures
# Linear - Arrays, Lists, Stacks, Queues
# Non-Linear - Trees, Graphs,  Hash Tables

# In Pandas ther are two main data structures:
# 1. DataFrames - rows and columns (like a table) structure format
# 2. Series - one-dimensional array-like structure (like a list) format 

# Series - one-dimensional array-like structure in Pandas that can hold a sequence of value of any data type
# Each value in a series is linked with a associated label, Known as index. You can also Customize the index labels in series.
# Creating a Series from scalar value with the custom index 
series_scalar = pd.Series(10, index=['a','b','c','d','e','f']) # Scalar value
print(series_scalar)
print(series_scalar['e']) # Accessing value using index label

data = [10, 20, 30, 40, 50, 60]
series_list = pd.Series(data)
print(series_list)
print(series_list[3])  # Accessing value using index position

# Slicing in Series
print(series_list[2:5])  # Slicing from index 2 to 4 (5 is exclusive)
print(series_scalar['c':'f'])  # Slicing from index 'c' to 'f' (f is inclusive)

# Attributes in Series
data1 = ['New Dehli','Washington','London','Paris']
index = ['India','USA','UK','France']
series_capital = pd.Series(data1, index=index)
print(series_capital)
print("Index of the series_capital country:\n ", series_capital.index) # Accessing index labels
print("Values of the series_capital country:\n ", series_capital.values) # Accessing values
print("Data type of the series_capital country:\n ", series_capital.dtype) # Accessing data type - object

# dtype - Data type of the each values in that type of data structure
# type - Type of the data structure

print("Shape of the series_capital country:\n ", series_capital.shape)  # Accessing shape - (number of rows, number of columns )
print("Size of the series_capital country:\n ", series_capital.size)  # Accessing size - number of elements in the series
print("is the series_capital country empty?:\n ", series_capital.empty)  # Checking if the series is empty
print("is nan value present in the series_capital country?:\n ", series_capital.isna())  # Checking if there is any NaN value in the series isna()/hasna
print("is null value present in the series_capital country?:\n ", series_capital.isnull())  # Checking if there is any null value in the series isnull()/hasnull
print("is the series_capital country unique?:\n ", series_capital.is_unique)  # Checking if the series is unique
print("Dimensions of the series_capital country:\n ", series_capital.ndim)  # Accessing dimensions - 1D for Series

# Methods in Series Data Structure
data_marks = [85, 60, 70, 88, 91]
data_students = ['Mohit', 'Aman', 'Rohit', 'Sahil', 'Ankit']

series_student = pd.Series(data_marks, index=data_students)
print("Series of Students and their Marks:\n", series_student)
print("Description of the series_student:\n", series_student.describe())  # Descriptive statistics of the series
print("value counts of the series_student:\n", series_student.value_counts())  # Count of unique values in the series
print("Sorting the series_student in ascending order:\n", series_student.sort_values())  # Sorting the series in ascending order
print("Sorting the series_student in descending order:\n", series_student.sort_values(ascending=False))  # Sorting the series in descending order
print("droping the series_student with index 'Rohit':\n", series_student.drop('Rohit'))  # Dropping a value from the series
print("drop inplace the series_student with index 'Rohit':\n", series_student.drop('Rohit', inplace=True))  # Dropping a value from the series in place in the original series
print("Series after dropping 'Rohit':\n", series_student)  # Displaying the series after dropping 'Rohit'
print("isnull.sum() of the series_student:\n", series_student.isnull().sum())  # Counting the number of null values in the series