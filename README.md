# 🎓 Master's Portfolio: Data Science & Artificial Intelligence

[![University](https://img.shields.io/badge/University-Rennes%202-6C1D45.svg)](https://formations.univ-rennes2.fr/)
[![Degree](https://img.shields.io/badge/Degree-Master%20MAS%20(Applied%20Math%20%26%20Stats)-0A66C2.svg)]()
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.3%2B-276DC3.svg?logo=r&logoColor=white)](https://www.r-project.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Tidymodels](https://img.shields.io/badge/Tidymodels-R-blue.svg)](https://www.tidymodels.org/)

This repository documents advanced machine learning pipelines, deep learning architectures, applied econometrics, and statistical algorithms developed during my **Master MAS (Applied Mathematics and Statistics - Data Science & AI track)** at *Université Rennes 2*.

---

## 🧭 Project Catalog

| Project | Domain | Key Techniques & Methodologies | Tech Stack |
| :--- | :--- | :--- | :--- |
| [**deep-learning-pytorch-trainer**](./deep-learning-pytorch-trainer/) | Deep Learning | Manual gradient backprop, modular `nn.Module`, OOP `Trainer` harness, optimizer benchmarks (SGD vs Adam) | PyTorch, NumPy |
| [**spatial-econometrics-education**](./spatial-econometrics-education/) | Econometrics & Stats | Territory-level determinants of graduate density, OLS regressions, robust standard errors (`sandwich`), VIF, [Interactive robobook report](./spatial-econometrics-education/index.html) | R, `ggplot2`, `stargazer` |
| [**nlp-political-speech-mining**](./nlp-political-speech-mining/) | NLP & Text Mining | French speech corpora tokenization, term-frequency indexing, WordClouds, POS-tagging & lemmatization via `spaCy` (`fr_core_news_md`) | Python, spaCy, NLTK |
| [**customer-profiling-etl**](./customer-profiling-etl/) | Data Engineering & Analytics | Relational data pipeline across 6 automotive operational tables, customer lifecycle metrics, basket & trade-in segmentation | Python, Pandas |
| [**functional-data-analysis-fda**](./functional-data-analysis-fda/) | Advanced Statistics | Continuous curve and signal modeling, Fourier and B-spline basis expansion, climatic & spectrometric series | R, `fda` |
| [**graph-mining-recommendation**](./graph-mining-recommendation/) | Data Mining & Recommender | FP-Tree / FP-Growth itemset mining from scratch, association rules (support/confidence/lift), bipartite user-item recommendation | Python, NetworkX |
| [**algorithms-from-scratch**](./algorithms-from-scratch/) | Foundational ML | Vectorized $k$-NN in NumPy, exact matrix metric triplet $(X, Q, D)$ PCA in R via `eigen`, REST API ingestion pipeline | Python, R |
| [**mathematical-optimization**](./mathematical-optimization/) | Optimization | Standard & adaptive gradient descent, loss landscapes, convergence rate analysis | Python, NumPy |
| [**interactive-shiny-dashboard**](./interactive-shiny-dashboard/) | Data Visualization | Reactive analytics dashboard with live statistical distributions and dynamic UI controls | R, Shiny |
| [**web-scraping-distributed**](./web-scraping-distributed/) | Data Ingestion | Multi-process parallel scraping with `multiprocessing.Pool` and `BeautifulSoup` (Python) alongside `rvest` (R) | Python, R |

---

## 🛠️ Installation & Reproduction

### Python Environment
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
