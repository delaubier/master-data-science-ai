# Master Sciences des Données & IA

### Machine Learning appliqué, architectures Deep Learning et modélisation statistique

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.3%2B-276DC3.svg)](https://www.r-project.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.2%2B-ee4c2c.svg)](https://pytorch.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.4%2B-f89939.svg)](https://scikit-learn.org/)
[![spaCy](https://img.shields.io/badge/spaCy-3.7%2B-09A3D5.svg)](https://spacy.io/)
[![Shiny](https://img.shields.io/badge/Shiny-R-276DC3.svg)](https://shiny.posit.co/)

🌐 **Langue / Language** : [English 🇬🇧](README.md) • **Français 🇫🇷**

---

Un ensemble de projets de Machine Learning, d'implémentations d'apprentissage profond *from scratch*, d'études économétriques appliquées et de modélisations statistiques développés au cours du **Master MAS (Mathématiques Appliquées, Statistique - parcours Sciences des Données & IA)** à l'*Université Rennes 2*.

---

## Fonctionnalités

La science des données moderne exige à la fois une rigueur mathématique pour concevoir des algorithmes fiables et des compétences en ingénierie logicielle pour déployer des pipelines exploitables.

**Master Sciences des Données & IA** couvre ce spectre à travers des projets concrets :
- **Construit les fondations du Deep Learning *from scratch*** avec rétropropagation manuelle des gradients, passage aux modules `torch.nn.Module`, et développement d'un `Trainer` orienté objet comparant SGD, Momentum et Adam.

- **Conduit une analyse économétrique rigoureuse** sur la concentration territoriale des diplômés du supérieur via régressions MCO multiples, matrice de variance-covariance robuste (`sandwich`) et rapport interactif.

- **Implémente des algorithmes fondamentaux sans bibliothèques "boîte noire"** incluant le $k$-NN vectorisé en pur NumPy et l'ACP par décomposition spectrale du triplet métrique $(X, Q, D)$ validée sous `FactoMineR`.

- **Développe des pipelines de données de bout en bout** intégrant un ETL relationnel automobile multi-tables (6 tables opérationnelles), du web scraping multi-processus distribué et du text-mining sous `spaCy`.

---

## Catalogue des projets

| Projet | Domaine | Méthodologies clés | Technologies |
| :--- | :--- | :--- | :--- |
| [**deep-learning-pytorch-trainer**](./deep-learning-pytorch-trainer/) | Deep Learning | Dérivation de gradient manuelle, `nn.Module`, classe `Trainer` modulaire, benchmark SGD vs Adam | PyTorch, NumPy |
| [**spatial-econometrics-education**](./spatial-econometrics-education/) | Économétrie & Stats | Facteurs territoriaux du capital humain, régressions MCO, inférence robuste, [Rapport HTML interactif](./spatial-econometrics-education/index.html) | R, `stargazer`, `ggplot2` |
| [**nlp-political-speech-mining**](./nlp-political-speech-mining/) | NLP & Text Mining | Tokenisation de discours politiques français, indexation TF, nuages de mots, étiquetage morphosyntaxique | Python, spaCy, NLTK |
| [**customer-profiling-etl**](./customer-profiling-etl/) | Data Engineering | Pipeline de jointures relationnelles sur 6 tables automobiles, métriques temporelles, segmentation client | Python, Pandas |
| [**functional-data-analysis-fda**](./functional-data-analysis-fda/) | Statistique avancée | Lissage de courbes continues, bases de Fourier et B-splines, séries climatiques et spectrométriques | R, `fda` |
| [**graph-mining-recommendation**](./graph-mining-recommendation/) | Data Mining & Reco | Arbres FP-Tree / FP-Growth *from scratch*, règles d'association (support/confiance/lift), filtrage collaboratif | Python, NetworkX |
| [**algorithms-from-scratch**](./algorithms-from-scratch/) | Algorithmes ML | $k$-NN vectorisé en NumPy, ACP matricielle $(X, Q, D)$ en R par `eigen`, client d'API REST publiques | Python, R |
| [**mathematical-optimization**](./mathematical-optimization/) | Optimisation | Descente de gradient classique et adaptative, paysages de perte, analyse de convergence | Python, NumPy |
| [**interactive-shiny-dashboard**](./interactive-shiny-dashboard/) | Visualisation de données | Dashboard analytique réactif avec distributions statistiques en temps réel et contrôles dynamiques | R, Shiny |
| [**web-scraping-distributed**](./web-scraping-distributed/) | Ingestion de données | Scraping parallèle avec `multiprocessing.Pool` et `BeautifulSoup` (Python) ainsi que `rvest` (R) | Python, R |

---

## Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/delaubier/master-data-science-ai.git
cd master-data-science-ai
```

### 2. Environnement Python
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install numpy scipy pandas scikit-learn torch torchvision spacy nltk matplotlib seaborn networkx beautifulsoup4 lxml
python -m spacy download fr_core_news_md
```

### 3. Environnement R
```r
install.packages(c("tidyverse", "tidymodels", "car", "lmtest", "sandwich", 
                   "stargazer", "rmdformats", "fda", "shiny", "colourpicker", 
                   "FactoMineR", "rvest"))
```

---

## Utilisation

### Consulter le rapport économétrique interactif
Ouvrez directement [`spatial-econometrics-education/index.html`](./spatial-econometrics-education/index.html) dans n'importe quel navigateur pour explorer les régressions, graphiques et tableaux.

### Lancer l'ETL de profiling client automobile
```bash
cd customer-profiling-etl
python pipeline_etl.py
```

### Lancer l'application réactive Shiny
```r
shiny::runApp("interactive-shiny-dashboard")
```
