# Budget Manager

## Overview
Budget Manager is a Python-based program that helps users **track their income and expenses**, calculate their balance, and view transaction history.

## Features
- Add **income** transactions.
- Add **expense** transactions.
- View **current balance**.
- Display **transaction history**.
- Interactive **menu-based system**.

## Data Structure
The Budget Manager uses a **dictionary-based structure** to store financial transactions.

```python
budget_data = {
    "balance": 500,
    "transactions": [
        {"type": "income", "amount": 1000, "description": "Salary"},
        {"type": "expense", "amount": 500, "description": "Groceries"}
    ]
}
