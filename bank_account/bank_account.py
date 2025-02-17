"""
Description: This file contains the BankAccount class for the banking application.
Author: Md Apurba Khan
"""

from abc import ABC, abstractmethod
from datetime import date

__author__ = "Md Apurba Khan"
__version__ = "2.0.0"

class BankAccount(ABC):
    """
    Abstract base class representing a bank account.
    """

    BASE_SERVICE_CHARGE = 0.50  # Base service charge for all accounts

    def __init__(self, account_number: int, client_number: int, balance: float, date_created=None):
        """
        Initializes a bank account with an account number, client number, and balance.

        Args:
            account_number (int): Unique identifier for the account.
            client_number (int): Unique identifier for the client.
            balance (float): Initial balance of the account.
            date_created (date, optional): Date the account was created. Defaults to today.
        """
        self._account_number = account_number
        self._client_number = client_number
        self._balance = balance
        self._date_created = date_created if isinstance(date_created, date) else date.today()

    @property
    def account_number(self):
        """Returns the account number."""
        return self._account_number

    @property
    def client_number(self):
        """Returns the client number."""
        return self._client_number

    @property
    def balance(self):
        """Returns the current balance."""
        return self._balance

    def deposit(self, amount: float):
        """
        Deposits money into the bank account.

        Args:
            amount (float): The amount to be deposited.
        """
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        """
        Withdraws money from the bank account.

        Args:
            amount (float): The amount to be withdrawn.
        """
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount.")

    @abstractmethod
    def get_service_charges(self):
        """Abstract method for calculating service charges."""
        pass

    def __str__(self):
        """Returns a formatted string representation of the account."""
        return f"Account Number: {self._account_number} Balance: ${self._balance:.2f}"