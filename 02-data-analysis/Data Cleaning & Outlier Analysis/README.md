# Data Cleaning Pipeline for Retail Transactions

This project contains a **Python class-based data cleaning pipeline** for retail transaction data. It normalizes and prepares a dataset for analysis by handling missing values, text inconsistencies, and numeric outliers, while logging all operations.

---

## Features

- **Transaction ID & Customer ID Normalization**  
  Converts IDs to lowercase, strips whitespace, and ensures consistency.

- **Category & Product Normalization**  
  Cleans category and item names, removes extra spaces, and handles missing product entries.

- **Numeric Data Cleaning**  
  Handles missing values and removes outliers in `Price Per Unit`, `Quantity`, and `Total Spent`.

- **Payment Method & Location Normalization**  
  Standardizes text for consistent values.

- **Transaction Date Parsing**  
  Converts dates to `datetime` objects for proper analysis.

- **Discount Applied Handling**  
  Fills missing discount values with `"Unknown"` to avoid inconsistencies.

- **Logging**  
  Every cleaning step is logged in `Cleaning.log` with timestamps for traceability.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/data-cleaning-pipeline.git
cd data-cleaning-pipeline

Install dependencies:

pip install pandas numpy matplotlib


Place your dataset in the project directory as Data.csv.

Usage
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


Each function cleans a specific column.

Logs are saved in Cleaning.log with timestamps.

Data is saved back to Data.csv after cleaning.

Project Structure
├── Data.csv                 # Raw dataset
├── Cleaning.log             # Log file generated during cleaning
├── data_cleaning.py         # Python class for data cleaning
├── README.md                # This documentation

Notes

The pipeline is designed to see the effect of each cleaning function individually.

Outliers in numeric columns can be removed using the remove_outliers(column_name) function.

Missing or malformed data is handled safely to avoid crashes.

Intended for small to medium retail datasets for step-by-step data cleaning and verification.

Author

Sohaib Asif
Bachelor in Artificial Intelligence | Data Enthusiast