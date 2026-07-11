from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "WineQT.csv" # relative to repo root, works on any machine
df = pd.read_csv(DATA_PATH) # turn into dataframe

print(df.head()) # shows 5 rows (pattern)
print(df.columns) # shows index of columns

# select data, starting with one: alcohol
data = df["alcohol"] # Name: alcohol, Length: 1143, dtype: float64
acidity = df["fixed acidity"]


print("mean: ", np.mean(data))
print("median: ", np.median(data))
print("standard deviation: ", np.std(data))

# histogram
plt.figure()
plt.hist(data, bins=20) # bins = groups histogram
plt.title("Alcohol Distribution")
plt.xlabel("Alcohol")
plt.ylabel("Frequency")
#plt.show()

# box plot
plt.figure()
plt.boxplot(data)
plt.title("alcohol distribution")
#plt.show()

plt.figure()
plt.boxplot([data, acidity])
plt.xticks([1, 2], ["alcohol", "acidity"]) # replace numeric x-axis positions with variable names
plt.title("Variable comparison")
plt.ylabel("values")
plt.show()

print(df["alcohol"].describe())
print(df["fixed acidity"].describe())