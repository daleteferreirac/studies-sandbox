# Study notes — Statistics

## 01 — distribution_stats

- **Mean vs median**: mean is pulled by outliers/skew, median isn't. Close values → symmetric; mean > median → right-skewed; mean < median → left-skewed.
- **Std deviation**: how spread out values are around the mean.
- **Histogram**: shows the distribution's shape (normal, skewed, multimodal).
- **Boxplot**: shows min/Q1/median/Q3/max + outliers; good for comparing spread across variables.

## 02 — sampling_errors

- **Population vs sample**: population = full dataset; sample = subset drawn from it.
- **Sampling error**: expected gap between a sample statistic and the true population value, just from which rows got picked.
- **Sample size**: bigger samples → smaller sampling error (law of large numbers). Same reason train/test splits need decent size in ML.

## 03 — correlation

**Correlation:** a number from -1 to +1 showing how two variables move together. Not causation, both could depend on a third factor.
**Plot first:** a coefficient alone can lie (Anscombe's quartet: 4 different-looking scatter plots, same Pearson value). 
**Pearson:** measures a linear relationship. Sensitive to outliers.
**Spearman:** measures a monotonic relationship (rises/falls consistently, even if curved), using ranks instead of raw values. More robust to outliers.
**Comparing them:** close values means the relationship is close to linear. Spearman clearly higher means there's a real trend that Pearson, being linear only, is underselling.
**Correlation matrix:** the same Pearson formula run for every pair of numeric columns at once. Diagonal is always 1, symmetric across the middle. The heatmap turns that grid into colors so patterns are easier to spot.
