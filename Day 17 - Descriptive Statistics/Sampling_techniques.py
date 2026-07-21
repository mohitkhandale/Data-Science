import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Population_Survey_Data.csv')
data2 = pd.read_csv('Manufacturing_Data.csv')
print(data.head(5))
#print(data2.head(5))

# 1. Simple Random Sampling 100 records randomly
sample_data = data.sample(n=100, random_state=42) # random_sate = 42 for reproducibility in simple terms it is a seed value for random number generator
#print(sample_data.head(5))

# 2. Stratified Sampling
sample_data2 = data.groupby('Region').apply(lambda x : x.sample(min(len(x),25), random_state=42)) #.apply() method is used to apply a function along an axis of the DataFrame. In this case, we are applying a lambda function to each group of the 'Region' column. The lambda function takes each group (x) and samples a minimum of 25 records from it. If a group has fewer than 25 records, it will sample all available records from that group. This ensures that we get a representative sample from each region while maintaining a maximum of 25 records per region.
#print(sample_data2)

# 3. Cluster Sampling
clusters = data2['Batchnumber'].unique() # The line of code `clusters = data2['Batchnumber'].unique()` retrieves the unique values from the 'Batchnumber' column in the `data2` DataFrame. This is important for cluster sampling because it identifies the distinct clusters (in this case, batches) from which we can sample.
sample_data3 = np.random.choice(clusters, size = 5, replace = False) # The line of code `sample_data3 = np.random.choice(clusters, size=5, replace=False)` randomly selects 5 unique clusters (batch numbers) from the `clusters` array without replacement. This means that once a cluster is selected, it cannot be selected again. This is important for cluster sampling because we want to ensure that we are sampling distinct clusters rather than potentially selecting the same cluster multiple times.
Clustered_sample = data2[data2['Batchnumber'].isin(sample_data3)] # The line of code `Clustered_sample = data2[data2['Batchnumber'].isin(sample_data3)]` filters the `data2` DataFrame to include only the rows where the 'Batchnumber' column values are in the `sample_data3` array.
# print(Clustered_sample)

# 4. Systematic Sampling
sample_data4 = data.iloc[::10, :] # The line of code `sample_data4 = data.iloc[::10, :]` selects every 10th row from the `data` DataFrame using the `.iloc` indexer. The `::10` slicing notation means "take every 10th row," starting from the first row (index 0). This is a systematic sampling technique where we select samples at regular intervals from the population.
# print(sample_data4)

# mean, median, mode
print(data2.head(5))
#mean_value = data2['Income'].mean()
##print("Mean Income:", mean_value)
