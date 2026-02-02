Exploratory Data Analysis (EDA) Pipeline for Retail Transactions

This repository contains a production-style Python EDA pipeline for analyzing retail transaction data.
The pipeline cleans raw data, engineers features, and generates business-ready summary tables in CSV format.

It is designed to support:

Business reporting

Data analysis workflows

Feature engineering for machine learning

Project Structure
Exploratory Data Analysis & Feature Engineering for Retail Dataset/
│
├── EDA_pipeline.py
├── README.md
├── data/
│   ├── input/
│   │   └── data.csv
│   │
│   └── output/
│       ├── EDA_aggrevated_results/
│       │   └── EDA_Featured_output.csv
│       │
│       ├── EDA_general_stats/
│       │   └── EDA_Featured_output.csv
│       │
│       ├── EDA_Revenue_output/
│       │   └── EDA_Revenue_output.csv
│       │
│       ├── EDA_top_customers/
│       │   └── EDA_top_customers.csv
│       │
│       └── EDA_monthly_revenue/
│           └── EDA_monthly_revenue.csv
│
└── logs/
    └── EDA_logs.log

Pipeline Overview

The pipeline performs the following steps:

1. Data Cleaning

Converts numeric fields (Total Spent, Quantity) to proper numeric types

Handles invalid values using coercion

Generates derived features:

Unit Price = Total Spent / Quantity

HighValueTransaction = True if Total Spent > 1000

2. Descriptive Statistics (by Category)

Output:

data/output/EDA_general_stats/EDA_Featured_output.csv


Includes:

Total Records

Average

Standard Deviation

Minimum

25th, 50th, 75th Percentiles

Maximum

Grouped by Category.

3. Revenue & Order Summary (by Category)

Output:

data/output/EDA_aggrevated_results/EDA_Featured_output.csv


Columns:

Category

Total Revenue

Average Order Value

Total Orders

Average Unit Price

Has High Value Transaction (True/False)

4. Revenue by Payment Method

Output:

data/output/EDA_Revenue_output/EDA_Revenue_output.csv


Columns:

Payment Method

Total Revenue

5. Customer-Level Metrics

Output:

data/output/EDA_top_customers/EDA_top_customers.csv


Columns:

Customer ID

Total Spent

Average Spent

Customer Purchase Count

6. Monthly Revenue

Output:

data/output/EDA_monthly_revenue/EDA_monthly_revenue.csv


Columns:

Month

Monthly Revenue

How to Run

Place your dataset in:

data/input/data.csv


Run:

python EDA_pipeline.py


Generated reports will appear in:

data/output/

Logging

All execution details and summaries are recorded in:

logs/EDA_logs.log

Technologies Used

Python

Pandas

NumPy

OS

Matplotlib

Author

Sohaib Asif
Bachelor’s in Artificial Intelligence, Bahria University

GitHub: https://github.com/Sohaibasif8532

LinkedIn: https://www.linkedin.com/in/sohaib-asif-28389627b/