"""
A client program to verify correctness of BankAccount and Client classes.
"""

__author__ = "Md Apurba Khan"
__version__ = "1.3.0"

from bank_account.bank_account import BankAccount
from client.client import Client


def main():
    """Test the functionality of the Client and BankAccount classes."""

    # 1. Create a valid Client instance
    try:
        client = Client(1001, "John", "Doe", "jdoe@example.com")
        print("Client created successfully:")
        print(client)
    except ValueError as e:
        print(f"Error creating client: {e}")

    # 2. Declare a BankAccount object with an initial value of None
    bank_account = None

    # 3. Instantiate a valid BankAccount object
    try:
        bank_account = BankAccount(2001, client.client_number, 1000.00)
        print("\nBank Account created successfully:")
        print(bank_account)
    except ValueError as e:
        print(f"Error creating bank account: {e}")

    # 4. Attempt invalid deposits
    for amount in ["invalid_amount", -100]:
        try:
            bank_account.deposit(amount)
        except ValueError as e:
            print(f"Deposit Error ({amount}): {e}")

    # 5. Attempt valid withdrawal
    try:
        bank_account.withdraw(500)
        print(f"Successful withdrawal! New balance: ${bank_account.balance:,.2f}")
    except ValueError as e:
        print(f"Withdrawal Error: {e}")

    # 6. Attempt invalid withdrawals
    for amount in ["invalid_amount", -100, 10000]:
        try:
            bank_account.withdraw(amount)
        except ValueError as e:
            print(f"Withdrawal Error ({amount}): {e}")

    # 7. Print final account details
    print("\nFinal Bank Account Details:")
    print(bank_account)


if __name__ == "__main__":
    main()
