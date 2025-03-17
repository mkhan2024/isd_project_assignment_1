from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.subject import Subject

__author__ = "Md Apurba Khan"
__version__ = "2.9.0"

class BankAccount(Subject, ABC):
    """Abstract base class representing a generic bank account, acting as a subject.

    Attributes:
        _account_number (str): The unique account number.
        _client_number (str): The client number associated with the account.
        _balance (float): The current balance of the account.
        _date_created (date): The date the account was created.
        _observers (list): The list of observers (inherited from Subject).

    Constants:
        LOW_BALANCE_LEVEL (float): Threshold for low balance notification.
        LARGE_TRANSACTION_THRESHOLD (float): Threshold for large transaction notification.
    """

    LOW_BALANCE_LEVEL = 100.00
    LARGE_TRANSACTION_THRESHOLD = 10000.00

    def __init__(self, account_number, client_number, balance, date_created):
        """Initialize a BankAccount instance.

        Args:
            account_number (str): The account number.
            client_number (str): The client number.
            balance (float): The initial balance.
            date_created (date): The date the account was created.

        Raises:
            TypeError: If account_number or client_number is not a string or is None.
            ValueError: If balance cannot be converted to a valid float.
        """
        super().__init__()
        if not isinstance(account_number, str) or account_number is None:
            raise TypeError("Account number must be a non-None string.")
        if not isinstance(client_number, str) or client_number is None:
            raise TypeError("Client number must be a non-None string.")
        
        self._account_number = account_number
        self._client_number = client_number
        self._balance = float(balance) if self._is_valid_float(balance) else 0.0
        self._date_created = date_created if isinstance(date_created, date) else date.today()

    def _is_valid_float(self, value):
        """Helper method to validate if a value can be converted to float.

        Args:
            value: The value to validate.

        Returns:
            bool: True if value can be converted to float, False otherwise.
        """
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False

    @property
    def balance(self):
        """Getter for the balance attribute.

        Returns:
            float: The current balance.
        """
        return self._balance

    @property
    def account_number(self):
        """Getter for the account_number attribute.

        Returns:
            str: The account number.
        """
        return self._account_number

    @property
    def client_number(self):
        """Getter for the client_number attribute.

        Returns:
            str: The client number.
        """
        return self._client_number

    @property
    def date_created(self):
        """Getter for the date_created attribute.

        Returns:
            date: The date the account was created.
        """
        return self._date_created

    def update_balance(self, amount):
        """Update the balance and notify observers if conditions are met.

        Args:
            amount (float): The amount to add (positive) or subtract (negative).

        Raises:
            ValueError: If amount is not a valid number.
        """
        if not self._is_valid_float(amount):
            raise ValueError("Amount must be a valid number.")
        amount = float(amount)
        self._balance += amount
        if self._balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self._balance:.2f}: on account {self._account_number}.")
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${abs(amount):.2f}: on account {self._account_number}.")

    @abstractmethod
    def deposit(self, amount):
        """Abstract method to deposit an amount into the account.

        Args:
            amount (float): The amount to deposit.
        """
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Abstract method to withdraw an amount from the account.

        Args:
            amount (float): The amount to withdraw.
        """
        pass

    @abstractmethod
    def get_service_charges(self):
        """Abstract method to calculate service charges.

        Returns:
            float: The calculated service charges.
        """
        pass

    def __str__(self):
        """Return a string representation of the BankAccount.

        Returns:
            str: A formatted string with account details.
        """
        return f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}"