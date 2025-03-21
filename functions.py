# functions.py

def add_income(budget_data: dict) -> dict:
    """
    Collects income info from the user and adds it to the data structure.
    :param budget_data: dict with 'balance' and 'transactions'
    :return: updated budget_data
    """
    # To be implemented by a teammate
    while True:
        try:
            answer: str = input("Would you like to deposit? yes/no \n").lower()  # Convert input to lowercase
            if answer == "yes":  # Check if user wants to deposit
                try:
                    income_to_add: int = int(input("How much would you like to deposit? \n"))
                    
                    if income_to_add > 0:  # Ensure number is positive
                        budget_data["balance"] += income_to_add  # Update balance
                        print(f"The new balance is: {budget_data['balance']}")  # Corrected syntax

                        # Transaction part
                        transaction_description: str = input("Please insert the transaction description: \n")  # Ask for description

                        new_transaction: dict = {  # Define transaction
                            "type": "income",
                            "amount": income_to_add,
                            "description": transaction_description
                        }

                        budget_data["transactions"].append(new_transaction)  # Add transaction

                        return budget_data  # Return updated data

                    else:
                        print("Please insert a positive number over 0 ...")
                except ValueError:  # Handle non-numeric inputs
                    print("Invalid input! Please enter a valid number for deposit.")
        
            elif answer == "no":  # Exit condition
                print("No deposit made.")
                return budget_data

            else:
                print("Invalid input! Please enter 'yes' or 'no'.")

        except Exception as e:  # Catch unexpected errors
            print(f"An error occurred: {e}")


def add_expense(budget_data):
    """
    Collects expense info from the user and adds it to the data structure.
    :param budget_data: dict with 'balance' and 'transactions'
    :return: updated budget_data
    """
    # To be implemented by a teammate
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
