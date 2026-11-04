import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

np.random.seed(42)
## Right skewed distribution
income_distribution = np.random.gamma(shape=2.0, scale=1000, size=1000) # Gamma distribution with shape parameter 2.0 and scale parameter 1000 and size 1000 means generating 1000 random samples from a gamma distribution with the specified shape and scale parameters.

## Calculate skewness
skew_value = skew(income_distribution)

sns.histplot(income_distribution, bins=30, kde=True) #Explain parameters of histplot income_distribution means the data to be plotted, bins=30 means the number of bins to be used in the histogram, kde=True means to plot the kernel density estimate on top of the histogram.
plt.title(f'Income Distribution (Skewness : {skew_value:.2f})')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.show()

# kutosis: measure of the "tailedness" of the probability distribution of a real-valued random variable. It is a descriptor of the shape of the distribution and can provide insights into the presence of outliers or extreme values in the data.
data = pd.read_csv('process_engineering_   data.csv')

# Calculate the range of the temperature column in the above data
temp_range = data['temperature'].max() - data['temperature'].min()
print(f'Temperature Range: {temp_range}')

# Calculate the interquartile range (IQR) of the temperature column
Q1 = data['temperature'].quantile(0.25)
Q3 = data['temperature'].quantile(0.75)
IQR = Q3 - Q1
print(f'Inter Quartile Range: {IQR}')

# Calculate the variance of the pressure column
pressure_variance = data['pressure'].var()
print(f'Pressure Variance: {pressure_variance}')

# Calculate the Standard Deviation of the Pressure column
pressure_std = data['pressure'].std()
print(f'Pressure Standard Deviation: {pressure_std}')

