import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data Creation of the Nominal Data Column named 'Colors'
np.random.seed(0) #For reproducibility
num_samples = 1000 # Number of samples
colors = ['red', 'blue', 'green', 'yellow', 'crimson', 'purple'] # Nominal categories
nominal_data = np.random.choice(colors, num_samples)   # Generating nominal data
print(nominal_data)
dataframes = pd.DataFrame(nominal_data, columns = ['Colors']) # Creating DataFrame
print(dataframes)

# Data Creation of the Ordinal Data Column named 'Satisfaction_levels'
satisfaction_levels = ['Low', 'Medium', 'High'] # Ordinal categories
ordinal_data = np.random.choice(satisfaction_levels, num_samples) # Generating ordinal data
print(ordinal_data)
dataframes['Satisfaction_levels'] = ordinal_data # Adding to DataFrame
print(dataframes)

# Data Creation of the interval data under temperature column
interval_data = np.random.randint(0,100, num_samples) # Generating interval data
dataframes['Temperature'] = interval_data # Adding to DataFrame
print(dataframes)

# Data Creation of the range data under the income Column
income_data = np.random.randint(20000,1000000  , num_samples) # Generating ratio data
dataframes['Income'] = income_data # Adding to DataFrame
print(dataframes)

#Save DataFrame to CSV
dataframes.to_csv('types_of_data.csv') 

# Plot Ratio Data
plt.hist(dataframes['Income'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Income Distribution')
plt.xlabel('Income(Rupees)')
plt.ylabel('Frequency')
plt.savefig('income_distribution.png')
plt.show()

