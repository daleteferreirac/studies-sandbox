from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "WineQT.csv" # relative to repo root, works on any machine

df = pd.read_csv(DATA_PATH)

# 1. look at the shape of the relationship BEFORE trusting any coefficient
# (see Anscombe's quartet)
plt.figure()
plt.scatter(df["alcohol"], df["quality"], alpha=0.3)
plt.xlabel("alcohol")
plt.ylabel("quality")
plt.title("alcohol vs quality")
#plt.show()

plt.figure()
plt.scatter(df["fixed acidity"], df["quality"], alpha=0.3)
plt.xlabel("fixed acidity")
plt.ylabel("quality")
plt.title("fixed acidity vs quality")
#plt.show()

# 2. Pearson — measures LINEAR relationship, -1 to +1
# use it when the scatter plot looks roughly like a straight line
pearson_alcohol = df["alcohol"].corr(df["quality"])
pearson_acidity = df["fixed acidity"].corr(df["quality"])
print("pearson alcohol x quality:", pearson_alcohol)
print("pearson fixed acidity x quality:", pearson_acidity)

# 3. Spearman — measures MONOTONIC relationship (always rising/falling,
# doesn't need to be a straight line), based on ranking instead of raw values
# use it when the scatter looks curved but still consistently trending,
# or when there are outliers skewing Pearson
spearman_alcohol = df["alcohol"].corr(df["quality"], method="spearman")
spearman_acidity = df["fixed acidity"].corr(df["quality"], method="spearman")
print("spearman alcohol x quality:", spearman_alcohol)
print("spearman fixed acidity x quality:", spearman_acidity)
# if pearson and spearman are close, the relationship is close to linear
# if spearman is clearly bigger, there's a monotonic relationship that
# the straight-line assumption of pearson is missing

# 4. full correlation matrix — same pairwise pearson calculation,
# just repeated for every pair of numeric columns at once
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)

plt.figure()
plt.imshow(corr_matrix, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar(label="correlation")
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.title("correlation matrix")
plt.tight_layout()
plt.show()

# 5. reminder: correlation != causation.
# e.g. alcohol and quality being correlated doesn't mean more alcohol
# CAUSES better quality — both could be driven by a third factor
# (e.g. how the wine was processed/aged).
