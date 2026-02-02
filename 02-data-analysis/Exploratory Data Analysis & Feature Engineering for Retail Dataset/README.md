# Data Cleaning Pipeline for Retail Transactions

This project contains a **Python class-based data cleaning pipeline** for retail transaction data.  
It normalizes and prepares a dataset for analysis by handling missing values, text inconsistencies, and numeric outliers, while logging all operations.

---

## Features

### Transaction ID & Customer ID Normalization
Converts IDs to lowercase, strips whitespace, and ensures consistency.

### Category & Product Normalization
Cleans category and item names, removes extra spaces, and handles missing product entries.

### Numeric Data Cleaning
Handles missing values and removes outliers in:
- Price Per Unit
- Quantity
- Total Spent

### Payment Method & Location Normalization
Standardizes text for consistent values.

### Transaction Date Parsing
Converts dates to `datetime` objects for proper analysis.

### Discount Applied Handling
Fills missing discount values with `"Unknown"` to avoid inconsistencies.

### Logging
Every cleaning step is logged in `Cleaning.log` with timestamps for traceability.

---

## Installation

### Clone the repository

git clone https://github.com/Sohaibasif8532/data-cleaning-pipeline.git
cd data-cleaning-pipeline

### Install dependencies
```bash
pip install pandas numpy matplotlib
```

### Usage
```python
from data_cleaning import DataCleaning

app = DataCleaning()
app.NormalizeTransactionID()
app.NormalizeCustomerID()
app.NormalizeCategory()
app.NormalizeProduct()
app.NormalizePricePerUnit()
app.NormalizeQuantity()
app.NormalizeTotalSpent()
app.NormalizePaymentMethod()
app.NormalizeDate()
app.NormalizeDiscountApplied()
app.save_and_log("Data Cleaning Completed")
```

### Project Structure
```bash
├── Data.csv
├── Cleaning.log
├── data_cleaning.py
├── README.md
```

### Notes

The pipeline is designed to see the effect of each cleaning function individually.

Outliers in numeric columns can be removed using remove_outliers(column_name).

Missing or malformed data is handled safely to avoid crashes.

Intended for small to medium retail datasets.

### Author

**Sohaib Asif**
Bachelor in Artificial Intelligence | Data Enthusiast

GitHub: https://github.com/Sohaibasif8532
LinkedIn: https://www.linkedin.com/in/sohaib-asif-28389627b/