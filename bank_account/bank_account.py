from abc import ABC, abstractmethod
from datetime import date

__author__ = "Md Apurba Khan"
__version__ = "2.6.0"

class BankAccount(ABC):
    """Abstract base class representing a generic bank account."""
    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number, client_number, balance, date_created):
        """Initialize a BankAccount instance.

        Args:
            account_number (str): The account number.
            client_number (str): The client number.
            balance (float): The initial balance.
            date_created (date): The date the account was created.
        """
        self._account_number = account_number
        self._client_number = client_number
        self._balance = float(balance) if self._is_valid_float(balance) else 0.0
        # Validate date_created, default to today if invalid
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