Sales & Retail Data Analyzer (CLI)

A command-line data analysis tool built in Python for analyzing retail sales data.
The application supports basic sales statistics computation and dataset filtering using pandas, with a focus on clean preprocessing and reproducible results.

Overview

This project demonstrates practical data analysis workflows using Python, including:

Data preprocessing and normalization

Sales metric computation

Command-line driven analytics

Vectorized filtering using pandas

The tool is designed to be lightweight, extensible, and suitable for automation or internal analytics use cases.

Key Capabilities

Load and preprocess retail sales data

Normalize categorical fields (product, category)

Compute core sales metrics:

Total sales

Average sales

Maximum and minimum sales

Record count

Filter dataset by:

Date

Product

Category

Export processed results to CSV

CLI-driven execution using Python 3.10+ match-case

Project Structure
Sales & Retail Data Analyzer/
│
├── Data.csv                # Input dataset
├── Results.csv             # Output results
├── SalesRetailAnalyzer.py  # Core application logic
└── README.md

Requirements

Python 3.10 or higher

pandas

matplotlib (reserved for future visualization support)

Install dependencies:

pip install pandas matplotlib

Usage

Run the application from the command line:

python SalesRetailAnalyzer.py <command> [argument]

Command Reference
Command	Description
1	Compute total sales
2	Compute average sales
3	Compute maximum and minimum sales
4	Count total sales records
5 <YYYY-MM-DD>	Filter records by date
6 <product>	Filter records by product
7 <category>	Filter records by category
Examples
python SalesRetailAnalyzer.py 1

python SalesRetailAnalyzer.py 5 2026-01-01

python SalesRetailAnalyzer.py 6 laptop

python SalesRetailAnalyzer.py 7 electronics

Output

Computed results are written to Results.csv

Filtered datasets are printed directly to standard output

All categorical filtering is case-insensitive via normalization

Design Notes

Centralized data loading and preprocessing via a single pipeline

Vectorized pandas operations used instead of row-wise iteration

CLI routing separated from business logic

Structured for easy extension (argparse, plotting, summaries)

Planned Enhancements

Replace sys.argv with argparse

Add summary-level output files

Integrate basic visualizations

Add unit tests

Package restructuring for reuse

Author

Sohaib Asif
Bachelor’s in Artificial Intelligence
Focus areas: Python, Data Analysis, Machine Learning Foundations