import pandas as pd
import numpy as np

# Read the data
data = pd.read_excel('E:\Data Science\Phase 0 - Python\Day 12 - Pandas Contd\customers.xlsx')
print(data.head())
print(data.info())

# Add a new column as 'Country' and the value inside that is 'India' in the above DataFrame
data['Country'] = 'India'
print(data.head())

'''
# Error: ValueError: Length of values (3) does not match length of index (5)
membership_status = ['Gold', 'Silver', 'Bronze']
data['membership_status'] = membership_status
print(data.head())
'''

# Create a new column 'Full Name' Which is composed of first name and the last name
data['full_name'] = data['first_name'] + ' ' + data['last_name']
print(data.head())

# .loc() vs .iloc()
# .loc[] is label based, .iloc[] is position based
dataframe_demo = {
    'Name' : ['Mohit','Amir','Abhishek','Arjun','Ekta'],
    'Age' : [23, 24, 22, 25, 21],
    'City' : ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata']
}
dataframe_demo = pd.DataFrame(dataframe_demo, index=['a', 'b', 'c', 'd', 'e'])
print(dataframe_demo)

# .loc - label based indexing
print(dataframe_demo.loc['b'])
print(dataframe_demo.loc['b':'d'])

# .iloc - position based indexing
print(dataframe_demo.iloc[1])
print(dataframe_demo.iloc[1:4])

print("Shape:",data.shape)

# Accessing the details of the id's of the customer from 500 to 504
print(data.loc[500:504]) 
print(data.iloc[500:505])  # Note: iloc is exclusive of the last index

data.drop(columns=['Country'], inplace = True)
print(data.head())

# Rename the row index with the custom index '0' - '1st Customer', '2nd Customer', etc.
rename_dict = {
    0: '1st Customer',
    1: '2nd Customer',
    2: '3rd Customer',
    3: '4th Customer',
    4: '5th Customer'
}
data.rename(index=rename_dict, inplace=True)
print(data.head())


unique_genders = data['gender'].unique() # Get unique values
print("Unique Genders:", unique_genders)
unique_genders_count = data['gender'].nunique() # Count of unique values
print("Count of Unique Genders:", unique_genders_count)
print(data['gender'].value_counts()) # Count of each unique value

# Renamming the column of street_num with street_number
data.rename(columns={'street_num': 'street_number'}, inplace=True)
print(data.head())

data2 = pd.read_excel('E:\Data Science\Phase 0 - Python\Day 12 - Pandas Contd\purchases.xlsx')
print(data2.head())
print(data2.info())

data2.drop(columns=['Unnamed: 0'], inplace=True)  # Drop the unnamed column
print(data2.head())

# Handle the data types of the columns in an appropriate way
data2['purch_date'] = pd.to_datetime(data2['purch_date'])  # Convert to datetime
print(data2.dtypes)

data2['id'] = data2['id'].astype(object)  # Convert to object type
print(data2.dtypes)

# paid -> float 
# paid -> data preprocessing and then only we can convert it to float
data2['paid'] = data2['paid'].str.replace('[\$,]', '', regex=True)  # Remove dollar sign
data2['paid'] = data2['paid'].astype(float)  # Convert to float type
print(data2.dtypes)

data3 = pd.read_excel('E:\Data Science\Phase 0 - Python\Day 12 - Pandas Contd\products.xlsx')
data3.drop(columns=['Unnamed: 0'], inplace=True)  # Drop the unnamed column
data3['cost'] = data3['cost'].str.replace('[\$,]', '', regex=True)  # Remove dollar sign
data3['cost'] = data3['cost'].astype(float)  # Convert cost to float

data3['id'] = data3['id'].astype(object)  # Convert id to object type
print(data3.head())
print(data3.info())

# Concat - to manipulate and combiine multiple dataframes in pandas
combined_df = pd.concat([data, data2, data3], axis = 0) # Concatenate along rows axis=0 , axis=1 for columns
print(combined_df)

# Merge - to combine dataframes based on a common key
merged_df = pd.merge(data, data2, on='id', how='inner')  # Inner join on 'id'
print(merged_df.head())

merged_df_right = pd.merge(data, data2, on='id', how='right')  # right join on 'id'
print(merged_df_right.head())

merged_df_left = pd.merge(data, data2, on='id', how='left')  # left join on 'id'
print(merged_df_left.head())

data_1 =  pd.DataFrame({
    'id': [1, 2, 3, 4, 5], 
    'name': ['Mohit', 'Arjun', 'Ekta', 'David', 'Eva'],
    'product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard']
})

data_2 = pd.DataFrame({
    'id': [1, 2, 3, 6, 7], 
    'product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    'amount': [1000, 500, 300, 200, 150]
})

# Can you give me the entire information of the customers detail including the amount as well?
merge_df_full = pd.merge(data_1, data_2, on = 'id', how = 'inner', suffixes = ('_cust', '_trans'))
print(merge_df_full)

# Missing Values - Handling missing values in pandas
print(data.isnull().sum())  # Check for missing values
customers_copy = data.copy()  # Create a copy of the DataFrame
customer_copy = customers_copy.dropna()  # Drop rows with any missing values
print(customer_copy.shape)  # Check for missing values after dropping

# dropna() -> only when you have a very small proportion of the missing data. Otherwise, please avoid this strategy because that leads to the loss of information

# Data Imputation - Filling missing values, with the measure of central tendency (mean, median, mode)
mode_gender = data['gender'].mode()[0]  # Get the mode of gender
print("Mode of Gender:", mode_gender)
data['gender'].fillna(mode_gender, inplace=True)  # Fill missing values with mode
print(data.shape)

# ffillna() -> only when you have a very small proportion of the missing data. Otherwise, please avoid this strategy because that leads to the loss of information
data['street_number'].fillna(method='ffill', inplace=True)  # Forward fill missing values
data['street_name'].fillna(method='ffill', inplace=True)  # Forward fill missing values
data['street_suffix'].fillna(method='ffill', inplace=True)  # Forward fill missing values
print(data.isnull().sum())  # Check for missing values after filling
print(data.head(40))

# bfillna() -> can be used to fill missing values with the next valid observation   
data['city'].fillna(method='bfill', inplace=True)  # Backward fill missing values
data['state'].fillna(method='bfill', inplace=True)  # Backward fill missing values
data['postcode'].fillna(method='bfill', inplace=True)  # Backward fill missing values
data['email'].fillna('Unknown', inplace=True)  # Backward fill missing values
print(data.isnull().sum())  # Check for missing values after filling
print(data.head(40))

# mean() -> can be used to fill missing values with the mean of the column
# median() -> can be used to fill missing values with the median of the column

# data analysis - Grouping and aggregating data
# group by 'customer_num' and compute the sum od 'amount' and 'paid' column
aggregated_purchase = data2.groupby('customer_num').agg({'amount': 'sum', 'paid': 'sum'})
print(aggregated_purchase)