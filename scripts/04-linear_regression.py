from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "WineQT.csv" # relative to repo root, works on any machine

df = pd.read_csv(DATA_PATH)

m, b = np.polyfit(df["alcohol"], df["quality"], 1) # fit a polynomial (1)
print("slope (m):", m) # inclinação
print("intercept (b):", b) # intercepto

plt.figure()
plt.scatter(df["alcohol"], df["quality"], alpha=0.3)
x_line = np.linspace(df["alcohol"].min(), df["alcohol"].max(), 100)
y_line = m * x_line + b
plt.plot(x_line, y_line, color="red")
plt.xlabel("alcohol")
plt.ylabel("quality")
plt.title("alcohol vs quality with fitted line")
plt.show()