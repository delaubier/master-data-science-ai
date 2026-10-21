# 🎓 Master's Portfolio: Data Science & Artificial Intelligence

[![University](https://img.shields.io/badge/University-Rennes%202-6C1D45.svg)](https://formations.univ-rennes2.fr/)
[![Degree](https://img.shields.io/badge/Degree-Master%20MAS%20(Applied%20Math%20%26%20Stats)-0A66C2.svg)]()
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.3%2B-276DC3.svg?logo=r&logoColor=white)](https://www.r-project.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Tidymodels](https://img.shields.io/badge/Tidymodels-R-blue.svg)](https://www.tidymodels.org/)

This repository documents academic research projects, algorithms coded from scratch, applied econometrics, and machine learning architectures developed during my **Master MAS (Applied Mathematics and Statistics - Data Science & AI track)** at *Université Rennes 2*.

---

## 🧭 Repository Roadmap

```
master-data-science-ai/
├── M1/                                  # First Year Master Projects
│   ├── spatial-econometrics-education/  # Higher education graduate density study (Rmd & robobook)
│   ├── customer-profiling-etl/          # Multi-table automotive transactional ETL & segmentation
│   ├── graph-mining-recommendation/     # FP-Tree, association rules & bipartite collaborative filtering
│   ├── algorithms-from-scratch/         # k-NN in pure Python/NumPy, PCA metric triplet in R
│   ├── interactive-shiny-dashboard/     # Reactive R Shiny application
│   └── web-scraping-distributed/        # Multi-process web scrapers (Python BeautifulSoup & R rvest)
│
└── M2/                                  # Second Year Master Projects (Advanced AI & Modeling)
    ├── deep-learning-pytorch-trainer/   # Manual backprop, nn.Module, modular Trainer (SGD vs Adam)
    ├── nlp-political-speech-mining/     # Linguistic extraction & TF analysis (spaCy, NLTK)
    ├── functional-data-analysis-fda/    # Continuous signal modeling & Fourier bases (R fda)
    └── mathematical-optimization/       # Gradient descent algorithms & convergence surfaces
```

---

## 🔬 Project Highlights

### 🌟 Master 2 (Advanced AI & Statistics)

1. [**Deep Learning PyTorch Trainer**](./M2/deep-learning-pytorch-trainer/)
   - Mathematical derivation of gradients and manual parameter optimization.
   - Evolution into modular `torch.nn.Module` architectures with an extensible `Trainer` class.
   - Empirical benchmark comparing SGD, Momentum, and Adam optimizers.

2. [**NLP Political Speech Mining**](./M2/nlp-political-speech-mining/)
   - Text preprocessing, tokenization, frequency indexing, and stop-word filtering.
   - Syntactic and linguistic analysis using `spaCy` (`fr_core_news_md`) on presidential speech corpora.

3. [**Functional Data Analysis (FDA)**](./M2/functional-data-analysis-fda/)
   - Modeling infinite-dimensional curves from discrete observations via the `fda` package in R.
   - Fourier and B-spline basis expansion applied to climatic series (*Canadian Weather*) and spectrometric signals.

4. [**Mathematical Optimization**](./M2/mathematical-optimization/)
   - Pure Python / NumPy implementations of gradient descent variants, learning rate decay, and loss landscape convergence.

---

### 🌟 Master 1 (Foundations, Modeling & Data Engineering)

1. [**Spatial Econometrics of Higher Education**](./M1/spatial-econometrics-education/)
   - Academic empirical investigation: *"What socio-economic factors drive the spatial concentration of higher education graduates?"*
   - Includes full Quarto/RMarkdown source and interactive compiled HTML report (`rmdformats::robobook`).
   - Multiple linear regressions, multicollinearity checks (VIF), heteroscedasticity-robust standard errors (`sandwich`, `lmtest`), and Stargazer regression tables.

2. [**Customer Profiling & Transactional ETL**](./M1/customer-profiling-etl/)
   - Comprehensive data engineering pipeline joining 6 relational operational tables (leads, orders, trade-ins, vehicles, financing, agencies).
   - Time-delta metrics, customer age distributions, RFM segmentation, and trade-in propensity profiling.

3. [**Graph Mining & Association Rules (FP-Tree)**](./M1/graph-mining-recommendation/)
   - Algorithmic implementation of FP-Growth trees, support/confidence/lift computation for itemset mining.
   - Bipartite user-item rating graphs and collaborative filtering algorithms using `networkx`.

4. [**Algorithms from Scratch**](./M1/algorithms-from-scratch/)
   - **k-NN Classifier**: Vectorized Euclidean metric computation and majority voting using only NumPy and SciPy.
   - **Metric Triplet PCA**: Full mathematical realization of Principal Component Analysis through the statistical triplet $(X, Q, D)$ diagonalized via `eigen`, verified against `FactoMineR`.
   - **REST API Pipeline**: Dynamic consumption and record linkage with public open-data APIs.

---

## 🛠️ Installation & Reproduction

### Python Dependencies
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install numpy scipy pandas scikit-learn torch torchvision spacy nltk matplotlib seaborn networkx beautifulsoup4 lxml
python -m spacy download fr_core_news_md
```

### R Dependencies
```r
install.packages(c("tidyverse", "tidymodels", "car", "lmtest", "sandwich", 
                   "stargazer", "rmdformats", "fda", "shiny", "colourpicker", 
                   "FactoMineR", "rvest"))
```

---

## 👤 Author

**Thomas De Laubier**  
- Master's in Applied Mathematics & Statistics, Data Science & AI (*Université Rennes 2*)
- [LinkedIn Profile](https://www.linkedin.com) • [GitHub Profile](https://github.com)
