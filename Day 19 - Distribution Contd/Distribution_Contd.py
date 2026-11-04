import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)

#Standard Normal Distribution (SNF)
portfolio_returns = np.random.normal(loc = 0, scale = 1, size = 1000) # mean = 0, std = 1 

#Adding the extreme values
portfolio_returns = np.random.normal(loc = 0, scale = 50, size = 50)

#Calculate the kurtosis
from scipy.stats import kurtosis
kurt = kurtosis(portfolio_returns)
print(f"Kurtosis: {kurt:.2f}")
sns.histplot(portfolio_returns, kde = True, color = 'blue', bins = 30)
plt.title(f'Portfolio Returns Distribution (Kurtosis: {kurt:.2f})')
plt.xlabel('Returns')
plt.ylabel('Frequency')
plt.show()