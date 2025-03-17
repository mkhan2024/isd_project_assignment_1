from bank_account.bank_account import BankAccount
from datetime import date

__author__ = "Md Apurba Khan"
__version__ = "1.1.0"

class TestableBankAccount(BankAccount):
    """Concrete class for testing BankAccount functionality.

    This class provides a minimal implementation of abstract methods for testing purposes.
    """

    def __init__(self, account_number, client_number, balance, date_created=None):
        """Initialize a TestableBankAccount instance.

        Args:
            account_number (str): The account number.
            client_number (str): The client number.
            balance (float): The initial balance.
            date_created (date, optional): The date the account was created. Defaults to today if not provided.
        """
        super().__init__(account_number, client_number, balance, date_created or date.today())

    def deposit(self, amount):
        """Deposit an amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is not a positive number.
        """
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self._balance += float(amount)

    def withdraw(self, amount):
        """Withdraw an amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is not a positive number or if there are insufficient funds.
        """
        if not self._is_valid_float(amount) or float(amount) <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        amount = float(amount)
        if self._balance - amount < 0:
            raise ValueError("Insufficient funds for withdrawal.")
        self._balance -= amount

    def get_service_charges(self):
        """Calculate service charges (dummy implementation for testing).

        Returns:
            float: A fixed service charge for testing purposes.
        """
        return 0.0  # Dummy value, as this is just for base class testing