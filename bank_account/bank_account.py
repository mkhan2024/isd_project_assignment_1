from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.observer import Subject, Observer

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

    def __init__(self, account_number: str, client_number: str, balance: float, date_created: date) -> None:
        """Initialize a BankAccount instance."""
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
        """Helper method to validate if a value can be converted to float."""
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False

    def attach(self, observer: Observer) -> None:
        """Add an observer to the list."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Remove an observer from the list."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """Notify all observers of a change."""
        for observer in self._observers:
            observer.update(message)

    @property
    def balance(self) -> float:
        """Getter for the balance attribute."""
        return self._balance

    @property
    def account_number(self) -> str:
        """Getter for the account_number attribute."""
        return self._account_number

    @property
    def client_number(self) -> str:
        """Getter for the client_number attribute."""
        return self._client_number

    @property
    def date_created(self) -> date:
        """Getter for the date_created attribute."""
        return self._date_created

    def update_balance(self, amount: float) -> None:
        """Update the balance and notify observers if conditions are met."""
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
        """Abstract method to deposit an amount into the account."""
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Abstract method to withdraw an amount from the account."""
        pass

    @abstractmethod
    def get_service_charges(self) -> float:
        """Abstract method to calculate service charges."""
        pass

    def __str__(self) -> str:
        """Return a string representation of the BankAccount."""
        return f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}"