# Master Data Science & AI

### Applied Machine Learning, Deep Learning, and Statistical Modeling

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.3%2B-276DC3.svg)](https://www.r-project.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.2%2B-ee4c2c.svg)](https://pytorch.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-f89939.svg)](https://scikit-learn.org/)
[![spaCy](https://img.shields.io/badge/spaCy-09A3D5.svg)](https://spacy.io/)

🌐 **Language / Langue** : **English 🇬🇧** • [Français 🇫🇷](README.fr.md)

---

Academic and applied data science projects developed during the Master MAS (Applied Mathematics & Statistics) at Université Rennes 2.

---

## Highlights

- **Deep Learning from scratch:** Manual backpropagation, custom `nn.Module` architectures, and an extensible `Trainer` benchmarking SGD, Momentum, and Adam.
- **Empirical econometrics:** Territory-level regression study on graduate concentration with robust standard errors and an [interactive HTML report](./spatial-econometrics-education/index.html).
- **Core ML algorithms:** Vectorized $k$-NN in NumPy and exact metric triplet $(X, Q, D)$ PCA in R coded without high-level wrappers.
- **Data engineering & NLP:** Multi-table relational ETL on automotive sales, French speech text-mining with spaCy, and parallel web scraping.

---

## Projects

| Project | Domain | Highlights | Stack |
| :--- | :--- | :--- | :--- |
| [**deep-learning-pytorch-trainer**](./deep-learning-pytorch-trainer/) | Deep Learning | Manual gradients, OOP Trainer, SGD vs Adam benchmark | PyTorch, NumPy |
| [**spatial-econometrics-education**](./spatial-econometrics-education/) | Econometrics | Human capital regression study, robust errors, [HTML report](./spatial-econometrics-education/index.html) | R, Stargazer |
| [**nlp-political-speech-mining**](./nlp-political-speech-mining/) | NLP | French presidential speech corpus, TF indexing, POS-tagging | Python, spaCy, NLTK |
| [**customer-profiling-etl**](./customer-profiling-etl/) | Data Engineering | Relational join pipeline across 6 automotive tables | Python, Pandas |
| [**functional-data-analysis-fda**](./functional-data-analysis-fda/) | Statistics | Continuous curve smoothing, Fourier and B-spline basis expansion | R, fda |
| [**graph-mining-recommendation**](./graph-mining-recommendation/) | Data Mining | FP-Tree itemset mining, association rules, bipartite recommender | Python, NetworkX |
| [**algorithms-from-scratch**](./algorithms-from-scratch/) | Machine Learning | Vectorized $k$-NN, metric triplet PCA, public REST API client | Python, R |
| [**mathematical-optimization**](./mathematical-optimization/) | Optimization | Gradient descent algorithms and convergence rate analysis | Python, NumPy |
| [**interactive-shiny-dashboard**](./interactive-shiny-dashboard/) | Visualization | Reactive web dashboard with live statistical distributions | R, Shiny |
| [**web-scraping-distributed**](./web-scraping-distributed/) | Data Ingestion | Parallel web scraping using multi-process pools | Python, R |
