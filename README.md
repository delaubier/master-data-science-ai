# Master Data Science & AI

### Applied Machine Learning, Deep Learning Architectures, and Statistical Modeling

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.3%2B-276DC3.svg)](https://www.r-project.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.2%2B-ee4c2c.svg)](https://pytorch.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.4%2B-f89939.svg)](https://scikit-learn.org/)
[![spaCy](https://img.shields.io/badge/spaCy-3.7%2B-09A3D5.svg)](https://spacy.io/)
[![Shiny](https://img.shields.io/badge/Shiny-R-276DC3.svg)](https://shiny.posit.co/)

🌐 **Language / Langue** : **English 🇬🇧** • [Français 🇫🇷](README.fr.md)

---

A comprehensive repository of machine learning systems, deep learning implementations from scratch, applied econometric research, and statistical modeling developed during the **Master MAS (Applied Mathematics and Statistics - Data Science & AI track)** at *Université Rennes 2*.

---

## Features

Modern data science requires both mathematical rigor to build reliable algorithms and software engineering skills to deploy production-ready analytical pipelines.

**Master Data Science & AI** covers this spectrum through applied projects:
- **Builds deep learning foundations from scratch** with manual gradient backpropagation, transition to `torch.nn.Module`, and a modular OOP `Trainer` benchmarking SGD, Momentum, and Adam.

- **Conducts rigorous econometric analysis** investigating territory-level graduate concentration via multiple OLS regressions, robust variance estimation (`sandwich`), and interactive reporting.

- **Implements algorithms without black-box libraries** including vectorized $k$-NN in NumPy and exact matrix metric triplet $(X, Q, D)$ PCA verified against `FactoMineR`.

- **Engineers end-to-end data pipelines** encompassing relational multi-table automotive ETL (6 operational tables), distributed multi-process web scraping, and NLP text-mining using `spaCy`.

---

## Projects Catalog

| Project | Domain | Core Methodologies | Key Technologies |
| :--- | :--- | :--- | :--- |
| [**deep-learning-pytorch-trainer**](./deep-learning-pytorch-trainer/) | Deep Learning | Manual gradient derivation, modular `nn.Module`, extensible `Trainer` harness, SGD vs Adam benchmarks | PyTorch, NumPy |
| [**spatial-econometrics-education**](./spatial-econometrics-education/) | Econometrics & Stats | Geographic human capital concentration, OLS regressions, robust covariance estimation, [Interactive HTML report](./spatial-econometrics-education/index.html) | R, `stargazer`, `ggplot2` |
| [**nlp-political-speech-mining**](./nlp-political-speech-mining/) | NLP & Text Mining | French political speech tokenization, TF indexing, WordClouds, POS-tagging & lemmatization | Python, spaCy, NLTK |
| [**customer-profiling-etl**](./customer-profiling-etl/) | Data Engineering | Relational join pipeline across 6 automotive operational tables, customer lifecycle metrics, basket segmentation | Python, Pandas |
| [**functional-data-analysis-fda**](./functional-data-analysis-fda/) | Advanced Statistics | Continuous curve smoothing, Fourier and B-spline basis expansion, Canadian weather & spectrometric series | R, `fda` |
| [**graph-mining-recommendation**](./graph-mining-recommendation/) | Data Mining & Recommender | FP-Tree / FP-Growth from scratch, association rules (support/confidence/lift), bipartite user-item recommendation | Python, NetworkX |
| [**algorithms-from-scratch**](./algorithms-from-scratch/) | Foundational ML | Vectorized $k$-NN in NumPy, metric triplet $(X, Q, D)$ PCA in R via `eigen`, public REST API ingestion | Python, R |
| [**mathematical-optimization**](./mathematical-optimization/) | Optimization | Standard & adaptive gradient descent, loss landscapes, convergence rate analysis | Python, NumPy |
| [**interactive-shiny-dashboard**](./interactive-shiny-dashboard/) | Data Visualization | Reactive analytics dashboard with live statistical distributions and dynamic UI controls | R, Shiny |
| [**web-scraping-distributed**](./web-scraping-distributed/) | Data Ingestion | Multi-process parallel scraping with `multiprocessing.Pool` and `BeautifulSoup` (Python) alongside `rvest` (R) | Python, R |

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/delaubier/master-data-science-ai.git
cd master-data-science-ai
```

### 2. Python Environment Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install numpy scipy pandas scikit-learn torch torchvision spacy nltk matplotlib seaborn networkx beautifulsoup4 lxml
python -m spacy download fr_core_news_md
```

### 3. R Environment Setup
```r
install.packages(c("tidyverse", "tidymodels", "car", "lmtest", "sandwich", 
                   "stargazer", "rmdformats", "fda", "shiny", "colourpicker", 
                   "FactoMineR", "rvest"))
```

---

## Usage

### Open the Interactive Econometrics Report
Open [`spatial-econometrics-education/index.html`](./spatial-econometrics-education/index.html) directly in any web browser to explore interactive findings, regression tables, and visualizations.

### Run the Automotive Customer Profiling ETL
```bash
cd customer-profiling-etl
python pipeline_etl.py
```

### Launch the Reactive Shiny Dashboard
```r
shiny::runApp("interactive-shiny-dashboard")
```
