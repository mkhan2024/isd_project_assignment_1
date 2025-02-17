"""
Description: This file contains the BankAccount class for the banking application.
Author: Md Apurba Khan
"""


class BankAccount:
    """
    Represents a bank account with deposit, withdraw, and balance update functionalities.
    """

    def __init__(self, account_number: int, client_number: int, balance: float = 0.0):
        """
        Initializes a bank account with an account number, client number, and balance.

        Raises:
            ValueError: If account_number or client_number is not an integer.
            ValueError: If balance is not a valid float.
        """
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")

        # **Fix: Ensure invalid balance raises ValueError**
        if isinstance(balance, str) or balance is None:
            raise ValueError("Balance must be a numeric value.")

        try:
            self.__balance = float(balance)
        except ValueError:
            raise ValueError("Balance must be a valid numeric value.")

        self.__account_number = account_number
        self.__client_number = client_number

    @property
    def account_number(self) -> int:
        """Returns the account number."""
        return self.__account_number

    @property
    def client_number(self) -> int:
        """Returns the client number."""
        return self.__client_number

    @property
    def balance(self) -> float:
        """Returns the current balance."""
        return self.__balance

    def update_balance(self, amount: float):
        """
        Updates the account balance.

        Args:
            amount (float): The amount to update (can be positive or negative).
        """
        try:
            self.__balance += float(amount)
        except ValueError:
            raise ValueError("Amount must be a numeric value.")

    def deposit(self, amount: float):
        """
        Deposits money into the bank account.

        Args:
            amount (float): The amount to be deposited.

        Raises:
            ValueError: If the amount is not numeric or is negative.
        """
        try:
            float_amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount must be numeric: {amount}")

        if float_amount <= 0:
            raise ValueError(f"Deposit amount must be positive: ${float_amount:,.2f}")

        self.update_balance(float_amount)

    def withdraw(self, amount: float):
        """
        Withdraws money from the bank account.

        Args:
            amount (float): The amount to be withdrawn.

        Raises:
            ValueError: If the amount is not numeric, is negative, or exceeds the balance.
        """
        try:
            float_amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdrawal amount must be numeric: {amount}")

        if float_amount <= 0:
            raise ValueError(
                f"Withdrawal amount must be positive: ${float_amount:,.2f}"
            )

        if float_amount > self.__balance:
            raise ValueError(
                f"Withdrawal amount (${
                    float_amount:,.2f}) cannot exceed account balance: ${
                    self.__balance:,.2f}"
            )

        self.update_balance(-float_amount)

    def __str__(self) -> str:
        """Returns a formatted string representation of the account."""
        return (
            f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}"
        )
