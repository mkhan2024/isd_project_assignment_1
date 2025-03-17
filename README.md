# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments. Each assignment will build on the work done in the previous assignment(s). Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Md Apurba Khan

## Assignment
### Assignment 1: Classes, Encapsulation and Unit Test Planning

## Encapsulation
Encapsulation was achieved by:
- Using private attributes (e.g., `_client_number`, `_balance`) to restrict direct access.
- Providing controlled access via `@property` methods.
- Adding validation in methods to ensure data integrity.

### Assignment 2: Inheritance and Polymorphism

## Inheritance
Inheritance was implemented by:
- Creating specialized bank account types (`ChequingAccount`, `SavingsAccount`, `InvestmentAccount`) that inherit from `BankAccount`.
- Using the `super()` function to call the constructor of the base `BankAccount` class.
- Extending functionality by adding specific attributes and methods unique to each account type.

## Polymorphism
Polymorphism was utilized by:
- Implementing the abstract method `get_service_charges()` in different account classes with unique logic for service charge calculation.
- Allowing different account types to be processed using a common interface.

## Unit Testing
- Developed unit tests for all account types to validate expected behaviors.
- Used assertions to check class-specific service charges, withdrawals, and deposits.
- Ensured that exceptions were raised correctly for invalid inputs.

### Assignment 3: Applying Design Patterns

## Strategy Pattern
- Used to calculate service charges in `ChequingAccount`, `SavingsAccount`, and `InvestmentAccount`.
- Logic is in `OverdraftStrategy`, `MinimumBalanceStrategy`, and `ManagementFeeStrategy`.
- Tested with `A02_main.py`.

## Observer Pattern
- Notifies clients of big transactions (> $10,000) and low balances (< $100).
- `Client` updates `observer_emails.txt`; `BankAccount` manages observers.
- Tested with `A03_main.py`.

## Running
- Tests: `python -m unittest discover -s tests`
- Strategy: `python A02_main.py`
- Observer: `python A03_main.py`