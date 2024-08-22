# Personal Finance Tracker (THIS IS A TRAINING PROJECT)

## Overview

The Personal Finance Tracker is a Python application designed to help users manage their finances by tracking income, expenses, and savings. Users can add transactions, view their transaction history, and calculate their total expenses and income.

## Project Structure

- `data/transactions.json`: Stores transaction data in JSON format.
- `finance_tracker/`
  - `__init__.py`: Initializes the finance_tracker package.
  - `calculations.py`: Contains functions for calculating total expenses and income.
  - `file_handler.py`: Functions for reading from and writing to the JSON file.
  - `transactions.py`: Functions for adding and managing transactions.
- `main.py`: Main script to interact with the finance tracker.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd personal_finance_tracker
