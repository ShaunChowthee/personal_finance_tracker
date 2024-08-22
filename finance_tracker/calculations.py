from .file_handler import read_transactions

def total_expenses(file_path):
  transactions = read_transactions(file_path)
  return sum(expense.get("amount") for expense in transactions)

def total_income(file_path):
  transactions = read_transactions(file_path)
  return sum(expense.get("amount") for expense in transactions if expense.get("category") == "Income")
