import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/daleteferreira/PycharmProjects/studies-sandbox/data/WineQT.csv") # turn into dataframe

print(df.head()) # shows 5 rows pattern
print(df.columns)

data = df["alcohol"] # Name: alcohol, Length: 1143, dtype: float64
print("mean: ", np.mean(data))
print("median: ", np.median(data))
print("standard deviation: ", np.std(data))

plt.hist(data, bins=20)
plt.title("Alcohol Distribution")
plt.xlabel("Alcohol")
plt.ylabel("Frequency")

plt.show()
