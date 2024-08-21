from file_handler import read_transactions

def total_expenses(file_path):
  transactions = read_transactions(file_path)
  print(sum(expense.get("amount") for expense in transactions))
