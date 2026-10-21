# 🚗 Customer Profiling & Multi-Table Transactional ETL

[![Python](https://img.shields.io/badge/Python-Pandas-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Data Engineering](https://img.shields.io/badge/Pipeline-ETL-orange.svg)]()

A relational data engineering pipeline and customer analytics project unifying 6 separate operational tables from an automotive dealership network (leads, orders, trade-ins, vehicle specifications, financing contracts, and geographic agencies).

---

## 🛠️ Pipeline Architecture

1. **Extraction & Deduplication:** Cleansing dirty lead identifiers and deduplicating customer profiles on unique master keys.
2. **Relational Integration:**
   - Merging transaction baskets (`TYPE_PANIER` split into purchases vs trade-ins).
   - Linking technical vehicle characteristics (`VEHICULE_ID`) and financing terms.
   - Spatial joining with nearest distribution agencies via postal code mapping.
3. **Feature Engineering:**
   - Calculation of customer transaction age: $\text{Age} = \text{Date}_{\text{basket}} - \text{Year}_{\text{birth}}$.
   - Gender ratios, financing penetration rates, and vehicle segment preferences.

---

## 📂 Source Code

- `pipeline_etl.py`: 8-step reproducible ETL script producing the master analytical dataset.
- `analysis_profiling.py`: Statistical profiling, customer lifetime estimation, and basket breakdown.
