# 🕸️ Graph Mining & Association Rules (FP-Tree & Recommendation)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20Theory-informational.svg)](https://networkx.org/)

An implementation of data mining algorithms and collaborative filtering models, covering frequent pattern mining with FP-Growth and graph-based recommendation systems.

---

## 🔬 Core Components

1. **FP-Tree & Association Rules (`armining/`):**
   - Construction of compact Frequent Pattern Trees (`fptree.py`) without candidate generation.
   - Recursive FP-Growth mining of frequent itemsets (`itemset.py`).
   - Generation of high-confidence association rules (`associationrule.py`) with support, confidence, and lift metrics.
2. **Graph-Based Recommender (`graphs.py`, `collaborative_filtering.py`):**
   - User-item bipartite interaction modeling using `networkx`.
   - Node centrality, common neighbors, and collaborative score imputation for missing user ratings.
