PET – Personal Expense Tracker (CLI)

A simple command-line Personal Expense Tracker built with Python.
It allows you to add, view, delete, and analyze expenses, storing everything in a CSV file and generating basic visual analytics.

This project is ideal for:

Practicing Python + Pandas

Learning logging

Building real CLI tools

Basic data analysis & visualization

Features

Add new expenses

View all expenses or filter by:

Category

Date

Delete expenses by index

Summary analytics:

Total खर्च

Average expense

Maximum & minimum expense

Automatic logging (PET.log)

Visual charts using Matplotlib:

Expenses over time

Expenses by category

Tech Stack

Python 3

Pandas

Matplotlib

Logging module

CSV for storage

Project Structure
PET/
│
├── PET.py        # Main application
├── PET.csv       # Expense data (auto-created)
├── PET.log       # Logs (auto-created)
└── README.md

Installation

Clone the repository:

git clone https://github.com/yourusername/PET.git
cd PET


Install dependencies:

pip install pandas matplotlib

Usage (CLI Commands)

Run everything from terminal:

1. Add an Expense
python PET.py add 500 Food "Lunch at KFC"

2. View All Expenses
python PET.py view

3. View by Category
python PET.py view Food

4. View by Category & Date
python PET.py view Food 2026-01-27

5. Delete an Expense (by index)
python PET.py delete 2

6. Summary & Analytics
python PET.py summary


This will:

Print totals

Show line chart (expenses over time)

Show bar chart (by category)

Sample Output
Console Summary
Total Expenses : 3200  
Average Expenses : 640  
Max Expenses : 1200  
Min Expenses : 200

Charts

Line graph → Spending over time

Bar chart → Spending per category

Logging

All actions are logged in:

PET.log


Example log:

2026-01-27 01:12:45 - Expense added successfully: 500, Food, Lunch at KFC
2026-01-27 01:15:02 - Expense deleted successfully: {...}

Why This Project is Good (From an Engineering POV)

This project demonstrates:

File handling

CLI argument parsing

Pandas data manipulation

Logging best practices

Data visualization

Clean modular structure

This is exactly the type of project recruiters like for juniors:

Small, practical, real-world, not tutorial garbage.

Future Improvements (Good for V2)

If you want to level this up:

Monthly reports

Export to Excel / PDF

Pie chart for categories

Budget limits + alerts

SQLite instead of CSV

GUI / Web dashboard (Streamlit / Flask)

Author

Sohaib Asif
AI Undergraduate | Aspiring AI Engineer
Building real projects, not just certificates.

License

MIT License – Free to use, modify, and improve.