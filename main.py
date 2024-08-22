from finance_tracker import read_transactions, write_transactions, view_all_transactions, add_transaction, total_expenses, total_income

file_path = "data/transactions.json"

def main():
  answer = True
  while answer:
    answer = input("Press 1 to add a transaction \nPress 2 to view all of your transactions \nPress 3 to check your total expenses \nPress 4 to check your total income \nPress 5 to exit \n")
    try:
      if int(answer) in range(1, 6):
        break
    except:
      print("You need to press a number between 1 and 5")
      answer = True
  
  match int(answer):
    case 1:
      add_transaction(file_path)
    case 2:
      view_all_transactions(file_path)
    case 3:
      print(total_expenses(file_path))
    case 4:
      print(total_income(file_path))
    case 5:
      print("Exiting the program")

main()
