# budget_manager.py
import functions


# Define the budget data structure
budget_data = {
    "balance": 0,
    "transactions": []
}


# Menu system
def main_menu():
    global budget_data  # Ensure global access
    
    while True:
        print("\nBudget Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Show Transaction History")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            # Add Income (function to be implemented)
            # budget_data = add_income(budget_data, amount, description)
            budget_data = functions.add_income(budget_data)
        elif choice == "2":
            # Add Expense (function to be implemented)
            # budget_data = add_expense(budget_data, amount, description)
            pass
        elif choice == "3":
            # Show Balance (function to be implemented)
            # show_balance(budget_data)
            pass
        elif choice == "4":
            # Show Transaction History (function to be implemented)
            # show_transactions(budget_data)
            pass
        elif choice == "5":
            print("Exiting Budget Manager. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# Run the program
if __name__ == "__main__":
    main_menu()
