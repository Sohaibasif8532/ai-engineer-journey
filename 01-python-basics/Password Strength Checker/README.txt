Password Strength Checker (CLI)
Description

A Python command-line application that evaluates the strength of a password based on common security rules.
The program analyzes the password and provides a strength score, classification, and clear feedback on how to improve weak passwords.

This project demonstrates strong fundamentals in:

String manipulation

Conditional logic

Clean function design

User input validation

Features

Checks minimum password length (8 characters)

Verifies presence of:

Uppercase letters

Lowercase letters

Digits

Special characters

Scores password strength out of 5

Categorizes password as:

Very Weak

Weak

Medium

Strong

Very Strong

Provides improvement suggestions when requirements are not met

Strength Criteria

Each of the following adds 1 point to the score:

Length ≥ 8 characters

At least one uppercase letter

At least one lowercase letter

At least one digit

At least one special character

How to Run
python password_checker.py


The program will prompt you to enter a password and will immediately analyze it.

Example Output
Enter your password: P@ss12

✘ Password must be at least 8 characters long
✘ Password must contain a digit

Score: 3 / 5
Password Strength: MEDIUM

Technologies Used

Python 3

Built-in string methods (isupper, islower, isdigit)

No external libraries or regex

Notes

Designed without regex to demonstrate full understanding of string traversal

Ideal as a foundational security-related Python project

Suitable for beginner-to-intermediate portfolios