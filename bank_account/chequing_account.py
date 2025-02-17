"""
Description: This file contains the ChequingAccount class, a subclass of BankAccount.
Author: Md Apurba Khan
"""

from bank_account.bank_account import BankAccount

__author__ = "Md Apurba Khan"
__version__ = "1.0.0"

class ChequingAccount(BankAccount):
    """
    Represents a chequing account with overdraft functionality.
    """

    def __init__(self, account_number, client_number, balance, date_created=None, overdraft_limit=-100.0, overdraft_rate=0.05):
        """
        Initializes a ChequingAccount with overdraft features.

        Args:
            account_number (int): Unique identifier for the account.
            client_number (int): Unique identifier for the client.
            balance (float): Initial balance of the account.
            date_created (date, optional): Date the account was created. Defaults to today.
            overdraft_limit (float, optional): Overdraft limit. Defaults to -100.0.
            overdraft_rate (float, optional): Overdraft rate. Defaults to 0.05.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self._overdraft_limit = float(overdraft_limit)
        self._overdraft_rate = float(overdraft_rate)

    def get_service_charges(self):
        """
        Calculates the service charges for a ChequingAccount.

        Returns:
            float: The calculated service charge.
        """
        if self._balance >= self._overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        overdraft_amount = self._overdraft_limit - self._balance
        return self.BASE_SERVICE_CHARGE + (overdraft_amount * self._overdraft_rate)

    def __str__(self):
        """Returns a formatted string representation of the ChequingAccount."""
        base_str = super().__str__()
        return (f"{base_str}\nOverdraft Limit: ${self._overdraft_limit:.2f} "
                f"Overdraft Rate: {self._overdraft_rate * 100:.2f}% "
                f"Account Type: Chequing")