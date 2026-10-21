# 🧠 Algorithms from Scratch

[![Python](https://img.shields.io/badge/Python-NumPy-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
[![R](https://img.shields.io/badge/R-Calculus-276DC3.svg?logo=r&logoColor=white)](https://www.r-project.org/)

Implementations of fundamental machine learning and statistical algorithms developed purely from mathematical definitions without relying on black-box libraries.

---

## 📐 Implemented Modules

### 1. Vectorized $k$-Nearest Neighbors (`knn_from_scratch.py`)
- Euclidean distance calculation in pure Python and NumPy.
- Efficient search of the $k$-nearest neighbors for arbitrary dimensions.
- Majority voting and continuous distance-weighted classification.

### 2. Matrix Metric Triplet PCA (`pca_triplet_matrix.qmd`)
- Exact realization of Principal Component Analysis through the French statistical school formalism: the metric triplet $(X, Q, D)$.
- Matrix operations: column metric $Q$, individual weight metric $D$, and spectral decomposition of $Q^{1/2} X^T D X Q^{1/2}$ via `eigen()`.
- Explicit computation of inertia percentages, principal axes, and row/column factor coordinates.
- Benchmarked and strictly validated against `FactoMineR::PCA`.

### 3. REST API Data Pipeline (`rest_api_data_ingestion.py`)
- Custom client interacting with public open data APIs (data.gouv and Geo API).
- Exception handling, pagination, address parsing, and geocoding integration.
