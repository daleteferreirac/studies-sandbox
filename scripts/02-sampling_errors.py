from pathlib import Path
import pandas as pd
import numpy as np

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "WineQT.csv" # relative to repo root, works on any machine
df = pd.read_csv(DATA_PATH)

sample_50 = df.sample(50) # keeps 50 rows and the 13 columns from the csv
# 50 from 1143
data_alcohol = df["alcohol"] # Name: alcohol, Length: 1143, dtype: float64
sample_alcohol = sample_50["alcohol"]
print(np.mean(data_alcohol)) # population mean
print(np.mean(sample_alcohol)) # sample mean