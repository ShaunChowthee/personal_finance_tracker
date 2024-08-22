from .file_handler import write_transactions, read_transactions

def add_transaction(file_path):
  amount = input("Enter the amount: ")
  category = input("Choose a category \n1 - Sport \n2 - Travel \n3 - Groceries \n4 - Income \n5 - Other")
  match int(category):
    case 1:
      category = "Sport"
    case 2:
      category = "Travel"
    case 3:
      category = "Groceries"
    case 4:
      category = "Income"
    case 5:
      category = "Other"
  date = input("Enter the date (DD-MM-YYYY)")

  transaction = {
    "amount": float(amount),
    "category": category,
    "date": date
  }

  transactions = read_transactions(file_path)
  transactions.append(transaction)
  write_transactions(file_path, transactions)
  print(f"Transaction succesfully added")

def view_all_transactions(file_path):
  transactions = read_transactions(file_path)
  for line in transactions:
    print(line)

