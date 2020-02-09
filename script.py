import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
sns.set_style('darkgrid')

df = pd.read_csv('flights.csv')
msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]
df.Price.hist()
plt.show()
