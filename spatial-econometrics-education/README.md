# 📊 Spatial Econometrics: Determinants of Higher Education Graduate Concentration

[![R](https://img.shields.io/badge/R-4.3%2B-276DC3.svg?logo=r&logoColor=white)](https://www.r-project.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()
[![Report](https://img.shields.io/badge/Interactive%20Report-HTML%20robobook-blue.svg)](./index.html)

An empirical econometrics study investigating regional disparities in human capital accumulation across French territories:
> *"Quels sont les facteurs qui favorisent une forte concentration de diplômés du supérieur dans une zone géographique ?"*

---

## 🔬 Methodology & Empirical Strategy

1. **Theoretical Framework:** Human capital spatial equilibrium (Moretti, Glaeser), agglomeration externalities, and local labor market amenities.
2. **Econometric Specification:**
   - Multiple Ordinary Least Squares (OLS) regressions.
   - Diagnostic tests: Multicollinearity assessment using Variance Inflation Factors (VIF with `car`), Breusch-Pagan heteroscedasticity testing (`lmtest`).
   - Inference: Heteroscedasticity-consistent covariance matrix estimation (HC3 robust standard errors via `sandwich`).
   - Model selection using AIC/BIC and stepwise variance comparisons.
3. **Reporting:** Publication-quality regression tables formatted with `stargazer` and compiled into an interactive `rmdformats::robobook` HTML interface.

---

## 📁 Files Included

- `DELAUBIER.Rmd`: Complete literate programming source code with mathematical formulations and chunk options.
- `index.html`: Fully rendered, self-contained interactive web report with dynamic TOC and embedded ggplot2 visualizations.
- `data.csv`: Aggregated demographic and economic indicators by geographic unit.

## 🚀 View the Interactive Report

Open `index.html` in any web browser to explore the full findings, interactive tables, and analytical visualizations.

