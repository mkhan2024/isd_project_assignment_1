__author__ = "Md Apurba Khan"
__version__ = "2.9.1"

from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.observer import Subject, Observer


class BankAccount(Subject, ABC):
    """Abstract base class representing a generic bank account, acting as a subject in the Observer pattern.

    This class provides the foundational attributes and methods for all bank account types,
    including balance management, observer notifications, and abstract methods for specific
    account behaviors.

    Attributes:
        _account_number (str): The unique account number.
        _client_number (str): The client number associated with the account.
        _balance (float): The current balance of the account.
        _date_created (date): The date the account was created.
        _observers (list): List of observers subscribed to account updates.

    Constants:
        LOW_BALANCE_LEVEL (float): Threshold for low balance notification (default: 100.00).
        LARGE_TRANSACTION_THRESHOLD (float): Threshold for large transaction notification (default: 10000.00).
    """

    LOW_BALANCE_LEVEL = 100.00
    LARGE_TRANSACTION_THRESHOLD = 10000.00

    def __init__(self, account_number: str, client_number: str, balance: float, date_created: date) -> None:
        """Initialize a BankAccount instance with the given parameters.

        Args:
            account_number (str): The unique account number.
            client_number (str): The client number associated with the account.
            balance (float): The initial balance of the account.
            date_created (date): The date the account was created.

        Raises:
            TypeError: If account_number or client_number is not a non-empty string.
            ValueError: If balance cannot be converted to a valid float.
        """
        super().__init__()
        if not isinstance(account_number, str) or not account_number:
            raise TypeError("Account number must be a non-empty string.")
        if not isinstance(client_number, str) or not client_number:
            raise TypeError("Client number must be a non-empty string.")
        
        self._account_number = account_number
        self._client_number = client_number
        self._balance = float(balance) if self._is_valid_float(balance) else 0.0
        self._date_created = date_created if isinstance(date_created, date) else date.today()
        self._observers = []

    def _is_valid_float(self, value) -> bool:
        """Validate if a value can be converted to a float.

        Args:
            value: The value to validate.

        Returns:
            bool: True if the value can be converted to a float, False otherwise.
        """
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False

    def attach(self, observer: Observer) -> None:
        """Add an observer to the list of subscribers.

        Args:
            observer (Observer): The observer to attach.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Remove an observer from the list of subscribers.

        Args:
            observer (Observer): The observer to detach.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """Notify all observers of a change with the given message.

        Args:
            message (str): The message to send to observers.
        """
        for observer in self._observers:
            observer.update(message)

    @property
    def balance(self) -> float:
        """Get the current balance of the account.

        Returns:
            float: The current balance.
        """
        return self._balance

    @property
    def account_number(self) -> str:
        """Get the account number.

        Returns:
            str: The account number.
        """
        return self._account_number

    @property
    def client_number(self) -> str:
        """Get the client number associated with the account.

        Returns:
            str: The client number.
        """
        return self._client_number

    @property
    def date_created(self) -> date:
        """Get the date the account was created.

        Returns:
            date: The creation date.
        """
        return self._date_created

    def update_balance(self, amount: float) -> None:
        """Update the account balance and notify observers if conditions are met.

        Conditions for notification:
        - Balance falls below LOW_BALANCE_LEVEL.
        - Transaction amount exceeds LARGE_TRANSACTION_THRESHOLD.

        Args:
            amount (float): The amount to add (positive) or subtract (negative) from the balance.

        Raises:
            ValueError: If the amount is not a valid number.
        """
        if not self._is_valid_float(amount):
            raise ValueError("Amount must be a valid number.")
        amount = float(amount)
        self._balance += amount
        if self._balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self._balance:,.2f}: on account {self._account_number}")
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${abs(amount):,.2f}: on account {self._account_number}")

    @abstractmethod
    def deposit(self, amount: float) -> None:
        """Deposit an amount into the account.

        This method must be implemented by subclasses.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is not a valid number or is negative.
        """
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Withdraw an amount from the account.

        This method must be implemented by subclasses.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is not a valid number, is negative, or exceeds the balance.
        """
        pass

    @abstractmethod
    def get_service_charges(self) -> float:
        """Calculate the service charges for the account.

        This method must be implemented by subclasses.

        Returns:
            float: The calculated service charges.
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the BankAccount.

        Returns:
            str: A string in the format "Account Number: {number} Balance: ${balance}".
        """
        return f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}"