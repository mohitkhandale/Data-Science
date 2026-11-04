import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data =  pd.read_excel('fraud_data.xlsx')
#print(data.head())

#Population mean
population_mean = data['amt'].mean()
print("Population Mean:", population_mean)

#Sample mean 
sample_mean = data['amt'].sample(n=1000, random_state=42).mean()
print("Sample Mean:", sample_mean)
"""
 Impact of sample size on sample mean: As the sample size increases, the sample mean tends to get closer to the population mean. 
 This is a demonstration of the Central Limit Theorem (CLT), which states that the distribution of sample means 
 will be approximately normally distributed, regardless of the shape of the population distribution, as long as the sample size is sufficiently large.
"""
sample_size = [10, 50, 100, 500, 1000, 5000, 7000]
sample_means = [data['amt'].sample(n=size, random_state=42).mean() for size in sample_size]
for size, mean in zip(sample_size, sample_means): #zip() combines two lists
    print(f"Sample Size: {size}, Sample Mean: {mean}") 

# Function Definition
def visualize_clt(data, sample_size, num_samples):
    sample_means = [np.mean(np.random.choice(data, size=sample_size))for _ in range(num_samples)] #Explaination of this line: np.random.choice(data, size=sample_size) randomly selects 'sample_size' number of elements from 'data', and np.mean() calculates the mean of those selected elements. This process is repeated 'num_samples' times to generate a list of sample means.
    sns.histplot(sample_means,bins = 30, kde=True)
    plt.title(f'Central Limit Theorem: Sample Size = {sample_size}, Number of Samples = {num_samples}')
    plt.xlabel('Sample Mean')
    plt.ylabel('Frequency')
    plt.show()

# Fuction calling
visualize_clt(data['amt'], 30, 1000)
visualize_clt(data['amt'], 50, 1000)
visualize_clt(data['amt'], 100, 1000)
visualize_clt(data['amt'], 200, 1000)
visualize_clt(data['amt'], 500, 1000)

'''
Difference between sample mean and sampling distribution mean
sample mean: The mean of a single sample
sampling distribution mean: The mean of all the possible sample means which approximates the population mean 
'''

population_std = data['amt'].std()
sample_sizes = [10, 50, 100, 500, 1000]
standard_errors = [population_std / np.sqrt(sample_size) for sample_size in sample_sizes] # standard_error = population_std / sqrt(sample_size) means 
plt.figure(figsize=(10, 6))
plt.plot(sample_sizes, standard_errors, marker='o', linestyle='--', color='b')
plt.xlabel('Sample Size')
plt.ylabel('Standard Error')
plt.title('Standard Error vs. Sample Size')
plt.show()