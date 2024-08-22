from .file_handler import write_transactions, read_transactions

def add_transaction(file_path):
    amount = float(input("Enter the amount: "))
    category = input("Choose a category \n1 - Sport \n2 - Travel \n3 - Groceries \n4 - Income \n5 - Other\n")
    category_dict = {1: "Sport", 2: "Travel", 3: "Groceries", 4: "Income", 5: "Other"}
    category = category_dict.get(int(category), "Other")
    date = input("Enter the date (DD-MM-YYYY): ")

    transaction = {"amount": amount, "category": category, "date": date}
    transactions = read_transactions(file_path)
    transactions.append(transaction)
    write_transactions(file_path, transactions)
    print("Transaction successfully added")

def view_all_transactions(file_path):
    transactions = read_transactions(file_path)
    for line in transactions:
        print(line)

