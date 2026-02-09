# Retail Data Cleaning & Feature Engineering Pipeline (RDCBA)

## Overview
This project implements a **robust, dynamic, and resource-efficient data pipeline** for retail transaction datasets. The core idea is **dynamic function execution** — functions only run if necessary, reducing resource cost and improving execution speed.  

Key features of this pipeline:

- **Dynamic Data Normalization:** Functions check if data requires cleaning (nulls, duplicates, special characters) before execution.
- **Feature Engineering:** Automatic creation of business-relevant features like total spend, average order value, purchase frequency, recency, and category diversity.
- **Target Variable Creation:** Generates `High Value Transaction` and `Repeating Customer` targets.
- **Exploratory Data Analysis (EDA):** Correlation matrix, distributions, and boxplots with PNG outputs.
- **Business Insights:** Aggregations to identify high-value segments, repeat behavior, and revenue-driving customers.
- **Logging:** Every step is logged to ensure reproducibility and auditability.

---

## Project Structure

data/
├─ input/
│ └─ input.csv # Raw dataset
├─ output/
│ ├─ cleaned/
│ │ └─ cleaned.csv # Cleaned dataset
│ ├─ features/
│ │ └─ features.csv # Feature-engineered dataset with target
│ ├─ analysis/
│ │ └─ analysis.csv # Aggregated stats / EDA results
│ └─ visuals/ # PNG plots of distributions & boxplots
logs/
└─ logs.log # Execution logs
src/
└─ rdcba_pipeline.py # Main pipeline class


---

## Key Pipeline Steps

### Step 1 — Data Validation & Cleaning
- Loads the raw CSV dataset.
- Validates schema and checks for nulls or duplicates.
- Cleans nulls with explicit strategies (`ffill`, `dropna`, default values).
- Removes duplicates only where duplicates are invalid.
- Logs every action.
- Outputs cleaned CSV: `data/output/cleaned/cleaned.csv`.

**Dynamic Function Execution:**  
Each cleaning function executes **only if required**. For example:  
- `CleanNullValues()` runs only if nulls exist.  
- `RemoveDuplicates()` runs only if duplicates exist.  
- `removespecial()` runs only if numeric columns contain special characters.  

---

### Step 2 — Target Variable Creation
- Creates **High Value Transaction** (`Price > 500`)  
- Creates **Repeating Customer** (`purchase count > 1`)  
- Thresholds can be justified and logged.  
- Logs positive vs negative counts.  
- Output CSV: `data/output/features/features.csv`.

---

### Step 3 — Feature Engineering
- **Customer Total Spend**  
- **Average Order Value**  
- **Purchase Frequency**  
- **Purchase Recency** (days since last purchase)  
- **Category Diversity** (number of unique products purchased)  
- Each feature is calculated **in a dedicated function** and logged.

---

### Step 4 — Exploratory Data Analysis (EDA)
- Generates **correlation matrix** for numeric features.
- Distribution checks via **histograms** and **boxplots**.
- Saves all charts as PNG in `data/output/visuals/`.
- Outputs aggregated stats CSV: `data/output/analysis/analysis.csv`.

---

### Step 5 — Business Insights
- Aggregates to answer:
  - Which customer segments drive most revenue?  
  - Repeat vs non-repeat customer behavior patterns.  
  - High-value customer identification.  
- Output CSV: included in `features.csv` and `analysis.csv`.

---

## Why This Pipeline is Unique

- **Dynamic Execution:** Reduces unnecessary function calls → faster runtime and lower resource consumption.
- **Intentionally Designed:** Each cleaning step and feature calculation is **executed only if required**, ensuring efficient and intelligent preprocessing.
- **Pipeline Ready:** Fully automated, modular, and reproducible. ML-ready datasets are generated at the end.

---

## How to Use

```python
from rdcba_pipeline import RDCBA
import os

# Initialize pipeline
app = RDCBA(inputdata, cleaned, featured, logfiles, analysis, visuals)

# Run pipeline
app.loadData()
app.validate_data()           # Dynamic cleaning
app.save_data(app.cleaned)    # Save cleaned data
app.CleanNumericColumns()     # Ensure numeric columns are clean

app.TargetVariable()          # Create target variables
app.Customer_total_spend()
app.AverageOrderValue()
app.PurchaseFrequency()
app.PurchaseRecency()
app.CategoryDiversity()
app.Aggregations(threshold=900)

app.save_data(app.featured, columns=[
    "Customer_ID","Transaction_ID","High Value Transaction","Repeating Customer",
    "Customer Total Spend","Average Order Value","Purchase Frequency","Purchase Recency",
    "Category Diversity","High/Low Value Customers","Most Revenue Segment","Repeating Behavior Pattern"
])

app.ExploratoryAnalysis()     # EDA + save charts
app.save_data(app.analysis)   # Save analysis results
