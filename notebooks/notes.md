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
**Conclusions:** if try to predict quality, alcohol is much more informative than fixed acidity;  in the group fixed acidity, citric acid, density and pH they have strong correlations with each other 
(fixed acidity x pH = -0.685, fixed acidity x citric acid = 0.673, fixed acidity x density = 0.68). This is expected chemically, when one changes, the others tend to change along with it. is called ML: multicollinearity (variables redundant with each other)

## 04 — linear_regression

- **The idea:** correlation says two variables move together; regression draws the actual line that best summarizes that relationship, so it can be used to predict.
- **The equation:** `y = m*x + b`. `m` (slope) = how much y changes per unit of x. `b` (intercept) = predicted y when x = 0.
- **Least squares:** the fitting method used by `np.polyfit`. For every possible line, measure the vertical distance from each point to the line (the residual), square it, sum everything, and pick the line that makes that sum smallest.
- **Link to correlation:** stronger correlation → points sit tighter around the line → better predictions. For simple linear regression, R² (how much of y's variation the line explains) is literally Pearson squared.
- **Fitted `alcohol ~ quality` line:** slope is positive, matching the 0.485 Pearson from section 03. Plotted over the scatter, the line passes through the densest rows (quality 5/6/7) rather than the sparse ones (3/4/8) — least squares is pulled toward wherever most data points are.
- **Quality is discrete, alcohol isn't:** the line will never sit exactly on any row of points, since quality only takes integer values. That's expected, not an error — the line is the best average trend, not an exact fit.
