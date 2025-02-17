"""
Description: This file contains the InvestmentAccount class, a subclass of BankAccount.
Author: Md Apurba Khan
"""

from bank_account.bank_account import BankAccount
from datetime import date, timedelta

__author__ = "Md Apurba Khan"
__version__ = "1.0.0"

class InvestmentAccount(BankAccount):
    """
    Represents an investment account with a management fee.
    """

    # Calculate date 10 years ago from today
    TEN_YEARS_AGO = date.today() - timedelta(days=3652)

    def __init__(self, account_number, client_number, balance, date_created=None, management_fee=2.55):
        """
        Initializes InvestmentAccount with a management fee.

        Args:
            account_number (int): Unique identifier for the account.
            client_number (int): Unique identifier for the client.
            balance (float): Initial balance of the account.
            date_created (date, optional): Date the account was created. Defaults to today.
            management_fee (float, optional): The management fee applied to the account. Defaults to 2.55.
        """
        super().__init__(account_number, client_number, balance, date_created)
        self._management_fee = float(management_fee)

    def get_service_charges(self):
        """
        Calculates the service charges for an InvestmentAccount.

        Returns:
            float: The calculated service charge.
        """
        if self._date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        return self.BASE_SERVICE_CHARGE + self._management_fee

    def __str__(self):
        """Returns a formatted string representation of the InvestmentAccount."""
        base_str = super().__str__()
        fee_str = f"${self._management_fee:.2f}" if self._date_created >= self.TEN_YEARS_AGO else "Waived"
        return f"{base_str}\nManagement Fee: {fee_str} Account Type: Investment"