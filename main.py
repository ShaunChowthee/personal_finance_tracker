from finance_tracker import read_transactions, write_transactions, view_all_transactions, add_transaction, total_expenses, total_income

file_path = "data/transactions.json"

def main():
    while True:
        answer = input(
            "Press 1 to add a transaction \n"
            "Press 2 to view all of your transactions \n"
            "Press 3 to check your total expenses \n"
            "Press 4 to check your total income \n"
            "Press 5 to exit \n"
        )

        if answer.isdigit():
            option = int(answer)
            if option in range(1, 6):
                match option:
                    case 1:
                        add_transaction(file_path)
                    case 2:
                        view_all_transactions(file_path)
                    case 3:
                        print(f"Total Expenses: {total_expenses(file_path)}")
                    case 4:
                        print(f"Total Income: {total_income(file_path)}")
                    case 5:
                        print("Exiting the program")
                        break
            else:
                print("Please select a number between 1 and 5.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

