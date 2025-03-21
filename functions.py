# functions.py

def add_income(budget_data: dict) -> dict:
    """
    Collects income info from the user and adds it to the data structure.
    :param budget_data: dict with 'balance' and 'transactions'
    :return: updated budget_data
    """
    while True:
        try:
            answer: str = input("Would you like to deposit? yes/no \n").lower()
            if answer == "yes":
                while True:  # Loop for making transactions
                    try:
                        income_to_add: int = int(input("How much would you like to deposit? \n"))
                        
                        if income_to_add > 0:
                            budget_data["balance"] += income_to_add
                            print(f"The new balance is: {budget_data['balance']}")

                            # Transaction part
                            transaction_description: str = input("Please insert the transaction description: \n")

                            new_transaction: dict = {
                                "type": "income",
                                "amount": income_to_add,
                                "description": transaction_description
                            }

                            budget_data["transactions"].append(new_transaction)
                            print(budget_data["transactions"])

                            # Ask for another transaction
                            another_transaction: str = input("Would you like to make another transaction? yes/no \n").lower()
                            if another_transaction != "yes":
                                print(r"Goodbye :)")
                                return budget_data  # Return after finishing transactions

                        else:
                            print("Please insert a positive number over 0 ...")
                    except ValueError:
                        print("Invalid input! Please enter a valid number for deposit.")

            elif answer == "no":
                print("No deposit made.")
                return budget_data  # Exit the function

            else:
                print("Invalid input! Please enter 'yes' or 'no'.")

        except Exception as e:
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
