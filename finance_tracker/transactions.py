from file_handler import write_transactions, read_transactions

def add_transaction(file_path):
  amount = input("Enter the amount: ")
  category = input("Enter the category: ")
  date = input("Enter the date (DD-MM-YYYY)")

  transaction = {
    "amount": float(amount),
    "category": category,
    "date": date
  }

  transactions = read_transactions(file_path)
  transactions.append(transaction)
  write_transactions(file_path, transactions)

def view_transactions(file_path):
  transactions = read_transactions(file_path)
  for line in transactions:
    print(line)

if __name__ == "__main__":
  file_path = "../data/transactions.json"
  #add_transaction(file_path)
  view_transactions(file_path)

