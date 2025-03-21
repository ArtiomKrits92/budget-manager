# functions.py

def add_income(budget_data):
    """
    Collects income info from the user and adds it to the data structure.
    :param budget_data: dict with 'balance' and 'transactions'
    :return: updated budget_data
    """
    # To be implemented by a teammate
    return budget_data


def add_expense(budget_data):
    """Adds a new expense to the db"""
    while True:
        try:
            print("\n=== ADD NEW EXPENSE ===\n")
            inputExpenseAmount = float(input("Enter Expense Amount (₪):\n> "))
            if inputExpenseAmount < 0:
                print("\n"+"="*80)
                print("❌ Error: Expense Amount cannot be less than 0")
                print("="*80+"\n\n")
                continue

            inputExpenseDescription = input("Enter Expense Description:\n> ")
            if not inputExpenseDescription.strip():
                print("\n"+"="*80)
                print("❌ Error: Expense Description cannot be empty")
                print("="*80+"\n\n")
                continue    

            # Subtract the expense amount from the balance
            budget_data["balance"] -= inputExpenseAmount

            # Add the expense transaction to the list
            budget_data["transactions"].append({
                "type": "expense",
                "amount": str(inputExpenseAmount),
                "description": inputExpenseDescription
            })

            # Success message
            print("\n"+"="*80)
            print(f"✅ SUCCESS: You added ₪ {inputExpenseAmount} to your EXPENSE with the description of '{inputExpenseDescription}'")
            print("="*80+"\n\n")
            
            # Add menu options after operation
            print("\n(1) - ADD another Expense")
            print("(2) - Go Back")
            print("(3) - Quit")
            
            action = int(input("> "))
            if action == 1:
                continue  # Back to add another expense
            elif action == 2:
                return budget_data  # Back to main menu
            elif action == 3:
                print("Exiting program. Goodbye!")
                exit()  # Exit program
            else:
                print("Invalid choice. Returning to main menu")
                return budget_data
                
        except ValueError:
            print("\n"+"="*80)
            print("❌ Error: Please enter valid values.")
            print("="*80+"\n\n")
            # Add menu options after error
            try:
                print("\n(1) - Try Again")
                print("(2) - Go Back")
                print("(3) - Quit")
                action = int(input("> "))
                if action == 1:
                    continue  # Try again
                elif action == 2:
                    return budget_data  # Back to main menu
                elif action == 3:
                    print("Exiting program. Goodbye!")
                    exit()  # Exit program
                else:
                    print("Invalid choice. Returning to main menu")
                    return budget_data
            except ValueError:
                print("Invalid input. Returning to main menu.")
                return budget_data
    
    return budget_data


def show_balance(budget_data):
    """
    Displays the current balance.
    :param budget_data: dict with 'balance' and 'transactions'
    :return: budget_data (unchanged)
    """
    # To be implemented by a teammate
    return budget_data


def show_transactions(budget_data):
    """
    Displays the full transaction history.
    :param budget_data: dict with 'balance' and 'transactions'
    :return: budget_data (unchanged)
    """
    # To be implemented by a teammate
    return budget_data
