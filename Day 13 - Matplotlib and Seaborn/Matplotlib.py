from cProfile import label
from sqlite3 import Time
from statistics import correlation
import time
from tkinter import font
from turtle import color
from matplotlib import markers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyparsing import col
import seaborn as sns 

# Matplotlip
# Read the data
data_customer = pd.read_excel('E:\Data Science\Phase 0 - Python\Day 13 - Matplotlib and Seaborn\customer_data.xlsx')
data_product = pd.read_excel('E:\Data Science\Phase 0 - Python\Day 13 - Matplotlib and Seaborn\product_data.xlsx')
data_purchase = pd.read_excel('E:\Data Science\Phase 0 - Python\Day 13 - Matplotlib and Seaborn\purchase_data.xlsx')

print(data_product.shape)
print(data_customer.shape)
print(data_purchase.shape)

print(data_customer.isnull().sum())
print(data_product.isnull().sum())
print(data_purchase.isnull().sum())

data_customer.drop(columns=['Unnamed: 0'], inplace=True)
print(data_customer.head(5))
data_purchase.drop(columns=['Unnamed: 0'], inplace=True)
print(data_purchase.head(5))
data_product.drop(columns=['Unnamed: 0'], inplace=True)
print(data_product.head(5))

print(data_customer.dtypes)
print(data_product.dtypes)
print(data_purchase.dtypes)

data_customer['id'] = data_customer['id'].astype(object)
data_product['id'] = data_product['id'].astype(object)
data_purchase['id'] = data_purchase['id'].astype(object)
data_customer['street_num'] = data_customer['street_num'].astype(object)
data_customer['postcode'] = data_customer['postcode'].astype(object)

# Average Cost Per Company
avg_cost = data_product.groupby('company')['cost'].mean().reset_index() #reset_index() to convert the Series to DataFrame
print("Average Cost Per Company:\n", avg_cost)

# Create a bar plot where x-axis is company and y-axis is average cost
plt.figure(figsize=(18,12))
plt.bar(avg_cost['company'], avg_cost['cost'], color='skyblue')
plt.title('Average Cost Per Company',fontsize=20)
plt.xlabel('Company', fontsize=15)
plt.ylabel('Average Cost', fontsize=15)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', linewidth=0.9, color='gray')
plt.savefig('average_cost_per_company.png')
plt.show()

# Bar plot -> x-axis(categorical data), Comparison
# Box Plot -> Outliers(Extreme Values in a Given dataset)

plt.figure(figsize=(8,6))
plt.boxplot(data_product['cost'])
plt.title("Box Plot of cost of the product",fontsize = 16)
plt.savefig('boxplot_cost_product.png')
plt.ylabel('Cost of the Product')
plt.show()

# Create a box plot of the paid column in the data_purchases dataframe
plt.figure(figsize=(18,12))
plt.boxplot(data_purchase['paid'])
plt.title("Box Plot of Product Purchase Amount is Paid",fontsize = 16)
plt.ylabel('Amount Paid')
plt.savefig('boxplot_paid_purchases.png')
plt.show()

# Gender Distribution: Pie chart
gender_count = data_customer['gender'].value_counts()
print(gender_count)

plt.figure(figsize=(4,4))
plt.pie(gender_count, autopct='%1.1f%%', labels=gender_count.index)
plt.title('Gender Distribution of Customer')
plt.savefig('piechart_gender_distribution.png')
plt.show()

# Task 
# Visualize the customer spending patterns over time on a montly basis using a line plot 
data_purchase['purch_date'] = pd.to_datetime(data_purchase['purch_date'])
monthly_spending = data_purchase.groupby(data_purchase['purch_date'].dt.to_period('M'))['paid'].sum().reset_index()
monthly_spending['purch_date']= monthly_spending['purch_date'].dt.to_timestamp()
plt.figure(figsize=(12,6))
plt.plot(monthly_spending['purch_date'],monthly_spending['paid'], marker='o')
plt.title('Customer Spending Patterns Over Time (Monthly)', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Amount Paid', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_customer_spending.png')
plt.show()

# Seaborn: Simply build on top of matplotlib only
tips = sns.load_dataset('tips')
print(tips)

# Total tips per day
sns.barplot(x='day', y='tip', data=tips, estimator=sum)
plt.title('Totsl Tips by Day')
plt.xlabel('Day')
plt.ylabel('Total tips')
plt.savefig('total_tips_by_day.png')
plt.show()

# KDE Plots: Visulize the probability density function of any given variable
sns.kdeplot(data=tips, x='total_bill', hue='time', fill=True)
plt.title("KDE Plot of the total bill")
plt.xlabel('Total Bill')
plt.savefig('KDE_Plot_of_Total_Bill.png')
plt.show()

sns.boxplot(x='day', y='tip', data=tips)
plt.title('Ditribution of tips per day')
plt.xlabel('Day')
plt.ylabel('Tips')
plt.savefig('Boxplot_Distribution_of_tips_per_day.png')
plt.show()

# Violinplot
sns.violinplot(x='day', y='tip', data=tips)
plt.title('Ditribution of tips per day')
plt.xlabel('Day')
plt.ylabel('Tips')
plt.savefig('Violinplot_Distribution_of_tips_per_day.png')
plt.show()

# Pairplot
sns.pairplot(data=tips)
plt.savefig('Pairplot.png')
plt.show()

# Regression Plot
sns.regplot(x='total_bill', y='tip', data=tips)
plt.savefig('Regresion_plot.png')
plt.show()

#Scatter Plot
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.savefig('scatter_plot.png')
plt.show()

# catplot
sns.catplot(x='smoker', y='tip', data=tips)
plt.savefig('catplot.png')
plt.show()

# Correlation Coefficient
numeric_tips = tips.select_dtypes(include='number')
correlation_cofficient = numeric_tips.corr()
print(correlation_cofficient)

sns.heatmap(correlation_cofficient, annot=True)
plt.title('Correlation Coefficient')
plt.savefig('heatmap_correlation_cofficiant.png')
plt.show()