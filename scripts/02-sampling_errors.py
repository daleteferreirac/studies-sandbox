import pandas as pd
import numpy as np

df = pd.read_csv("/Users/daleteferreira/PycharmProjects/studies-sandbox/data/WineQT.csv")

sample_50 = df.sample(50) # keeps 50 rows and the 13 columns from the csv
# 50 from 1143
data_alcohol = df["alcohol"] # Name: alcohol, Length: 1143, dtype: float64
sample_alcohol = sample_50["alcohol"]
print(np.mean(data_alcohol)) # population mean
print(np.mean(sample_alcohol)) # sample mean