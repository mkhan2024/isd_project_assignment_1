"""
Description: This file contains the SavingsAccount class, a subclass of BankAccount.
Author: Md Apurba Khan
"""

from bank_account.bank_account import BankAccount

__author__ = "Md Apurba Khan"
__version__ = "1.0.0"

class SavingsAccount(BankAccount):
    """
    Represents a savings account with a minimum balance requirement.
    """

    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, account_number, client_number, balance, date_created=None, minimum_balance=50.0):
        """
        Initializes SavingsAccount with a minimum balance.

        Args:
            account_number (int): Unique identifier for the account.
            client_number (int): Unique identifier for the client.
            balance (float): Initial balance of the account.
            date_created (date, optional): Date the account was created. Defaults to today.
            minimum_balance (float, optional): Minimum required balance. Defaults to 50.0.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self._minimum_balance = float(minimum_balance)

    def get_service_charges(self):
        """
        Calculates the service charges for a SavingsAccount.

        Returns:
            float: The calculated service charge.
        """
        if self._balance >= self._minimum_balance:
            return self.BASE_SERVICE_CHARGE
        return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

    def __str__(self):
        """Returns a formatted string representation of the SavingsAccount."""
        base_str = super().__str__()
        return f"{base_str}\nMinimum Balance: ${self._minimum_balance:.2f} Account Type: Savings"