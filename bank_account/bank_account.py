"""
Description: This file contains the BankAccount class for the banking app.
Author: Md Apurba Khan
"""

from abc import ABC, abstractmethod
from datetime import date

__author__ = "Md Apurba Khan"
__version__ = "1.6.2"


class BankAccount(ABC):
    """
    Represents a bank account with deposit, withdraw, and balance updates.
    """

    BASE_SERVICE_CHARGE = 0.50  # Base service charge for all accounts

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float = 0.0,
        date_created=None,
    ):
        """
        Initializes a bank account.

        Args:
            account_number (int): Unique account number.
            client_number (int): Unique client number.
            balance (float): Initial balance, default is 0.0.
            date_created (date, optional): Creation date, default is today.

        Raises:
            ValueError: If parameters have incorrect data types.
        """
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        if not isinstance(balance, (int, float)):
            raise ValueError("Balance must be a numeric value.")

        self._account_number = account_number
        self._client_number = client_number
        self._balance = float(balance)

        self._date_created = (
            date_created if isinstance(date_created, date) else date.today()
        )

    @property
    def account_number(self) -> int:
        """Returns the account number."""
        return self._account_number

    @property
    def client_number(self) -> int:
        """Returns the client number."""
        return self._client_number

    @property
    def balance(self) -> float:
        """Returns the current balance."""
        return self._balance

    def deposit(self, amount: float):
        """
        Deposits money into the account.

        Args:
            amount (float): Deposit amount.

        Raises:
            ValueError: If the amount is non-numeric or negative.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Deposit amount must be numeric.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self._balance += amount

    def withdraw(self, amount: float):
        """
        Withdraws money from the account.

        Args:
            amount (float): Withdrawal amount.

        Raises:
            ValueError: If the amount is invalid or exceeds balance.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Withdrawal amount must be numeric.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError(
                f"Insufficient funds. Cannot withdraw ${amount:.2f}"
            )

        self._balance -= amount

    @abstractmethod
    def get_service_charges(self) -> float:
        """Abstract method to get service charges, must be overridden."""
        pass

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the account.

        Returns:
            str: Formatted account details.
        """
        return (
            f"Account Number: {self._account_number}\n"
            f"Balance: ${self._balance:.2f}"
        )
